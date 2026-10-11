# AI Design Workflow: Project Workspace

Đây là workspace cho một **dự án thiết kế có AI hỗ trợ**: nơi giữ bối cảnh, bằng chứng, quyết định và prototype của dự án, và nối mọi quyết định về nhu cầu của người dùng đứng sau nó.

Bạn học cách làm việc này trong khoá AI Design Workflow, rồi **dùng tiếp cho các dự án thật**. Bạn không cần biết GitHub hay lập trình để bắt đầu.

## Start a project in 3 steps

1. **Lấy workspace về máy.** Mở trang GitHub của repo này, bấm nút xanh **Code**, chọn **Download ZIP**. Giải nén và đặt folder vào `Documents`.
2. **Đặt tên cho dự án.** Đổi tên folder `my-case` theo dự án của bạn: chữ thường, nối bằng dấu gạch ngang, ví dụ `onboarding-redesign`.
3. **Xem hub.** Bấm đúp file `index.html` trong folder dự án: nó mở bằng trình duyệt và không cần cài gì. Khi làm việc, mở **cả folder dự án** bằng công cụ bạn quen (AI coding tool, VS Code hay Obsidian).

Xong ba bước này là dự án đã có chỗ ở. Các bước sau làm dần theo tiến độ thật của dự án.

## One project, one folder

Mỗi dự án là **một case folder độc lập và tự chứa**: nó mang theo luật cho AI (`AGENTS.md`), các bước làm việc (`workflow/`), script tạo trang chủ (`tools/`) và hub. Bạn copy nguyên folder ra khỏi workspace này, ví dụ vào folder dự án của công ty, và nó vẫn chạy.

(Trong tài liệu này, "case" nghĩa là "một dự án thiết kế".)

## Words you will see

| Từ | Nghĩa |
|---|---|
| **AI tool** | Công cụ AI bạn dùng: chat để hỏi đáp, hoặc coding tool để đọc và ghi file trong folder |
| **Ẩn danh** | Thay tên người, tên công ty và số liệu thật bằng tên và số giả trước khi đưa cho AI |
| **Hub** | Folder `hub/`, nơi ghi lại các quyết định thiết kế và lý do đứng sau chúng. File `index.html` là trang chủ để xem nó |
| **Item** | Một nhu cầu, giả thuyết, quyết định, bài kiểm tra hoặc chỉ số. Mỗi item là một file |
| **Step card** | File trong `workflow/` hướng dẫn một bước làm việc với AI |
| **assumed** | Nhãn bạn ghi cạnh con số chưa được ai xác nhận |

## Inside a project folder

```
my-case/
├── index.html       trang chủ của hub: bấm đúp để xem bằng trình duyệt
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
├── tools/           script tạo trang chủ `index.html` từ hub
├── _personal/       ghi chú riêng của bạn, không đưa cho AI
└── case-log.md      nhật ký quyết định, mỗi quyết định một dòng
```

Bên ngoài `my-case/` còn `guides/` (hướng dẫn từng bước cho người chưa dùng GitHub) và `demo-case/` (một dự án mẫu hoàn chỉnh để xem hoặc luyện tập).

## The life of a project

Một dự án đi qua năm giai đoạn. Bạn không cần làm hết một lượt: điền các file khi dự án thực sự tới giai đoạn đó.

| Giai đoạn | Câu hỏi cần trả lời | File chính | Trong khoá |
|---|---|---|---|
| **Setup** | Dự án là gì, ai dùng, được đưa gì cho AI? | `00-context/`: `product-and-users.md`, `accessibility-rules.md`, `data-rules.md`, `open-questions.md` | Tuần 1 |
| **Discover** | Chúng ta chưa biết gì, và bằng chứng nào có thể tin? | `01-discover/scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` | Tuần 2 |
| **Define** | Vấn đề nào đáng giải, và thành công trông thế nào? | `02-define/problem-brief.md`, `00-context/principle-checks.md` | Tuần 3 |
| **Develop** | Giải bằng cách nào, và vì sao chọn cách đó? | `03-develop/options.md`, `prototype/`, `alignment.md`, `00-context/design-system-notes.md` | Tuần 4 đến 6 |
| **Deliver** | Nó có hiệu quả không, và bàn giao gì? | `04-deliver/test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` | Tuần 6 và 7 |
| **Mọi giai đoạn** | Chúng ta đã quyết định gì, và vì sao? | `case-log.md` và các trang của `hub/` | Mỗi tuần |

Dự án thật không đi một chiều. Khi có thông tin mới, bạn quay lại giai đoạn trước: cập nhật file ở giai đoạn đó, rồi tạo lại hub (xem `workflow/refresh-hub.md`).

## Keep a project alive

Workspace chỉ có giá trị khi nó phản ánh dự án hôm nay. Bốn thói quen giữ nó sống:

