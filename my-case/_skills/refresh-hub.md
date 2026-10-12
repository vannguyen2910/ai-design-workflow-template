# Workflow: Review the Hub

Nhờ AI đọc các file item và liệt kê những chỗ chưa nối, chưa khớp hoặc còn thiếu, rồi bạn quyết định xử lý từng cái. **Workflow này không ghi vào file nào**: các bảng và warnings trong báo cáo do `python3 _skills/export-hub.py` tự tính.

*Trạng thái: bản nháp.*

| | |
|---|---|
| Khi nào | Sau khi bạn thêm hoặc sửa nhiều item, hoặc trước khi handoff |
| Làm trước | Chạy `python3 _skills/export-hub.py` để báo cáo cập nhật |
| Working file | Không có. Kết quả trả lời ngay trong chat |

## Step 1: Review (AI)

**Who:** AI
**Input:** `insights/opportunities/*.md`, `insights/hypotheses/*.md`, `insights/metrics/*.md`, `insights/decisions/*.md`, `insights/evidence/*.md`, `insights/findings/*.md`, `standards/gates.md`, `standards/principle-checks.md`
**Output:** Danh sách vấn đề tìm thấy, trả lời trong chat. Không ghi vào file nào.

**Instruction:**
> Đọc các file input và liệt kê vấn đề, mỗi loại một nhóm, viết bằng lời thường kèm mã item. Quan hệ nằm trong properties ở đầu mỗi file item (wikilink) và chỉ được khai báo một chiều: H có `serves` (O) và `metric` (M); D có `tests` (H), `follows` và `pulls_against` (P); E có `tests` (H) và `measures` (M); F có `found_in` (E), `affects` (D), `principle` (P), `severity` (0 đến 4) và `resolution`. Hướng ngược lại bạn suy ra.
>
> - Decision chưa nối được về nhu cầu nào của người dùng (`tests` rỗng); decision đi ngược một principle (`pulls_against`); nhu cầu chưa có decision phục vụ; hypothesis chưa có evidence hoặc chưa có metric; evidence có `status: planned` hoặc `participants_type: simulated`; hypothesis mà mọi test đều là planned hoặc simulated.
> - Metric chưa có `target`, hoặc có `verdict` mà chưa có `result`; decision `accepted` chưa có `owner`; opportunity chưa có `rank_reason`.
> - Finding thiếu `severity` hoặc `found_in`; finding mức 3 hoặc 4 chưa xử lý.
> - Principle trong `principle-checks.md` chưa có câu hỏi có/không.
>
> Không sửa file nào. Không đoán: nếu một link trỏ tới file không tồn tại, hoặc ID không khớp tên file, hoặc có ID trùng, liệt kê vào cuối câu trả lời.

**Check:** Mở 3 mục bất kỳ trong danh sách và đối chiếu với file item tương ứng.
**Failure sign:** AI báo vấn đề không có trong file item; AI sửa file; danh sách thiếu vấn đề mà báo cáo đã cảnh báo.

## Step 2: Decide (YOU)

**Who:** YOU
**Input:** Warnings vừa được dựng, và câu trả lời của AI ở step 1
**Output:** `work/alignment.md` (verdict cho từng warning), `insights/case-log.md`

Với mỗi warning, chọn một: sửa file item, chấp nhận như một trade-off có lý do, hoặc cắt. Item bị cắt thì xoá file và chạy lại workflow này.

**Check:** Bạn bảo vệ được từng decision bằng cách chỉ vào opportunity và hypothesis phía sau không?
**Failure sign:** Warning bị bỏ qua vì "AI báo sai" mà chưa mở file kiểm tra.
