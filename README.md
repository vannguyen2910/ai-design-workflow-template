# Product Workspace with AI

Đây là workspace cho một **dự án sản phẩm có AI hỗ trợ**. Nó dành cho bất kỳ ai làm sản phẩm: product manager, designer, researcher, hay người làm một mình. Workspace giữ context, evidence, decision và prototype của dự án, và nối mỗi decision về user need đứng sau nó.

Bạn không cần biết GitHub hay lập trình để bắt đầu.

## Bắt đầu từ đâu

| Tôi muốn... | Làm gì |
|---|---|
| Xem một dự án hoàn chỉnh trước khi làm của mình | Bấm đúp `demo-case/index.html` |
| Bắt đầu một dự án của tôi | Làm theo "Start a project in 3 steps" ngay bên dưới |
| Làm việc trong một dự án đã có | Mở folder dự án, đọc `README.md` ở đó: nó có bảng "Tôi muốn... mở..." cho từng việc |
| Cần hướng dẫn từng bước (GitHub, chia sẻ, Obsidian) | Mở folder [`guides/`](guides/) |

## Start a project in 3 steps

1. **Lấy workspace về máy.** Mở trang GitHub của repo này, bấm nút xanh **Code**, chọn **Download ZIP**. Giải nén và đặt folder vào `Documents`.
2. **Tạo folder cho dự án.** Mở Terminal tại folder workspace và chạy lệnh dưới đây (Python 3 có sẵn trên Mac). Tên dự án viết chữ thường, nối bằng dấu gạch ngang. Lệnh tạo một folder sạch, đã xoá sẵn dữ liệu mẫu, và `my-case` được giữ nguyên làm template.

   ```
   python3 tools/new-case.py onboarding-redesign
   ```

   Không dùng được Terminal? Đổi tên folder `my-case` theo dự án của bạn, rồi tự xoá các item `[EXAMPLE]` trong `hub/`.
3. **Xem hub.** Bấm đúp file `index.html` trong folder dự án: nó mở bằng trình duyệt và không cần cài gì. Khi làm việc, mở **cả folder dự án** bằng công cụ bạn quen (AI coding tool, VS Code hay Obsidian).

Xong ba bước này là dự án đã có chỗ ở. Các bước sau làm dần theo tiến độ thật của dự án.

## One project, one folder

Mỗi dự án là **một case folder độc lập và tự chứa**: nó mang theo luật cho AI (`AGENTS.md`), các bước làm việc (`steps/`), script tạo báo cáo và hub. Bạn copy nguyên folder ra khỏi workspace này, ví dụ vào folder dự án của công ty, và nó vẫn chạy.

```
workspace/
├── README.md            file này
├── guides/              hướng dẫn từng bước
├── tools/new-case.py    lệnh tạo một dự án mới
├── my-case/             template sạch (đừng điền vào)
├── demo-case/           dự án mẫu hoàn chỉnh
└── <tên-dự-án>/         dự án của bạn, tạo bằng new-case.py
```

(Trong tài liệu này, "case" nghĩa là "một dự án sản phẩm".)

## Words you will see

| Từ | Nghĩa |
|---|---|
| **AI tool** | Công cụ AI bạn dùng: chat để hỏi đáp, hoặc coding tool để đọc và ghi file trong folder |
| **Ẩn danh** | Thay tên người, tên công ty và số liệu thật bằng tên và số giả trước khi đưa cho AI |
| **Hub** | Folder `hub/`, nơi ghi lại các design decision và lý do đứng sau chúng. File `index.html` là trang chủ để xem nó |
| **Item** | Một nhu cầu (opportunity), hypothesis, decision, evidence hoặc metric. Mỗi item là một file |
| **Step card** | File trong `steps/` hướng dẫn một bước làm việc với AI |
| **assumed** | Nhãn bạn ghi cạnh con số chưa được ai xác nhận |

## Inside a project folder

