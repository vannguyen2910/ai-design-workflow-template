# Demo project: Travel Buddy

Đây là một dự án thật, đã chạy qua các giai đoạn từ Discover tới Test: **Travel Buddy**, một app đồng hành du lịch. Nó được dùng làm dự án mẫu để bạn thấy một workspace đầy đủ trông như thế nào, và thấy **chỗ nào còn khoảng trống**.

Dự án gốc được làm trước khi có quy trình AI-assisted của workspace này. Vì vậy một số file ghi rõ "không áp dụng", và một số gate ở trạng thái `open` hoặc `failed`. Đó là chủ ý: một dự án mẫu trung thực hữu ích hơn một dự án được dọn cho đẹp.

## Start here

1. Bấm đúp `index.html` để xem hub trong trình duyệt. Bắt đầu ở tab **Tổng quan**, rồi mở tab **Truy vết** để đi từ một quyết định ngược về nhu cầu của người dùng.
2. Đọc `00-context/product-and-users.md` để biết dự án là gì.
3. Mở `hub/gates.md` để thấy gate nào đạt, gate nào chưa, và vì sao.

## What is in here

| Phần | Nội dung | Dùng cho giai đoạn |
|---|---|---|
| `00-context/` | Tổng quan dự án, người dùng, design system, câu hỏi mở | Setup |
| `01-discover/` | Scope, tổng hợp tiếng nói người dùng, phân tích đối thủ | Discover |
| `01-discover/sources/anonymised/` | Tài liệu nghiên cứu gốc: giả thuyết, khảo sát, hướng dẫn phỏng vấn, tổng hợp, đối thủ | Discover |
| `02-define/` | Problem brief | Define |
| `03-develop/` | Các hướng, alignment, wireframe | Develop |
| `04-deliver/` | Kế hoạch test, findings, handoff, kế hoạch đo | Deliver |
| `hub/` | 5 nhu cầu, 6 giả thuyết, 7 quyết định, 2 bài kiểm tra, 5 chỉ số, 4 gate | Mọi giai đoạn |
| `reference/` | Tài liệu gốc của giai đoạn Define đến Test (personas, solution pool, flow, IA, PRD, test plan, findings) | Tham khảo |

## What this project teaches (including by example of what is missing)

- **Truy vết đầy đủ.** Mọi quyết định nối được về một giả thuyết và một nhu cầu có bằng chứng.
- **Bằng chứng yếu.** Nghiên cứu mới có 13 phản hồi khảo sát và một cuộc phỏng vấn; vòng usability test duy nhất là **mô phỏng** (AI đóng vai người dùng). Hub đánh dấu điều này ở mọi giả thuyết, và gate 4a ở trạng thái `failed`.
- **Thiếu nguyên tắc thiết kế.** Chưa có principle checks, nên mọi quyết định thiếu cột "Theo nguyên tắc".
- **Không có người đồng ký.** Stakeholder được mô phỏng, nên agreement status là `not available`.

## Conventions in this demo

- `RH1`..`RH10`: research hypothesis của dự án gốc (`H1`..`H10` trong `01_Research_Hypotheses.md`).
- `SP-D1`, `SP-P3`...: ID trong Solution Pool gốc (`reference/07_Solution_Pool.md`).
- `O`, `H`, `D`, `T`, `M` trong `hub/`: item của workspace.
- Tài liệu gốc viết bằng tiếng Anh và giữ nguyên; phần tổng hợp trong working file viết bằng tiếng Việt.
- Tên công cụ AI, tên chủ dự án, thành phố của người phỏng vấn và liên kết prototype riêng tư đã được gỡ khỏi bản sao trong `reference/` và `sources/`.

## Rules

1. **Đừng chép nội dung của dự án mẫu vào dự án thật của bạn.**
2. **Chỉ coi số liệu khảo sát là định hướng:** mẫu nhỏ (13), lệch về châu Á và người trẻ.
3. **Đừng coi kết quả test mô phỏng là bằng chứng.** Xem `04-deliver/findings.md`.
