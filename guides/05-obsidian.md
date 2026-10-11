# Obsidian

Guide này **không bắt buộc**. Hub dùng được trong mọi công cụ mở được folder (xem [`02-set-up-your-case.md`](02-set-up-your-case.md)). Obsidian là một lựa chọn thêm khi bạn muốn nhìn quan hệ giữa decision, hypothesis và test bằng hình, và có bảng theo loại mà không cần chạy script.

## Setup

1. Cài Obsidian từ [obsidian.md](https://obsidian.md) (miễn phí cho dùng cá nhân). Cần bản **1.9 trở lên** để dùng được Bases.
2. Mở Obsidian và chọn **Open folder as vault**. (Vault là cách Obsidian gọi một folder mà nó quản lý.)
3. Chọn **folder case của bạn** (ví dụ `onboarding-redesign`). Đừng chọn folder gốc của workspace.
4. Obsidian sẽ tạo thêm folder `.obsidian/` trong case folder để lưu cài đặt. Bạn không cần đụng vào nó.
5. Mở **Settings**, chọn **Core plugins**, và bật **Bases** nếu nó chưa bật.

Obsidian có thể hỏi bạn có muốn bật "community plugins". Bạn không cần bật chúng.

## What you get

| Tính năng | Dùng để | Làm thế nào |
|---|---|---|
| **Bảng theo loại** | Xem mọi decision, hypothesis, test cùng lúc | Mở `insights/traceability.base`, rồi chuyển giữa các tab: Opportunities, Hypotheses, Decisions, Tests, Metrics |
| **Properties** | Nối một item với item khác mà không phải gõ mã | Mở một file item, bấm vào dòng `tests`, gõ `[[`, rồi chọn file trong danh sách |
| **Backlinks** | Thấy những item nào đang nối tới item này | Mở khung Backlinks ở thanh bên phải khi đang mở một item |
| **Graph view** | Nhìn cả mạng quan hệ trong một hình | `Cmd+G` (Mac) hoặc `Ctrl+G` (Windows) |
| **Search** | Tìm theo mã hoặc từ khoá | `Cmd+Shift+F` hoặc `Ctrl+Shift+F`, ví dụ `file:/^D\d+/ P8` (chỉ các file decision) |

## Make the graph readable

Mặc định Graph view hiện cả các file làm việc. Để chỉ thấy hub:

1. Trong Graph view, mở khung **Filters** và gõ `path:insights` vào ô tìm kiếm.
2. Mở **Groups** và thêm một group cho mỗi loại, mỗi cái một màu:
   - `file:/^O\d+/`
   - `file:/^H\d+/`
   - `file:/^D\d+/`
   - `file:/^T\d+/`
   - `file:/^M\d+/`
3. Một item đứng riêng, không có đường nối, là item chưa được nối vào nhu cầu nào. Đó chính là một "warnings" của hub.

## Rules that keep it working

- **Giá trị nối item là mã đặt trong hai cặp ngoặc vuông và dấu nháy**, ví dụ `"[[H1]]"`. Nếu bạn nhập bằng khung Properties của Obsidian, dấu nháy được thêm tự động.
- **Chỉ khai báo một chiều.** Decision nói nó kiểm chứng hypothesis nào; Obsidian tự hiện chiều ngược lại ở Backlinks.
- **Giữ nguyên tên file item.** Tên file chính là mã của item.
- **Ẩn danh trước khi bỏ dữ liệu vào folder này.** Obsidian mở cả folder `_raw-private/` và `_personal/`.

## Limits

- **Các liên kết trong Properties chỉ bấm được trong Obsidian.** Trên GitHub chúng hiện như chữ thường. Để chia sẻ với người khác, hãy tạo báo cáo HTML (xem [`04-share-your-hub.md`](04-share-your-hub.md)).
- **Plugin AI trong Obsidian đọc được cả folder**, kể cả `_raw-private/`. Nếu bạn cài plugin loại đó, áp dụng cùng quy tắc dữ liệu như với AI coding tool.
- **Bases còn mới**, nên cách hiển thị có thể khác giữa các bản Obsidian. Nếu `traceability.base` báo lỗi, bạn xoá file đó đi. Hub vẫn chạy bình thường vì dữ liệu nằm trong các file item.
