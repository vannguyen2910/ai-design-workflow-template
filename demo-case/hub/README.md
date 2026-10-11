# Overview · Knowledge Hub

Case ở một cái nhìn: mỗi gate đang ở đâu, và mỗi decision lần ngược về brief như thế nào.

> **Trang này làm gì:** cho thấy dự án đang ở đâu và decision nào chưa có lý do phía sau. Bạn chỉ cần điền tên dự án, tình trạng đồng thuận và phần kể chuyện ở các trang giai đoạn. Các bảng bên dưới là phần tự động: nhờ AI tool cập nhật, đừng sửa tay (xem [`how-the-hub-works.md`](how-the-hub-works.md)). Đây là hub của dự án mẫu Travel Buddy.

## Case

| | |
|---|---|
| Tên case | Travel Buddy |
| Agreement status | not available *(agreed / pending / not available)* |

## Gates

<!-- generated:gates (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Gate | Name | Status |
|---|---|---|
| Discover | Question + evidence | open (2 trên 3 check passed) |
| Define | Evidence + agreement | open (3 trên 4 check passed) |
| Develop | Alignment | open (1 trên 4 check passed) |
| Deliver | Real users + buildability | failed (0 trên 4 check passed) |
<!-- /generated -->

Status của từng check được đặt ở [`gates.md`](../reference/gates.md).

## Alignment table

Mỗi dòng là một design decision. Ô ghi **missing** là chỗ chưa nối được về hypothesis, nhu cầu hoặc evidence; nên xử lý trước gate Develop.

<!-- generated:alignment (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Decision | Tests (hypothesis) | Serves (opportunity) | Test | Follows | Pulls against |
|---|---|---|---|---|---|
| [D1](decisions/D1.md) | [H2](hypotheses/H2.md) | [O2](opportunities/O2.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D2](decisions/D2.md) | [H3](hypotheses/H3.md) | [O5](opportunities/O5.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D3](decisions/D3.md) | [H2](hypotheses/H2.md) | [O2](opportunities/O2.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D4](decisions/D4.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D5](decisions/D5.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D6](decisions/D6.md) | [H4](hypotheses/H4.md) | [O4](opportunities/O4.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
| [D7](decisions/D7.md) | [H5](hypotheses/H5.md), [H6](hypotheses/H6.md) | [O3](opportunities/O3.md) | [E1](evidence/E1.md), [E2](evidence/E2.md) |  |  |
<!-- /generated -->

P1 đến P10 là các principle trong [`reference/principle-checks.md`](../reference/principle-checks.md).

## Warnings

Verdict của bạn cho từng warning (sửa, chấp nhận như trade-off, hoặc cắt) viết ở [`05-alignment.md`](05-alignment.md).

<!-- generated:warnings (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
- **Evidence này dùng người mô phỏng, không phải người dùng thật: chưa tính là bằng chứng thật:** E1
- **Evidence này mới ở dạng kế hoạch, chưa chạy:** E2
- **Hypothesis này chưa có bằng chứng từ người dùng thật:** H1, H2, H3, H4, H5, H6
- **Principle chưa có câu hỏi có/không để kiểm tra:** P1, P2, P3, P4, P5, P6, P7, P8, P9, P10
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
