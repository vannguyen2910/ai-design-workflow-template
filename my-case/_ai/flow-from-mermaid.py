#!/usr/bin/env python3
"""
flow-from-mermaid.py - turn a Mermaid flowchart into archify diagrams, one per phase.

    python3 _ai/flow-from-mermaid.py work/user-flow.md --out work/user-flow --title "My product"

What it does
  - reads the first ```mermaid flowchart in the file (or a .mmd file)
  - every `subgraph` becomes its own diagram, so a long flow is never squeezed into one picture
  - adds one overview diagram of the phases when there is more than one
  - sizes nodes from their text, puts "· A4" style solution codes into a tag, wraps long chains
    into extra rows (6 columns per row), and shows links to other phases as small stub nodes
  - writes <slug>.json and runs `archify finalize` for each, so you get checked HTML files

Needs Python 3 and the archify skill (set ARCHIFY_BIN to its bin/archify.mjs if it lives elsewhere).
Without archify it still writes the .json files.
"""
import argparse
import json
import os
import re
import subprocess
import sys

COLS = 6
PILLAR_TYPES = ["frontend", "backend", "database", "cloud", "security"]


def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s, flags=re.U).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "flow"


def strip_emoji(s):
    return re.sub(r"[^\w\s&/,.'’()+–—-]", "", s, flags=re.U).strip()


def short_phase(s):
    s = strip_emoji(s)
    return re.split(r"\s+[—–-]\s+", s)[0].strip() or s


# ---------------------------------------------------------------- parsing
NODE_RE = re.compile(r"""^\s*([A-Za-z_][\w]*)\s*(?:
    \(\[\s*"?(?P<stad>.*?)"?\s*\]\) |
    \{\s*"?(?P<dec>.*?)"?\s*\} |
    \[\s*"?(?P<rect>.*?)"?\s*\] |
    \(\s*"?(?P<round>.*?)"?\s*\)
)?""", re.X)
EDGE_SPLIT = re.compile(r"\s*(?:--\s*(?P<l1>[^->|]+?)\s*-->|-->\s*\|(?P<l2>[^|]+)\||-\.->|==>|-->)\s*")


class G(object):
    def __init__(self):
        self.nodes = {}          # id -> dict(text, kind, group)
        self.order = []
        self.edges = []          # (a, b, label)
        self.groups = []         # (id, title)


def parse(text):
    g = G()
    m = re.search(r"```mermaid\s*\n(.*?)```", text, re.S)
    body = m.group(1) if m else text
    stack = []
    for raw in body.split("\n"):
        line = raw.strip()
        if not line or line.startswith("%%") or re.match(r"(flowchart|graph)\b", line):
            continue
        sg = re.match(r'subgraph\s+(\w+)\s*(?:\[\s*"?(.*?)"?\s*\])?\s*$', line)
        if sg:
            gid, title = sg.group(1), sg.group(2) or sg.group(1)
            g.groups.append((gid, title))
            stack.append(gid)
            continue
        if line == "end":
            if stack:
                stack.pop()
            continue
        cur = stack[-1] if stack else None
        parts = EDGE_SPLIT.split(line)
        # re.split with named groups returns [text, l1, l2, text, ...]; rebuild sequentially
        items, labels = [], []
        pos = 0
        for mm in EDGE_SPLIT.finditer(line):
            items.append(line[pos:mm.start()])
            labels.append((mm.group("l1") or mm.group("l2") or "").strip())
            pos = mm.end()
        items.append(line[pos:])
        ids = []
        for it in items:
            it = it.strip()
            if not it:
                continue
            nm = NODE_RE.match(it)
            if not nm:
                continue
            nid = nm.group(1)
            txt = nm.group("stad") or nm.group("dec") or nm.group("rect") or nm.group("round")
            kind = "start" if nm.group("stad") is not None else "decision" if nm.group("dec") is not None else "step"
            if nid not in g.nodes:
                g.nodes[nid] = {"text": txt if txt is not None else nid, "kind": kind, "group": cur}
                g.order.append(nid)
            elif txt is not None and g.nodes[nid]["text"] == nid:
                g.nodes[nid].update({"text": txt, "kind": kind})
                if cur and not g.nodes[nid]["group"]:
                    g.nodes[nid]["group"] = cur
            ids.append(nid)
        for i in range(len(ids) - 1):
            g.edges.append((ids[i], ids[i + 1], labels[i] if i < len(labels) else ""))
    return g


