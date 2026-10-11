# GitHub Basics

Guide này dành cho người chưa từng dùng GitHub. Bạn không cần đọc nó để học khoá này: cách A trong [`01-get-the-folder.md`](01-get-the-folder.md) không cần tài khoản. Đọc nó khi bạn muốn lưu bản làm việc lên GitHub.

## Seven words

| Từ | Nghĩa | Hình dung |
|---|---|---|
| **Git** | Phần mềm ghi lại lịch sử thay đổi của một folder | Nút "undo" cho cả folder |
| **GitHub** | Website lưu các folder dùng Git | Google Drive, nhưng nhớ từng thay đổi |
| **Repository** (repo) | Một folder được lưu trên GitHub | Một folder dự án |
| **Template** | Một repo mẫu để bạn tạo bản riêng từ nó | Một file mẫu để bạn "Save as" |
| **Clone** | Tải một repo về máy | Tải folder về |
| **Commit** | Lưu một mốc thay đổi, kèm một dòng ghi chú | Nút "Save" có kèm lời nhắn |
| **Push** | Gửi các mốc đã lưu từ máy lên GitHub | Đồng bộ bản của bạn lên mạng |

## What you need to do

Bạn chỉ làm bốn việc, và đều bằng cách bấm nút trong **GitHub Desktop**, không gõ lệnh:

1. **Clone** repo của bạn về máy. Làm một lần.
2. Làm việc trong folder như bình thường.
3. **Commit** khi xong một phần việc, kèm một dòng ghi chú.
4. **Push** để bản của bạn lên GitHub.

Các bước bấm chi tiết nằm ở phần "Option B" trong [`01-get-the-folder.md`](01-get-the-folder.md).

## Private or public?

| | Private | Public |
|---|---|---|
| Ai thấy | Chỉ bạn, và những người bạn mời | Bất kỳ ai có link, kể cả công cụ tìm kiếm |
| Dùng cho | Case đầy đủ: context, nguồn dữ liệu, các file làm việc | Chỉ một case mà bạn được phép chia sẻ toàn bộ |
| Hiển thị Markdown trên GitHub | Có, cho người được mời | Có, cho mọi người |

Quy tắc đơn giản: **repo chứa case của bạn để Private.** Chỉ khi cả case được phép chia sẻ mới tạo một repo Public riêng, từ bản đã làm sạch. Xem [`04-share-your-hub.md`](04-share-your-hub.md).

## Common worries

| Bạn lo | Thực tế |
|---|---|
| "Tôi bấm sai thì mất file" | Mỗi commit là một mốc. Bạn luôn quay lại được bản trước đó |
| "Có ai thấy bài của tôi không" | Repo Private thì chỉ bạn thấy. Người khác (kể cả giảng viên) chỉ thấy khi bạn mời hoặc gửi link |
| "Tôi gặp một thông báo lạ" | Chụp màn hình và gửi vào nhóm lớp. Trong lúc chờ, bạn vẫn làm việc bình thường: Git không chặn việc bạn sửa file |
| "Mọi thứ rối hết cả lên" | Tải lại một bản ZIP mới, rồi chép các file bạn đã sửa sang folder mới |

## Do not commit

Đừng lưu những thứ này vào repo, kể cả repo Private:

- Mật khẩu, API key, token
- Dữ liệu cá nhân của người dùng (tên, email, số điện thoại, bản ghi âm có tên thật)
- Số liệu tài chính hoặc chiến lược chưa công bố của công ty
- File của công ty mà bạn chưa được phép mang ra ngoài

Repo Private vẫn là một nơi trên internet. Nếu chưa chắc, hãy ẩn danh trước khi lưu.
