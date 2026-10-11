# Alignment check

*Mỗi decision có lần ngược được về brief và đạt các principle không? Sửa, chấp nhận như một trade-off đã ghi lại, hoặc cắt.*

> **Cách điền:** bảng alignment nằm ở [Overview](README.md). Trang này dành cho principle audit và verdict của bạn cho từng warning. AI soạn nháp audit và lập luận chỗ nào thiết kế vi phạm principle; bạn quyết định. Làm đầy đủ ở [`work/develop/alignment.md`](../work/develop/alignment.md).

## Principle audit

Chưa làm. Cần viết `reference/principle-checks.md` cho Travel Buddy trước, rồi chấm lại ba decision quan trọng nhất (D2, D6, D7).

## Verdict on each warning

| Warning | Verdict | Reason |
|---|---|---|
| Mười principle chưa có câu hỏi có/không | Fix | Cần để chạy principle audit; làm trước khi bàn giao |
| Mọi hypothesis chưa có bằng chứng từ người dùng thật | Accept for now | Đã có kế hoạch test không điều phối (E2); chạy với người thật trước khi coi gate 4a là đạt |
| E1 dùng người mô phỏng | Accept as trade-off | Dùng như pilot để tìm vấn đề sớm, không dùng làm bằng chứng |

## Gate

Bạn có bảo vệ được mọi decision bằng cách chỉ vào brief không? **Về truy vết: có**, mọi decision nối được về một hypothesis và một nhu cầu. **Về bằng chứng: chưa**, vì các hypothesis chưa được kiểm tra với người thật.
