# Demo case: Kitchen Crate

**Mọi thứ trong folder này đều bịa.** Không có công ty, người, review hay con số thật.

Kitchen Crate là một app meal-kit theo subscription. Đội sản phẩm thấy nhiều khách mới tạm dừng hoặc huỷ sau hộp đầu tiên, và muốn cải thiện onboarding.

Cấu trúc folder giống hệt `my-case`. Khác biệt là folder này đã có sẵn dữ liệu đầu vào của case, nên bạn bắt đầu làm được ngay.

## What is already here

| File | Nội dung | Dùng ở |
|---|---|---|
| `AGENTS.md`, `workflow/` | Luật cho AI tool và các step card | Mọi tuần |
| `00-context/case-card.md` | Một trang giới thiệu case | Tuần 1 |
| `01-discover/sources/anonymised/quotes.md` | 24 quote giả, có ID, từ ba loại nguồn | Tuần 2, session B |
| `01-discover/sources/anonymised/competitors/` | Ba trang đối thủ giả | Tuần 2, phần demo |
| `03-develop/prototype/` | Starter: một design system nhỏ, file rules và một trang trống | Tuần 5 |
| `03-develop/prototype-checkpoint/` | Prototype ba màn hình chạy được, cố ý còn thiếu một số thứ để bạn chỉnh | Tuần 6, hoặc khi bạn bỏ lỡ tuần 5 |
| `hub/` | Hub với dữ liệu ví dụ | Mọi tuần |

Các working file còn lại (scope, problem brief, options…) vẫn trống. Bạn điền chúng khi làm theo từng tuần.

## How to use it

- **Để xem mẫu:** mở `hub/README.md` để thấy hub, và mở `03-develop/prototype-checkpoint/index.html` bằng trình duyệt để thấy một prototype hoàn chỉnh.
- **Để luyện tập:** làm theo bảng "What to fill each week" ở [`README.md`](../README.md) của workspace, và điền vào các file trong folder này.
- **Để bắt kịp một tuần đã bỏ lỡ:** dùng các file nguồn ở trên, và đừng chép nội dung của người khác vào `my-case`.

## Rules

1. Case này là giả, nhưng vẫn giữ thói quen đúng: ghi `assumed` cho mọi con số chưa xác nhận.
2. Chỉ dùng ba trang đối thủ trong `sources/anonymised/competitors/` làm nguồn. Chỗ nào trang không nói thì câu trả lời là "unknown".
3. Giữ bản nháp của AI và bản bạn đã kiểm tra ở hai section riêng.
