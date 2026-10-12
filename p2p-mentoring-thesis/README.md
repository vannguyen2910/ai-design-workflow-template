# Project: P2P mentoring service (Master Thesis)

File này là trang đầu của dự án. Điền **Project card** trước, rồi dùng bảng "Bắt đầu từ đâu" bên dưới để chọn việc tiếp theo.

## Project card

| | |
|---|---|
| Tên dự án | P2P mentoring service (Master Thesis) |
| Câu hỏi của business (một câu) | |
| Giai đoạn hiện tại | Setup / Discover / Define / Develop / Deliver |
| Chủ dự án | |
| Người liên quan (product, business, engineering) | |
| Bắt đầu | |
| Cập nhật lần cuối | |
| Công cụ AI được phép dùng cho dự án này | |
| Agreement status | pending *(agreed / pending / not available)* |
| Quy tắc dữ liệu | Xem `context/data-rules.md` |

## Bắt đầu từ đâu

Chọn việc bạn muốn làm, rồi mở đúng chỗ trong cột giữa.

| Tôi muốn... | Mở | Nhờ AI chạy |
|---|---|---|
| **Bắt đầu dự án:** ghi sản phẩm, người dùng, quy tắc dữ liệu | `context/product-and-users.md`, rồi `context/data-rules.md` | |
| **Hiểu người dùng và thị trường** (Discover) | `work/scope.md`, `work/user-voice-synthesis.md`, `work/competitor-analysis.md` | `_ai/user-voice-synthesis.md`, `_ai/competitor-analysis.md` |
| **Chốt vấn đề đáng giải** (Define) | `work/problem-brief.md` | |
| **Khám phá hướng giải, dựng prototype** (Develop) | `work/options.md`, `work/alignment.md`, `work/prototype/` | |
| **Test và bàn giao** (Deliver) | `work/test-plan.md`, `work/findings.md`, `work/handoff.md`, `work/measurement-plan.md` | |
| **Ghi lại một quyết định** | `insights/decisions/` (một file mỗi decision) và `insights/case-log.md` (một dòng) | `python3 _ai/new-item.py D` |
| **Thêm ảnh, video, PDF hoặc tài liệu vào báo cáo** (wireframe, screenshot, persona, flow, prototype) | Thả vào một folder trong `work/` (xem mục "Thêm ảnh, video, PDF" ở `work/README.md`) | `_ai/add-media.md` |
| **Đánh giá thiết kế theo heuristics, chấm severity** | `standards/principle-checks.md`, `standards/severity-levels.md` | |
| **Ghi một vấn đề usability tìm thấy (finding)** | `insights/findings/` (một file mỗi finding; chấm severity theo `standards/severity-levels.md`) | `python3 _ai/new-item.py F` |
| **Kiểm tra gate** | `standards/gates.md` | `python3 _ai/export-hub.py` (cột Kiểm tra tự động) |
| **Xem tiến độ và những chỗ cần xem lại** | `index.html`, mục Overview | |
| **Gửi báo cáo cho người khác** | `index.html` (đổi tên rồi gửi) | `_ai/export-hub.md` |
| **Thêm một trang tra cứu của riêng bạn** (glossary, brand voice...) | Thả một file `.md` vào `standards/` | |

**Nhờ AI đặt đúng chỗ.** Bạn không cần nhớ folder: đưa ảnh, tài liệu hoặc một quyết định cho AI tool và nói "thêm vào dự án". `AGENTS.md` có bảng "Where things go" để AI chọn chỗ (ảnh và tài liệu vào `work/`, quyết định vào `insights/decisions/`...) và nói lại chỗ nó đã đặt. Nếu không chắc nó sẽ hỏi bạn một câu.

## Sơ đồ folder

