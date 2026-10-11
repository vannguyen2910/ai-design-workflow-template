# Findings

*Người dùng thật đã làm gì: task success, thời gian, lỗi và mức hài lòng, đặt cạnh baseline.*

> **Cách điền:** mỗi evidence (một test hoặc nghiên cứu) là một file riêng trong `hub/evidence/`, ghi rõ nó kiểm chứng hypothesis nào và đo metric nào; bảng bên dưới do AI cập nhật từ các file đó. Báo cáo kết quả so với baseline. Kiểm tra mọi phân tích có AI hỗ trợ với ghi chú hoặc bản ghi gốc. Copy từ [`work/deliver/findings.md`](../work/deliver/findings.md).

> **Quan trọng:** kết quả dưới đây từ vòng test **mô phỏng** (E1), không phải người thật. Chúng là hypothesis cần xác nhận.

## Evidence

<!-- generated:evidence (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Mã | Evidence | Kiểm chứng | Đo bằng |
|---|---|---|---|
| [E1](evidence/E1.md) | Usability test điều phối, mô phỏng (ba persona do người nghiên cứu đóng vai) | H1, H2, H3, H4, H5, H6 | M2, M3 |
| [E2](evidence/E2.md) | Usability test không điều phối, 8 đến 12 người (đã lên kế hoạch, chưa chạy) | H1, H2, H3, H4, H5, H6 | M1, M2, M3 |
<!-- /generated -->

## Results against the baseline

| Metric | Baseline | Result | Met? |
|---|---|---|---|
| M1: task success | chưa có | T1, T2, T4 hoàn thành; T3 bằng đường vòng; T5 bị chặn | no |
| M2: SEQ | chưa có | 4,6/7 | no |
| M3: SUS | chưa có | 69,2/100 | yes (mô phỏng, chỉ mang tính tham khảo) |

## Findings, weighted by importance

Hai phát hiện **Critical**, cùng một nguyên nhân: thiếu mẫu tương tác "tìm một người cụ thể và mời". Nó khiến hai flow độc lập (Connect và chia sẻ nhật ký) cùng thất bại. Hai phát hiện **Major**: danh sách người địa phương trộn nhiều thành phố; bộ phân tích lịch trình AI không sắp vào cấu trúc ngày. Còn lại là Minor và Cosmetic. Đầy đủ: [`work/deliver/findings.md`](../work/deliver/findings.md).

## What changed because of this

Cần thiết kế một mẫu "tìm người và mời" dùng chung (chưa thực hiện). Thêm vào [case log](../reference/case-log.md) khi quyết định. Phải chạy lại với người thật trước khi dùng kết quả để quyết định.
