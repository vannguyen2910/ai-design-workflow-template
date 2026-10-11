# Design system notes

*Viết khi bắt đầu dựng prototype, theo dạng AI coding tool đọc được. Ngắn, cụ thể, không có đoạn văn nào cần suy diễn.*

## Where the source of truth lives
`work/original-docs/10_Prototype_Plan.md`, mục 2 (Design Direction & Design System). Prototype: `work/prototype/`.

## Tokens
- Colour: `--primary` #5DB85C (CTA chính, verified badge); `--primary-lime` #C4E03A (nav đang chọn, chip nổi bật); `--primary-dark` #3A7A39 (trạng thái nhấn); `--nav-bg` #1C1C2E (thanh điều hướng dưới); `--surface` #FFFFFF; `--bg` #F7F7F7; `--text` #111111; `--text-secondary` #555555; `--border` #EBEBEB; `--warning` #F5A623 (crowd signal cao); `--danger` #E74C3C (an toàn, report/block, lỗi)
- Type: DM Sans (dự phòng Inter, SF Pro Text). Display 32–38px/800; screen title 24px/700; section 18px/600; card title 16px/600; body 14px/400; caption 12px/500; button 15px/600
- Spacing và radius: đơn vị gốc 4px (4, 8, 16, 24, 32, 48). Photo card 20px; card 16px; bottom sheet 24px (hai góc trên); CTA và chip dạng pill (50px); input 14px

## Components
| Component | States it has | Rules |
|---|---|---|
| Tip card (ảnh phủ) | mặc định, đã lưu | Có crowd signal badge; chữ trên ảnh dùng gradient để đạt tương phản |
| Map pin | local favourite (xanh), popular (hổ phách), very touristy (đỏ) | Gom thành cụm khi gần nhau; chạm để mở peek card |
| Bottom sheet | thu gọn (peek), mở | Dùng cho peek card, safety context, sign-up gate |
| Filter chip | mặc định, đang chọn | Dạng pill; phải giữ nguyên khi đổi mode |

## Patterns
Mobile 390 × 844px. Thanh điều hướng tối ở dưới, nội dung nền sáng và định hướng ảnh. Explore có ba mode (Near Me, Country, Map) dùng chung một hệ thống filter.

## Do and do not
- Do: để người xem duyệt tip mà không cần tài khoản; chỉ đòi đăng ký khi Save hoặc Connect
- Do not: dùng huy hiệu độ phổ biến; thay vào đó dùng crowd signal

## Accessibility rules
Xem `accessibility-rules.md`. Dự án này chưa kiểm tra riêng cho từng component ngoài yêu cầu tương phản trên ảnh phủ.
