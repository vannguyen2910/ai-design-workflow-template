# AGENTS.md: workspace

Đây là **gốc workspace**: nơi chứa nhiều dự án (mỗi dự án là một case folder) và `toolkit/` dùng chung. Luật làm việc *bên trong* một dự án nằm ở `AGENTS.md` của dự án đó (ví dụ `my-case/AGENTS.md`). Khi đang làm việc trong một dự án, đọc file đó, không đọc file này.

## Folder nào là gì

| Folder | Là gì | Bạn làm gì |
|---|---|---|
| `my-case/` | Template trống | **Không điền vào đây.** Chỉ để `new-case.py` sao chép |
| `demo-case/` | Dự án mẫu (Travel Buddy) | Đọc để tham khảo, không sửa trừ khi được yêu cầu |
| `<tên-dự-án>/` | Dự án của chủ workspace | Làm việc theo `AGENTS.md` của dự án đó |
| `toolkit/` | Hướng dẫn, mẫu tài liệu, step card, script | Đọc, không sửa trừ khi được yêu cầu |
| `index.html` | Trang chủ: mỗi dự án một thẻ | Không sửa tay. Tạo bằng `toolkit/skills/export-home.py` |

## Khi được yêu cầu tạo một dự án mới

Ví dụ: "Tạo một dự án mới tên …", "Create a new project called …", "Bắt đầu dự án …".

1. **Hỏi tên dự án** nếu chưa có. Một câu là đủ.
2. **Chạy lệnh, không tự sao chép `my-case`:**

   ```
   python3 toolkit/tools/new-case.py "<Tên dự án>"
   ```

   Lệnh tự đổi tên có dấu hoặc có khoảng trắng thành tên folder, xoá item `[EXAMPLE]`, điền tên dự án, dựng `index.html` của dự án và thêm thẻ vào trang chủ. Thêm `--title "…"` nếu muốn tên hiển thị khác tên folder.
3. **Nói lại cho chủ workspace:** đường dẫn folder mới, rằng trang chủ đã có thẻ cho dự án, và việc đầu tiên cần làm: điền Project card trong `README.md` của dự án, rồi `context/product-and-users.md` và `context/data-rules.md`.
4. **Đừng điền thay.** Không bịa tên sản phẩm, người dùng hay số liệu. Chỗ nào chưa biết thì để trống để chủ dự án điền.

Nếu folder cùng tên đã tồn tại, lệnh sẽ dừng. Đừng xoá hay ghi đè: hỏi lại chủ workspace chọn tên khác.

## Các yêu cầu khác ở cấp workspace

| Yêu cầu | Làm gì |
|---|---|
| Xem hoặc cập nhật trang chủ | `python3 toolkit/skills/export-home.py` |
| Xem báo cáo một dự án | Mở `<dự án>/index.html`. Muốn tạo lại: chạy `python3 ../toolkit/skills/export-hub.py` **trong** folder dự án |
| Thêm tài liệu mới vào một dự án | Mở mẫu trong `toolkit/templates/`, copy vào `work/` của dự án đó, và làm theo `AGENTS.md` của dự án |
| Không rõ thuộc dự án nào | Hỏi lại một câu. Đừng đoán |

## Luật cứng

1. **Không đọc** `_personal/` và `work/sources/_raw-private/` của bất kỳ dự án nào.
2. **Không sửa `my-case/`** khi tạo hay làm việc với một dự án. Nó phải giữ nguyên để làm template.
3. **Đề xuất trước** với mọi việc tạo hoặc đổi nhiều file. Chờ chủ workspace duyệt.
4. **Ẩn danh trước khi dùng dữ liệu thật.** Tên người, tên công ty và số liệu thật không đưa cho AI tool khi chưa ẩn danh.
