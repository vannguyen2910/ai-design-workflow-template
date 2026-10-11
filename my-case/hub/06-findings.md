# Findings

*Người dùng thật đã làm gì: task success, thời gian, lỗi và mức hài lòng, đặt cạnh baseline.*

> **Cách điền:** mỗi evidence (một test hoặc nghiên cứu) là một file riêng trong `hub/evidence/`, ghi rõ nó kiểm chứng hypothesis nào và đo metric nào; bảng bên dưới do AI cập nhật từ các file đó. Báo cáo kết quả so với baseline. Kiểm tra mọi phân tích có AI hỗ trợ với ghi chú hoặc bản ghi gốc. Copy từ [`work/deliver/findings.md`](../work/deliver/findings.md).

## Evidence

<!-- generated:evidence (phần tự động: đừng sửa tay, nhờ AI cập nhật bằng bước "Refresh the hub") -->
| Mã | Evidence | Kiểm chứng | Đo bằng |
|---|---|---|---|
| [E1](evidence/E1.md) | [EXAMPLE] Test task với 5 người: hoàn tất setup không cần trợ giúp | H1 | M1 |
<!-- /generated -->

## Results against the baseline

| Metric | Baseline | Result | Met? |
|---|---|---|---|
| M1 | [baseline] | [result] | [yes / no] |

## Findings, weighted by importance

*Xếp theo mức severity (từ 4 xuống 0), không theo số lần được nhắc. Thang 0 đến 4 và cách chấm nằm ở [Severity levels](../reference/severity-levels.md); principle bị vi phạm lấy từ [Principle checks](../reference/principle-checks.md).*

| Finding | Principle bị vi phạm | Severity (0 đến 4) | Bằng chứng | Việc cần làm |
|---|---|---|---|---|
| [MỘT CÂU mô tả vấn đề, từ góc nhìn người dùng] | [P1 đến P10] | [0 đến 4, kèm lý do nếu là 3 hoặc 4] | [mã evidence hoặc bản ghi] | [sửa / chấp nhận / hoãn] |

Finding mức 4 chặn handoff. Finding mức 3 cần một quyết định rõ: sửa, hoặc chấp nhận như một trade-off và ghi vào [case log](../reference/case-log.md).

## What changed because of this

[Thay đổi thiết kế và các decision đã cập nhật. Thêm chúng vào [case log](../reference/case-log.md).]
