# Overview · Knowledge Hub

Case ở một cái nhìn: mỗi gate đang ở đâu, và mỗi decision lần ngược về brief như thế nào.

> **Trang này làm gì:** cho thấy dự án đang ở đâu và decision nào chưa có lý do phía sau. Bạn chỉ cần điền tên dự án, tình trạng đồng thuận và phần kể chuyện ở các trang giai đoạn. Các bảng bên dưới là phần tự động: nhờ AI tool cập nhật, đừng sửa tay (xem [`how-the-hub-works.md`](how-the-hub-works.md)). Dữ liệu `[EXAMPLE]` ở đây để bạn thấy hub chạy ra sao. Xoá và thay bằng dữ liệu của bạn.

## Case

| | |
|---|---|
| Tên case | [CASE NAME] |
| Agreement status | pending *(agreed / pending / not available)* |

## Gates

<!-- generated:gates (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Gate | Name | Status |
|---|---|---|
| Discover | Question + evidence | open (0 trên 3 check passed) |
| Define | Evidence + agreement | open (0 trên 4 check passed) |
| Develop | Alignment | open (0 trên 4 check passed) |
| Deliver | Real users + buildability | open (0 trên 4 check passed) |
<!-- /generated -->

Status của từng check được đặt ở [`gates.md`](../reference/gates.md).

## Alignment table

Mỗi dòng là một design decision. Ô ghi **missing** là chỗ chưa nối được về hypothesis, nhu cầu hoặc evidence; nên xử lý trước gate Develop.

<!-- generated:alignment (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Decision | Tests (hypothesis) | Serves (opportunity) | Test | Follows | Pulls against |
|---|---|---|---|---|---|
| [D1](decisions/D1.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [E1](evidence/E1.md) | P1, P6 | |
| [D2](decisions/D2.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [E1](evidence/E1.md) | P1 | **P8** |
| [D3](decisions/D3.md) | **missing** | **missing** | **missing** | | |
<!-- /generated -->

P1 đến P10 là các principle trong [`reference/principle-checks.md`](../reference/principle-checks.md).

## Warnings

Verdict của bạn cho từng warning (sửa, chấp nhận như trade-off, hoặc cắt) viết ở [`05-alignment.md`](05-alignment.md).

<!-- generated:warnings (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
- **Decision chưa nối được về nhu cầu nào của người dùng:** D3
- **Decision đi ngược một principle:** D2 đi ngược P8. Cân nhắc sửa, hoặc ghi lại vì sao chấp nhận.
- **Nhu cầu chưa có design decision nào phục vụ:** O2
- **Hypothesis chưa có test:** H2
- **Hypothesis chưa có metric để biết đúng hay sai:** H2
<!-- /generated -->


## Pages

| Page | Giai đoạn | Nội dung | Copy từ |
|---|---|---|---|
| [Scope](01-scope.md) | Discover | Business question, outcome, agreement | `work/discover/scope.md` |
| [Evidence](02-evidence.md) | Discover | Điều đã học từ nguồn, mỗi claim một nguồn | `work/discover/user-voice-synthesis.md`, `competitor-analysis.md` |
| [Problem brief](03-problem-brief.md) | Define | Opportunity, hypothesis, metric, principle | `work/define/problem-brief.md` |
| [Options, flows, prototype](04-develop.md) | Develop | Các hướng đã khám phá, decision | `work/develop/options.md`, `prototype/` |
| [Alignment check](05-alignment.md) | Develop | Principle audit, verdict | `work/develop/alignment.md` |
| [Findings](06-findings.md) | Deliver | Kết quả test với người dùng | `work/deliver/findings.md` |
| [Handoff and measurement](07-handoff.md) | Deliver | Handoff pack, measurement plan | `work/deliver/handoff.md`, `measurement-plan.md` |
| [Case log](../reference/case-log.md) | mọi giai đoạn | Mỗi decision một dòng | `reference/case-log.md` ở folder gốc của case |
