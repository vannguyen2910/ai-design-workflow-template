# How the Hub Works

Hub là nơi ghi lại **điều dự án đã quyết định và vì sao**. Mỗi quyết định thiết kế được nối ngược về nhu cầu của người dùng đứng sau nó, nên bất kỳ ai cũng có thể hỏi "vì sao ta làm thế này?" và lần ra câu trả lời.

Từ "hub" ở đây là tên gọi chung cho cả bộ nội dung của dự án và báo cáo `index.html` hiển thị nó. Trang này có hai phần: **Đọc hub** dành cho mọi người, và **Cập nhật hub** dành cho người giữ hub.

---

# Đọc hub

## Xem hub ở đâu

Bấm đúp file `index.html` ở folder dự án: nó mở bằng trình duyệt, không cần cài gì. Menu bên trái có sáu mục, mỗi mục ứng với một folder cùng tên:

| Mục | Folder | Bạn thấy gì |
|---|---|---|
| **Overview** | `README.md` | Dự án đang ở đâu: số lượng từng loại item, các gate, những chỗ cần xem lại (warnings), và mức nối decision về nhu cầu |
| **Context** | `context/` | Sản phẩm là gì, người dùng là ai, quy tắc dữ liệu, design system |
| **Stages** | `stages/` | Câu chuyện của dự án theo từng giai đoạn: scope, evidence, problem brief, các hướng giải, findings, handoff. Tự ghép từ file ở `work/` và item ở `insights/`, không viết riêng |
| **Work** | `work/` | Mọi thứ làm ra trong dự án: file làm việc, phân tích đối thủ, persona, khảo sát, wireframe, prototype |
| **Insights** | `insights/` (`opportunities/`, `hypotheses/`, `decisions/`, `evidence/`, `findings/`, `metrics/`) | Mọi item nối với nhau. Có thể lọc, tìm kiếm, và xem dạng Thẻ, Cây hoặc Bảng đối chiếu |
| **Reference** | `reference/` | Gates, principle checks, severity levels, nhật ký quyết định |

## Sáu loại item

| Loại | Là gì | Ví dụ |
|---|---|---|
| **Opportunity** | Một nhu cầu hoặc khó khăn của người dùng, có bằng chứng. Không phải một tính năng | "Du khách muốn lập kế hoạch ở một nơi" |
| **Hypothesis** | Điều nhóm tin là đúng, kèm cách sẽ biết nó đúng hay sai | "Lưu một chạm giúp đưa thông tin vào kế hoạch nhanh hơn" |
| **Decision** | Một lựa chọn thiết kế cụ thể, kèm lý do | "Mở tab Explore ở chế độ Near Me" |
| **Evidence** | Một test hoặc nghiên cứu kiểm chứng hypothesis, kèm kết quả | "Usability test với 8 người" |
| **Metric** | Con số cho biết hypothesis đúng hay sai | "Từ 80% người dùng hoàn thành task không cần trợ giúp" |
| **Finding** | Một vấn đề usability tìm thấy khi đánh giá hoặc test, có mức độ nghiêm trọng (0 đến 4) | "Không có cách mời người ngoài danh sách" |

Chuỗi đọc đúng là: **Opportunity → Hypothesis → Decision**, và **Evidence** kiểm chứng hypothesis đo bằng **Metric**. Từ Evidence, **Finding** cho biết vấn đề nào đã lộ ra và nó ảnh hưởng tới decision nào.

## Vài điều cần biết khi đọc

- **Dấu ⚠** nghĩa là chỗ đó cần được xem lại, không phải lỗi. Có thể là decision chưa nối được về nhu cầu nào, hypothesis chưa có test, hoặc evidence mới chỉ là kế hoạch.
- **assumed** là con số chưa được ai xác nhận. Đừng coi nó là sự thật.
- **Evidence có nhãn Simulated hoặc Planned** chưa phải bằng chứng từ người dùng thật. Hub gắn nhãn để bạn không nhầm.
- **Item có `state` là `shipped`, `superseded` hoặc `dropped`** bị ẩn mặc định ở Insights. Bật "Hiện cả mục đã đóng" để thấy lại.
- **Chia sẻ:** gửi file `index.html` (đổi tên cho dễ nhận, ví dụ `onboarding-redesign-report.html`), không gửi cả folder.

