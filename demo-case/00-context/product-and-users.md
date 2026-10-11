# Product and users

*Nửa trang, đã ẩn danh. File này được đưa vào các bước AI trước tiên, nên hãy viết cho người đọc chưa biết gì về dự án.*

> **Về bản demo này:** nội dung được rút gọn từ các tài liệu gốc của dự án Travel Buddy (xem `reference/` và `01-discover/sources/anonymised/`). Mã `RH1`..`RH10` là các research hypothesis (`H1`..`H10` trong tài liệu gốc); mã `SP-D1`, `SP-P3`... là ID trong Solution Pool gốc. Mã `O`, `H`, `D`, `T`, `M` trong `hub/` là item của workspace.

## The product
Travel Buddy là ý tưởng một app đồng hành du lịch ở giai đoạn đầu. App gom ba việc mà du khách hiện làm bằng 8 đến 10 app khác nhau: tìm gợi ý đáng tin và phi thương mại (Discover), kết nối với người địa phương mà không phải trả tiền (Connect), và lập kế hoạch linh hoạt rồi lưu lại chuyến đi (Plan & Journal).

## The users
Du khách đã đi chơi ít nhất một chuyến trong 12 tháng gần nhất, dùng điện thoại và ít nhất một công cụ số khi đi. Ba persona chính:

- **Aisha, Explorer / Pragmatic Planner:** lập kế hoạch kỹ trước chuyến đi nhưng thay đổi 30 đến 40% khi tới nơi; dùng 8 đến 10 công cụ và tự chép thông tin giữa chúng.
- **Marco, Connector:** muốn gặp người địa phương nhưng cần tín hiệu an toàn và không muốn trả tiền cho sự kết nối.
- **Ji-yeon, Documenter:** chụp nhiều nhưng không có hệ thống; muốn ký ức tự được sắp xếp và chia sẻ riêng tư.

Phía cung là người địa phương làm guide không chính thức; nhóm này chưa được nghiên cứu.

## Where it stands now
Dự án đã có: survey (13 phản hồi hợp lệ), một cuộc phỏng vấn (P1), phân tích 5 đối thủ, personas, Solution Pool 26 giải pháp, E2E flow, information architecture giả thuyết, PRD cho tab Explore, prototype high-fidelity 32 màn hình, kế hoạch test không điều phối, và một vòng usability test **mô phỏng** (không phải người thật).

## What success might look like
Các mục tiêu sau lấy từ PRD của tab Explore. Chúng là mục tiêu do chính nhóm đặt và chưa được ai xác nhận, nên đều là **assumed**:

- Thời gian tới tương tác đầu tiên với một tip: dưới 30 giây từ lúc mở app
- Khách chưa đăng ký chuyển thành người dùng đã đăng ký khi bấm Save: từ 25%
- Số tip được lưu mỗi phiên (người dùng đã đăng ký): từ 2

## What I do not know
- Người địa phương có sẵn lòng làm guide cho du khách không (RH6): chưa phỏng vấn ai
- Người dùng thật phản ứng ra sao với prototype: vòng test duy nhất là mô phỏng
- Cái gì nằm sau paywall khi mô hình là free-first
- Crowd signal là dữ liệu người dùng báo, điểm do thuật toán tính, hay cả hai
