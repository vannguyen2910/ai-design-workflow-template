# AI Design Workflow: Workspace

Đây là folder làm việc của bạn trong 7 tuần của khoá AI Design Workflow. Ghi chú, bằng chứng, quyết định và prototype của case nằm ở đây. Bạn không cần biết GitHub hay lập trình để bắt đầu.

## Start in 3 steps

1. **Lấy folder về máy.** Mở trang GitHub của repo này, bấm nút xanh **Code**, chọn **Download ZIP**. Giải nén file vừa tải và đặt folder vào `Documents`.
2. **Đặt tên cho case.** Đổi tên folder `my-case` theo case của bạn: chữ thường, nối bằng dấu gạch ngang, ví dụ `onboarding-redesign`.
3. **Mở bằng Obsidian.** Cài [Obsidian](https://obsidian.md) (miễn phí), chọn **Open folder as vault**, rồi chọn folder case của bạn. Mở file `hub/README.md` để thấy trang tổng quan.

Xong ba bước này là bạn đã có chỗ làm việc. Phần còn lại làm dần theo từng tuần.

Chưa muốn cài Obsidian? Các file đều là text, nên bạn đọc được bằng trình soạn thảo bất kỳ. Các cách xem khác nằm ở [`guides/02-set-up-your-case.md`](guides/02-set-up-your-case.md).

## What is inside

Bên ngoài:

```
ai-design-workflow-workspace/
├── README.md        file này
├── guides/          hướng dẫn từng bước, viết cho người chưa dùng GitHub
├── my-case/         folder của bạn: các file còn trống, sẵn để điền
└── demo-case/       một case giả (Kitchen Crate) để xem mẫu hoặc luyện tập
```

Bên trong `my-case/`:

```
my-case/
├── AGENTS.md        "luật chơi" cho AI tool; tool tự đọc file này khi bạn mở folder
├── 00-context/      thông tin nền về sản phẩm và người dùng; đưa cho AI đọc trước tiên
├── 01-discover/     tìm hiểu vấn đề: scope, tiếng nói của người dùng, đối thủ
│   └── sources/     dữ liệu gốc: anonymised/ (đã ẩn danh, AI được đọc)
│                    và _raw-private/ (chưa ẩn danh, AI không được đọc)
├── 02-define/       problem brief: vấn đề đáng giải
├── 03-develop/      các hướng giải quyết, alignment check, prototype
├── 04-deliver/      kế hoạch test, kết quả test, handoff, kế hoạch đo
├── hub/             Knowledge Hub: nơi mọi quyết định được nối về nhu cầu của người dùng
├── workflow/        các bước làm việc với AI, mỗi bước một file hướng dẫn
├── tools/           script tạo báo cáo HTML từ hub
├── _personal/       ghi chú riêng của bạn, không đưa cho AI
└── case-log.md      nhật ký quyết định, mỗi quyết định một dòng
```

## Words you will see

| Từ | Nghĩa |
|---|---|
| **AI tool** | Công cụ AI bạn dùng: chat để hỏi đáp, hoặc coding tool để đọc và ghi file trong folder |
| **Ẩn danh** | Thay tên người, tên công ty và số liệu thật bằng tên và số giả trước khi đưa cho AI |
| **Hub** | Folder `hub/`, nơi ghi lại các quyết định thiết kế và lý do đứng sau chúng |
| **Item** | Một nhu cầu, giả thuyết, quyết định, bài kiểm tra hoặc chỉ số. Mỗi item là một file |
| **Step card** | File trong `workflow/` hướng dẫn một bước làm việc với AI |
| **assumed** | Nhãn bạn ghi cạnh con số chưa được ai xác nhận |

## Which case do I use?

| Tình huống | Dùng |
|---|---|
| Bạn có case thật và đã ẩn danh được | `my-case` |
| Công ty cấm AI tool, hoặc case quá nhạy cảm để đưa vào lớp | `demo-case` |
| Bạn bỏ lỡ một tuần và cần bắt kịp | `demo-case` (có sẵn prototype ở tuần 6) |
| Bạn muốn xem một case chạy hết quy trình trước khi làm case của mình | `demo-case` |

`demo-case` là case giả, mọi thứ trong đó đều bịa. Cấu trúc của nó giống hệt `my-case`, nên bạn có thể làm hết khoá trên đó.

## What to fill each week

| Tuần | Module | Điền vào |
|---|---|---|
| 1 | Your Design Process, with AI | `00-context/`: `product-and-users.md`, `accessibility-rules.md`, `data-rules.md`, rồi `open-questions.md` (`glossary.md` là tuỳ chọn); `_personal/my-direction.md` |
| 2 | Discover the Problem | `01-discover/scope.md`, `user-voice-synthesis.md`; dữ liệu đã ẩn danh bỏ vào `sources/anonymised/` |
| 3 | Frame the Problem | `00-context/principle-checks.md`, `02-define/problem-brief.md` |
| 4 | Explore Ideas | `03-develop/options.md` |
| 5 | Build Your First Prototype | `00-context/design-system-notes.md`, `03-develop/prototype/` |
| 6 | Refine and Test | `prototype/` (chỉnh lại), `03-develop/alignment.md`, `04-deliver/test-plan.md`, `findings.md` |
| 7 | Hand Off and Present | `04-deliver/handoff.md`, `measurement-plan.md`; đọc lại `_personal/my-direction.md` |
| Mỗi tuần | | `case-log.md` và trang hub tương ứng |

## Four rules

1. **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `01-discover/sources/_raw-private/`, bạn tự thay tên rồi mới lưu bản sạch vào `anonymised/`.
2. **Mỗi lần chỉ nhờ AI viết một phần.** Bạn đọc kết quả rồi tự dán vào file, để AI không viết đè phần bạn đã chốt.
3. **Giữ bản nháp của AI và bản bạn đã sửa ở hai chỗ riêng.** Chênh lệch giữa hai bản cho bạn thấy AI sai nhiều hay ít.
4. **Con số nào chưa xác nhận được thì ghi `assumed`.**

## Make it yours

Bạn đổi được hầu hết mọi thứ:

- Đổi tên `my-case`, nhân đôi nó cho case thứ hai, hoặc thêm folder riêng như `05-notes/`.
- Xoá file bạn không dùng, ví dụ `glossary.md` hay `competitor-analysis.md`.
- Sửa nội dung các file mẫu cho hợp cách làm của bạn.

Có hai thứ nên giữ nguyên để AI tool và hub đọc đúng:

- **Tên folder `00-context` đến `04-deliver`, folder `workflow/` và file `AGENTS.md`.** Các bài và các step card gọi file theo đúng đường dẫn này.
- **Tên file trong `hub/` và mã của item** (`O1`, `H1`, `D1`...). Các item nối với nhau qua mã, nên đổi tên là làm đứt liên kết.

## Stuck?

Chụp màn hình chỗ bạn đang kẹt và gửi vào nhóm lớp, kèm một câu cho biết bạn đang làm bước nào. Trong lúc chờ, bạn vẫn làm tiếp phần khác được.

## Guides

| File | Khi nào đọc |
|---|---|
| [`01-get-the-folder.md`](guides/01-get-the-folder.md) | Trước tuần 1: lấy folder về máy, có hoặc không dùng GitHub |
| [`05-obsidian.md`](guides/05-obsidian.md) | Tuần 1: cách xem và làm việc với hub bằng Obsidian (khuyên dùng) |
| [`02-set-up-your-case.md`](guides/02-set-up-your-case.md) | Tuần 1: đặt tên, hiểu từng folder, làm việc với AI tool |
| [`03-github-basics.md`](guides/03-github-basics.md) | Khi bạn muốn lưu bản làm việc lên GitHub và chưa từng dùng |
| [`04-share-your-hub.md`](guides/04-share-your-hub.md) | Khi bạn cần cho stakeholder hoặc người khác xem hub |
