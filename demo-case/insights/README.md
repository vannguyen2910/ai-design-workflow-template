# Insights

Folder này giữ **các item nối với nhau**: nhu cầu của người dùng, điều nhóm tin, quyết định thiết kế, bằng chứng, vấn đề tìm thấy, và con số đo. Mỗi item là một file, mỗi loại một folder:

| Folder | Loại | Mã | Là gì |
|---|---|---|---|
| `opportunities/` | Opportunity | O1, O2... | Một nhu cầu hoặc khó khăn của người dùng, có bằng chứng |
| `hypotheses/` | Hypothesis | H1... | Điều nhóm tin là đúng, kèm cách biết đúng hay sai |
| `decisions/` | Decision | D1... | Một lựa chọn thiết kế, kèm lý do |
| `evidence/` | Evidence | E1... | Một test hoặc nghiên cứu kiểm chứng hypothesis |
| `findings/` | Finding | F1... | Một vấn đề usability, kèm severity 0 đến 4 |
| `metrics/` | Metric | M1... | Con số cho biết hypothesis đúng hay sai |

## Thêm một item

1. Copy một file trong `_templates/` vào folder loại tương ứng.
2. Đặt tên file theo mã tiếp theo (ví dụ `D4.md`). Mã là duy nhất trong cả dự án.
3. Điền phần thông tin ở đầu file, nhất là các dòng nối về item khác (`tests`, `serves`, `found_in`...).

Báo cáo hiện các item này ở mục **Insights**, nối chúng thành cây từ nhu cầu tới decision, và tự cảnh báo chỗ thiếu liên kết. Cách nối chi tiết nằm ở `reference/how-the-hub-works.md`.

File `README.md` này không hiện trong báo cáo.