# ---------------------------------------------------------------- layout
def depths(nodes, edges):
    """longest-path depth, ignoring back edges so loops do not blow up"""
    out = {n: [] for n in nodes}
    for a, b, _ in edges:
        if a in out and b in out:
            out[a].append(b)
    state, back = {}, set()

    def dfs(n):
        state[n] = 1
        for m in out[n]:
            if state.get(m) == 1:
                back.add((n, m))
            elif m not in state:
                dfs(m)
        state[n] = 2
    incoming = {b for a, b, _ in edges if a in out and b in out}
    roots = [n for n in nodes if n not in incoming] or nodes[:1]
    for r in roots + nodes:
        if r not in state:
            dfs(r)
    d = {n: 0 for n in nodes}
    changed = True
    guard = 0
    while changed and guard < len(nodes) + 5:
        changed, guard = False, guard + 1
        for a, b, _ in edges:
            if a in d and b in d and (a, b) not in back and d[b] < d[a] + 1:
                d[b] = d[a] + 1
                changed = True
    return d, back


def split_text(text):
    """label, sublabel, tag from 'Free access granted · A1'"""
    tag = ""
    m = re.match(r"^(.*?)\s*[·|]\s*([A-Z]\d+(?:[–-][A-Z]?\d+)?(?:\s*,\s*[A-Z]\d+)*)\s*$", text)
    if m:
        text, tag = m.group(1).strip(), m.group(2).strip()
    sub = ""
    if len(text) > 24 and " " in text:
        words = text.split(" ")
        best, cut = 10 ** 9, 1
        for i in range(1, len(words)):
            a, b = len(" ".join(words[:i])), len(" ".join(words[i:]))
            if abs(a - b) < best:
                best, cut = abs(a - b), i
        text, sub = " ".join(words[:cut]), " ".join(words[cut:])
    return text, sub, tag


def node_width(label, sub, tag):
    n = max(len(label), len(sub))
    return int(min(176, max(124, n * 7.4 + 34)))


