# Demo project: Travel Buddy

| | |
|---|---|
| Tên dự án | Travel Buddy |
| Agreement status | not available |

Đây là một dự án thật, đã chạy qua các giai đoạn từ Discover tới Test: **Travel Buddy**, một app đồng hành du lịch. Nó được dùng làm dự án mẫu để bạn thấy một workspace đầy đủ trông như thế nào, và thấy **chỗ nào còn khoảng trống**.

Dự án gốc được làm trước khi có quy trình AI-assisted của workspace này. Vì vậy một số file ghi rõ "không áp dụng", và một số gate ở trạng thái `open` hoặc `failed`. Đó là chủ ý: một dự án mẫu trung thực hữu ích hơn một dự án được dọn cho đẹp.

## Start here

1. Bấm đúp `index.html` để xem hub trong trình duyệt. Bắt đầu ở mục **Overview**, rồi mở **Insights** (chế độ Cây) để đi từ một decision ngược về nhu cầu của người dùng.
2. Đọc `context/product-and-users.md` để biết dự án là gì.
3. Mở `standards/gates.md` để thấy gate nào đạt, gate nào chưa, và vì sao.

## What is in here

| Phần | Nội dung | Dùng cho giai đoạn |
|---|---|---|
| `context/*.md` | Tổng quan dự án, người dùng, design system, câu hỏi mở | Setup |
| `work/scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` | Scope, tổng hợp tiếng nói người dùng, phân tích đối thủ | Discover |
| `work/sources/anonymised/` | Tài liệu nghiên cứu gốc: hypothesis, khảo sát, hướng dẫn phỏng vấn, tổng hợp, đối thủ | Discover |
| `work/problem-brief.md` | Problem brief | Define |
| `work/options.md`, `alignment.md`, `work/wireframes/` | Các hướng, alignment, wireframe | Develop |
| `work/test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` | Kế hoạch test, findings, handoff, kế hoạch đo | Deliver |
| `insights/` | 5 nhu cầu, 6 hypothesis, 7 decision, 2 evidence, 7 finding, 5 metric | Mọi giai đoạn |
| `stages/README.md` | Bảng bảy trang giai đoạn (scope, evidence, problem brief, develop, alignment, findings, handoff); mỗi trang tự dựng từ `work/` và `insights/` | Mọi giai đoạn |
| `standards/` | Gates, principle checks, severity levels, case log | Mọi giai đoạn |
| `_skills/` | Các bước làm việc với AI (step card) | Mọi giai đoạn |
| `work/original-docs/` | Tài liệu gốc của giai đoạn Define đến Test (personas, solution pool, flow, IA, PRD, test plan, findings) | Tham khảo |

## What this project teaches (including by example of what is missing)

- **Truy vết đầy đủ.** Mọi decision nối được về một hypothesis và một nhu cầu có bằng chứng.
- **Bằng chứng yếu.** Nghiên cứu mới có 13 phản hồi khảo sát và một cuộc phỏng vấn; vòng usability test duy nhất là **mô phỏng** (AI đóng vai người dùng). Hub đánh dấu điều này ở mọi hypothesis, và gate 4a ở trạng thái `failed`.
- **Thiếu design principle.** Chưa có principle checks, nên mọi decision thiếu cột "Theo principle".
- **Không có người đồng ký.** Stakeholder được mô phỏng, nên agreement status là `not available`.

## Conventions in this demo

- `RH1`..`RH10`: research hypothesis của dự án gốc (`H1`..`H10` trong `01_Research_Hypotheses.md`).
- `SP-D1`, `SP-P3`...: ID trong Solution Pool gốc (`work/original-docs/07_Solution_Pool.md`).
- `O`, `H`, `D`, `E`, `M` trong `insights/`: item của workspace (Opportunity, Hypothesis, Decision, Evidence, Metric).
- Tài liệu gốc viết bằng tiếng Anh và giữ nguyên; phần tổng hợp trong working file viết bằng tiếng Việt.
- Tên công cụ AI, tên chủ dự án, thành phố của người phỏng vấn và liên kết prototype riêng tư đã được gỡ khỏi bản sao trong `work/original-docs/` và `sources/`.

## Rules

1. **Đừng chép nội dung của dự án mẫu vào dự án thật của bạn.**
2. **Chỉ coi số liệu khảo sát là định hướng:** mẫu nhỏ (13), lệch về châu Á và người trẻ.
3. **Đừng coi kết quả test mô phỏng là bằng chứng.** Xem `work/findings.md`.
