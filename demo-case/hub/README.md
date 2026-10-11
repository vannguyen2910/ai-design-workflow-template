# Overview · Knowledge Hub

Case ở một cái nhìn: mỗi gate đang ở đâu, và mỗi decision lần ngược về brief như thế nào.

> **Cách điền:** bạn chỉ sửa tên case, agreement status và phần narrative ở các trang tuần. Bảng Gates, bảng alignment và Warnings do AI dựng từ các file item và `gates.md` (xem [`how-the-hub-works.md`](how-the-hub-works.md)). Đây là hub của dự án mẫu Travel Buddy.

## Case

| | |
|---|---|
| Tên case | Travel Buddy |
| Agreement status | not available *(agreed / pending / not available)* |

## Gates

<!-- generated:gates (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| Gate | Name | Status |
|---|---|---|
| Discover | Question + evidence | open (2 trên 3 check passed) |
| Define | Evidence + agreement | open (3 trên 4 check passed) |
| Develop | Alignment | open (1 trên 4 check passed) |
| Deliver | Real users + buildability | failed (0 trên 4 check passed) |
<!-- /generated -->

Status của từng check được đặt ở [`gates.md`](gates.md).

## Alignment table

Mỗi dòng là một quyết định thiết kế. Ô ghi **missing** là chỗ chưa nối được về giả thuyết, nhu cầu hoặc bài kiểm tra; nên xử lý trước gate Develop.

<!-- generated:alignment (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| Decision | Tests (hypothesis) | Serves (opportunity) | Test | Follows | Pulls against |
|---|---|---|---|---|---|
| [D1](decisions/D1.md) | [H2](hypotheses/H2.md) | [O2](opportunities/O2.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D2](decisions/D2.md) | [H3](hypotheses/H3.md) | [O5](opportunities/O5.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D3](decisions/D3.md) | [H2](hypotheses/H2.md) | [O2](opportunities/O2.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D4](decisions/D4.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D5](decisions/D5.md) | [H1](hypotheses/H1.md) | [O1](opportunities/O1.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D6](decisions/D6.md) | [H4](hypotheses/H4.md) | [O4](opportunities/O4.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
| [D7](decisions/D7.md) | [H5](hypotheses/H5.md), [H6](hypotheses/H6.md) | [O3](opportunities/O3.md) | [T1](tests/T1.md), [T2](tests/T2.md) |  |  |
<!-- /generated -->

P1 đến P10 là các principle trong [`00-context/principle-checks.md`](../00-context/principle-checks.md).

## Warnings

Verdict của bạn cho từng warning (sửa, chấp nhận như trade-off, hoặc cắt) viết ở [`05-alignment.md`](05-alignment.md).

<!-- generated:warnings (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
- **Bài kiểm tra này dùng người mô phỏng, không phải người dùng thật: chưa tính là bằng chứng:** T1
- **Bài kiểm tra này mới ở dạng kế hoạch, chưa chạy:** T2
- **Giả thuyết này chưa có bằng chứng từ người dùng thật:** H1, H2, H3, H4, H5, H6
- **Nguyên tắc chưa có câu hỏi có/không để kiểm tra:** P1, P2, P3, P4, P5, P6, P7, P8, P9, P10
<!-- /generated -->


## Pages

| Page | Giai đoạn | Nội dung | Copy từ |
|---|---|---|---|
| [Scope](01-scope.md) | Discover | Business question, outcome, agreement | `01-discover/scope.md` |
| [Evidence](02-evidence.md) | Discover | Điều đã học từ nguồn, mỗi claim một nguồn | `01-discover/user-voice-synthesis.md`, `competitor-analysis.md` |
| [Problem brief](03-problem-brief.md) | Define | Opportunity, hypothesis, metric, principle | `02-define/problem-brief.md` |
| [Options, flows, prototype](04-develop.md) | Develop | Các hướng đã khám phá, decision | `03-develop/options.md`, `prototype/` |
| [Alignment check](05-alignment.md) | Develop | Principle audit, verdict | `03-develop/alignment.md` |
| [Findings](06-findings.md) | Deliver | Kết quả test với người dùng | `04-deliver/findings.md` |
| [Handoff and measurement](07-handoff.md) | Deliver | Handoff pack, measurement plan | `04-deliver/handoff.md`, `measurement-plan.md` |
| [Case log](../case-log.md) | mọi giai đoạn | Mỗi quyết định một dòng | `case-log.md` ở folder gốc của case |