def build_phase(g, gid, title, args, pillar_map):
    members = [n for n in g.order if g.nodes[n]["group"] == gid]
    mset = set(members)
    internal = [(a, b, l) for a, b, l in g.edges if a in mset and b in mset]
    nodes = list(members)
    stubs, extra_edges = {}, []
    outs, ins = [], []
    for a, b, l in g.edges:
        if a in mset and b not in mset and b in g.nodes:
            outs.append((a, short_phase(dict(g.groups).get(g.nodes[b]["group"], "next")), l))
        elif b in mset and a not in mset and a in g.nodes:
            ins.append((b, short_phase(dict(g.groups).get(g.nodes[a]["group"], "previous")), l))
    if outs:  # one stub for everything that leaves this phase
        names = sorted({t for _, t, _ in outs}, key=[t for _, t, _ in outs].index)
        stubs["to_next"] = {"text": "Continues: " + " / ".join(names), "kind": "start", "group": gid}
        nodes.append("to_next")
        for a, _t, l in outs:
            extra_edges.append((a, "to_next", l))
    if ins:   # one stub for everything that enters it
        names = sorted({t for _, t, _ in ins}, key=[t for _, t, _ in ins].index)
        stubs["from_prev"] = {"text": "From: " + " / ".join(names), "kind": "start", "group": gid}
        nodes.insert(0, "from_prev")
        for b, _t, l in ins:
            extra_edges.append(("from_prev", b, l))
    edges = internal + extra_edges
    meta = dict(g.nodes)
    meta.update(stubs)
    d, back = depths(nodes, edges)

    seg_slots = {}
    place = {}
    for n in nodes:
        seg = d[n] // COLS
        slot = seg_slots.setdefault((seg, d[n]), [])
        k = len(slot)
        slot.append(n)
        col = d[n] % COLS
        place[n] = (seg, k, col)
    max_slot = {}
    for n, (seg, k, col) in place.items():
        max_slot[seg] = max(max_slot.get(seg, 0), k + 1)
    lanes, lane_of = [], {}
    nseg = max(max_slot) + 1 if max_slot else 1
    for seg in range(nseg):
        for k in range(max_slot.get(seg, 1)):
            lid = "r%d_%d" % (seg, k)
            if k == 0:
                label = title if nseg == 1 else "%s (%d/%d)" % (title, seg + 1, nseg)
            else:
                label = "Alternative" if nseg == 1 else "Alternative (%d/%d)" % (seg + 1, nseg)
            lanes.append({"id": lid, "label": label})
            lane_of[(seg, k)] = lid

    jn = []
    for n in nodes:
        seg, k, col = place[n]
        info = meta[n]
        label, sub, tag = split_text(strip_emoji(info["text"]) if info["kind"] == "start" and n in ("to_next", "from_prev") else info["text"])
        t = "frontend"
        icon = None
        if info["kind"] == "decision":
            t, icon = "messagebus", "flag"
        elif info["kind"] == "start":
            t = "external"
            icon = "person" if n in members and d[n] == 0 else None
        elif tag:
            t = pillar_map.get(re.match(r"[A-Z]", tag).group(0), "frontend")
        node = {"id": n, "lane": lane_of[(seg, k)], "col": col, "type": t, "label": label,
                "width": node_width(label, sub, tag)}
        if sub:
            node["sublabel"] = sub
        if tag:
            node["tag"] = tag
        if icon:
            node["icon"] = icon
        jn.append(node)

    je = []
    merged = {}
    for a, b, l in edges:  # two edges between the same pair become one, with their labels joined
        if a in place and b in place:
            merged.setdefault((a, b), [])
            if l and l not in merged[(a, b)]:
                merged[(a, b)].append(l)
    edges = [(a, b, " / ".join(ls)) for (a, b), ls in merged.items()]
    for i, (a, b, l) in enumerate(edges):
        e = {"id": "e%d" % i, "from": a, "to": b, "variant": "default"}
        if l:
            e["label"] = l
        if (a, b) in back:
            e["variant"], e["role"] = "dashed", "return"
        elif place[a][0] != place[b][0]:  # wraps to the next row: columns restart, so it is drawn as a return
            e["role"] = "return"
        je.append(e)

    main = longest_path(nodes, [(a, b) for a, b, _ in edges if (a, b) not in back and place[a][0] == place[b][0] and place[b][2] > place[a][2]])
    if len(main) < 2:
        main = [nodes[0], nodes[-1]] if len(nodes) > 1 else nodes
    return jn, je, lanes, main


def longest_path(nodes, edges):
    out = {n: [] for n in nodes}
    for a, b in edges:
        out[a].append(b)
    best = {}

    def go(n, seen):
        if n in best:
            return best[n]
        r = [n]
        for m in out[n]:
            if m in seen:
                continue
            c = [n] + go(m, seen | {n})
            if len(c) > len(r):
                r = c
        best[n] = r
        return r
    incoming = {b for _, b in edges}
    roots = [n for n in nodes if n not in incoming] or nodes[:1]
    path = []
    for r in roots:
        p = go(r, set())
        if len(p) > len(path):
            path = p
    return path


def legend_for(nodes, names, pillar_map):
    entries = {"messagebus": {"label": "Decision"}, "external": {"label": "Start or link to another phase"}}
    used = {n["type"] for n in nodes}
    for letter, t in pillar_map.items():
        if t in used:
            entries[t] = {"label": names.get(letter, "Solutions %s" % letter)}
    if "frontend" in used and "frontend" not in entries:
        entries["frontend"] = {"label": "Step"}
    return {"entries": {k: v for k, v in entries.items() if k in used}}


def diagram(title, jn, je, lanes, main, legend, out_name):
    return {
        "schema_version": 2,
        "diagram_type": "workflow",
        "meta": {"title": title, "locale": "en", "quality_profile": "showcase", "legend": legend, "output": out_name},
        "lanes": lanes,
        "mainPath": main,
        "nodes": jn,
        "edges": je,
    }


def find_archify():
    for p in (os.environ.get("ARCHIFY_BIN"), os.path.expanduser("~/.claude/skills/archify/bin/archify.mjs")):
        if p and os.path.isfile(p):
            return p
    return None


