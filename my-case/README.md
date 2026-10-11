# Project: [tên dự án]

File này là trang đầu của dự án. Điền **Project card** trước, rồi dùng bảng "Bắt đầu từ đâu" bên dưới để chọn việc tiếp theo.

## Project card

| | |
|---|---|
| Tên dự án | |
| Câu hỏi của business (một câu) | |
| Giai đoạn hiện tại | Setup / Discover / Define / Develop / Deliver |
| Chủ dự án | |
| Người liên quan (product, business, engineering) | |
| Bắt đầu | |
| Cập nhật lần cuối | |
| Công cụ AI được phép dùng cho dự án này | |
| Quy tắc dữ liệu | Xem `context/data-rules.md` |

<!-- template-only -->
> **Đang ở trong `my-case`, folder template.** Hub của nó còn dữ liệu mẫu `[EXAMPLE]` để bạn thấy hub chạy ra sao. Để bắt đầu một dự án thật, chạy `python3 tools/new-case.py <tên-dự-án>` ở folder gốc của workspace: lệnh tạo một folder sạch cạnh `my-case`. Đừng điền thẳng vào `my-case`.
<!-- /template-only -->

## Bắt đầu từ đâu

Chọn việc bạn muốn làm, rồi mở đúng chỗ trong cột giữa.

| Tôi muốn... | Mở | Nhờ AI chạy |
|---|---|---|
| **Bắt đầu dự án:** ghi sản phẩm, người dùng, quy tắc dữ liệu | `context/product-and-users.md`, rồi `context/data-rules.md` | |
| **Hiểu người dùng và thị trường** (Discover) | `work/discover/` | `steps/user-voice-synthesis.md`, `steps/competitor-analysis.md` |
| **Chốt vấn đề đáng giải** (Define) | `work/define/problem-brief.md` | |
| **Khám phá hướng giải, dựng prototype** (Develop) | `work/develop/`, `work/prototype/` | |
| **Test và bàn giao** (Deliver) | `work/deliver/` | |
| **Ghi lại một quyết định** | `hub/decisions/` (một file mỗi decision) và `reference/case-log.md` (một dòng) | `steps/refresh-hub.md` |
| **Thêm một tài liệu vào báo cáo** (persona, flow, ảnh, prototype) | `hub/artifacts/` | |
| **Đánh giá thiết kế theo heuristics, chấm severity** | `reference/principle-checks.md`, `reference/severity-levels.md` | |
| **Kiểm tra gate** | `reference/gates.md` | `steps/refresh-hub.md` |
| **Xem tiến độ và những chỗ cần xem lại** | `index.html`, mục Overview | |
| **Gửi báo cáo cho người khác** | `index.html` (đổi tên rồi gửi) | `steps/export-hub.md` |
| **Thêm một trang tra cứu của riêng bạn** (glossary, brand voice...) | Thả một file `.md` vào `reference/` | |

## Sơ đồ folder

```
my-case/
├── README.md        trang này: bắt đầu từ đâu
├── index.html       báo cáo hub: bấm đúp để xem bằng trình duyệt
├── AGENTS.md        luật cho AI tool (tool tự đọc file này khi bạn mở folder)
│
├── context/         THÔNG TIN NỀN: sản phẩm, người dùng, quy tắc. Đưa cho AI đọc trước
├── work/            LÀM VIỆC theo giai đoạn
│   ├── discover/    define/    develop/    deliver/
│   ├── sources/     dữ liệu nghiên cứu: anonymised/ (đã ẩn danh) và _raw-private/ (gốc, không đưa cho AI)
│   └── prototype/   code prototype
├── hub/             BẢN GHI QUYẾT ĐỊNH: opportunities/, hypotheses/, decisions/, evidence/, metrics/,
│                    các trang giai đoạn 01 đến 07, và artifacts/ (tài liệu)
├── reference/       TRA CỨU: gates, principle checks, severity levels, case log, và trang bạn thêm
│
├── steps/           CÁC BƯỚC LÀM VIỆC VỚI AI (step card): nói với AI "chạy steps/<tên>.md"
├── _scripts/        script tạo báo cáo (bạn hiếm khi cần mở)
└── _personal/       ghi chú riêng, không đưa cho AI
```

Bốn folder đầu là bốn việc: **hiểu bối cảnh → làm việc → ghi quyết định → tra cứu**. Hai folder bắt đầu bằng `_` là phần kỹ thuật: bạn không cần mở chúng để làm việc.

## Rules

1. **Ẩn danh trước khi dán vào AI tool.** Dữ liệu gốc để ở `work/sources/_raw-private/`.
2. **AI chỉ trả về một phần mỗi lần, và bạn tự dán vào.**
3. **Bản nháp của AI và bản bạn đã kiểm tra nằm ở hai chỗ riêng.** Chênh lệch giữa hai bản là tỷ lệ lỗi của AI.
4. **Con số chưa xác nhận được thì ghi `assumed`.**

## Giữ cho dự án luôn mới

- **Quyết định mới:** một file ở `hub/decisions/` và một dòng ở `reference/case-log.md`.
- **Thông tin mới:** sửa file item hoặc file làm việc, nhờ AI chạy `steps/refresh-hub.md`, rồi tạo lại `index.html` (nhờ AI chạy `python3 _scripts/export-hub.py`).
- **Trước thay đổi lớn:** lưu một mốc (commit) hoặc copy folder thành bản `-backup`.
- **Gửi cho người khác:** copy `index.html` ra ngoài và đổi tên (ví dụ `onboarding-redesign-report.html`).
