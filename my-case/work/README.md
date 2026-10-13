# Work

Folder này là **nơi mọi thứ làm ra trong dự án nằm cùng một chỗ**: file làm việc của từng giai đoạn (`scope.md`, `problem-brief.md`, `findings.md`...), và các tài liệu (phân tích đối thủ, persona, wireframe, prototype, user flow...).

Mỗi file hoặc folder có `index.md` ở đây hiện thành một thẻ ở mục **Work** của báo cáo `index.html`, và nối với các item nó làm bằng chứng cho (opportunity, hypothesis, decision, evidence, metric). Từ một decision, người đọc bấm sang tài liệu đứng sau nó, và ngược lại. Các phần có chữ "(AI draft)" ở tiêu đề bị ẩn khỏi báo cáo.

Hai folder con không hiện thành thẻ: `sources/` (dữ liệu nghiên cứu, kèm `_raw-private/` không bao giờ đưa cho AI) và `original-docs/` nếu có. Một folder con chỉ hiện thành thẻ khi nó có `index.md`.

## Thêm một file hoặc tài liệu

Chọn tình huống của bạn:

| Bạn có | Làm gì |
|---|---|
| Một file văn bản (`.md`) | Đặt file vào folder `work/`, ví dụ `competitor-analysis.md` |
| Nhiều file: ảnh, PDF, HTML, video | Tạo một folder con trong `work/` (ví dụ `user-flow/`), thêm một file `index.md` mô tả, rồi **thả các file vào folder đó** |
| Nội dung nằm sẵn ở nơi khác trong dự án (ví dụ `work/sources/`) | Tạo file `.md` ở đây và dùng `source:` trỏ về file đó, để nội dung không bị chép hai lần |
| Một link Figma, Miro, Notion... | Ghi link vào tài liệu (xem "Link ngoài" bên dưới) |

Cách dễ nhất: **bắt đầu từ một mẫu trong folder `toolkit/templates/`** ở gốc workspace, ngang hàng với các case (copy vào `work/`, đổi tên). Hoặc nhờ AI tool: *"Tạo tài liệu persona từ mẫu `toolkit/templates/persona.md`."*

Loại tài liệu là **tự do**: bạn có thể đặt loại `journey-map` hay `brand-guidelines`, báo cáo vẫn hiện bình thường.

## Thêm ảnh, video, PDF

Báo cáo tự nhận ra định dạng theo đuôi tệp, **bạn không cần cấu hình gì**. Có hai cách, tuỳ bạn muốn media là một tài liệu riêng hay nằm giữa một trang.

### Cách 1: Thả vào folder của một tài liệu (khuyến nghị)

1. Tạo folder `work/<tên-ngắn>/`, ví dụ `work/wireframes/`.
2. Thả ảnh, video, PDF vào đó.
3. Thêm một file `index.md` (copy từ mẫu trong `toolkit/templates/` ở gốc workspace) có `title` và `type`.

Xong. Báo cáo dựng một trang tài liệu có **thẻ ở mục Work**, ảnh đầu tiên làm ảnh bìa, và mọi tệp trong folder hiện trên trang. Bạn có thể nhờ AI tool làm cả ba bước: *"Thêm các ảnh này vào dự án như một tài liệu wireframe."*

| Bạn thả vào | Báo cáo hiện |
|---|---|
| `.png` `.jpg` `.jpeg` `.gif` `.webp` `.svg` `.avif` `.bmp` | Lưới ảnh, bấm để xem cỡ đầy đủ. **Tên file thành chú thích** |
| `.mp4` `.webm` | Trình phát video ngay trên trang |
| `.pdf` | Thẻ có nút mở; thêm `embed: true` để xem ngay trong trang |
| `.html` (prototype, flow) | Thẻ "Mở ở tab mới"; thêm `embed: true` để chạy ngay trong trang |
| `.csv` | Bảng (40 dòng đầu) |
| `.xlsx` `.docx` `.pptx` và tệp khác | Thẻ đính kèm có nút mở |

**Mẹo đặt tên:** tên file thành chú thích (`2-discover.png` hiện "2 discover") và các ảnh xếp theo thứ tự tên, nên đặt số đầu tên (`1-`, `2-`, `3-`) để kiểm soát thứ tự.

### Cách 2: Chèn ảnh vào giữa một trang

Trong bất kỳ trang hoặc item nào (trang giai đoạn, decision, evidence, finding), viết:

```
![Mô tả ảnh](đường-dẫn/ảnh.png)
```

Đường dẫn tính **từ chính file bạn đang viết**. Ví dụ trong `insights/decisions/D4.md`, ảnh nằm ở `work/wireframes/3-plan.png` thì viết `![Màn Plan](../../work/wireframes/3-plan.png)`. Video chèn bằng cùng cú pháp (`![demo](../../work/flow/demo.mp4)`). Với PDF và HTML, dùng liên kết thường hoặc cách 1.

### Các tệp báo cáo không lấy

- Tệp nằm trong `_personal/` hoặc `work/sources/_raw-private/` (vùng riêng tư): bị bỏ qua.
- Tệp ở ngoài folder dự án: không được đóng gói. Hãy copy vào folder dự án.

### Báo cáo sẽ nhắc bạn khi có vấn đề

Ngay trên trang tài liệu (và trong kết quả khi tạo báo cáo) hiện cảnh báo nếu: tệp không tìm thấy, ảnh nặng hơn 2,5 MB (nên nén dưới 2 MB), định dạng trình duyệt không hiển thị (`.heic`, `.tiff`, `.psd`, `.fig`: xuất sang PNG hoặc JPG), hoặc video `.mov` (xuất sang `.mp4`).

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
source: "competitor-analysis.md"   # tuỳ chọn: lấy nội dung từ file làm việc
media:                           # tuỳ chọn: tệp nằm ở nơi khác trong dự án
  - "prototype/index.html"
links:                           # tuỳ chọn: link ngoài, dạng "Nhãn | URL"
  - "Prototype trên Figma | https://www.figma.com/..."
embed: true                      # tuỳ chọn: nhúng tệp HTML hoặc PDF ngay trong trang
embed_url: ""                    # tuỳ chọn: nhúng một địa chỉ web trong trang
---
```

Chỉ `title` và `type` là cần có. Các dòng còn lại làm trang đầy đủ hơn.

## Lệnh xuất gói

```
python3 ../toolkit/skills/export-hub.py --bundle gui-stakeholder --zip
```

Lệnh này tạo folder gọn và file zip như mô tả ở trên. Chạy với `--team` thì các phần nháp của AI hiện ra (gấp lại).