```
p2p-mentoring-thesis/
├── README.md        OVERVIEW: project card và bảng "Tôi muốn... mở..."
├── index.html       báo cáo: bấm đúp để xem bằng trình duyệt
├── AGENTS.md        luật cho AI tool (tool tự đọc file này khi bạn mở folder)
│
├── context/         CONTEXT    thông tin nền: sản phẩm, người dùng, quy tắc, design system
├── stages/          STAGES     mỗi giai đoạn một trang, tự dựng từ work/ và insights/
├── work/            WORK       mọi thứ làm ra: file làm việc, wireframe, prototype, persona, nguồn nghiên cứu
├── insights/        INSIGHTS   nhu cầu, hypothesis, decision, evidence, finding, metric (mỗi loại một folder)
├── standards/       REFERENCE  gates, principle checks, severity levels, case log
│
├── _ai/             step card và script cho AI (hiếm khi cần mở tay)
└── _personal/       ghi chú riêng, không đưa cho AI
```

**Một quy tắc để nhớ: mỗi folder không có `_` là một mục trong menu báo cáo, cùng tên.** Folder có `_` không nằm trong báo cáo.

### Menu của báo cáo ↔ folder

Báo cáo `index.html` ghi sẵn dòng "Folder" và "Thêm mới" ở đầu mỗi mục, và "File gốc" ở cuối mỗi trang, nên từ báo cáo bạn luôn biết file nằm ở đâu.

| Mục trong báo cáo | Folder | Có gì | Muốn thêm mới thì |
|---|---|---|---|
| **Overview** | `README.md` | Project card, tiến độ, những chỗ cần xem lại (tự tính) | Sửa `README.md` và các file nguồn, rồi tạo lại báo cáo |
| **Context** | `context/` | Sản phẩm, người dùng, quy tắc dữ liệu, design system | Thả một file `.md` vào folder |
| **Stages** | `stages/` | Một trang cho mỗi giai đoạn, tự dựng từ `work/` và `insights/` (bạn không viết ở đây) | Thêm một dòng vào bảng Pages ở `stages/README.md`: chọn file ở `work/` và bảng item muốn hiện |
| **Work** | `work/` | Mọi thứ làm ra: file làm việc, wireframe, prototype, persona, flow | Thả file vào folder, hoặc tạo folder con (kèm `index.md`) rồi thả ảnh, PDF, video vào đó |
| **Insights** | `insights/` (`opportunities/`, `hypotheses/`, `decisions/`, `evidence/`, `findings/`, `metrics/`) | Các item nối với nhau | Chạy `python3 _ai/new-item.py`: lệnh hỏi từng câu, chọn mã tiếp theo và nối quan hệ giúp bạn |
| **Standards** | `standards/` | Thước đo để kiểm tra: gates, principle checks, severity levels | Thả một file `.md` vào folder |

## Rules

1. **Ẩn danh trước khi dán vào AI tool.** Dữ liệu gốc để ở `work/sources/_raw-private/`.
2. **AI chỉ trả về một phần mỗi lần, và bạn tự dán vào.**
3. **Bản nháp của AI và bản bạn đã kiểm tra nằm ở hai chỗ riêng.** Chênh lệch giữa hai bản là tỷ lệ lỗi của AI.
4. **Con số chưa xác nhận được thì ghi `assumed`.**

## Giữ cho dự án luôn mới

- **Quyết định mới:** chạy `python3 _ai/new-item.py D` (lệnh tạo file ở `insights/decisions/` và ghi một dòng vào `insights/case-log.md`).
- **Thông tin mới:** sửa file item hoặc file làm việc, rồi tạo lại `index.html` (nhờ AI chạy `python3 _ai/export-hub.py`; lệnh này cũng tự cập nhật các bảng item trong `stages/`).
- **Trước thay đổi lớn:** lưu một mốc (commit) hoặc copy folder thành bản `-backup`.
- **Gửi cho người khác:** copy `index.html` ra ngoài và đổi tên (ví dụ `onboarding-redesign-report.html`).
