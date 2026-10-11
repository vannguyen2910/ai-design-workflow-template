# Options, flows and prototype

*Điều đã khám phá, điều đã chọn, và mỗi design decision kèm lý do.*

> **Cách điền:** viết mỗi design decision thành một file trong `decisions/` (D1, D2...); bảng bên dưới do AI dựng từ các file đó. Ghi decision kiểm tra hypothesis nào, theo hoặc kéo ngược principle nào. Decision không có user need phía sau sẽ hiện ở warnings của [Overview](README.md).

## Directions explored

Ba hướng định vị: lập kế hoạch dẫn đầu, khám phá bản địa dẫn đầu, nhật ký dẫn đầu. **Chọn:** khám phá là cửa vào, lập kế hoạch là hook định vị; nhật ký và kết nối là trụ hỗ trợ. Chi tiết và lý do gác lại hai hướng còn lại: [`03-develop/options.md`](../03-develop/options.md). *(Ba hướng được rút ra từ các "open tension" của dự án gốc, không phải một bước chọn hướng chính thức.)*

## Flows and content

Hành trình đầu cuối theo bốn giai đoạn của chuyến đi: Onboarding, Pre-trip, In-destination, Post-trip. Sơ đồ: [`reference/08_E2E_User_Flow.md`](../reference/08_E2E_User_Flow.md). Information architecture (giả thuyết trước card sort): xem tài liệu [Information architecture và card sort](artifacts/ia-sitemap/index.md) trong tab Tài liệu.

## Prototype

Prototype high-fidelity mobile, 32 màn hình, 4 flow: [`03-develop/prototype/`](../03-develop/prototype/). Đây là tài liệu tham chiếu cho developer, không phải production code.

## Design decisions

<!-- generated:decisions (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| ID | Decision | Tests | Follows | Pulls against |
|---|---|---|---|---|
| [D1](decisions/D1.md) | Tab Explore mở ở mode Near Me; Country và Map là cách khám phá xa hơn | H2 | — | — |
| [D2](decisions/D2.md) | Khách duyệt mọi mode không cần tài khoản; chỉ đòi đăng ký khi Save hoặc Connect | H3 | — | — |
| [D3](decisions/D3.md) | Hiện crowd signal (xanh, hổ phách, đỏ) thay cho huy hiệu độ phổ biến | H2 | — | — |
| [D4](decisions/D4.md) | Lưu một chạm từ bất kỳ tip nào vào shortlist của chuyến đi | H1 | — | — |
| [D5](decisions/D5.md) | Cho nhập lịch trình do AI viết vào kế hoạch chuyến đi | H1 | — | — |
| [D6](decisions/D6.md) | Kết nối theo khung trao đổi hai chiều, hồ sơ xác minh; nhắn tin chỉ mở sau khi cả hai quan tâm | H4 | — | — |
| [D7](decisions/D7.md) | Nhật ký tự ghi, riêng tư mặc định, chỉ chia sẻ với người được chọn | H5, H6 | — | — |
<!-- /generated -->
