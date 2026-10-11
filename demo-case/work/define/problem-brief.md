# Problem brief

*Giai đoạn Define. Yêu cầu chung. Đồng ký với product và business, hoặc ghi lại agreement status.*

## Outcome and success metrics
*Goal, signal, metric. Ghi **assumed** cho mọi thứ PO chưa xác nhận. Mỗi metric là một file trong `hub/` (M1, M2 ...) và file đó là nguồn duy nhất.*

| Goal | Signal | Metric (and baseline) | Status |
|---|---|---|---|
| Người dùng mới thấy giá trị ngay trong phiên đầu | Họ chạm vào hoặc lưu một tip sớm | M4: thời gian tới tương tác đầu tiên dưới 30 giây (baseline: chưa có) | assumed |
| Biến khách thành người dùng đã đăng ký | Họ chấp nhận cổng đăng ký khi bấm Save | M5: từ 25% khách bấm Save đăng ký (baseline: chưa có) | assumed |
| Mọi hành trình cốt lõi làm được không cần trợ giúp | Họ hoàn thành task mà không hỏi | M1: tỷ lệ hoàn thành task từ 80% (dưới 60% là ưu tiên thiết kế lại) | assumed |
| Dùng thấy dễ | Điểm dễ dùng theo task và theo bộ câu hỏi chuẩn | M2: SEQ từ 5,5/7; M3: SUS từ 68 | assumed |

## Opportunities (ranked)
*Là nhu cầu người dùng có evidence, không phải feature. Mỗi opportunity là một file trong `hub/` (O1, O2 ...) và file đó là nguồn duy nhất: viết trực tiếp ở đó, không giữ bảng trùng ở đây. Bảng tổng hợp có ở `hub/03-problem-brief.md`, do AI dựng.*

Thứ hạng lấy theo điểm quan trọng người dùng gán cho tính năng trong khảo sát (n=13): lập kế hoạch 4,38; khám phá 3,85; nhật ký 3,62; kết nối miễn phí 3,38.

## Hypotheses
*Chúng tôi tin rằng [decision] dành cho [users] sẽ [thay đổi gì], và chúng tôi sẽ biết nhờ [test và metric]. Mỗi hypothesis là một file trong `hub/` (H1, H2 ...), có dòng `Serves` trỏ tới opportunity và dòng `Metric`.*

Sáu hypothesis thiết kế (`H1`..`H6`) được rút từ sáu câu hỏi mở của kế hoạch test (`work/original-docs/12_Unmoderated_Usability_Test_Plan.md`, mục 2.2). Chúng khác với `RH1`..`RH10` ở `scope.md`, là các hypothesis về người dùng.

## Principle checks to apply
(Dẫn tới `reference/principle-checks.md`)
*Dự án gốc chưa viết principle checks, nên file đó còn là template. Đây là một khoảng trống thật của dự án, được ghi ở gate 2d và 3c.*

## Agreement
Status: **not available**. Dự án là bài thực hành học thuật, không có người đồng ký thật.
