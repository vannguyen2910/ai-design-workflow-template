# Get the Folder

Guide này giúp bạn đưa workspace về máy. Có hai cách, và bạn chỉ cần chọn một.

**Chưa dùng GitHub bao giờ? Chọn cách A.** Bạn dùng được workspace này mà không cần tài khoản.

| | Cách | Cần tài khoản GitHub | Có bản sao lưu | Hợp khi |
|---|---|---|---|---|
| A | Download ZIP | Không | Không, bạn tự sao lưu | Bạn muốn bắt đầu ngay |
| B | Use this template, rồi GitHub Desktop | Có (miễn phí) | Có, kèm lịch sử thay đổi | Bạn muốn một bản sao lưu tự động |

## Where to keep it

Đặt folder ở một nơi bình thường trên máy, ví dụ `Documents`.

**Đừng đặt trong Google Drive, iCloud, OneDrive hay Dropbox.** AI coding tool ghi nhiều file cùng lúc, và folder đồng bộ lên cloud có thể bị lỗi giữa chừng. Muốn có bản sao lưu thì dùng cách B.

## Option A: Download ZIP

1. Mở trang GitHub của repo (đường dẫn do người chia sẻ template gửi).
2. Bấm nút xanh **Code**, rồi chọn **Download ZIP**.
3. Giải nén file ZIP vừa tải:
   - Mac: bấm đúp vào file.
   - Windows: bấm chuột phải, chọn **Extract All**.
4. Kéo folder vừa giải nén vào `Documents`.
5. Mở folder. Bạn sẽ thấy `README.md`, `guides`, `my-case` và `demo-case`.

**Sao lưu:** thỉnh thoảng nén `my-case` thành một file ZIP và cất đi, hoặc chép sang ổ khác. Cuối mỗi đợt làm việc là thời điểm tốt.

## Option B: Use this template, rồi GitHub Desktop

Cách này tạo cho bạn một **repo** riêng (repo là một folder được lưu trên GitHub). Bạn để nó ở chế độ **Private**, nên chỉ mình bạn thấy.

### Part 1: Tạo repo của bạn

1. Vào [github.com](https://github.com) và đăng nhập. Chưa có tài khoản thì bấm **Sign up** (miễn phí).
2. Mở trang GitHub của repo mà người chia sẻ template gửi.
3. Bấm nút xanh **Use this template**, rồi chọn **Create a new repository**.
4. Ở ô **Repository name**, đặt một cái tên, ví dụ `my-design-workflow`.
5. Chọn **Private**.
6. Bấm **Create repository**.

Không thấy nút **Use this template**? Dùng cách A, hoặc nhắn người chia sẻ template.

> **Đừng tải thẳng repo gốc về để lưu công việc.** Bạn không có quyền ghi vào repo đó, nên các thay đổi của bạn không lưu lên được. Hãy tạo repo riêng bằng **Use this template** trước.

### Part 2: Đưa repo về máy

1. Cài **GitHub Desktop** từ [desktop.github.com](https://desktop.github.com) và đăng nhập bằng tài khoản GitHub.
2. Chọn **File**, rồi **Clone repository**. (Clone nghĩa là tải một repo về máy.)
3. Ở tab **GitHub.com**, chọn repo bạn vừa tạo.
4. Ở ô **Local path**, chọn `Documents`.
5. Bấm **Clone**.
6. Chọn **Repository**, rồi **Show in Finder** (Mac) hoặc **Show in Explorer** (Windows) để mở folder.

### Part 3: Lưu bản làm việc

Làm sau mỗi lần làm việc xong một phần:

1. Mở GitHub Desktop. Cột bên trái liệt kê các file bạn đã sửa.
2. Ở góc dưới bên trái, gõ một dòng tóm tắt, ví dụ `Discover: scope và user-voice synthesis`.
3. Bấm **Commit to main**. (Commit là lưu một mốc thay đổi, kèm lời nhắn. `main` là nhánh chính, bạn cứ để nguyên.)
4. Bấm **Push origin** ở thanh trên. (Push là gửi các mốc đó lên GitHub.)

Bốn thao tác này là toàn bộ những gì bạn cần biết về Git. Các từ vừa gặp được giải thích thêm ở [`03-github-basics.md`](03-github-basics.md).

## Check before you start

- [ ] Folder nằm trong `Documents`, không nằm trong folder đồng bộ cloud.
- [ ] Bạn thấy `my-case` và `demo-case` trong folder.
- [ ] Bạn mở được file `my-case/README.md` và đọc được nội dung.

Mở được nhưng bảng và link hiển thị thô? Bình thường: file Markdown cần một trình xem. Xem phần "View markdown files" trong [`02-set-up-your-case.md`](02-set-up-your-case.md).