1. **Ghi quyết định ngay khi quyết định.** Một dòng vào `case-log.md`: quyết định gì, vì sao, AI đã giúp ở đâu.
2. **Mỗi thông tin mới đi vào một chỗ.** Sửa file item hoặc working file, không copy sang nơi khác. Rồi tạo lại hub và `index.html`.
3. **Lưu một mốc trước thay đổi lớn.** Dùng GitHub Desktop (commit) hoặc copy folder thành bản `-backup`.
4. **Gửi trang chủ, không gửi folder.** Cho stakeholder xem bằng `index.html` đã đổi tên (xem [`guides/04-share-your-hub.md`](guides/04-share-your-hub.md)).

Khi dự án kết thúc: đặt status các gate, viết ba dòng rút kinh nghiệm vào `case-log.md`, tạo lại `index.html` lần cuối rồi lưu trữ folder.

## Start another project

Giữ một bản template sạch để dùng lại:

1. **Đừng điền vào bản template gốc nếu bạn định làm nhiều dự án.** Lấy template mới (tải ZIP, hoặc **Use this template** lần nữa) cho mỗi dự án.
2. Đổi tên folder `my-case` trong bản mới theo dự án.
3. Xoá dữ liệu mẫu: các item `[EXAMPLE]` trong `hub/` và tên case trong `hub/README.md`. `index.html` có thanh đen nhắc bạn khi còn dữ liệu mẫu.
4. Điền `00-context/` đầu tiên, rồi làm theo giai đoạn.

## Use it for real work

Khi dùng cho dự án thật của công ty:

- **Kiểm tra chính sách AI của công ty trước.** Viết `00-context/data-rules.md` bằng lời của bạn.
- **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `01-discover/sources/_raw-private/`: nó không lên GitHub và AI không đọc.
- **Để repo ở chế độ Private.** Chỉ công khai khi toàn bộ dự án được phép chia sẻ.
- **Hub giúp bạn giải thích quyết định,** nhưng `assumed` và `unknown` phải được giữ đúng: đừng biến một con số chưa xác nhận thành một sự thật trong báo cáo gửi đi.

## Four rules

1. **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `01-discover/sources/_raw-private/`, bạn tự thay tên rồi mới lưu bản sạch vào `anonymised/`.
2. **Mỗi lần chỉ nhờ AI viết một phần.** Bạn đọc kết quả rồi tự dán vào file, để AI không viết đè phần bạn đã chốt.
3. **Giữ bản nháp của AI và bản bạn đã sửa ở hai chỗ riêng.** Chênh lệch giữa hai bản cho bạn thấy AI sai nhiều hay ít.
4. **Con số nào chưa xác nhận được thì ghi `assumed`.**

## Make it yours

Bạn đổi được hầu hết mọi thứ:

- Đổi tên folder dự án, nhân đôi nó, hoặc thêm folder riêng như `05-notes/`.
- Xoá file bạn không dùng, ví dụ `glossary.md` hay `competitor-analysis.md`.
- Sửa nội dung các file mẫu cho hợp cách làm của team bạn.

Có hai thứ nên giữ nguyên để AI tool và hub đọc đúng:

- **Tên folder `00-context` đến `04-deliver`, folder `workflow/` và file `AGENTS.md`.** Các step card gọi file theo đúng đường dẫn này.
- **Tên file trong `hub/` và mã của item** (`O1`, `H1`, `D1`...). Các item nối với nhau qua mã, nên đổi tên là làm đứt liên kết.

## Which folder do I use?

| Tình huống | Dùng |
|---|---|
| Bạn có một dự án thật hoặc một case của riêng bạn | `my-case` |
| Công ty cấm AI tool, hoặc dự án quá nhạy cảm để đưa vào lớp | `demo-case` |
| Bạn muốn xem một dự án chạy hết quy trình trước khi làm của mình | `demo-case` |
| Bạn kẹt ở một giai đoạn và cần một ví dụ đã làm xong | `demo-case` |

`demo-case` là dự án mẫu, mọi thứ trong đó đều bịa. Cấu trúc của nó giống hệt `my-case`.

## Stuck?

Chụp màn hình chỗ bạn đang kẹt và gửi vào nhóm lớp, kèm một câu cho biết bạn đang làm bước nào. Trong lúc chờ, bạn vẫn làm tiếp phần khác được.

## Guides

| File | Khi nào đọc |
|---|---|
| [`01-get-the-folder.md`](guides/01-get-the-folder.md) | Khi bắt đầu: lấy folder về máy, có hoặc không dùng GitHub |
| [`02-set-up-your-case.md`](guides/02-set-up-your-case.md) | Khi bắt đầu: đặt tên, hiểu từng folder, làm việc với AI tool, chọn công cụ để mở folder |
| [`03-github-basics.md`](guides/03-github-basics.md) | Khi bạn muốn lưu bản làm việc lên GitHub và chưa từng dùng |
| [`04-share-your-hub.md`](guides/04-share-your-hub.md) | Khi bạn cần cho stakeholder hoặc người khác xem hub |
| [`05-obsidian.md`](guides/05-obsidian.md) | Tuỳ chọn: xem quan hệ giữa các quyết định bằng Obsidian |
