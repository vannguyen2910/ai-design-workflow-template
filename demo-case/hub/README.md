# Overview · Knowledge Hub

Case ở một cái nhìn: mỗi gate đang ở đâu, và mỗi decision lần ngược về brief như thế nào.

> **Cách điền:** bạn chỉ sửa tên case, agreement status và phần narrative ở các trang tuần. Bảng Gates, bảng alignment và Warnings do AI dựng từ các file item và `gates.md` (xem [`how-the-hub-works.md`](how-the-hub-works.md)). Đây là hub của dự án mẫu Travel Buddy.

## Case

| | |
|---|---|
| Tên case | Travel Buddy |
| Agreement status | not available *(agreed / pending / not available)* |

## Gates

<!-- generated:gates (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| Gate | Name | Status |
|---|---|---|
| Discover | Question + evidence | open (2 trên 3 check passed) |
| Define | Evidence + agreement | open (3 trên 4 check passed) |
| Develop | Alignment | open (1 trên 4 check passed) |
| Deliver | Real users + buildability | failed (0 trên 4 check passed) |
<!-- /generated -->

Status của từng check được đặt ở [`gates.md`](gates.md).

## Alignment table

Mỗi dòng là một design decision. Ô ghi **missing** là chỗ chưa nối được về hypothesis, nhu cầu hoặc test; nên xử lý trước gate Develop.

<!-- generated:alignment (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
| Decision | Tests (hypothesis) | Serves (opportunity) | Test | Follows | Pulls against |
|---|---|---|---|---|---|
| [D1](D1.md) | [H2](H2.md) | [O2](O2.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D2](D2.md) | [H3](H3.md) | [O5](O5.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D3](D3.md) | [H2](H2.md) | [O2](O2.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D4](D4.md) | [H1](H1.md) | [O1](O1.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D5](D5.md) | [H1](H1.md) | [O1](O1.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D6](D6.md) | [H4](H4.md) | [O4](O4.md) | [T1](T1.md), [T2](T2.md) |  |  |
| [D7](D7.md) | [H5](H5.md), [H6](H6.md) | [O3](O3.md) | [T1](T1.md), [T2](T2.md) |  |  |
<!-- /generated -->

P1 đến P10 là các principle trong [`learnings/context-principle-checks.md`](../learnings/context-principle-checks.md).

## Warnings

Verdict của bạn cho từng warning (sửa, chấp nhận như trade-off, hoặc cắt) viết ở [`05-alignment.md`](05-alignment.md).

<!-- generated:warnings (không sửa tay; dựng lại bằng tools/step-refresh-hub.md) -->
- **Test này dùng người mô phỏng, không phải người dùng thật: chưa tính là bằng chứng:** T1
- **Test này mới ở dạng kế hoạch, chưa chạy:** T2
- **Hypothesis này chưa có bằng chứng từ người dùng thật:** H1, H2, H3, H4, H5, H6
- **Principle chưa có câu hỏi có/không để kiểm tra:** P1, P2, P3, P4, P5, P6, P7, P8, P9, P10
<!-- /generated -->


## Pages

| Page | Giai đoạn | Nội dung | Copy từ |
|---|---|---|---|
| [Scope](01-scope.md) | Discover | Business question, outcome, agreement | `learnings/discover-scope.md` |
| [Evidence](02-evidence.md) | Discover | Điều đã học từ nguồn, mỗi claim một nguồn | `learnings/discover-user-voice-synthesis.md`, `competitor-analysis.md` |
| [Problem brief](03-problem-brief.md) | Define | Opportunity, hypothesis, metric, principle | `learnings/define-problem-brief.md` |
| [Options, flows, prototype](04-develop.md) | Develop | Các hướng đã khám phá, decision | `learnings/develop-options.md`, `prototype/` |
| [Alignment check](05-alignment.md) | Develop | Principle audit, verdict | `learnings/develop-alignment.md` |
| [Findings](06-findings.md) | Deliver | Kết quả test với người dùng | `learnings/deliver-findings.md` |
| [Handoff and measurement](07-handoff.md) | Deliver | Handoff pack, measurement plan | `learnings/deliver-handoff.md`, `measurement-plan.md` |
| [Case log](../case-log.md) | mọi giai đoạn | Mỗi decision một dòng | `case-log.md` ở folder gốc của case |
