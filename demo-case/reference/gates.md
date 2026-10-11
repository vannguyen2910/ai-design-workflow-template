# Gates

Bốn gate (cổng kiểm tra) mà dự án đi qua. Mỗi check có một trạng thái: `open` (chưa xong), `passed` (đạt) hoặc `failed` (chưa đạt). **Không đổi tên check, chỉ đổi trạng thái.** Một gate đạt khi mọi check của nó đạt.

## Gate 1: Discover (Question + evidence)

| Check | Nội dung | Status |
|---|---|---|
| 1a | Business question và outcome đã được thống nhất với product owner, hoặc ghi **assumed** kèm agreement status | passed |
| 1b | Mọi insight lần ngược được về một nguồn gốc bạn mở ra được | passed |
| 1c | Không có gì được đoán: unknown và counterexample được ghi lại; bản nháp của AI để cạnh bản đã kiểm tra, kèm tỷ lệ lỗi | open |

## Gate 2: Define (Evidence + agreement)

| Check | Nội dung | Status |
|---|---|---|
| 2a | Mỗi opportunity dẫn evidence phía sau nó | passed |
| 2b | Problem brief được product và business đồng ký, hoặc ghi lại agreement status | passed |
| 2c | Mỗi hypothesis có một test và một metric (metric chưa xác nhận thì ghi **assumed**) | passed |
| 2d | Principle checks được viết thành câu hỏi có/không | open |

## Gate 3: Develop (Alignment)

| Check | Nội dung | Status |
|---|---|---|
| 3a | Đã khám phá ít nhất ba hướng khác nhau; lựa chọn và lý do được ghi lại | open |
| 3b | Mỗi decision lần ngược về một opportunity có evidence và một hypothesis (không decision nào thiếu user need, không opportunity nào bị bỏ sót) | passed |
| 3c | Mỗi decision đạt principle checks, hoặc xung đột được ghi lại thành trade-off | open |
| 3d | Prototype dùng design system và các accessibility rules đã được kiểm tra | open |

## Gate 4: Deliver (Real users + buildability)

| Check | Nội dung | Status |
|---|---|---|
| 4a | Người dùng thật đã test các hypothesis; kết quả được đặt cạnh baseline | failed |
| 4b | Các finding lần ngược về ghi chú hoặc bản ghi gốc và được xếp theo mức độ quan trọng | open |
| 4c | Developer có thể dựng mà không phải hỏi lại (handoff pack và decision log đầy đủ) | open |
| 4d | Measurement plan đã được đưa cho product owner | open |

Sau khi đổi trạng thái ở đây, nhờ AI tool cập nhật bảng Gates ở trang Overview ([`README.md`](../hub/README.md)).

## Ghi chú về trạng thái (bản demo)

Trạng thái do người dựng demo đặt dựa trên tài liệu gốc; chủ dự án cần xác nhận lại.

- **1a, 2b `passed`:** không có product owner thật, nhưng agreement status (`not available`) và các số được ghi là `assumed`.
- **1c `open`:** không có bản nháp AI để so sánh, nên không tính được tỷ lệ lỗi.
- **2d, 3c `open`:** chưa viết câu hỏi có/không cho 10 principle.
- **3a `open`:** dự án có 26 giải pháp trong Solution Pool nhưng chưa có bước chọn giữa ba hướng.
- **4a `failed`:** vòng test duy nhất dùng người mô phỏng, không thoả "người dùng thật đã kiểm tra các hypothesis". Chạy E2 với người thật để chuyển trạng thái này.