```
my-case/
├── README.md        trang đầu: bảng "Tôi muốn... mở..." cho từng việc
├── index.html       báo cáo hub: bấm đúp để xem bằng trình duyệt
├── AGENTS.md        luật cho AI tool; tool tự đọc file này khi bạn mở folder
│
├── context/         THÔNG TIN NỀN: sản phẩm, người dùng, quy tắc (đưa cho AI đọc trước tiên)
├── work/            LÀM VIỆC theo giai đoạn: discover/, define/, develop/, deliver/,
│                    cùng sources/ (dữ liệu nghiên cứu) và prototype/
├── hub/             BẢN GHI QUYẾT ĐỊNH: opportunities/, hypotheses/, decisions/, evidence/, metrics/,
│                    các trang giai đoạn, và artifacts/ (tài liệu)
├── reference/       TRA CỨU: gates, principle checks, severity levels, case log, và trang bạn thêm
│
├── steps/           CÁC BƯỚC LÀM VIỆC VỚI AI (step card)
├── _scripts/        script tạo báo cáo (hiếm khi cần mở)
└── _personal/       ghi chú riêng, không đưa cho AI
```

Bốn folder đầu là bốn việc: **hiểu bối cảnh, làm việc, ghi quyết định, tra cứu**. Folder bắt đầu bằng `_` là phần kỹ thuật hoặc riêng tư.


## The life of a project

Một dự án đi qua năm giai đoạn. Bạn không cần làm hết một lượt: điền các file khi dự án thực sự tới giai đoạn đó.

| Giai đoạn | Câu hỏi cần trả lời | File chính |
|---|---|---|
| **Setup** | Dự án là gì, ai dùng, được đưa gì cho AI? | `context/product-and-users.md`, `accessibility-rules.md`, `data-rules.md`, `open-questions.md` |
| **Discover** | Chúng ta chưa biết gì, và bằng chứng nào có thể tin? | `work/discover/scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` |
| **Define** | Vấn đề nào đáng giải, và thành công trông thế nào? | `work/define/problem-brief.md`, `reference/principle-checks.md` |
| **Develop** | Giải bằng cách nào, và vì sao chọn cách đó? | `work/develop/options.md`, `work/prototype/`, `work/develop/alignment.md`, `context/design-system-notes.md` |
| **Deliver** | Nó có hiệu quả không, và bàn giao gì? | `work/deliver/test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md`; chấm mức độ bằng `reference/severity-levels.md` |
| **Mọi giai đoạn** | Chúng ta đã quyết định gì, và vì sao? | `reference/case-log.md` và các trang của `hub/` |

Dự án thật không đi một chiều. Khi có thông tin mới, bạn quay lại giai đoạn trước: cập nhật file ở giai đoạn đó, rồi tạo lại hub (xem `steps/refresh-hub.md`).

## Keep a project alive

Workspace chỉ có giá trị khi nó phản ánh dự án hôm nay. Bốn thói quen giữ nó sống:

1. **Ghi decision ngay khi quyết định.** Một dòng vào `reference/case-log.md`: quyết định gì, vì sao, AI đã giúp ở đâu.
2. **Mỗi thông tin mới đi vào một chỗ.** Sửa file item hoặc working file, không copy sang nơi khác. Rồi tạo lại hub và `index.html`.
3. **Lưu một mốc trước thay đổi lớn.** Dùng GitHub Desktop (commit) hoặc copy folder thành bản `-backup`.
4. **Gửi trang chủ, không gửi folder.** Cho stakeholder xem bằng `index.html` đã đổi tên (xem [`guides/04-share-your-hub.md`](guides/04-share-your-hub.md)).

Khi dự án kết thúc: đặt status các gate, viết ba dòng rút kinh nghiệm vào `reference/case-log.md`, tạo lại `index.html` lần cuối rồi lưu trữ folder.

## Start another project

Giữ một bản template sạch để dùng lại:

1. **Chạy lại `python3 tools/new-case.py <tên-dự-án>`** cho mỗi dự án. Mỗi lần ra một folder sạch cạnh `my-case`; không cần tải template mới.
2. **Đừng điền vào `my-case`.** Hãy để nó là template gốc. Nếu lỡ điền vào, lấy lại bản sạch bằng cách tải ZIP hoặc **Use this template** lần nữa.
3. Điền các file trong `context/` đầu tiên, rồi làm theo giai đoạn. `index.html` có thanh đen nhắc bạn khi còn nội dung mẫu hoặc chỗ chưa điền.

