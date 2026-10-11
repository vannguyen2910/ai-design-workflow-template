# Share Your Hub

Hub của bạn mặc định là riêng tư: nó nằm trong folder case trên máy bạn, và không ai thấy nếu bạn không gửi. Guide này nói cách cho người khác xem, từ cách ít rủi ro nhất đến cách nhiều rủi ro nhất.

## Choose how to share

| Bạn muốn | Cách | Người nhận cần |
|---|---|---|
| Stakeholder đọc, không phải cài gì | **Báo cáo HTML** (Option 1) hoặc **PDF** (Option 2) | Một trình duyệt |
| Gửi cả folder cho đồng nghiệp | **File ZIP** (Option 3) | Obsidian hoặc VS Code để xem đẹp |
| Một người xem trực tiếp trên GitHub | **Mời vào repo Private** (Option 4) | Tài khoản GitHub miễn phí |
| Ai có link cũng xem được | **Repo Public** (Option 5), chỉ khi case được phép chia sẻ | Không cần gì |

**Với công việc thật của công ty, hãy dùng Option 1 hoặc 2.**

## Option 1: Báo cáo HTML

Một file HTML tự chứa, có menu, bấm đúp là mở bằng trình duyệt, gửi email được.

1. **Tạo báo cáo.** Cách dễ nhất: nhờ AI tool đang mở folder case chạy lệnh `python3 tools/export-hub.py`.
   - Tự chạy trên Mac: bấm chuột phải vào folder case, chọn **New Terminal at Folder**, rồi gõ lệnh trên.
   - Tự chạy trên Windows: mở folder case, bấm vào thanh địa chỉ, gõ `cmd`, nhấn Enter, rồi gõ lệnh trên.
   - Máy cần có Python 3. Mac có thể hỏi bạn cài một bộ công cụ ở lần chạy đầu; Windows cần cài Python từ [python.org](https://www.python.org).
2. **Mở file** `hub/_export/<tên-case>-report.html` bằng trình duyệt.
3. **Kiểm tra trước khi gửi.** Nếu đầu trang có thanh đen "còn nội dung mẫu hoặc chỗ chưa điền", hub vẫn còn mục `[EXAMPLE]` hoặc chỗ trống. Điền hoặc xoá chúng rồi tạo lại.
4. **Gửi file.** Người nhận chỉ cần trình duyệt.

Báo cáo chỉ gồm hub, nhật ký quyết định và các nguyên tắc. Nó không có file làm việc hay bản nháp của AI.

## Option 2: PDF

1. Mở trang hub bạn muốn gửi: trong báo cáo HTML ở Option 1, hoặc trong Obsidian hay VS Code.
2. In trang đó (`Cmd+P` trên Mac, `Ctrl+P` trên Windows) và chọn **Save as PDF**.
3. Lặp lại cho các trang chính: Tổng quan, Problem brief, Findings.
4. Gửi các file PDF, hoặc đính kèm vào wiki của công ty.

## Option 3: File ZIP

1. Nén **cả folder case**, không chỉ `hub/`, vì các trang hub nối tới `00-context/`, `case-log.md` và các file làm việc.
2. Gửi file ZIP. Người nhận giải nén và mở cả folder bằng Obsidian hoặc VS Code.
3. Thử mở trên một máy khác trước khi gửi.

## Option 4: Mời một người vào repo Private

1. Mở repo của bạn trên GitHub, chọn **Settings**, rồi **Collaborators**.
2. Bấm **Add people** và nhập tên tài khoản hoặc email của người đó.
3. Họ nhận email mời. Sau khi chấp nhận, họ đọc hub ngay trên GitHub.

Bạn thu hồi quyền bất cứ lúc nào ở cùng màn hình.

## Option 5: Repo Public

GitHub hiển thị Markdown trực tiếp, nên không cần dựng website: link tới repo chính là hub.

Chỉ làm khi **toàn bộ case folder** được phép chia sẻ, ví dụ case của khoá, hoặc một bản đã làm sạch từ công việc thật. Hub nối tới các file ngoài `hub/`, nên công khai riêng `hub/` sẽ làm các liên kết đó hỏng.

1. Tạo một repo **mới** trên GitHub và chọn **Public**. Đừng đổi repo Private đang dùng thành Public, vì lịch sử cũ vẫn còn trong đó.
2. Copy folder case đã làm sạch vào repo mới.
3. Mở link repo trong **cửa sổ ẩn danh** để thấy đúng những gì người khác thấy.

## Before you share anything

- **Không đưa lên số liệu mật của công ty,** chi tiết sản phẩm chưa phát hành, dữ liệu cá nhân của người dùng, hay mật khẩu. Kiểm tra chính sách của công ty trước.
- **Link công khai có thể bị chuyển tiếp** cho bất kỳ ai.
- **Tên tài khoản GitHub nằm trong địa chỉ repo.** Chọn một tên bạn thấy thoải mái khi nó hiện ra.
- **Bạn là người chia sẻ và chịu trách nhiệm** về link và nội dung. Giảng viên không đăng thay bạn.
- **Dùng dữ liệu đã ẩn danh hoặc dữ liệu giả** cho mọi thứ công khai.
