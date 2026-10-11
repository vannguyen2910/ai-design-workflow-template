# How the Hub Works

Hub là nơi ghi lại **điều dự án đã quyết định và vì sao**. Mỗi quyết định thiết kế được nối ngược về nhu cầu của người dùng đứng sau nó, nên bất kỳ ai cũng có thể hỏi "vì sao ta làm thế này?" và lần ra câu trả lời.

Trang này có hai phần: **Đọc hub** dành cho mọi người, và **Cập nhật hub** dành cho người giữ hub.

---

# Đọc hub

## Xem hub ở đâu

Bấm đúp file `index.html` ở folder dự án: nó mở bằng trình duyệt, không cần cài gì. Menu bên trái có năm mục:

| Mục | Bạn thấy gì |
|---|---|
| **Overview** | Dự án đang ở đâu: số lượng từng loại item, các gate, những chỗ cần xem lại (warnings), và mức nối decision về nhu cầu |
| **Journey** | Câu chuyện của dự án theo từng giai đoạn: scope, evidence, problem brief, các hướng giải, findings, handoff |
| **Documents** | Các tài liệu làm ra trong dự án: phân tích đối thủ, persona, khảo sát, user flow, prototype |
| **Insights** | Mọi item (opportunity, hypothesis, decision, evidence, metric) nối với nhau. Có thể lọc, tìm kiếm, và xem dạng Thẻ, Cây hoặc Bảng đối chiếu |
| **Reference** | Gates, các principle thiết kế, và nhật ký quyết định |

## Năm loại item

| Loại | Là gì | Ví dụ |
|---|---|---|
| **Opportunity** | Một nhu cầu hoặc khó khăn của người dùng, có bằng chứng. Không phải một tính năng | "Du khách muốn lập kế hoạch ở một nơi" |
| **Hypothesis** | Điều nhóm tin là đúng, kèm cách sẽ biết nó đúng hay sai | "Lưu một chạm giúp đưa thông tin vào kế hoạch nhanh hơn" |
| **Decision** | Một lựa chọn thiết kế cụ thể, kèm lý do | "Mở tab Explore ở chế độ Near Me" |
| **Evidence** | Một test hoặc nghiên cứu kiểm chứng hypothesis, kèm kết quả | "Usability test với 8 người" |
| **Metric** | Con số cho biết hypothesis đúng hay sai | "Từ 80% người dùng hoàn thành task không cần trợ giúp" |

Chuỗi đọc đúng là: **Opportunity → Hypothesis → Decision**, và **Evidence** kiểm chứng hypothesis đo bằng **Metric**.

## Vài điều cần biết khi đọc

- **Dấu ⚠** nghĩa là chỗ đó cần được xem lại, không phải lỗi. Có thể là decision chưa nối được về nhu cầu nào, hypothesis chưa có test, hoặc evidence mới chỉ là kế hoạch.
- **assumed** là con số chưa được ai xác nhận. Đừng coi nó là sự thật.
- **Evidence ghi là mô phỏng hoặc mới ở dạng kế hoạch** chưa phải bằng chứng từ người dùng thật. Hub gắn nhãn để bạn không nhầm.
- **Item có trạng thái "Đã ship", "Đã được thay thế" hoặc "Đã bỏ"** bị ẩn mặc định ở Insights. Bật "Hiện cả mục đã đóng" để thấy lại.
- **Chia sẻ:** gửi file `index.html` (đổi tên cho dễ nhận, ví dụ `onboarding-redesign-report.html`), không gửi cả folder.

---

# Cập nhật hub

Phần này dành cho người giữ hub.

## Hub gồm những gì

```
hub/
├── README.md              Overview: gates, bảng đối chiếu, warnings, danh sách trang
├── how-the-hub-works.md   file này
├── gates.md               bốn gate và các check 1a đến 4d (bạn đặt status)
├── traceability.base      bảng theo loại item, dùng khi mở bằng Obsidian
├── 01-scope.md … 07-handoff.md   mỗi giai đoạn một trang (phần kể chuyện do bạn viết)
├── opportunities/         O1.md, O2.md ...   mỗi item một file, mỗi loại một folder
├── hypotheses/            H1.md ...
├── metrics/               M1.md ...
├── decisions/             D1.md ...
├── evidence/              E1.md ...
├── _item-templates/       mẫu rỗng cho từng loại item (copy vào folder loại)
└── artifacts/             tài liệu của dự án (phân tích đối thủ, persona, flow, prototype...)
```

