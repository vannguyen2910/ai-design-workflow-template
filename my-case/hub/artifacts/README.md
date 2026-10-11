# Tài liệu của dự án

Tài liệu là thứ đã làm ra trong dự án và cần một **trang riêng** để người khác đọc sâu: phân tích đối thủ, persona, kết quả khảo sát, user flow, sitemap, prototype, báo cáo test.

Mỗi tài liệu hiện ở mục **Documents** của báo cáo `index.html`, và nối với các item nó làm bằng chứng cho (opportunity, hypothesis, decision, evidence, metric). Từ một decision, người đọc bấm sang tài liệu đứng sau nó, và ngược lại.

## Thêm một tài liệu

Chọn tình huống của bạn:

| Bạn có | Làm gì |
|---|---|
| Một file văn bản (`.md`) | Đặt file vào folder `hub/artifacts/`, ví dụ `competitor-analysis.md` |
| Nhiều file: ảnh, PDF, HTML, video | Tạo một folder con trong `hub/artifacts/` (ví dụ `user-flow/`), thêm một file `index.md` mô tả, rồi **thả các file vào folder đó** |
| Một file làm việc đã có trong `work/` | Tạo tài liệu và trỏ về file làm việc đó, để nội dung không bị chép hai lần |
| Một link Figma, Miro, Notion... | Ghi link vào tài liệu (xem "Link ngoài" bên dưới) |

Cách dễ nhất: **bắt đầu từ một mẫu trong folder `_templates/`** (copy ra ngoài, đổi tên). Hoặc nhờ AI tool: *"Tạo tài liệu persona từ mẫu trong `hub/artifacts/_templates/`."*

Loại tài liệu là **tự do**: bạn có thể đặt loại `journey-map` hay `brand-guidelines`, báo cáo vẫn hiện bình thường.

## Báo cáo hiển thị từng loại tệp thế nào

Báo cáo tự nhận diện tệp theo đuôi, bạn không cần khai báo cách hiển thị.

| Tệp | Hiển thị |
|---|---|
| `.md` | Nội dung trang (chữ, bảng, danh sách) |
| `.png`, `.jpg`, `.svg`, `.gif`, `.webp` | Ảnh trong khung, bấm để xem cỡ đầy đủ |
| `.html` (prototype, flow, trang tĩnh) | Thẻ có nút "Mở ở tab mới"; có thể nhúng để chạy ngay trong trang |
| `.pdf` | Thẻ có nút mở; có thể nhúng để xem ngay trong trang |
| `.mp4`, `.webm` | Trình phát video |
| `.csv` | Bảng (40 dòng đầu) |
| Tệp khác (`.xlsx`, `.docx`, `.fig`...) | Thẻ đính kèm có nút mở |
| Link ngoài | Thẻ có tên nền tảng (Figma, Miro, Notion...) và nút mở |

**Link ngoài hay tệp trong folder?** Figma và các công cụ trực tuyến nên dùng link (luôn là bản mới nhất). Prototype dạng HTML nên để trong folder dự án (chạy được khi không có mạng, và đi kèm khi bạn gửi báo cáo).

## Bản nháp của AI

File làm việc có hai phần: **(AI draft)** là bản AI soạn nguyên gốc, **(verified)** là bản bạn đã kiểm tra. Báo cáo mặc định **ẩn** mọi phần có chữ "AI draft" ở tiêu đề, để người xem chỉ thấy nội dung đã được kiểm tra. Có một chế độ dành cho nhóm làm việc, hiện các phần nháp ở dạng gấp lại và ghi "chưa kiểm tra". Đừng gửi bản đó cho người ngoài.

## Gửi báo cáo cho người khác

Nhờ AI tool: *"Xuất gói báo cáo gửi stakeholder, kèm file zip."* AI sẽ tạo một folder gọn chỉ gồm `index.html` và đúng các tệp mà tài liệu dùng. Gói này **không chứa** file làm việc thô, dữ liệu gốc chưa ẩn danh, hay ghi chú riêng của bạn.

---

# Chi tiết kỹ thuật (tuỳ chọn)

Phần này dành cho người muốn tự viết phần thông tin đầu file hoặc tự chạy lệnh.

## Thông tin đầu file

Mỗi tài liệu `.md` có một khối nằm giữa hai dòng `---` ở đầu file:

```
---
type: "competitor-analysis"      # loại tài liệu, tự do
title: "Phân tích đối thủ"
stage: "Discover"                # Setup, Discover, Define, Develop hoặc Deliver
status: "verified"               # verified, draft, simulated hoặc planned
summary: "Một câu tóm tắt."
takeaways:                       # 2 đến 4 điểm chính
  - "Điểm chính thứ nhất"
supports:                        # item mà tài liệu này làm bằng chứng cho
  - "[[O1]]"
  - "[[D3]]"
source: "../../work/discover/competitor-analysis.md"   # tuỳ chọn: lấy nội dung từ file làm việc
media:                           # tuỳ chọn: tệp nằm ở nơi khác trong dự án
  - "../../work/prototype/index.html"
links:                           # tuỳ chọn: link ngoài, dạng "Nhãn | URL"
  - "Prototype trên Figma | https://www.figma.com/..."
embed: true                      # tuỳ chọn: nhúng tệp HTML hoặc PDF ngay trong trang
embed_url: ""                    # tuỳ chọn: nhúng một địa chỉ web trong trang
---
```

Chỉ `title` và `type` là cần có. Các dòng còn lại làm trang đầy đủ hơn.

## Lệnh xuất gói

```
python3 _scripts/export-hub.py --bundle gui-stakeholder --zip
```

Lệnh này tạo folder gọn và file zip như mô tả ở trên. Chạy với `--team` thì các phần nháp của AI hiện ra (gấp lại).
