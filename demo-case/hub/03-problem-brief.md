# Problem brief

*Yêu cầu chung: outcome, các opportunity đã xếp hạng, hypothesis, success metric và các principle để kiểm tra.*

> **Cách điền:** copy từ [`02-define/problem-brief.md`](../02-define/problem-brief.md). Mỗi opportunity, hypothesis và metric là một file riêng trong folder của nó và là nguồn duy nhất. Các bảng trong khối `generated` do AI dựng từ các file đó, bạn không sửa tay. Đồng ký brief với product và business trước khi thiết kế bắt đầu.

## Outcome and success

Người dùng mới thấy giá trị ngay trong phiên đầu và coi Travel Buddy là nơi duy nhất cho khám phá và lập kế hoạch. Đồng ký bởi: **không có** (stakeholder được mô phỏng).

## Opportunities (ranked)

*Nhu cầu người dùng có evidence, không phải feature. Xếp hạng chúng.*

<!-- generated:opportunities (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| Rank | ID | Opportunity |
|---|---|---|
| 1 | [O1](opportunities/O1.md) | Du khách muốn lập kế hoạch linh hoạt ở một nơi, thay vì xoay 8 đến 10 app |
| 2 | [O2](opportunities/O2.md) | Du khách muốn gợi ý bản địa đáng tin, không thương mại |
| 3 | [O3](opportunities/O3.md) | Du khách muốn lưu giữ chuyến đi mà không tốn công |
| 4 | [O4](opportunities/O4.md) | Du khách muốn kết nối với người địa phương theo cách an toàn, miễn phí và không giao dịch |
| 5 | [O5](opportunities/O5.md) | Du khách cần vượt qua các rào cản dùng thử: giá, quyền riêng tư và mạng lưới bạn bè |
<!-- /generated -->

## Hypotheses

*Chúng tôi tin rằng [decision] dành cho [users] sẽ [thay đổi gì], và chúng tôi sẽ biết nhờ [test và metric].*

<!-- generated:hypotheses (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| ID | Hypothesis | Serves | Test |
|---|---|---|---|
| [H1](hypotheses/H1.md) | Lưu bằng một chạm và nhập lịch trình AI cho phép đưa thông tin vào kế hoạch mà không phải chép tay | O1 | T1, T2 |
| [H2](hypotheses/H2.md) | Tip có danh tính người đóng góp và crowd signal giúp người dùng tự đánh giá độ tin cậy | O2 | T1, T2 |
| [H3](hypotheses/H3.md) | Cho duyệt không cần tài khoản và chỉ đòi đăng ký khi Save là một đánh đổi chấp nhận được | O5 | T1, T2 |
| [H4](hypotheses/H4.md) | Khung trao đổi hai chiều cùng hồ sơ xác minh khiến người dùng nhắn cho người địa phương mà không do dự | O4 | T1, T2 |
| [H5](hypotheses/H5.md) | Người dùng tự tìm thấy nhật ký tự sinh mà không cần được chỉ | O3 | T1, T2 |
| [H6](hypotheses/H6.md) | Nhật ký riêng tư mặc định và chia sẻ theo người cụ thể đáp ứng nhu cầu chia sẻ | O3 | T1, T2 |
<!-- /generated -->

## Success metrics

*Goal, rồi signal, rồi metric. Ghi **assumed** cho mọi thứ PO chưa xác nhận.*

<!-- generated:metrics (không sửa tay; dựng lại bằng workflow/refresh-hub.md) -->
| ID | Metric | Baseline | Status |
|---|---|---|---|
| [M1](metrics/M1.md) | Tỷ lệ hoàn thành task không cần trợ giúp từ 80% (dưới 60% là ưu tiên thiết kế lại) | chưa có | assumed |
| [M2](metrics/M2.md) | SEQ từ 5,5/7 mỗi task (dưới 4,5 bị đánh dấu) | chưa có | assumed |
| [M3](metrics/M3.md) | SUS từ 68/100 (trên trung bình), dùng làm kiểm tra sức khoẻ chung, không phải ngưỡng đạt | chưa có | assumed |
| [M4](metrics/M4.md) | Thời gian tới tương tác đầu tiên với một tip dưới 30 giây từ lúc mở app | chưa có | assumed |
| [M5](metrics/M5.md) | Từ 25% khách bấm Save chuyển thành người dùng đã đăng ký | chưa có | assumed |
<!-- /generated -->

## Principle checks

Các principle P1 đến P10 (10 heuristics của Nielsen) và principle riêng của tổ chức nằm ở [`00-context/principle-checks.md`](../00-context/principle-checks.md). Dự án gốc chưa viết câu hỏi có/không cho từng principle; đây là khoảng trống đã được ghi ở gate 2d.

## Agreement

Status: **not available**. Không có người đồng ký thật.
