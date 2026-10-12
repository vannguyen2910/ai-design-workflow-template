---
type: "handoff"
title: "Handoff"
stage: "Deliver"
status: "draft"
summary: ""
supports: []
---
*Giai đoạn Deliver, khi bàn giao. Những gì developer cần để dựng được mà không phải hỏi lại.*

> **Trạng thái:** chưa sẵn sàng bàn giao. Mới có PRD cho một tab (Explore); các tab Plan, Connect, Journal chưa có PRD. Gate 4c còn `open`.

## The prototype
Link hoặc folder. Đây là tài liệu tham chiếu, không phải production code.

- Wireframe: `work/wireframes/Travel_Buddy_Wireframe.html`
- Prototype cuối: `work/final-prototype/travel-buddy-final-prototype.html`
- Kế hoạch dựng, danh sách 32 màn hình, 4 flow: `work/original-docs/10_Prototype_Plan.md`
- E2E flow: `work/original-docs/08_E2E_User_Flow.md`

## Decisions and reasons
(Dẫn tới decision log trong `insights/case-log.md`)

Bảy decision và lý do nằm ở `insights/decisions/`; nhật ký thời gian nằm ở `insights/case-log.md`.

## Acceptance notes
*Điều gì phải đúng khi sản phẩm được dựng xong. Từ PRD của tab Explore (mục 8).*
- Cả ba mode (Near Me, Country, Map) điều hướng được qua mode toggle
- Panel filter mở được từ cả ba mode và áp dụng đúng
- Crowd signal badge hiện trên mọi tip card ở mọi mode
- Bấm Save ở trạng thái khách mở sign-up bottom sheet
- Video player và safety panel mở được từ tip card và màn Tip Detail
- Khách duyệt được mọi mode mà không bị bắt đăng ký
- Prototype được test với ít nhất hai người tham gia theo các task của kế hoạch

## Open questions
- Crowd signal là dữ liệu người dùng báo, điểm do thuật toán, hay cả hai?
- Video do du khách tải lên, Travel Buddy tuyển chọn, hay cả hai ở v1?
- Map mode mặc định ở vị trí hiện tại hay ở điểm đến của chuyến đã lưu?
- Cần tối thiểu bao nhiêu tip để một điểm đến hiện trong Country mode?
