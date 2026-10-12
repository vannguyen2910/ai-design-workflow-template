---
type: "opportunity-solution-tree"
title: "Cây cơ hội và giải pháp"
stage: "Define"
status: "draft"
summary: ""
takeaways:
  - ""
supports: []
# source: "../../work/opportunity-solution-tree.md"
# media: []
# links: []
# embed: false
---
## Desired outcome
Một kết quả mong muốn, đo được, thuộc quyền tác động của nhóm (ví dụ: "tăng tỷ lệ khách đăng ký sau khi bấm Save từ X% lên Y%"). Liên kết metric (M#) nếu đã có.

## Tree
Đi từ trên xuống: outcome → opportunity (nhu cầu, điểm đau của người dùng) → giải pháp → giả định cần kiểm tra. Mỗi opportunity phải có **bằng chứng** (E# hoặc nguồn). Mỗi nhánh nên có từ 2 giải pháp trở lên để so sánh.

```
Outcome: ...
├── O1 Opportunity: ...            (bằng chứng: E?)
│   ├── Giải pháp A: ...
│   │   └── Giả định cần kiểm tra: ...   → H?
│   └── Giải pháp B: ...
│       └── Giả định cần kiểm tra: ...   → H?
└── O2 Opportunity: ...            (bằng chứng: E?)
    ├── Giải pháp C: ...
    └── Giải pháp D: ...
```

## Opportunities
| # | Opportunity | Người dùng bị ảnh hưởng | Bằng chứng | Tác động | Độ chắc chắn |
|---|---|---|---|---|---|
| O1 | | | | cao / vừa / thấp | cao / vừa / thấp |

## Solutions
| Giải pháp | Phục vụ O# | Giả định lớn nhất | Cách kiểm tra rẻ nhất |
|---|---|---|---|
| A | O1 | | |

## Where to test first
Chọn **một** opportunity và 2 đến 3 giải pháp để test trước, kèm lý do. Ghi kết quả vào `insights/` khi đã có decision.

## What this cannot tell us
Điều cây này không cho biết. Cây phản ánh hiểu biết tại thời điểm vẽ và cần cập nhật khi có bằng chứng mới.

*Ảnh, video và PDF của tài liệu này: thả vào cùng folder với file này, báo cáo tự hiện. Xem `work/README.md`.*