---

# Cập nhật hub

Phần này dành cho người giữ hub.

## Cấu trúc folder

```
(thư mục gốc của dự án)
├── README.md              Overview: project card, và nguồn của trang Overview trong báo cáo
├── context/               thông tin nền: sản phẩm, người dùng, quy tắc, design system
├── stages/                các trang giai đoạn tự dựng từ work/ và insights/
│   └── README.md          bảng Pages: mỗi dòng là một trang, theo thứ tự trong báo cáo
├── work/                  mọi thứ làm ra: file làm việc, wireframe, prototype, persona...
│   ├── README.md          cách thêm tài liệu, ảnh, video, PDF
│   ├── sources/           dữ liệu nghiên cứu (anonymised/ và _raw-private/)
│   └── prototype/
├── insights/
│   ├── opportunities/     O1.md, O2.md ...   mỗi item một file, mỗi loại một folder
│   ├── hypotheses/  metrics/  decisions/  evidence/  findings/
│   ├── _templates/        mẫu rỗng cho từng loại item (copy vào folder loại)
│   └── traceability.base  bảng theo loại item, dùng khi mở bằng Obsidian
├── reference/             gates, principle checks, severity levels, case log, và trang này
├── _ai/                   step card và script cho AI
└── _personal/             ghi chú riêng
```

Nhật ký quyết định nằm ở `reference/case-log.md`, và các principle (P1 đến P10) ở `reference/principle-checks.md`.

## Nguyên tắc: mỗi thông tin chỉ ghi một chỗ

**Mỗi item là một file riêng, và file đó là nguồn duy nhất.** Mọi bảng tổng hợp trong hub (đối chiếu, warnings, danh sách item, trạng thái gate, các bảng ở trang giai đoạn) do `export-hub.py` tự dựng từ các file item, `gates.md` và file ở `work/`. Bạn không điền tay và không copy item sang nơi khác. Sửa một decision thì sửa file của decision đó, rồi nhờ AI cập nhật các bảng.

| Bạn tự viết | Báo cáo tự dựng (đừng sửa tay) |
|---|---|
| File item (`O*.md`, `H*.md`, `M*.md`, `D*.md`, `E*.md`, `F*.md`) | Bảng đối chiếu, Warnings và danh sách item |
| File làm việc ở `work/` (scope, problem brief, options, findings, learning...) | Các trang giai đoạn ở mục Stages |
| Trạng thái từng check trong `reference/gates.md` | Bảng Gates và dòng gate ở mỗi giai đoạn |
| Verdict của bạn ở `work/alignment.md` | Bảng Outcomes ở trang Learning |

## Tạo một item

1. Copy một file trong `insights/_templates/` vào folder loại tương ứng (ví dụ `insights/decisions/`).
2. Đặt tên file theo mã tiếp theo (ví dụ `D4.md`). Mã là duy nhất trong cả hub; chữ cái đầu cho biết loại: O, H, M, D, E.
3. Điền phần thông tin ở đầu file và vài dòng mô tả.

Phần thông tin đầu file (giữa hai dòng `---`) là nơi duy nhất ghi **quan hệ giữa các item**. Quan hệ chỉ ghi một chiều, từ item phía sau về item phía trước:

| Loại | Điền gì | Trỏ tới |
|---|---|---|
| Opportunity | `title`, `rank`, `evidence` | mã quote hoặc nguồn |
| Hypothesis | `title`, `serves`, `metric` | Opportunity, Metric |
| Metric | `title`, `status`, `baseline`, `measured_by` | giá trị |
| Decision | `title`, `tests`, `follows`, `pulls_against` | Hypothesis, principle |
| Evidence | `title`, `tests`, `measures`, `participants`, `result`; tuỳ chọn `status` (`planned` nếu chưa chạy) và `participants_type` (`simulated` nếu không phải người thật) | Hypothesis, Metric |
| Finding | `title`, `severity` (0 đến 4), `principle`, `found_in`, `affects`, `resolution` (`open`, `fixed`, `accepted`, `deferred`) | Principle, Evidence, Decision |

