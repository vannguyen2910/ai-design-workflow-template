# Toolkit

Mọi thứ dùng chung cho các dự án trong workspace. Trang chủ liệt kê mọi dự án là `index.html` ở gốc workspace. **Bạn không điền gì vào đây.** Mỗi dự án (`my-case`, `demo-case`, dự án của bạn) nằm ngoài folder này.

| Folder | Có gì | Khi nào mở |
|---|---|---|
| `guides/` | Hướng dẫn từng bước: lấy folder về máy, thiết lập dự án, GitHub, chia sẻ báo cáo, Obsidian | Lần đầu làm quen, hoặc khi bí |
| `templates/` | Mẫu rỗng cho tài liệu làm việc (research plan, interview guide, PESTEL, journey map...) | Khi bắt đầu một tài liệu mới |
| `skills/` | Các bước cho AI tool (step card) và script tạo báo cáo `index.html` | Hiếm khi: AI tool tự đọc |
| `tools/` | `new-case.py`: tạo một dự án mới bằng lệnh | Khi muốn tạo dự án mới |

Tạo dự án mới (từ gốc workspace):

```
python3 toolkit/tools/new-case.py ten-du-an
```

Chi tiết: [`guides/02-set-up-your-case.md`](guides/02-set-up-your-case.md).
