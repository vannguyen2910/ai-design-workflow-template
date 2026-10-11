# Findings

*Người dùng thật đã làm gì: task success, thời gian, lỗi và mức hài lòng, đặt cạnh baseline.*

> **Cách điền:** mỗi evidence (một test hoặc nghiên cứu) là một file riêng trong `insights/evidence/`, ghi rõ nó kiểm chứng hypothesis nào và đo metric nào; bảng bên dưới do AI cập nhật từ các file đó. Báo cáo kết quả so với baseline. Kiểm tra mọi phân tích có AI hỗ trợ với ghi chú hoặc bản ghi gốc. Copy từ [`work/findings.md`](../work/findings.md).

> **Quan trọng:** kết quả dưới đây từ vòng test **mô phỏng** (E1), không phải người thật. Chúng là hypothesis cần xác nhận.

## Evidence

<!-- generated:evidence (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Mã | Evidence | Kiểm chứng | Đo bằng |
|---|---|---|---|
| [E1](../insights/evidence/E1.md) | Usability test điều phối, mô phỏng (ba persona do người nghiên cứu đóng vai) | H1, H2, H3, H4, H5, H6 | M2, M3 |
| [E2](../insights/evidence/E2.md) | Usability test không điều phối, 8 đến 12 người (đã lên kế hoạch, chưa chạy) | H1, H2, H3, H4, H5, H6 | M1, M2, M3 |
<!-- /generated -->

## Results against the baseline

| Metric | Baseline | Result | Met? |
|---|---|---|---|
| M1: task success | chưa có | T1, T2, T4 hoàn thành; T3 bằng đường vòng; T5 bị chặn | no |
| M2: SEQ | chưa có | 4,6/7 | no |
| M3: SUS | chưa có | 69,2/100 | yes (mô phỏng, chỉ mang tính tham khảo) |

## Findings, weighted by importance

*Xếp theo mức severity (từ 4 xuống 0), không theo số lần được nhắc. Thang 0 đến 4 và cách chấm nằm ở [Severity levels](../reference/severity-levels.md); principle bị vi phạm lấy từ [Principle checks](../reference/principle-checks.md). Mỗi finding là một file riêng trong `insights/findings/`.*

<!-- generated:findings (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Mã | Finding | Severity | Principle | Phát hiện trong | Ảnh hưởng | Cách xử lý |
|---|---|---|---|---|---|---|
| [F1](../insights/findings/F1.md) | Màn Connect → Browse không có tìm kiếm hay lọc; chỉ tìm được một người địa phương cụ thể bằng cách lần ngược qua tip của họ | 4 Catastrophe | — | E1 | D6 | Open |
| [F2](../insights/findings/F2.md) | Màn chia sẻ nhật ký chỉ có danh sách cố định 3 người, không tìm hay mời theo tên; không chọn được người ngoài danh sách | 4 Catastrophe | — | E1 | D7 | Open |
| [F3](../insights/findings/F3.md) | Danh sách Browse trộn người địa phương từ nhiều thành phố, không có lọc theo vị trí hay chuyến đi | 3 Major | — | E1 | D6 | Open |
| [F4](../insights/findings/F4.md) | Bộ phân tích lịch trình AI giữ nhãn ngày làm một phần tên địa điểm và không sắp vào cấu trúc ngày đã có | 3 Major | — | E1 | D5 | Open |
| [F5](../insights/findings/F5.md) | Badge “X% match” không giải thích nó dựa trên gì | 2 Minor | — | E1 | D6 | Open |
| [F6](../insights/findings/F6.md) | Mục nhập từ AI hiện ảnh xám và dấu gạch ngang thay vì thời lượng, trông kém chất lượng hơn tip lưu thủ công | 2 Minor | — | E1 | D5 | Open |
| [F7](../insights/findings/F7.md) | Nhãn “Local resident” trong khi task nói “another traveler” | 1 Cosmetic | — | E1 | — | Open |
<!-- /generated -->

## What changed because of this

Cần thiết kế một mẫu "tìm người và mời" dùng chung (chưa thực hiện). Thêm vào [case log](../reference/case-log.md) khi quyết định. Phải chạy lại với người thật trước khi dùng kết quả để quyết định.
