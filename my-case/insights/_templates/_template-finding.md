---
type: "finding"
title: ""
area: ""
severity: 2
principle:
  - "[[principle-checks|P1]]"
found_in:
  - "[[E1]]"
affects:
  - "[[D1]]"
resolution: "open"
---
*Cách dùng: copy file này vào folder `insights/findings/`, đặt tên theo mã tiếp theo (ví dụ `F1.md`), điền title (một câu mô tả vấn đề từ góc nhìn người dùng), rồi xoá dòng này.*

- `severity`: số từ 0 đến 4, xem [Severity levels](../../standards/severity-levels.md). Với mức 3 và 4, ghi lý do ngắn ở phần mô tả.
- `principle`: principle bị vi phạm (P1 đến P10). Bỏ trống nếu chưa gắn được.
- `found_in`: evidence mà finding được phát hiện.
- `affects`: decision bị ảnh hưởng (có thể để `[]`).
- `resolution`: `open` (chưa xử lý), `fixed`, `accepted` (chấp nhận như trade-off) hoặc `deferred`.

## What happened
Người dùng đã làm gì, ở đâu, và vấn đề gì xảy ra.

## Why it matters
Tần suất, tác động và độ dai dẳng (xem Severity levels).

*Ảnh minh hoạ vấn đề: thả vào `work/<tên>/` rồi chèn bằng `![mô tả](../../work/<tên>/<ảnh>.png)`.*