Nhật ký quyết định nằm ở `../reference/case-log.md`, và các principle (P1 đến P10) ở `../reference/principle-checks.md`.

## Nguyên tắc: mỗi thông tin chỉ ghi một chỗ

**Mỗi item là một file riêng, và file đó là nguồn duy nhất.** Mọi bảng tổng hợp trong hub (đối chiếu, warnings, danh sách item, trạng thái gate) do AI dựng lại từ các file item và từ `gates.md`. Bạn không điền tay và không copy item sang nơi khác. Sửa một decision thì sửa file của decision đó, rồi nhờ AI cập nhật các bảng.

| Bạn tự viết | AI cập nhật (đừng sửa tay) |
|---|---|
| File item (`O*.md`, `H*.md`, `M*.md`, `D*.md`, `E*.md`) | Các bảng nằm giữa `<!-- generated:... -->` và `<!-- /generated -->` |
| Trạng thái từng check trong `gates.md` | Bảng Gates ở `README.md` |
| Phần kể chuyện ở các trang giai đoạn (scope, evidence, các hướng giải, verdict) | Bảng đối chiếu và Warnings ở `README.md` |
| Verdict của bạn ở `05-alignment.md` | Danh sách item ở các trang giai đoạn |

## Tạo một item

1. Copy một file trong `_item-templates/` vào folder loại tương ứng (ví dụ `decisions/`).
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
| `state` | `active` (mặc định), `shipped`, `superseded`, `dropped` | Item `shipped`, `superseded`, `dropped` bị ẩn mặc định ở Insights và không còn tạo warning |

## Tài liệu (artifact)

Item cho biết **điều gì đã quyết định và vì sao**. Tài liệu là **thứ đã làm ra** đứng sau các decision: phân tích đối thủ, persona, kết quả khảo sát, user flow, prototype, báo cáo test. Mỗi tài liệu có trang riêng ở mục Documents và nối với các item nó hỗ trợ.

Cách thêm tài liệu nằm ở `artifacts/README.md`. Tài liệu trỏ về file làm việc gốc thay vì chép nội dung, để một thông tin chỉ nằm ở một chỗ.

## Mỗi lần cập nhật

1. Tạo hoặc sửa các file item của giai đoạn bạn đang làm.
2. Viết phần kể chuyện ở trang giai đoạn, từ bản đã kiểm tra. Không đưa bản nháp của AI lên hub.
3. Cập nhật status trong `gates.md`.
4. Nhờ AI tool cập nhật hub (xem bên dưới) để dựng lại các bảng và warnings.
5. Đọc warnings, quyết định từng cái, và ghi verdict ở `05-alignment.md`.
6. Thêm một dòng vào `../reference/case-log.md`.
7. Tạo lại `index.html` để người khác xem bản mới.

## Nhờ AI cập nhật hub

Lưu một mốc trước (commit trong GitHub Desktop, hoặc copy folder thành bản `-backup`), rồi nói với AI tool:

> Chạy `steps/refresh-hub.md`.

Bước này chỉ ghi vào các bảng tự động và trả về danh sách vấn đề tìm thấy. Nó không sửa file item, `gates.md` hay phần kể chuyện của bạn. Sau khi chạy, đối chiếu vài dòng trong bảng với file item để chắc AI không suy ra sai quan hệ.

Để tạo lại `index.html`, nhờ AI tool chạy `python3 _scripts/export-hub.py`. Muốn xem thay đổi ngay khi lưu file, chạy `python3 _scripts/serve-hub.py` (chi tiết ở `steps/export-hub.md`).

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
| Decision có `tests: []` | Nối nó với một hypothesis, hoặc cắt nó. Ghi vào verdict ở `05-alignment.md` |
| Liên kết `[[ ]]` không bấm được trên GitHub | Đúng như thiết kế: chỉ Obsidian biến chúng thành link. Dùng báo cáo `index.html` để chia sẻ |

## Ghi chú

- Hub mặc định là riêng tư. Cách cho người khác xem nằm ở `guides/04-share-your-hub.md` ở folder gốc của workspace.
- P1 đến P10 là 10 usability heuristics của Nielsen. Thêm principle riêng của tổ chức từ P11 trở đi trong `reference/principle-checks.md`.
- Hub dùng được với bất kỳ công cụ nào mở được cả folder: AI coding tool, VS Code hoặc Obsidian. Obsidian thêm Graph view và Backlinks (xem `guides/05-obsidian.md`).