Cách ghi một quan hệ:

```
---
type: "decision"
title: "Thêm progress bar vào checklist"
tests:
  - "[[H1]]"
follows:
  - "[[principle-checks|P1]]"
pulls_against:
  - "[[principle-checks|P8]]"
---
```

Quy tắc:

1. **Mỗi liên kết viết dạng `"[[H1]]"`**, có dấu nháy và hai cặp ngoặc vuông. Với principle, viết `"[[principle-checks|P8]]"`.
2. **Chưa có thì ghi `[]`.** Đừng xoá dòng.
3. **Trong Obsidian không cần gõ tay:** bấm vào mục đó, gõ `[[`, chọn file.
4. Decision đi ngược một principle thì điền `pulls_against`, và ghi lý do chấp nhận ở phần mô tả.
5. Chưa xác nhận được thì ghi `assumed`.

Chiều ngược lại (opportunity này được hypothesis nào phục vụ, hypothesis này có evidence nào) **không ghi vào file**: báo cáo tự suy ra, hiện ở phần "Được nối từ".

## Chủ đề và tình trạng (tuỳ chọn)

Khi hub có nhiều item, hai mục này giúp lọc. Dùng được cho mọi loại item:

| Thông tin | Giá trị | Tác dụng |
|---|---|---|
| `area` | một từ tự đặt, ví dụ `onboarding`, `pricing` | Lọc theo chủ đề ở Insights. Item không có `area` luôn hiện, kể cả khi bạn lọc |
| `state` | `active` (mặc định), `proposed`, `accepted`, `shipped`, `superseded`, `dropped` | `shipped`, `superseded`, `dropped` bị ẩn mặc định ở Insights và không còn tạo warning. `proposed` và `accepted` dùng cho decision: đề xuất, rồi đã được chấp nhận |

## Tài liệu (artifact)

Item cho biết **điều gì đã quyết định và vì sao**. Tài liệu là **thứ đã làm ra** đứng sau các decision: phân tích đối thủ, persona, kết quả khảo sát, user flow, prototype, báo cáo test. Mỗi tài liệu có trang riêng ở mục Work và nối với các item nó hỗ trợ.

Cách thêm tài liệu nằm ở `work/README.md`. Tài liệu trỏ về file làm việc gốc thay vì chép nội dung, để một thông tin chỉ nằm ở một chỗ.

## Thêm ảnh, video, PDF

Thả ảnh, video hoặc PDF vào một folder trong `work/`, hoặc chèn ảnh giữa trang bằng `![mô tả](đường-dẫn)`. Báo cáo tự nhận ra định dạng; chi tiết và các cảnh báo nằm ở `work/README.md`.

## Mỗi lần cập nhật

1. Tạo hoặc sửa các file item của giai đoạn bạn đang làm.
2. Viết phần kể chuyện ở trang giai đoạn, từ bản đã kiểm tra. Không đưa bản nháp của AI lên hub.
3. Cập nhật status trong `gates.md`.
4. Nhờ AI tool cập nhật hub (xem bên dưới) để dựng lại các bảng và warnings.
5. Đọc warnings, quyết định từng cái, và ghi verdict ở `alignment.md`.
6. Thêm một dòng vào `../reference/case-log.md`.
7. Tạo lại `index.html` để người khác xem bản mới.

## Nhờ AI rà soát hub

Lưu một mốc trước (commit trong GitHub Desktop, hoặc copy folder thành bản `-backup`), rồi nói với AI tool:

> Chạy `_ai/refresh-hub.md` (rà soát những chỗ item chưa nối hoặc còn thiếu).

Bước này chỉ trả về danh sách vấn đề tìm thấy; nó không ghi vào file nào. Sau khi chạy, đối chiếu vài dòng trong bảng với file item để chắc AI không suy ra sai quan hệ.

Để tạo lại `index.html`, nhờ AI tool chạy `python3 _ai/export-hub.py`. Muốn xem thay đổi ngay khi lưu file, chạy `python3 _ai/serve-hub.py` (chi tiết ở `_ai/export-hub.md`).

## Quyết định, thứ hạng và vòng outcome

