---
type: "heuristic-evaluation"
title: "Đánh giá heuristic"
stage: "Discover"
status: "draft"
summary: ""
takeaways:
  - ""
supports: []
# source: "../../work/heuristic-evaluation.md"
# media: []
# links: []
# embed: false
---
## Scope
Sản phẩm hoặc bản thiết kế được đánh giá, phiên bản, các task chính (3 đến 5), người đánh giá và ngày. Khi có thể, nên có từ 2 người đánh giá độc lập.

## Method
Đi qua từng task, kiểm từng màn hình với 10 heuristic của Nielsen. Dùng mã **P1 đến P10** trong Principle checks (`standards/principle-checks.md` của case) (không dùng `H#`, đó là mã hypothesis). Mức độ nghiêm trọng chấm theo Severity levels (`standards/severity-levels.md` của case).

| Mức | Tên | Nghĩa ngắn |
|---|---|---|
| 0 | Không phải vấn đề | Bạn không đồng ý đây là vấn đề usability |
| 1 | Cosmetic | Chỉ là hình thức, không cản trở |
| 2 | Minor | Gây khó chịu, người dùng vẫn hoàn thành |
| 3 | Major | Nhiều người bị chặn hoặc phải đi đường vòng |
| 4 | Catastrophe | Không hoàn thành được việc chính, hoặc mất dữ liệu, mất tiền |

Chấm bằng ba yếu tố nhìn chung (tần suất, tác động, độ khó để vượt qua); chi tiết ở trang Severity levels.

## Problems
Mỗi vấn đề một dòng. Ghi điều quan sát được, không ghi giải pháp.

| # | Task | Màn hình / bước | Vấn đề | Principle (P#) | Mức độ (0-4) | Bằng chứng |
|---|---|---|---|---|---|---|
| 1 | | | | P? | | ảnh / link |

## Heuristic coverage
Principle nào xuất hiện nhiều nhất, và principle nào chưa có vấn đề nào (để biết đã kiểm hay chưa).

| Principle | Số vấn đề | Mức cao nhất |
|---|---|---|
| P1 Visibility of system status | | |
| P2 Match between system and real world | | |
| P3 User control and freedom | | |
| P4 Consistency and standards | | |
| P5 Error prevention | | |
| P6 Recognition rather than recall | | |
| P7 Flexibility and efficiency of use | | |
| P8 Aesthetic and minimalist design | | |
| P9 Help users recover from errors | | |
| P10 Help and documentation | | |

## Top problems
Ba đến năm vấn đề nghiêm trọng nhất (mức 3 và 4 trước), kèm lý do ưu tiên.

## What this cannot tell us
Đánh giá heuristic là ý kiến của chuyên gia, không thay thế test với người dùng. Ghi những vấn đề cần xác nhận bằng test.

*Ảnh, video và PDF của tài liệu này: thả vào cùng folder với file này, báo cáo tự hiện. Xem `work/README.md` của case.*
