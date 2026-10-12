# Rules for the AI tool

File này dành cho AI tool. Đọc nó trước khi làm bất cứ việc gì trong folder này. Chủ dự án là người quyết định; bạn soạn nháp và kiểm tra giúp.

## What this folder is

Case folder của một người làm sản phẩm (designer, researcher, PM...) làm việc theo quy trình AI-assisted: AI soạn nháp, chủ dự án kiểm tra và quyết định. Folder chia theo việc bạn làm: `context/` (thông tin nền), `stages/` (trang kể lại từng giai đoạn), `work/` (mọi thứ làm ra), `insights/` (các item nối với nhau), `standards/` (trang tra cứu), và `_skills/` (step card và script cho AI). Mỗi bước làm việc với AI được định nghĩa bằng một step card trong `_skills/`.

## Map

Mỗi folder không có `_` ở gốc là một mục trong menu của báo cáo `index.html`, cùng tên.

| Đường dẫn | Là gì | Bạn được làm gì |
|---|---|---|
| `AGENTS.md` | Luật cho AI tool (file này) | Đọc |
| `README.md` | Overview: project card và bảng "Bạn muốn làm gì?" | Đọc. Chỉ sửa khi được yêu cầu |
| `guide.md` | Trang Hướng dẫn sử dụng của báo cáo (tab "Hướng dẫn" ở menu bên trái): workspace là gì, bắt đầu dự án mới, thêm task mới, preview hub, thuật ngữ làm việc với AI; viết cho người không rành kỹ thuật | Đọc. Chỉ sửa khi được yêu cầu; giữ giọng đơn giản và các câu mẫu dán được cho AI tool |
| `context/*.md` | Context pack: thông tin nền (sản phẩm, người dùng, quy tắc dữ liệu, design system) | Đọc đầu tiên ở mọi bước. Không sửa trừ khi được yêu cầu |
| `_skills/*.md` | Định nghĩa từng bước làm việc với AI (step card) | Đọc card của bước đang chạy |
| `stages/README.md` | Bảng Pages: mỗi dòng là một trang giai đoạn, tự ghép từ file ở `work/` và bảng item ở `insights/` | Chỉ sửa bảng khi được yêu cầu. Không tạo file `.md` nào khác ở đây: trang giai đoạn không có nội dung riêng |
| `work/*.md`, `work/<tên>/index.md` | Mọi thứ làm ra: file làm việc theo giai đoạn (`scope`, `problem-brief`, `findings`...) và tài liệu (wireframe, persona, flow). Có thể kèm ảnh, PDF, HTML trong folder | Chỉ ghi vào đúng section được yêu cầu. Không chép nội dung vào `stages/`: trang đó dẫn về file làm việc |
| `work/sources/anonymised/` | Dữ liệu đã ẩn danh, có ID | Đọc. Nguồn duy nhất cho quote và số liệu |
| `work/wireframes/` | Wireframe: ảnh lo-fi và bản HTML các màn hình chính | Đọc. Thêm ảnh hoặc file vào đây khi được yêu cầu |
| `insights/opportunities/O1.md`, `hypotheses/H1.md`, `metrics/M1.md`, `decisions/D1.md`, `evidence/E1.md`, `findings/F1.md`… | **Nguồn duy nhất** của mỗi item (O, H, M, D, E, F). Mỗi loại một folder; tên file là mã của item | Đọc. Chỉ sửa khi được yêu cầu sửa đúng item đó. Không tự đặt `resolution: fixed` hay `accepted` cho finding |
| `insights/_templates/` | Mẫu rỗng cho từng loại item | Đọc. Copy vào đúng folder loại (ví dụ `insights/decisions/`) khi được yêu cầu tạo item mới, không sửa file mẫu |
| `standards/*.md` | Thước đo để kiểm tra công việc: gates, principle checks, severity levels, và mọi tiêu chí chủ dự án thêm vào | Đọc. Chỉ sửa khi được yêu cầu đúng trang đó. `insights/case-log.md`: thêm dòng khi được yêu cầu |
| `_skills/new-item.py` | Lệnh tạo một item mới và nối quan hệ | Chạy khi được yêu cầu tạo item (xem mục Where things go). Không sửa |
| `_skills/export-hub.py` | Script xuất báo cáo ra một file HTML | Chạy khi được yêu cầu (`python3 _skills/export-hub.py`). Không sửa, và không tự viết HTML thay cho script |
| `index.html` | Báo cáo, xuất ra từ Markdown để xem bằng trình duyệt | Không đọc, không sửa tay. Muốn cập nhật thì chạy `_skills/export-hub.py` |
| `_personal/` | Ghi chú riêng của chủ dự án | **Không đọc, không ghi** |
| `work/sources/_raw-private/` | Dữ liệu gốc chưa ẩn danh | **Không đọc, không ghi** |
| `work/original-docs/` | Tài liệu gốc của dự án mẫu (chỉ có ở demo-case) | Đọc để đối chiếu. Không sửa |

