# Workflow: Add media to the Hub

Đưa ảnh, video, PDF hoặc một tài liệu vào hub để nó hiện trong báo cáo, đúng chỗ và có nối về item nó làm bằng chứng cho.

*Trạng thái: bản nháp.*

| | |
|---|---|
| Khi nào | Khi bạn có ảnh (wireframe, screenshot, ảnh phiên test), video, PDF hoặc prototype HTML cần cho báo cáo |
| Làm trước | Lưu một mốc (commit hoặc copy folder) |
| Working file | Không có. Kết quả ghi vào `work/` |
| Hướng dẫn đầy đủ | `work/README.md`, mục "Thêm ảnh, video, PDF" |

## Step 1: Place the files (AI)

**Who:** AI
**Input:** Các tệp bạn đưa, và danh sách folder trong `work/`
**Output:** Một folder `work/<tên-ngắn>/` chứa các tệp, hoặc các tệp lẻ vào đúng folder đã có

**Instruction:**
> Đặt các tệp được đưa vào `work/<tên-ngắn>/`. Đặt tên folder và tên tệp bằng chữ thường, nối bằng dấu gạch ngang, và thêm số đầu tên (`1-`, `2-`...) cho ảnh theo thứ tự muốn hiện, vì tên tệp thành chú thích. Đổi `.heic`, `.tiff`, `.psd` hoặc `.mov` sang `.png`, `.jpg`, `.pdf` hoặc `.mp4` nếu có thể, nếu không thì nói rõ. Không ghi đè tệp đã có và không đặt tệp vào `_personal/` hay `work/sources/`. Nếu tệp có vẻ chứa tên người hoặc dữ liệu cá nhân thật, dừng và hỏi.

**Check:** Mở folder và đối chiếu tên tệp với danh sách bạn đưa.
**Failure sign:** Tệp bị ghi đè hoặc đặt ở ngoài `work/`.

## Step 2: Describe it (AI)

**Who:** AI
**Input:** Các tệp ở step 1, mẫu trong `work/_templates/`, và danh sách item trong `insights/`
**Output:** `work/<tên-ngắn>/index.md`

**Instruction:**
> Tạo `index.md` từ mẫu gần nhất. Điền `type` (tự do), `title`, `stage`, `status` (`draft` nếu chưa kiểm tra) và `summary` một câu. Chỉ điền `takeaways` bằng điều nhìn thấy được trong chính tệp. Điền `supports` bằng mã item mà tài liệu này rõ ràng làm bằng chứng cho; nếu không chắc thì để `[]` và liệt kê các item có thể liên quan ở cuối câu trả lời. Không bịa nội dung không có trong tệp.

**Check:** Mở `index.md`: mọi mã trong `supports` có file item tương ứng không?
**Failure sign:** `takeaways` nói điều không có trong ảnh; `supports` trỏ tới item không tồn tại.

## Step 3: Rebuild and look (YOU)

**Who:** YOU
**Input:** `work/<tên-ngắn>/`
**Output:** `index.html` mới

Nhờ AI tool chạy `python3 _skills/export-hub.py`, mở `index.html`, vào mục **Work** và bấm thẻ mới.

**Check:** Ảnh hiện đủ và đúng thứ tự, chú thích dễ hiểu, và không có cảnh báo vàng (tệp nặng, định dạng không hiển thị, tệp không tìm thấy).
**Failure sign:** Còn cảnh báo ở trang tài liệu: làm theo nội dung cảnh báo rồi tạo lại báo cáo.
