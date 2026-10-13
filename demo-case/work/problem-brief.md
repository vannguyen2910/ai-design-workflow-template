---
type: "problem-brief"
title: "Problem brief"
stage: "Define"
status: "draft"
summary: ""
supports: []
---
*Define stage. A shared requirement. Sign it off with product and business, or record the agreement status.*

## Outcome and success metrics
*Goal, signal, metric. Write **assumed** for anything the PO has not confirmed. Each metric is a file in `insights/metrics/` (M1, M2 ...) and that file is the single source.*

| Goal | Signal | Metric (and baseline) | Status |
|---|---|---|---|
| Người dùng mới thấy giá trị ngay trong phiên đầu | Họ chạm vào hoặc lưu một tip sớm | M4: thời gian tới tương tác đầu tiên dưới 30 giây (baseline: chưa có) | assumed |
| Biến khách thành người dùng đã đăng ký | Họ chấp nhận cổng đăng ký khi bấm Save | M5: từ 25% khách bấm Save đăng ký (baseline: chưa có) | assumed |
| Mọi hành trình cốt lõi làm được không cần trợ giúp | Họ hoàn thành task mà không hỏi | M1: tỷ lệ hoàn thành task từ 80% (dưới 60% là ưu tiên thiết kế lại) | assumed |
| Dùng thấy dễ | Điểm dễ dùng theo task và theo bộ câu hỏi chuẩn | M2: SEQ từ 5,5/7; M3: SUS từ 68 | assumed |

## Opportunities (ranked)
*A user need backed by evidence, not a feature. Each opportunity is a file in `insights/opportunities/` (O1, O2 ...) and that file is the single source: write it there directly, do not keep a duplicate table here. The summary table shows on the Problem brief page in Stages, built from those files.*

Thứ hạng lấy theo điểm quan trọng người dùng gán cho tính năng trong khảo sát (n=13): lập kế hoạch 4,38; khám phá 3,85; nhật ký 3,62; kết nối miễn phí 3,38.

## Hypotheses
*We believe that [decision] for [users] will [change what], and we will know by [test and metric]. Each hypothesis is a file in `insights/hypotheses/` (H1, H2 ...), with a `Serves` line pointing to the opportunity and a `Metric` line.*

Sáu hypothesis thiết kế (`H1`..`H6`) được rút từ sáu câu hỏi mở của kế hoạch test (`work/original-docs/12_Unmoderated_Usability_Test_Plan.md`, mục 2.2). Chúng khác với `RH1`..`RH10` ở `scope.md`, là các hypothesis về người dùng.

## Principle checks to apply
(Point to `standards/principle-checks.md`)
*Dự án gốc chưa viết principle checks, nên file đó còn là template. Đây là một khoảng trống thật của dự án, được ghi ở gate 2d và 3c.*

## Agreement
Status: **not available**. Dự án là bài thực hành học thuật, không có người đồng ký thật.