def finalize(bin_path, json_path, html_path, cwd):
    r = subprocess.run(["node", bin_path, "finalize", "workflow", os.path.basename(json_path), os.path.basename(html_path),
                        "--quality", "showcase", "--json"], cwd=cwd, capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return False, [r.stderr.strip()[-300:] or "archify did not return JSON"]
    msgs = [x.get("message", "") for x in d.get("diagnostics", [])]
    # keep the folder tidy: the receipts are not needed in a project
    base = os.path.splitext(os.path.basename(html_path))[0]
    for suf in (".finalize.json", ".finalize-summary.json", ".delivery.json", ".delivery-pending.json", ".browser-check.json"):
        p = os.path.join(cwd, base + suf)
        if os.path.exists(p):
            os.remove(p)
    return d.get("status") == "pass", msgs


def main():
    ap = argparse.ArgumentParser(description="Mermaid flowchart -> one archify diagram per phase")
    ap.add_argument("source", help="markdown file with a ```mermaid block, or a .mmd file")
    ap.add_argument("--out", required=True, help="folder for the .json and .html files")
    ap.add_argument("--title", default="", help="product name used in diagram titles")
    ap.add_argument("--legend", default="", help='names for solution-code letters, e.g. "A=Onboarding,D=Discover,P=Plan"')
    ap.add_argument("--no-overview", action="store_true", help="skip the phase overview diagram")
    ap.add_argument("--no-run", action="store_true", help="write the .json files only")
    a = ap.parse_args()

    text = open(a.source, encoding="utf-8").read()
    g = parse(text)
    if not g.nodes:
        sys.exit("No Mermaid flowchart found in %s" % a.source)
    os.makedirs(a.out, exist_ok=True)
    names = dict(kv.split("=", 1) for kv in a.legend.split(",") if "=" in kv)

    letters = []
    for n in g.order:
        m = re.search(r"[·|]\s*([A-Z])\d", g.nodes[n]["text"])
        if m and m.group(1) not in letters:
            letters.append(m.group(1))
    pillar_map = {l: PILLAR_TYPES[i % len(PILLAR_TYPES)] for i, l in enumerate(letters)}

    groups = g.groups or [("flow", a.title or "Flow")]
    if not g.groups:
        for n in g.nodes.values():
            n["group"] = "flow"
    prefix = (a.title + ": ") if a.title else ""
    jobs = []
    if len(groups) > 1 and not a.no_overview:
        ov_nodes = [{"id": gid, "lane": "phases", "col": i % COLS, "type": "frontend", "label": short_phase(t),
                     "width": 150} for i, (gid, t) in enumerate(groups)]
        idx = {gid: i for i, (gid, _) in enumerate(groups)}
        ov_edges, seen = [], set()
        for x, y, l in g.edges:
            gx, gy = g.nodes[x]["group"], g.nodes[y]["group"]
            if gx and gy and gx != gy and (gx, gy) not in seen:
                seen.add((gx, gy))
                e = {"id": "o%d" % len(ov_edges), "from": gx, "to": gy, "variant": "default"}
                if l:
                    e["label"] = l
                if idx[gy] < idx[gx]:
                    e["variant"], e["role"] = "dashed", "return"
                ov_edges.append(e)
        diag = diagram(prefix + "journey overview", ov_nodes, ov_edges, [{"id": "phases", "label": "Phases"}],
                       [gid for gid, _ in groups], {"entries": {"frontend": {"label": "Phase"}}}, "overview.html")
        jobs.append(("overview", diag))
    for gid, title in groups:
        jn, je, lanes, main_path = build_phase(g, gid, short_phase(title), a, pillar_map)
        diag = diagram(prefix + short_phase(title), jn, je, lanes, main_path, legend_for(jn, names, pillar_map), "%s.html" % slugify(short_phase(title)))
        jobs.append((slugify(short_phase(title)), diag))

    bin_path = None if a.no_run else find_archify()
    if not a.no_run and not bin_path:
        print("archify not found (set ARCHIFY_BIN); writing .json only")
    ok_all = True
    for slug, diag in jobs:
        jp = os.path.join(a.out, slug + ".json")
        diag["meta"]["output"] = slug + ".html"
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(diag, f, indent=2, ensure_ascii=False)
            f.write("\n")
        if bin_path:
            ok, msgs = finalize(bin_path, jp, os.path.join(a.out, slug + ".html"), os.path.abspath(a.out))
            ok_all = ok_all and ok
            print("%-22s %s" % (slug, "ok" if ok else "FAILED: " + "; ".join(msgs)[:300]))
        else:
            print("%-22s json written" % slug)
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
