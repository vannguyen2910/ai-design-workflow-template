# Alignment check

*Cuối giai đoạn Develop. Mỗi decision có lần ngược được về một user need và đạt các principle không? bảng alignment nằm ở `hub/README.md`; file này giữ phần audit và verdict của bạn.*

## Alignment table
*Dán hoặc dẫn link bảng từ `hub/README.md`. Ghi lại mọi decision không có user need phía sau, mọi opportunity không có decision, mọi hypothesis không có test.*

Xem [`../hub/README.md`](../hub/README.md) hoặc tab Truy vết trong `index.html`. Với bảy decision và sáu hypothesis hiện có, mọi decision đều nối được về một hypothesis và một nhu cầu. Hai chỗ còn thiếu:

- **Hai hypothesis chưa có bài kiểm tra với người thật.** Vòng test duy nhất là mô phỏng (T1); vòng không điều phối (T2) mới ở dạng kế hoạch.
- **Mười nguyên tắc chưa có câu hỏi có/không**, nên cột "Theo nguyên tắc" của mọi decision trống.

## Principle audit (top three decisions)
*AI lập luận mỗi decision vi phạm principle ở đâu; bạn quyết định.*

| Decision | Principle | Passes? | Reason |
|---|---|---|---|
| | | | Chưa làm: cần viết `00-context/principle-checks.md` trước |

## Verdicts
| Finding | Fix / accept as a recorded trade-off / cut | Reason |
|---|---|---|
| Mười nguyên tắc chưa có câu hỏi có/không | Fix | Viết principle checks cho Travel Buddy rồi chấm lại ba decision quan trọng nhất (D2, D6, D7) |
| Một số hypothesis chưa có test với người thật | Accept for now | Đã có kế hoạch test không điều phối (T2); chạy trước khi bàn giao |
