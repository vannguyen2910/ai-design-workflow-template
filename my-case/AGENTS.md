# Rules for the AI tool

File này dành cho AI tool. Đọc nó trước khi làm bất cứ việc gì trong folder này. Chủ dự án là người quyết định; bạn soạn nháp và kiểm tra giúp.

## What this folder is

Case folder của một người làm sản phẩm (designer, researcher, PM...) làm việc theo quy trình AI-assisted: AI soạn nháp, chủ dự án kiểm tra và quyết định. Folder chia theo việc bạn làm: `context/` (thông tin nền), `work/` (file làm việc theo giai đoạn), `hub/` (bản ghi quyết định), `reference/` (trang tra cứu), `steps/` (các bước làm việc với AI). Mỗi bước được định nghĩa bằng một step card trong `steps/`.

## Map

| Đường dẫn | Là gì | Bạn được làm gì |
|---|---|---|
| `AGENTS.md` | Luật cho AI tool (file này) | Đọc |
| `context/*.md` | Context pack: thông tin nền của case (sản phẩm, người dùng, quy tắc dữ liệu) | Đọc đầu tiên ở mọi bước. Không sửa trừ khi được yêu cầu |
| `steps/*.md` | Định nghĩa từng bước làm việc với AI (step card) | Đọc card của bước đang chạy |
| `work/discover/`, `work/define/`, `work/develop/`, `work/deliver/` | Working file theo giai đoạn | Chỉ ghi vào đúng section được yêu cầu |
| `work/sources/anonymised/` | Dữ liệu đã ẩn danh, có ID | Đọc. Nguồn duy nhất cho quote và số liệu |
| `hub/opportunities/O1.md`, `hypotheses/H1.md`, `metrics/M1.md`, `decisions/D1.md`, `evidence/E1.md`… | **Nguồn duy nhất** của mỗi item (O, H, M, D, E). Mỗi loại một folder; tên file là mã của item | Đọc. Chỉ sửa khi được yêu cầu sửa đúng item đó |
| `hub/_item-templates/` | Mẫu rỗng cho từng loại item | Đọc. Copy vào đúng folder loại (ví dụ `hub/decisions/`) khi được yêu cầu tạo item mới, không sửa file mẫu |
| `hub/artifacts/` | Tài liệu của dự án: một file `.md`, hoặc một folder có `index.md` cùng các tệp ảnh, PDF, HTML | Đọc. Tạo hoặc sửa khi được yêu cầu đúng tài liệu đó. Không chép nội dung working file vào đây: dùng `source:` |
| `hub/README.md` và các trang `hub/*.md` | Tổng hợp và narrative | Chỉ ghi vào các khối `generated` khi chạy `steps/refresh-hub.md` |
| `work/prototype/` | Code prototype | Làm việc ở đây khi dựng prototype, theo `project-rules.md` trong folder đó |
| `reference/*.md` | Trang tra cứu: gates, principle checks, severity levels, case log, và mọi trang chủ dự án thêm vào | Đọc. Chỉ sửa khi được yêu cầu đúng trang đó. `reference/case-log.md`: thêm dòng khi được yêu cầu |
| `_scripts/export-hub.py` | Script xuất hub ra một file HTML | Chạy khi được yêu cầu (`python3 _scripts/export-hub.py`). Không sửa, và không tự viết HTML thay cho script |
| `index.html` | Trang chủ của hub, xuất ra từ Markdown để xem bằng trình duyệt | Không đọc, không sửa tay. Muốn cập nhật thì chạy `_scripts/export-hub.py` |
| `_personal/` | Ghi chú riêng của chủ dự án | **Không đọc, không ghi** |
| `work/sources/_raw-private/` | Dữ liệu gốc chưa ẩn danh | **Không đọc, không ghi** |

## Hard rules

1. **Chỉ trả về section được yêu cầu.** Không sửa section khác, không sửa file khác. Chủ dự án tự dán kết quả vào, hoặc bạn ghi đúng vào section được chỉ định.
2. **Không sửa section "(AI draft)" sau khi đã tạo, và không sửa section "(verified)" của chủ dự án** trừ khi được yêu cầu đúng section đó. Bản nháp và bản đã kiểm tra luôn nằm ở hai section riêng.
3. **Chỉ dùng nguồn trong `work/sources/anonymised/`.** Không bịa quote, số liệu, tên sản phẩm hay nguồn. Không có trong nguồn thì ghi `unknown`.
4. **Quote nguyên văn, kèm ID.** Không viết lại, không rút gọn.
5. **Con số nào chưa được xác nhận thì ghi `assumed`.** Suy luận không có trong nguồn thì ghi `inferred`.
6. **Dừng và báo** nếu bạn thấy dữ liệu có vẻ chưa ẩn danh (tên người, email, username, tên công ty) trong folder bạn được phép đọc.
7. **Nói rõ điều bạn không chắc.** Liệt kê item bạn không chắc thay vì đoán link hay quan hệ.
8. **Không tạo bản sao của một item.** Item chỉ tồn tại trong file của nó (`hub/decisions/D2.md`...). Quan hệ nằm trong properties (khối `---` ở đầu file) dưới dạng wikilink trong dấu nháy, và chỉ khai báo một chiều. Các bảng ở nơi khác là khối `generated`, không điền tay.
9. **Nếu folder là git repo và có thay đổi chưa commit,** nhắc chủ dự án commit trước khi bạn ghi file.

## Reading order

1. `AGENTS.md`
2. `context/*.md` (toàn bộ, trừ khi card nói khác)
3. Card của bước đang chạy trong `steps/`
4. Đúng các file input mà card liệt kê, không hơn

Không đọc cả folder để "lấy thêm ngữ cảnh": thêm file không liên quan làm kết quả tệ đi.

## Running a step

Khi chủ dự án nói "chạy step N của `steps/<tên>.md`":

1. Đọc card, tìm step N.
2. Chỉ đọc các file ở dòng `Input` của step đó.
3. Làm theo dòng `Instruction` và ghi kết quả vào section ở dòng `Output`.
4. Báo lại: đã đọc file nào, đã ghi vào đâu, điều gì bạn không chắc.

Step có nhãn **(YOU)** là việc của chủ dự án: bạn không làm thay, chỉ giúp nếu được hỏi.

## Writing

- Viết bằng tiếng Việt, giữ các thuật ngữ nghề bằng tiếng Anh (insight, hypothesis, opportunity, handoff...).
- Giữ nguyên tiêu đề section bằng tiếng Anh, vì các step card và hub gọi theo đúng tên đó.
