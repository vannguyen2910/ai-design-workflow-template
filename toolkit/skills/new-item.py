#!/usr/bin/env python3
"""
new-item.py - add an item (O, H, M, D, E, F) to insights/ and fill its relations.

Run it with no arguments and it asks one question at a time:

    python3 new-item.py

An AI tool (or you) can pass everything at once:

    python3 new-item.py D --title "Hiện crowd signal thay cho badge" --tests H2 --follows P1 --pulls-against P8
    python3 new-item.py E --title "Test task với 5 người" --tests H1 --measures M1 --participants 5
    python3 new-item.py D --title "..." --tests H1 --state accepted --owner "Lan (PM)"
    python3 new-item.py O --title "..." --impact high --confidence medium --rank-reason "..."
    python3 new-item.py M --title "..." --target "≥ 80% hoàn tất không cần trợ giúp"
    python3 new-item.py F --title "..." --severity 3 --found-in E1 --affects D2 --principle P8

It picks the next free ID, writes the file in the right folder, checks that every ID you
point at exists, tells you what is still missing, and rebuilds index.html (--no-build to skip).
It never overwrites a file. Needs only Python 3.
"""
import argparse
import datetime
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

def find_case(start=None):
    """The case folder: the nearest folder, from `start` (default: the current folder) upwards,
    that has AGENTS.md next to insights/ or work/. Falls back to the folder above this script
    (a copy of this script in the workspace's toolkit/skills/ folder)."""
    p = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and (
                os.path.isdir(os.path.join(p, "insights")) or os.path.isdir(os.path.join(p, "work"))):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            break
        p = parent
    legacy = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir(os.path.join(legacy, "insights")):
        return legacy
    return None

CASE = None  # set in main() from --case or the current folder

KINDS = {
    "O": ("opportunity", "opportunities", "Opportunity: nhu cầu người dùng có evidence"),
    "H": ("hypothesis", "hypotheses", "Hypothesis: điều bạn tin và sẽ kiểm tra"),
    "M": ("metric", "metrics", "Metric: cách biết hypothesis đúng hay sai"),
    "D": ("decision", "decisions", "Decision: một quyết định thiết kế"),
    "E": ("evidence", "evidence", "Evidence: một test hoặc nghiên cứu"),
    "F": ("finding", "findings", "Finding: một vấn đề usability tìm thấy"),
}

# (field, targets, many, question)
RELATIONS = {
    "O": [],
    "H": [("serves", "O", True, "Hypothesis này phục vụ opportunity nào?"),
          ("metric", "M", True, "Đo bằng metric nào?")],
    "M": [],
    "D": [("tests", "H", True, "Decision này kiểm chứng hypothesis nào?"),
          ("follows", "P", True, "Theo principle nào?"),
          ("pulls_against", "P", True, "Đi ngược principle nào? (bỏ trống nếu không)")],
    "E": [("tests", "H", True, "Evidence này kiểm chứng hypothesis nào?"),
          ("measures", "M", True, "Đo metric nào?")],
    "F": [("found_in", "E", True, "Phát hiện trong evidence nào?"),
          ("affects", "D", True, "Ảnh hưởng decision nào? (bỏ trống nếu không)"),
          ("principle", "P", True, "Vi phạm principle nào? (bỏ trống nếu chưa gắn được)")],
}
FLAG = {"serves": "serves", "metric": "metric", "tests": "tests", "follows": "follows", "pulls_against": "pulls-against",
        "measures": "measures", "found_in": "found-in", "affects": "affects", "principle": "principle"}


