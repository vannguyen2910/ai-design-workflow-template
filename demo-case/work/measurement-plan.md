---
type: "measurement-plan"
title: "Measurement plan"
stage: "Deliver"
status: "draft"
summary: ""
supports: []
---
*Deliver stage, at handoff. What to track after launch, and who is responsible. Give it to the PO even if you cannot see the data yourself.*

> **Trạng thái:** kế hoạch đo từ PRD của tab Explore và kế hoạch test. Chưa có chủ sở hữu thật (không có PO thật) và chưa đặt ngày xem lại. Gate 4d còn `open`.

| Metric | Where to track it | Who owns it | Review date |
|---|---|---|---|
| M4: thời gian tới tương tác đầu tiên với một tip (mục tiêu dưới 30 giây) | Analytics của app (sự kiện mở app, chạm tip, lưu tip) | Chưa có (cần PO) | Chưa đặt |
| M5: khách chuyển thành người dùng đã đăng ký khi bấm Save (từ 25%) | Analytics của app (funnel Save → đăng ký) | Chưa có (cần PO) | Chưa đặt |
| Số tip lưu mỗi phiên, người dùng đã đăng ký (từ 2) | Analytics của app | Chưa có (cần PO) | Chưa đặt |
| Tỷ lệ dùng filter hằng tuần (từ 40% người dùng hoạt động) | Analytics của app | Chưa có (cần PO) | Chưa đặt |
| M1, M2, M3: task success, SEQ, SUS | Vòng test không điều phối (E2) | Người nghiên cứu | Trước khi bàn giao |

## How the AI-assisted workflow performed
*Counts, not impressions: time per step, the error rate caught at the gates, the number of redos.*

Không áp dụng cho bản demo này: dự án gốc được làm trước khi có quy trình AI-assisted, nên không có số đếm nào. Một vòng test dùng AI đóng vai người dùng (E1) được ghi nhận như một **hạn chế**, không phải kết quả của quy trình.
