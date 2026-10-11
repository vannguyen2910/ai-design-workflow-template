# Findings

*Giai đoạn Deliver, sau khi test. Người dùng thật đã làm gì. AI có thể giúp phân tích; kiểm tra từng finding với ghi chú hoặc bản ghi.*

> **Đọc kỹ trước khi dùng:** vòng test này là **mô phỏng**. Người nghiên cứu (qua một AI tool) đóng vai từng persona trên prototype thật, thay vì dùng người tham gia độc lập. Theo nguyên tắc của workspace (AI không đóng vai người dùng), kết quả dưới đây chỉ là **giả thuyết cần xác nhận** và **không** thoả gate 4a. Nguyên văn phần giới hạn: `reference/13_Simulated_Usability_Findings.md`, mục 6.

## Results against the baseline
| Metric | Baseline | Result | Met? |
|---|---|---|---|
| Task success | chưa có | T1, T2, T4 hoàn thành; T3 hoàn thành bằng đường vòng; T5 bị chặn | không (2 trên 5 task có vấn đề nghiêm trọng) |
| SEQ trung bình | chưa có | 4,6/7 (T1 6, T2 6, T3 3, T4 7, T5 1) | không (mục tiêu từ 5,5) |
| SUS trung bình | chưa có | 69,2/100 (Aisha 80; Marco 62,5; Ji-yeon 65) | có, nhưng bị kéo lên bởi một lượt chạy tốt và chỉ là mô phỏng |

## Findings, weighted by importance
*Xếp theo mức độ quan trọng, không theo số lần được nhắc. Dẫn mỗi finding về một bản ghi hoặc ghi chú.*

| Finding | Severity | Evidence | What changes |
|---|---|---|---|
| Màn Connect → Browse không có tìm kiếm hay lọc; chỉ tìm được một người địa phương cụ thể bằng cách lần ngược qua tip của họ | **Critical** | Ghi chú phiên Connect, màn S22 | Thêm tìm kiếm theo tên và lời mời (khuyến nghị #1) |
| Màn chia sẻ nhật ký chỉ có danh sách cố định 3 người, không tìm hay mời theo tên; không chọn được người ngoài danh sách | **Critical** | Ghi chú phiên Journal, màn S30 | Thêm tìm người nhận và mời (khuyến nghị #2) |
| Danh sách Browse trộn người địa phương từ nhiều thành phố, không có lọc theo vị trí hay chuyến đi | **Major** | Ghi chú phiên Connect, S22 | Lọc theo điểm đến của chuyến đi (khuyến nghị #3) |
| Bộ phân tích lịch trình AI giữ nhãn ngày làm một phần tên địa điểm và không sắp vào cấu trúc ngày đã có | **Major** | Ghi chú phiên Plan, S17 và S18 | Sắp vào ngày tương ứng (khuyến nghị #4) |
| Badge "X% match" không giải thích nó dựa trên gì | Minor | Quan sát trực tiếp, S22 | Giải thích hoặc bỏ (khuyến nghị #6) |
| Mục nhập từ AI hiện ảnh xám và dấu gạch ngang thay vì thời lượng, trông kém chất lượng hơn tip lưu thủ công | Minor | Quan sát trực tiếp, S18 | Hiện ảnh và ước lượng thời lượng (khuyến nghị #9) |
| Nhãn "Local resident" trong khi task nói "another traveler" | Cosmetic | Phiên Discover, S10 | Rà lại ngôn ngữ (khuyến nghị #10) |

*Hai finding Critical có chung một nguyên nhân: thiếu mẫu tương tác "tìm một người cụ thể và mời". Nên sửa như một việc, không phải hai.*

## What changed because of this
- Gom hai finding Critical thành một việc: thiết kế mẫu **tìm người và mời** dùng chung cho Connect và chia sẻ nhật ký. Chưa thực hiện (chưa có quyết định ghi trong `hub/decisions/`).
- Cổng đăng ký (sign-up gate) không được kiểm tra hợp lệ trong vòng này: prototype xác thực tức thì, không có bước email hay mật khẩu, nên mức chấp nhận bị đánh giá quá cao.
- Kết quả first-click của T1 có thể bị thổi phồng vì màn chọn điểm đến đã tô sẵn "Thailand"; coi là cận trên.
- **Việc cần làm trước khi coi là bằng chứng:** chạy lại với người tham gia thật (T2 trong `hub/tests/`).
