# Options, flows and prototype

*Điều đã khám phá, điều đã chọn, và mỗi design decision kèm lý do.*

> **Cách điền:** ghi mỗi design decision thành một file riêng trong `insights/decisions/`; bảng bên dưới do AI cập nhật từ các file đó. Ghi decision kiểm tra hypothesis nào, theo hoặc kéo ngược principle nào. Decision không có user need phía sau sẽ hiện ở warnings của [Overview](../README.md).

## Directions explored

Ba hướng định vị: lập kế hoạch dẫn đầu, khám phá bản địa dẫn đầu, nhật ký dẫn đầu. **Chọn:** khám phá là cửa vào, lập kế hoạch là hook định vị; nhật ký và kết nối là trụ hỗ trợ. Chi tiết và lý do gác lại hai hướng còn lại: [`work/options.md`](../work/options.md). *(Ba hướng được rút ra từ các "open tension" của dự án gốc, không phải một bước chọn hướng chính thức.)*

## Flows and content

Hành trình đầu cuối theo bốn giai đoạn của chuyến đi: Onboarding, Pre-trip, In-destination, Post-trip. Sơ đồ: [`work/original-docs/08_E2E_User_Flow.md`](../work/original-docs/08_E2E_User_Flow.md). Information architecture (hypothesis trước card sort): xem tài liệu [Information architecture và card sort](../work/ia-sitemap/index.md) trong mục Tài liệu.

## Prototype

Prototype high-fidelity mobile, 32 màn hình, 4 flow: [`work/prototype/`](../work/prototype/). Đây là tài liệu tham chiếu cho developer, không phải production code.

## Design decisions

<!-- generated:decisions (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Mã | Decision | Kiểm chứng | Theo principle | Đi ngược principle |
|---|---|---|---|---|
| [D1](../insights/decisions/D1.md) | Tab Explore mở ở mode Near Me; Country và Map là cách khám phá xa hơn | H2 | — | — |
| [D2](../insights/decisions/D2.md) | Khách duyệt mọi mode không cần tài khoản; chỉ đòi đăng ký khi Save hoặc Connect | H3 | — | — |
| [D3](../insights/decisions/D3.md) | Hiện crowd signal (xanh, hổ phách, đỏ) thay cho huy hiệu độ phổ biến | H2 | — | — |
| [D4](../insights/decisions/D4.md) | Lưu một chạm từ bất kỳ tip nào vào shortlist của chuyến đi | H1 | — | — |
| [D5](../insights/decisions/D5.md) | Cho nhập lịch trình do AI viết vào kế hoạch chuyến đi | H1 | — | — |
| [D6](../insights/decisions/D6.md) | Kết nối theo khung trao đổi hai chiều, hồ sơ xác minh; nhắn tin chỉ mở sau khi cả hai quan tâm | H4 | — | — |
| [D7](../insights/decisions/D7.md) | Nhật ký tự ghi, riêng tư mặc định, chỉ chia sẻ với người được chọn | H5, H6 | — | — |
<!-- /generated -->
