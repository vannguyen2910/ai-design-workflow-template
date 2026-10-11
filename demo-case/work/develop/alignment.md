# Alignment check

*Cuối giai đoạn Develop. Mỗi decision có lần ngược được về một user need và đạt các principle không? bảng alignment nằm ở `hub/README.md`; file này giữ phần audit và verdict của bạn.*

## Alignment table
*Dán hoặc dẫn link bảng từ `hub/README.md`. Ghi lại mọi decision không có user need phía sau, mọi opportunity không có decision, mọi hypothesis không có test.*

Xem [`../hub/README.md`](../../hub/README.md) hoặc mục Insights trong `index.html`. Với bảy decision và sáu hypothesis hiện có, mọi decision đều nối được về một hypothesis và một nhu cầu. Hai chỗ còn thiếu:

- **Hai hypothesis chưa có test với người thật.** Vòng test duy nhất là mô phỏng (E1); vòng không điều phối (E2) mới ở dạng kế hoạch.
- **Mười principle chưa có câu hỏi có/không**, nên cột "Theo principle" của mọi decision trống.

## Principle audit (top three decisions)
*AI lập luận mỗi decision vi phạm principle ở đâu; bạn quyết định.*

| Decision | Principle | Passes? | Reason |
|---|---|---|---|
| | | | Chưa làm: cần viết `reference/principle-checks.md` trước |

## Verdicts
| Finding | Fix / accept as a recorded trade-off / cut | Reason |
|---|---|---|
| Mười principle chưa có câu hỏi có/không | Fix | Viết principle checks cho Travel Buddy rồi chấm lại ba decision quan trọng nhất (D2, D6, D7) |
| Một số hypothesis chưa có test với người thật | Accept for now | Đã có kế hoạch test không điều phối (E2); chạy trước khi bàn giao |
