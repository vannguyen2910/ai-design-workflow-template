---
type: "measurement-plan"
title: "Kế hoạch đo lường"
stage: "Deliver"
status: "draft"
summary: ""
takeaways:
  - ""
supports: []
# source: "../../work/measurement-plan.md"
# media: []
# links: []
# embed: false
---
*Trả lời câu hỏi: sau khi phát hành, ta biết nó có hiệu quả hay không bằng cách nào. Mỗi metric là một file trong `insights/metrics/` (M#) và file đó là nguồn duy nhất về `target`, `result` và `verdict`. Bảng ở đây ghi **cách đo**, không chép lại các số đó.*

## Goal
Outcome mong muốn (từ Problem brief) và câu hỏi cần trả lời sau khi phát hành.

## Metrics
| Metric (M#) | Định nghĩa chính xác | Công thức | Mục tiêu | Loại (kết quả / dẫn dắt / phụ) |
|---|---|---|---|---|
| M? | | | | |

*Mỗi plan nên có một metric kết quả chính, một đến hai metric dẫn dắt, và một metric "an toàn" để biết ta không làm hỏng điều khác.*

## Data and tracking
| Metric | Nguồn dữ liệu | Sự kiện / truy vấn cần có | Đã có sẵn? | Ai dựng |
|---|---|---|---|---|
| M? | | | có / chưa | |

## Segments and baseline
Chia theo nhóm nào (người dùng mới / cũ, thiết bị...), mốc hiện tại lấy ở đâu, hoặc ghi `assumed` nếu chưa có.

## Cadence and owners
| Metric | Ai chịu trách nhiệm | Khi nào xem | Ngưỡng cần hành động |
|---|---|---|---|
| M? | | | |

## Decision rules
Quyết định trước khi có số: kết quả thế nào thì **tiếp tục**, **chỉnh**, **dừng**. Viết trước để khỏi diễn giải theo ý muốn.

| Nếu | Thì |
|---|---|
| Đạt hoặc vượt mục tiêu | |
| Gần mục tiêu | |
| Không đạt | |

## Qualitative signals
Tín hiệu định tính cùng theo dõi (phản hồi, ticket hỗ trợ, buổi gặp người dùng), để giải thích *vì sao* số thay đổi.

## Limits
Điều làm số liệu kém tin cậy (mẫu nhỏ, mùa vụ, thay đổi khác cùng lúc). Điền `result` và `verdict` vào từng file M# khi đã đo; chỉ chủ dự án đặt `verdict`.

*Ảnh, video và PDF của tài liệu này: thả vào cùng folder với file này, báo cáo tự hiện. Xem `work/README.md` của case.*