Ba nhóm thông tin giúp hub trả lời "vì sao" và "kết quả ra sao". Tất cả đều tuỳ chọn, nhưng báo cáo sẽ nhắc khi thiếu:

| Item | Property | Ý nghĩa |
|---|---|---|
| Decision | `owner`, `decided_on`, `state` | Ai chịu trách nhiệm, ngày quyết định, và đang ở `proposed` hay `accepted`. Decision đã `accepted` mà thiếu `owner` sẽ bị nhắc |
| Opportunity | `rank`, `impact`, `confidence`, `rank_reason` | Thứ hạng kèm lý do: tác động (`high`/`medium`/`low`), độ chắc chắn của evidence, và một hai câu giải thích |
| Metric | `target`, `result`, `measured_on`, `verdict` | Ngưỡng đạt, kết quả đo, ngày đo, và kết luận: `pending`, `met`, `missed`, `inconclusive` |

Sau launch, điền `result` và `verdict` vào file metric, rồi mở trang **Learning** trong Stages: bảng Outcomes tự nối mỗi metric về hypothesis và opportunity phía sau, và metric `missed` đánh dấu opportunity "xem lại". Phần chữ (điều đã học, opportunity cần mở lại) bạn viết ở `work/learning.md`.

## Báo cáo tự kiểm tra gì

Báo cáo không chỉ hiển thị mà còn đối chiếu các phần với nhau:

- **Gates:** với các check dữ liệu trả lời được (1b, 2a, 2c, 2d, 3b, 3c, 4a, 4b), cột "Kiểm tra tự động" ở trang Gates cho biết dữ liệu đang đạt hay chưa. Trạng thái bạn đặt vẫn là của bạn; nếu bạn đặt `passed` mà dữ liệu chưa đạt, báo cáo hiện một warning.
- **Finding:** mức 4 chưa xử lý chặn handoff, mức 3 chưa xử lý cần một quyết định, và decision bị ảnh hưởng cũng được đánh dấu.
- **Case log:** mã nhắc ở cột Items phải tồn tại, và mỗi decision nên có ít nhất một dòng trong log. Mã được biến thành link.

## Gates

Bốn gate và các check 1a đến 4d nằm ở [`gates.md`](../reference/gates.md). Với mỗi check, đặt status là `open`, `passed` hoặc `failed`. **Không đổi tên check, chỉ đổi status.** Gate `passed` khi mọi check `passed`, `failed` khi có check `failed`, còn lại là `open`.

## Lỗi thường gặp

| Lỗi | Cách sửa |
|---|---|
| Sửa tay một bảng tự động | Lần cập nhật sau sẽ ghi đè. Sửa ở file item rồi nhờ AI cập nhật lại |
| Copy một item sang trang giai đoạn hoặc file làm việc | Chỉ link tới file item, đừng copy nội dung |
| Hai item dùng chung một mã | Đổi một item sang mã mới, và đổi cả tên file |
| Mã trong file không khớp tên file | Đổi cho khớp |
| Một liên kết trỏ tới file không tồn tại | Tạo file item còn thiếu, hoặc sửa mã |
| Ghi quan hệ ở cả hai đầu | Giữ ở đầu `serves` / `tests` / `follows`, xoá đầu còn lại |
| Decision có `tests: []` | Nối nó với một hypothesis, hoặc cắt nó. Ghi vào verdict ở `alignment.md` |
| Liên kết `[[ ]]` không bấm được trên GitHub | Đúng như thiết kế: chỉ Obsidian biến chúng thành link. Dùng báo cáo `index.html` để chia sẻ |

## Ghi chú

- Hub mặc định là riêng tư. Cách cho người khác xem nằm ở `guides/04-share-your-hub.md` ở folder gốc của workspace.
- P1 đến P10 là 10 usability heuristics của Nielsen. Thêm principle riêng của tổ chức từ P11 trở đi trong `reference/principle-checks.md`.
- Hub dùng được với bất kỳ công cụ nào mở được cả folder: AI coding tool, VS Code hoặc Obsidian. Obsidian thêm Graph view và Backlinks (xem `guides/05-obsidian.md`).