def load_hub():
    spec = importlib.util.spec_from_file_location("export_hub", os.path.join(HERE, "export-hub.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ask(prompt, default=""):
    try:
        v = input("%s%s: " % (prompt, (" [%s]" % default) if default else "")).strip()
    except EOFError:
        sys.exit("\nKhông có đầu vào. Truyền đủ tham số (xem --help) khi chạy không tương tác.")
    return v or default


def ids_of(text):
    return [t for t in re.split(r"[,\s]+", text.upper()) if t]


def pick(prompt, options, many=True):
    """options: list of (id, label). Accepts numbers or IDs, comma separated. Enter skips."""
    if not options:
        print("  (%s) chưa có gì để chọn: bỏ qua, báo cáo sẽ nhắc bạn nối sau." % prompt.rstrip("?").rstrip())
        return []
    print("\n%s" % prompt)
    for n, (i, lab) in enumerate(options, 1):
        print("  %d) %s  %s" % (n, i, lab[:90]))
    while True:
        raw = ask("  Chọn (số hoặc mã, cách nhau bằng dấu phẩy; Enter để bỏ qua)")
        if not raw:
            return []
        chosen, bad = [], []
        for tok in ids_of(raw):
            if tok.isdigit() and 1 <= int(tok) <= len(options):
                chosen.append(options[int(tok) - 1][0])
            elif tok in [o[0] for o in options]:
                chosen.append(tok)
            else:
                bad.append(tok)
        if bad:
            print("  Không có: %s. Thử lại." % ", ".join(bad))
            continue
        return list(dict.fromkeys(chosen))


def next_id(letter, existing):
    nums = [int(re.sub(r"\D", "", i)) for i in existing if i.startswith(letter) and re.sub(r"\D", "", i)]
    return "%s%d" % (letter, (max(nums) + 1) if nums else 1)


def yaml_str(v):
    return '"%s"' % str(v).replace("\\", "\\\\").replace('"', '\\"')


def yaml_list(key, ids, principle_ids):
    if not ids:
        return ["%s: []" % key]
    out = ["%s:" % key]
    for i in ids:
        out.append('  - "[[%s]]"' % (("principle-checks|%s" % i) if i in principle_ids else i))
    return out


def template_body(folder_kind):
    """The body of the matching template, without its 'Cách dùng' line."""
    t = os.path.join(CASE, "insights", "_templates", "_template-%s.md" % folder_kind)
    if not os.path.isfile(t):
        return ""
    raw = open(t, encoding="utf-8").read()
    m = re.match(r"^---\n.*?\n---\n?", raw, re.S)
    body = raw[m.end():] if m else raw
    body = re.sub(r"^\*Cách dùng[^\n]*\n\n?", "", body, flags=re.M)
    return body.lstrip("\n")


def main():
    ap = argparse.ArgumentParser(description="Thêm một item vào insights/ và nối quan hệ của nó.")
    ap.add_argument("kind", nargs="?", help="O, H, M, D, E hoặc F (bỏ trống để được hỏi)")
    ap.add_argument("--title", help="một câu mô tả item")
    ap.add_argument("--area", default="", help="chủ đề (tuỳ chọn), ví dụ: onboarding")
    for field, flag in FLAG.items():
        ap.add_argument("--" + flag, help="mã cách nhau bằng dấu phẩy, ví dụ H1,H2")
    ap.add_argument("--severity", type=int, choices=range(0, 5), help="finding: 0 đến 4")
    ap.add_argument("--resolution", default="open", help="finding: open, fixed, accepted, deferred")
    ap.add_argument("--rank", type=int, help="opportunity: thứ hạng (mặc định: cuối danh sách)")
    ap.add_argument("--evidence-note", dest="evidence_note", help="opportunity: nguồn hoặc quote ID")
    ap.add_argument("--participants", type=int, default=0, help="evidence: số người tham gia")
    ap.add_argument("--status", help="evidence: planned hoặc run; metric: assumed hoặc confirmed")
    ap.add_argument("--baseline", help="metric: mốc hiện tại (hoặc unknown)")
    ap.add_argument("--reason", help="decision: lý do một câu, ghi luôn vào case log")
    ap.add_argument("--solutions", help="decision: mã giải pháp mà nó thực hiện, ví dụ A4,P3 (sơ đồ flow dùng để gắn mã decision)")
    ap.add_argument("--owner", help="decision: ai chịu trách nhiệm")
    ap.add_argument("--decided-on", dest="decided_on", help="decision: ngày YYYY-MM-DD (mặc định: hôm nay khi state là accepted)")
    ap.add_argument("--state", choices=["proposed", "accepted", "shipped", "superseded", "dropped"], help="decision: mặc định proposed")
    ap.add_argument("--impact", choices=["high", "medium", "low"], help="opportunity: tác động")
    ap.add_argument("--confidence", choices=["high", "medium", "low"], help="opportunity: độ chắc chắn của evidence")
    ap.add_argument("--rank-reason", dest="rank_reason", help="opportunity: vì sao nó đứng ở thứ hạng này")
    ap.add_argument("--target", help="metric: ngưỡng thế nào là đạt")
    ap.add_argument("--result", help="metric: kết quả đo được")
    ap.add_argument("--verdict", choices=["pending", "met", "missed", "inconclusive"], help="metric: kết luận so với target")
    ap.add_argument("--measured-on", dest="measured_on", help="metric: ngày đo YYYY-MM-DD")
    ap.add_argument("--no-log", action="store_true", help="decision: không thêm dòng vào case log")
    ap.add_argument("--no-build", action="store_true", help="không tạo lại index.html")
    ap.add_argument("--case", default="", help="case folder (default: the case you are standing in)")
    a = ap.parse_args()
    global CASE
    CASE = os.path.abspath(a.case) if a.case else find_case()
    if not CASE:
        sys.exit("Không tìm thấy case folder. Chạy trong một case (có AGENTS.md và insights/), hoặc dùng --case <đường dẫn>.")
    interactive = a.kind is None

    hub = load_hub()
    _ov, _wk, items, _ref, _ctx = hub.collect(CASE)
    by_id = {p.id: p for p in items}
    pr_path = os.path.join(CASE, "standards", "principle-checks.md")
    if not os.path.isfile(pr_path):
        pr_path = os.path.join(CASE, "reference", "principle-checks.md")
    principles = hub.parse_principles(open(pr_path, encoding="utf-8").read()) if os.path.isfile(pr_path) else {}

    # 1. kind
    kind = (a.kind or "").upper()
    if not kind:
        print("Thêm item mới. Chọn loại:")
        for k, (_n, _f, lab) in KINDS.items():
            print("  %s) %s" % (k, lab))
        kind = ask("Loại (O/H/M/D/E/F)").upper()
    if kind not in KINDS:
        sys.exit("Loại phải là một trong: %s" % ", ".join(KINDS))
    type_name, folder, _lab = KINDS[kind]

    # 2. title
    title = a.title or ask("\nMột câu mô tả %s này" % type_name)
    if not title:
        sys.exit("Cần một title.")

    # 3. relations
    def options_for(target):
        if target == "P":
            return [(pid, nm) for pid, (nm, _chk) in principles.items()]
        return [(i, p.title) for i, p in sorted(by_id.items(), key=lambda kv: hub._natkey(kv[0])) if p.letter == target]

    rel = {}
    for field, target, many, question in RELATIONS[kind]:
        opts = options_for(target)
        valid = {o[0] for o in opts}
        given = getattr(a, field, None)
        if given is not None:
            ids = ids_of(given)
            bad = [i for i in ids if i not in valid]
            if bad:
                sys.exit("%s: không có mã %s (có: %s)" % (FLAG[field], ", ".join(bad), ", ".join(sorted(valid)) or "không có gì"))
        elif interactive:
            ids = pick(question, opts, many)
        else:
            ids = []
        rel[field] = ids

    # 4. extra fields
    extra = []
    if kind == "O":
        existing_ranks = [p.rank for p in items if p.letter == "O" and p.rank != 999]
        default_rank = max(existing_ranks or [0]) + 1
        rank = a.rank or (int(ask("\nThứ hạng (1 là quan trọng nhất)", str(default_rank))) if interactive else default_rank)
        note = a.evidence_note if a.evidence_note is not None else (ask("Nguồn hoặc quote ID của evidence", "chưa có") if interactive else "chưa có")
        impact = a.impact or (ask("Tác động lên người dùng (high/medium/low)", "medium") if interactive else "")
        conf = a.confidence or (ask("Độ chắc chắn của evidence (high/medium/low)", "medium") if interactive else "")
        why = a.rank_reason if a.rank_reason is not None else (ask("Vì sao nó đứng ở thứ hạng này (một hai câu)") if interactive else "")
        for v_, n_ in ((impact, "impact"), (conf, "confidence")):
            if v_ and v_ not in ("high", "medium", "low"):
                sys.exit("%s phải là high, medium hoặc low" % n_)
        extra = ["rank: %d" % rank] + (["impact: %s" % yaml_str(impact)] if impact else []) + (["confidence: %s" % yaml_str(conf)] if conf else []) \
            + ["rank_reason: %s" % yaml_str(why), "evidence: %s" % yaml_str(note)]
    elif kind == "M":
        base = a.baseline if a.baseline is not None else (ask("\nMốc hiện tại (hoặc unknown)", "unknown") if interactive else "unknown")
        st = a.status or "assumed"
        tgt = a.target if a.target is not None else (ask("Target: thế nào là đạt (ví dụ ≥ 80% hoàn tất)") if interactive else "")
        extra = ["status: %s" % yaml_str(st), "baseline: %s" % yaml_str(base), 'measured_by: "usability test / analytics"',
                 "target: %s" % yaml_str(tgt), "result: %s" % yaml_str(a.result or ""), "measured_on: %s" % yaml_str(a.measured_on or ""),
                 "verdict: %s" % yaml_str(a.verdict or "pending")]
    elif kind == "E":
        st = a.status or (ask("\nTrạng thái (planned = chưa chạy, run = đã chạy)", "planned") if interactive else "planned")
        n = a.participants or (int(ask("Số người tham gia", "0") or 0) if interactive else 0)
        extra = ["participants: %d" % n, 'result: ""', "status: %s" % yaml_str(st)]
    elif kind == "F":
        sev = a.severity if a.severity is not None else (int(ask("\nSeverity 0 đến 4 (xem standards/severity-levels.md)", "2")) if interactive else 2)
        extra = ["severity: %d" % sev, "resolution: %s" % yaml_str(a.resolution)]

    if kind == "D":
        st_ = a.state or (ask("\nTrạng thái (proposed/accepted/shipped/superseded/dropped)", "proposed") if interactive else "proposed")
        owner = a.owner if a.owner is not None else (ask("Ai chịu trách nhiệm (owner)") if interactive else "")
        when = a.decided_on if a.decided_on is not None else (datetime.date.today().isoformat() if st_ in ("accepted", "shipped") else "")
        extra = ["state: %s" % yaml_str(st_), "owner: %s" % yaml_str(owner), "decided_on: %s" % yaml_str(when)]
        if a.solutions:
            extra.append("solutions: [%s]" % ", ".join(yaml_str(c) for c in ids_of(a.solutions)))

    # 5. write the file
    new_id = next_id(kind, by_id)
    d = os.path.join(CASE, "insights", folder)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, new_id + ".md")
    if os.path.exists(path):
        sys.exit("File đã tồn tại: %s (không ghi đè)" % path)
    fm = ["---", "type: %s" % yaml_str(type_name), "title: %s" % yaml_str(title)]
    if a.area:
        fm.append("area: %s" % yaml_str(a.area))
    fm += extra
    for field, _t, _m, _q in RELATIONS[kind]:
        fm += yaml_list(field, rel.get(field, []), set(principles))
    fm.append("---")
    body = template_body(type_name) or "## Why\n\n"
    open(path, "w", encoding="utf-8").write("\n".join(fm) + "\n" + body)
    rel_path = os.path.relpath(path, CASE)
    print("\nĐã tạo %s  (%s)" % (new_id, rel_path))

    # 6. case log for decisions
    if kind == "D" and not a.no_log:
        reason = a.reason if a.reason is not None else (ask("\nLý do một câu để ghi vào case log (Enter để bỏ qua)") if interactive else "")
        log = os.path.join(CASE, "insights", "case-log.md")
        if not os.path.isfile(log):
            log = os.path.join(CASE, "reference", "case-log.md")
        if reason and os.path.isfile(log):
            row = "| %s | %s | %s | %s |\n" % (datetime.date.today().isoformat(), title.replace("|", "/"), reason.replace("|", "/"),
                                              ", ".join([new_id] + rel.get("tests", [])))
            txt = open(log, encoding="utf-8").read().rstrip("\n") + "\n"
            lines = txt.split("\n")
            if len(lines) > 1 and re.fullmatch(r"\|(\s*\|)+", lines[-2].strip()):  # the empty placeholder row
                lines.pop(-2)
            open(log, "w", encoding="utf-8").write("\n".join(lines).rstrip("\n") + "\n" + row)
            print("Đã thêm một dòng vào insights/case-log.md")
        elif not reason:
            print("  Còn thiếu: chưa có dòng trong insights/case-log.md (thêm --reason \"...\" hoặc ghi tay)")

    # 7. what is still missing
    missing = []
    if kind == "D" and not rel.get("tests"):
        missing.append("chưa nối về hypothesis nào (tests): decision này sẽ bị cảnh báo là chưa có user need")
    if kind == "H" and not rel.get("serves"):
        missing.append("chưa nối về opportunity nào (serves)")
    if kind == "H" and not rel.get("metric"):
        missing.append("chưa có metric")
    if kind == "E" and not rel.get("tests"):
        missing.append("chưa nối về hypothesis nào (tests)")
    if kind == "F" and not rel.get("found_in"):
        missing.append("chưa nối về evidence nào (found_in)")
    if kind == "D" and extra and 'state: "accepted"' in extra[0] and 'owner: ""' in extra[1]:
        missing.append("decision đã chấp nhận nhưng chưa có owner")
    if kind == "M" and 'target: ""' in "\n".join(extra):
        missing.append("metric chưa có target")
    if kind == "O" and 'rank_reason: ""' in "\n".join(extra):
        missing.append("opportunity chưa có lý do xếp hạng (--rank-reason)")
    for m_ in missing:
        print("  Còn thiếu: " + m_)
    print("Mở %s để viết phần nội dung." % rel_path)

    # 8. rebuild
    if not a.no_build:
        r = subprocess.run([sys.executable, os.path.join(HERE, "export-hub.py"), "--case", CASE], cwd=CASE, capture_output=True, text=True)
        print("index.html: %s" % ("đã tạo lại" if r.returncode == 0 else "lỗi, hãy tạo lại báo cáo bằng export-hub.py"))
        if r.returncode != 0:
            print(r.stderr.strip()[-400:])


if __name__ == "__main__":
    main()
