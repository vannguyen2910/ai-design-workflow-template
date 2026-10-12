# Workflow: Add insights from new research

Biến một tài liệu nghiên cứu mới (phỏng vấn, khảo sát, kết quả test) thành các item trong `insights/`, để insight mới hiện ở trang Insights và nối được về nhu cầu, hypothesis, decision phía sau.

*Trạng thái: bản nháp. Hãy thử trên một tài liệu thật và chỉnh theo cách bạn làm trước khi dựa vào nó.*

| | |
|---|---|
| Khi nào | Sau khi bạn thêm một file nghiên cứu vào `work/` (hoặc `work/<tên>/index.md`) và muốn đưa điều học được vào hub |
| Làm trước | Ẩn danh dữ liệu, lưu một mốc (commit hoặc copy folder) |
| Working file | Không có. Kết quả ghi vào `insights/` và property `supports` của tài liệu |
| Liên quan | `_ai/new-item.py` (tạo item), `_ai/refresh-hub.md` (kiểm tra warnings sau đó) |

Hub **không tự rút insight** từ file ở `work/`. Workflow này là bước làm việc đó, và bạn là người duyệt trước khi bất cứ file nào được tạo.

## Step 1: Propose (AI)

**Who:** AI
**Input:** Tài liệu mới (một file duy nhất), danh sách item hiện có trong `insights/` (mã và title), `reference/principle-checks.md`
**Output:** Một bảng đề xuất ngay trong chat. **Chưa tạo file nào.**

**Instruction:**
> Đọc tài liệu mới. Đề xuất các insight có trong chính tài liệu đó, mỗi insight một dòng của bảng gồm: (1) trích ngắn hoặc mã quote làm nguồn, (2) loại item đề xuất (evidence, opportunity, finding, hypothesis), (3) title một câu, (4) quan hệ với item đã có (`tests`, `serves`, `found_in`...) bằng mã có thật, (5) nó **củng cố**, **mâu thuẫn** hay **mới** so với item hiện có, (6) độ chắc chắn: một nguồn hay nhiều nguồn.
>
> Quy tắc: chỉ dùng điều có trong tài liệu, không suy diễn thêm. Một buổi phỏng vấn hay một cuộc test luôn là một evidence; chỉ đề xuất opportunity mới khi nhu cầu chưa có trong danh sách. Nếu insight mâu thuẫn một item đã có, nói rõ và đừng gộp. Đừng đặt decision nào thành `accepted`, và đừng tự chọn thứ hạng hay impact: để trống để tôi quyết.

**Check:** Mở tài liệu và đối chiếu ba dòng bất kỳ: nguồn có đúng ở đó không?
**Failure sign:** Có insight không có nguồn trong tài liệu; mã item trong cột quan hệ không tồn tại; AI gộp một insight mâu thuẫn vào item cũ mà không nói.

## Step 2: Decide (YOU)

**Who:** YOU
**Input:** Bảng đề xuất ở step 1
**Output:** Danh sách dòng được duyệt, kèm chỉnh sửa của bạn

Với mỗi dòng chọn một: giữ, sửa title hoặc quan hệ, hoặc cắt. Với opportunity mới, tự nói `impact`, `confidence` và lý do xếp hạng (hoặc để trống và bổ sung sau).

**Check:** Bạn bảo vệ được từng dòng được giữ bằng cách chỉ vào đoạn trong tài liệu không?
**Failure sign:** Giữ một dòng chỉ vì AI viết nghe hợp lý.

## Step 3: Create the items (AI)

**Who:** AI
**Input:** Các dòng đã duyệt ở step 2
**Output:** Các file mới trong `insights/<loại>/`

**Instruction:**
> Với từng dòng đã duyệt, chạy `python3 _ai/new-item.py <loại> --title "..." <các quan hệ> --no-build`. Evidence của một buổi phỏng vấn hoặc test đã diễn ra: `--status run --participants <số người>`. Không ghi đè file. Sau khi tạo xong, điền phần nội dung của từng file bằng điều có trong tài liệu, kèm nguồn. Nếu lệnh báo mã không tồn tại, dừng và hỏi tôi, đừng đoán.

**Check:** Mở hai file vừa tạo: title, quan hệ và nguồn khớp với dòng bạn đã duyệt?
**Failure sign:** Số file tạo ra nhiều hơn số dòng được duyệt; item có `status: run` nhưng buổi test chưa từng chạy.

## Step 4: Link the document (AI)

**Who:** AI
**Input:** Tài liệu mới và mã các item vừa tạo hoặc bị ảnh hưởng
**Output:** Property `supports` trong phần đầu của tài liệu

**Instruction:**
> Điền `supports` của tài liệu bằng mã các item vừa tạo và các item đã có mà tài liệu củng cố hoặc mâu thuẫn. Chỉ sửa property này; không sửa nội dung tài liệu.

**Check:** Mở tài liệu trong báo cáo: dòng "Hỗ trợ cho" liệt kê đúng các item?
**Failure sign:** `supports` trỏ tới item không liên quan.

## Step 5: Rebuild and read the warnings (YOU)

**Who:** YOU
**Input:** Toàn bộ hub
**Output:** `index.html` mới

Chạy `python3 _ai/export-hub.py`, mở trang **Insights** để xem item mới, rồi đọc mục warnings ở Overview: opportunity mới chưa có decision, hypothesis chưa có test, metric chưa có target là việc cần làm tiếp. Nếu muốn buổi nghiên cứu này hiện ở trang Evidence trong Stages, thêm tên file vào cột **Từ work** của dòng `evidence` trong `stages/README.md`.

**Check:** Mỗi insight bạn đã duyệt có thể tìm thấy ở Insights, và đi ngược được về tài liệu?
**Failure sign:** Item mới không nối với gì (nằm trong nhóm "Chưa nối vào opportunity nào").
