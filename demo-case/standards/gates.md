# Gates

The four gates (checkpoints) a project goes through. Each check has a status: `open` (not done), `passed` or `failed`. **Do not rename a check, only change its status.** A gate passes when all of its checks pass.

## Gate 1: Discover (Question + evidence)

| Check | What | Status |
|---|---|---|
| 1a | Business question và outcome đã được thống nhất với product owner, hoặc ghi **assumed** kèm agreement status | passed |
| 1b | Mọi insight lần ngược được về một nguồn gốc bạn mở ra được | passed |
| 1c | Nothing is guessed: unknowns and counterexamples are recorded; the AI draft sits next to the checked version, with the error rate | open |

## Gate 2: Define (Evidence + agreement)

| Check | What | Status |
|---|---|---|
| 2a | Mỗi opportunity dẫn evidence phía sau nó | passed |
| 2b | Problem brief được product và business đồng ký, hoặc ghi lại agreement status | passed |
| 2c | Mỗi hypothesis có một test và một metric (metric chưa xác nhận thì ghi **assumed**) | passed |
| 2d | The principle checks are written as yes/no questions | open |

## Gate 3: Develop (Alignment)

| Check | What | Status |
|---|---|---|
| 3a | At least three different directions were explored; the choice and its reason are recorded | open |
| 3b | Mỗi decision lần ngược về một opportunity có evidence và một hypothesis (không decision nào thiếu user need, không opportunity nào bị bỏ sót) | passed |
| 3c | Every decision passes the principle checks, or the conflict is recorded as a trade-off | open |
| 3d | The prototype uses the design system and the accessibility rules that were checked | open |

## Gate 4: Deliver (Real users + buildability)

| Check | What | Status |
|---|---|---|
| 4a | Người dùng thật đã test các hypothesis; kết quả được đặt cạnh baseline | failed |
| 4b | Findings trace back to the original notes or recordings and are ranked by importance | open |
| 4c | A developer can build without coming back with questions (handoff pack and decision log are complete) | open |
| 4d | The measurement plan was given to the product owner | open |

The **Automatic check** column (in the report) shows whether the current data meets that check. It does not change the status you set; if you set `passed` and the data does not support it, the report shows a warning.

After you change a status here, ask the AI tool to update the Gates table on the Overview page ([`README.md`](../README.md)).

## Ghi chú về trạng thái (bản demo)

Trạng thái do người dựng demo đặt dựa trên tài liệu gốc; chủ dự án cần xác nhận lại.

- **1a, 2b `passed`:** không có product owner thật, nhưng agreement status (`not available`) và các số được ghi là `assumed`.
- **1c `open`:** không có bản nháp AI để so sánh, nên không tính được tỷ lệ lỗi.
- **2d, 3c `open`:** chưa viết câu hỏi có/không cho 10 principle.
- **3a `open`:** dự án có 26 giải pháp trong Solution Pool nhưng chưa có bước chọn giữa ba hướng.
- **4a `failed`:** vòng test duy nhất dùng người mô phỏng, không thoả "người dùng thật đã kiểm tra các hypothesis". Chạy E2 với người thật để chuyển trạng thái này.