## Use it for real work

Khi dùng cho dự án thật của công ty:

- **Kiểm tra chính sách AI của công ty trước.** Viết `context/data-rules.md` bằng lời của bạn.
- **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `work/sources/_raw-private/`: nó không lên GitHub và AI không đọc.
- **Để repo ở chế độ Private.** Chỉ công khai khi toàn bộ dự án được phép chia sẻ.
- **Hub giúp bạn giải thích decision,** nhưng `assumed` và `unknown` phải được giữ đúng: đừng biến một con số chưa xác nhận thành một sự thật trong báo cáo gửi đi.

## Four rules

1. **Ẩn danh trước khi đưa cho AI.** Dữ liệu gốc để ở `work/sources/_raw-private/`, bạn tự thay tên rồi mới lưu bản sạch vào `anonymised/`.
2. **Mỗi lần chỉ nhờ AI viết một phần.** Bạn đọc kết quả rồi tự dán vào file, để AI không viết đè phần bạn đã chốt.
3. **Giữ bản nháp của AI và bản bạn đã sửa ở hai chỗ riêng.** Chênh lệch giữa hai bản cho bạn thấy AI sai nhiều hay ít.
4. **Con số nào chưa xác nhận được thì ghi `assumed`.**

## Make it yours

Bạn đổi được hầu hết mọi thứ:

- Đổi tên folder dự án, nhân đôi nó, hoặc thêm folder riêng như `notes/`. Muốn thêm một trang tra cứu, chỉ cần thả file `.md` vào `reference/`.
- Xoá file bạn không dùng, ví dụ `context/glossary.md` hay `work/discover/competitor-analysis.md`.
- Sửa nội dung các file mẫu cho hợp cách làm của team bạn.

Có hai thứ nên giữ nguyên để AI tool và hub đọc đúng:

- **Tên các folder `context/`, `work/`, `hub/`, `reference/`, `steps/`, `_scripts/` và file `AGENTS.md`.** Các step card gọi file theo đúng đường dẫn này.
- **Tên file trong `hub/` và mã của item** (`O1`, `H1`, `D1`...). Các item nối với nhau qua mã, nên đổi tên là làm đứt liên kết.

## Which folder do I use?

| Tình huống | Dùng |
|---|---|
| Bạn có một dự án thật hoặc một case của riêng bạn | `my-case` |
| Công ty cấm AI tool, hoặc dự án quá nhạy cảm để đưa cho AI | `demo-case` |
| Bạn muốn xem một dự án chạy hết quy trình trước khi làm của mình | `demo-case` |
| Bạn kẹt ở một giai đoạn và cần một ví dụ đã làm xong | `demo-case` |

`demo-case` là dự án mẫu, mọi thứ trong đó đều bịa. Cấu trúc của nó giống hệt `my-case`.

## Stuck?

Chụp màn hình chỗ bạn đang kẹt và hỏi người chia sẻ template hoặc đồng nghiệp, kèm một câu cho biết bạn đang làm bước nào. Trong lúc chờ, bạn vẫn làm tiếp phần khác được.

## Guides

| File | Khi nào đọc |
|---|---|
| [`01-get-the-folder.md`](guides/01-get-the-folder.md) | Khi bắt đầu: lấy folder về máy, có hoặc không dùng GitHub |
| [`02-set-up-your-case.md`](guides/02-set-up-your-case.md) | Khi bắt đầu: đặt tên, hiểu từng folder, làm việc với AI tool, chọn công cụ để mở folder |
| [`03-github-basics.md`](guides/03-github-basics.md) | Khi bạn muốn lưu bản làm việc lên GitHub và chưa từng dùng |
| [`04-share-your-hub.md`](guides/04-share-your-hub.md) | Khi bạn cần cho stakeholder hoặc người khác xem hub |
| [`05-obsidian.md`](guides/05-obsidian.md) | Tuỳ chọn: xem quan hệ giữa các decision bằng Obsidian |