## Where things go

Khi chủ dự án nhờ bạn làm hoặc thêm một thứ gì đó mà không nói đặt ở đâu, bạn tự chọn chỗ theo bảng này. Nếu chủ dự án đã nói rõ chỗ thì làm theo họ.

| Chủ dự án đưa hoặc nhờ | Đặt ở | Ghi chú |
|---|---|---|
| Ảnh, PDF, video, prototype HTML, flow, hoặc tài liệu để người khác xem | `work/<tên-ngắn>/` kèm `index.md` (bắt đầu từ mẫu trong `work/_templates/`); tệp lẻ thì `work/<tên>.md`. Làm theo `_skills/add-media.md` | Điền `supports` bằng mã item nó làm bằng chứng cho nếu biết. Không biết thì để `[]`, đừng đoán |
| Sơ đồ flow từ Mermaid (user flow, E2E) | `python3 _skills/flow-from-mermaid.py <file.md> --out work/<tên> --title "..."`: mỗi subgraph một hình; mã giải pháp (A4, P3) được gắn thêm mã decision lấy từ property `solutions` của decision | Cần skill archify. Nếu decision thực hiện một giải pháp, ghi mã đó vào `solutions` |
| Chạy một phương pháp (assumptions map, journey map, ideation...) | Điền vào file method card có sẵn trong `work/` (xem tab theo giai đoạn của Work); không tạo file mới nếu đã có | Đổi `status` từ `planned` khi bắt đầu |
| Bản nháp hoặc tổng hợp của một giai đoạn | `work/<tên>.md` đúng file của giai đoạn (`scope`, `user-voice-synthesis`, `competitor-analysis`, `problem-brief`, `options`, `alignment`, `test-plan`, `findings`, `handoff`, `measurement-plan`) | Chỉ ghi vào đúng section được yêu cầu |
| Một quyết định thiết kế | `python3 _skills/new-item.py D ...` kèm `--owner`, `--state`, `--reason` (ghi luôn case log). Không tự đặt `accepted` khi chủ dự án chưa nói | `proposed` là mặc định |
| Một tài liệu nghiên cứu mới (phỏng vấn, khảo sát, test) cần rút insight | Làm theo `_skills/add-insights.md`: đề xuất trước, chờ chủ dự án duyệt, rồi mới tạo item bằng `new-item.py` | Không tạo item khi chưa được duyệt |
| Kết quả đo của một metric sau launch | Điền `result`, `measured_on`, `verdict` trong `insights/metrics/M<số>.md`; điều đã học viết ở `work/learning.md` | Chỉ ghi số chủ dự án đưa, không suy đoán `verdict` |
| Một nhu cầu, hypothesis, metric, decision, evidence hoặc finding | `python3 _skills/new-item.py <O/H/M/D/E/F> --title "..."` kèm các quan hệ (`--tests H1`, `--serves O1`, `--found-in E1`...). Lệnh chọn mã tiếp theo, tạo file đúng folder và kiểm tra mọi mã bạn nối có thật | Tự điền quan hệ từ nội dung chủ dự án đưa; nếu chưa chắc về một quan hệ thì hỏi, đừng đoán. Xem `python3 _skills/new-item.py --help` |
| Thông tin nền mới về sản phẩm (glossary, brand voice, quy tắc...) | `context/<tên>.md` | AI đọc trước tiên; tự hiện ở mục Context |
| Một tiêu chí hoặc checklist mới để kiểm tra công việc | `standards/<tên>.md` | Tự hiện ở mục Standards |
| Dữ liệu nghiên cứu thô (phỏng vấn, khảo sát) | **Không** tự đặt vào `work/sources/anonymised/`. Nhắc chủ dự án ẩn danh trước; bản gốc để ở `work/sources/_raw-private/`, bạn không đọc | |
| Ghi chú riêng của chủ dự án | `_personal/` | Bạn không đọc, không ghi |
| Không rõ thuộc loại nào | Hỏi lại một câu | Đừng đoán và đừng đặt ở gốc folder |

