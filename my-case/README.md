# Project: [tên dự án]

Trang đầu của dự án. Điền **Project card** trước, rồi chọn việc tiếp theo ở bảng bên dưới.

## Project card

| | |
|---|---|
| Tên dự án | |
| Câu hỏi của business (một câu) | |
| Giai đoạn hiện tại | Setup / Discover / Define / Develop / Deliver |
| Chủ dự án | |
| Người liên quan (product, business, engineering) | |
| Bắt đầu | |
| Cập nhật lần cuối | |
| Công cụ AI được phép dùng cho dự án này | |
| Agreement status | pending *(agreed / pending / not available)* |
| Quy tắc dữ liệu | Xem `context/data-rules.md` |

<!-- template-only -->
> **Đây là `my-case`, workspace trống.** Đừng điền thẳng vào đây: hãy mở folder workspace bằng AI tool và nói "Tạo một dự án mới tên *tên-dự-án*". Muốn xem một dự án đã làm xong, mở `demo-case`.
<!-- /template-only -->

## Bạn muốn làm gì?

Mở folder này bằng AI tool và nói một câu bình thường.

| Tôi muốn | Nói với AI |
|---|---|
| Ghi sản phẩm và người dùng | "Giúp tôi điền thông tin nền về sản phẩm và người dùng. Hỏi tôi từng câu một." |
| Rút điều học được từ phỏng vấn hoặc khảo sát | "Rút insight từ file *tên-file*. Đề xuất trước, đừng tạo." |
| Ghi một quyết định | "Ghi một quyết định: *một câu*. Lý do: *…*. Chưa chấp nhận." |
| Thêm ảnh, wireframe, prototype | "Thêm các file trong folder *tên-folder* vào báo cáo." |
| Xem tiến độ | Bấm đúp `index.html`, mở tab **Overview** |
| Gửi báo cáo cho người khác | "Đóng gói báo cáo thành một file zip để gửi đi." |

Danh sách đầy đủ nằm ở tab **Guide** trong `index.html`.

## Bốn quy tắc

1. **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `work/sources/_raw-private/`.
2. **Để AI đề xuất trước,** bạn duyệt rồi mới cho tạo.
3. **Bản nháp của AI và bản bạn đã kiểm tra ở hai chỗ riêng.**
4. **Con số chưa ai xác nhận thì ghi `assumed`.**

## Folder nào là gì

| Folder | Có gì |
|---|---|
| `context/` | Sản phẩm là gì, người dùng là ai |
| `work/` | Mọi thứ bạn làm: phân tích, wireframe, prototype |
| `insights/` | Điều đã học và các quyết định |
| `stages/` | Câu chuyện từng giai đoạn (tự dựng, bạn không viết ở đây) |
| `standards/` | Thước đo để kiểm tra công việc |
| `_skills/`, `AGENTS.md` | Các bước và luật cho AI tool, hiếm khi cần mở tay |
| `_personal/` | Ghi chú riêng, không đưa cho AI |