Khi đặt file:

1. **Mã kế tiếp:** liệt kê folder loại và dùng số lớn nhất cộng một. Không bao giờ ghi đè file đã có.
2. **Tên file ngắn, chữ thường, nối bằng dấu gạch ngang** cho tài liệu; mã item cho item.
3. **Nói lại chỗ bạn đã đặt:** nêu đường dẫn đầy đủ, và những gì bạn không chắc (ví dụ `supports` còn trống).
4. **Nhắc chủ dự án** tạo lại `index.html` (`python3 _skills/export-hub.py`) khi cần; muốn rà soát thì dùng `_skills/refresh-hub.md`.

## Hard rules

1. **Chỉ trả về section được yêu cầu.** Không sửa section khác, không sửa file khác. Chủ dự án tự dán kết quả vào, hoặc bạn ghi đúng vào section được chỉ định.
2. **Không sửa section "(AI draft)" sau khi đã tạo, và không sửa section "(verified)" của chủ dự án** trừ khi được yêu cầu đúng section đó. Bản nháp và bản đã kiểm tra luôn nằm ở hai section riêng.
3. **Chỉ dùng nguồn trong `work/sources/anonymised/`.** Không bịa quote, số liệu, tên sản phẩm hay nguồn. Không có trong nguồn thì ghi `unknown`.
4. **Quote nguyên văn, kèm ID.** Không viết lại, không rút gọn.
5. **Con số nào chưa được xác nhận thì ghi `assumed`.** Suy luận không có trong nguồn thì ghi `inferred`.
6. **Dừng và báo** nếu bạn thấy dữ liệu có vẻ chưa ẩn danh (tên người, email, username, tên công ty) trong folder bạn được phép đọc.
7. **Nói rõ điều bạn không chắc.** Liệt kê item bạn không chắc thay vì đoán link hay quan hệ.
8. **Không tạo bản sao của một item.** Item chỉ tồn tại trong file của nó (`insights/decisions/D2.md`...). Quan hệ nằm trong properties (khối `---` ở đầu file) dưới dạng wikilink trong dấu nháy, và chỉ khai báo một chiều. Các bảng ở nơi khác là khối `generated`, không điền tay.
9. **Nếu folder là git repo và có thay đổi chưa commit,** nhắc chủ dự án commit trước khi bạn ghi file.

## Reading order

1. `AGENTS.md`
2. `context/*.md` (toàn bộ, trừ khi card nói khác)
3. Card của bước đang chạy trong `_skills/`
4. Đúng các file input mà card liệt kê, không hơn

Không đọc cả folder để "lấy thêm ngữ cảnh": thêm file không liên quan làm kết quả tệ đi.

## Running a step

Khi chủ dự án nói "chạy step N của `_skills/<tên>.md`":

1. Đọc card, tìm step N.
2. Chỉ đọc các file ở dòng `Input` của step đó.
3. Làm theo dòng `Instruction` và ghi kết quả vào section ở dòng `Output`.
4. Báo lại: đã đọc file nào, đã ghi vào đâu, điều gì bạn không chắc.

Step có nhãn **(YOU)** là việc của chủ dự án: bạn không làm thay, chỉ giúp nếu được hỏi.

## Writing

- Viết bằng tiếng Việt, giữ các thuật ngữ nghề bằng tiếng Anh (insight, hypothesis, opportunity, handoff...).
- Giữ nguyên tiêu đề section bằng tiếng Anh, vì các step card và hub gọi theo đúng tên đó.
