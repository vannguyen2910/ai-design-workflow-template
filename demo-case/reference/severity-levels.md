# Severity levels

*Thang đo mức độ nghiêm trọng của một vấn đề usability, dùng khi bạn đánh giá thiết kế (Heuristic Evaluation) hoặc ghi findings từ một lần test với người dùng. Dựa trên thang 0 đến 4 của Nielsen. Dùng cùng một thang cho mọi finding để các mức có thể so sánh với nhau.*

## Thang 0 đến 4

| Mức | Tên | Nghĩa | Ví dụ | Nên làm gì |
|---|---|---|---|---|
| **0** | Không phải vấn đề | Bạn không đồng ý đây là vấn đề usability | Một người đánh giá thấy nhãn hơi lạ, nhưng người dùng thật hiểu ngay | Ghi lại và loại bỏ, kèm lý do |
| **1** | Cosmetic | Chỉ là vấn đề về hình thức, không cản trở người dùng làm việc | Hai biểu tượng lệch nhau vài pixel; nhãn viết hoa không đồng nhất | Chỉ sửa nếu còn thời gian |
| **2** | Minor | Vấn đề nhỏ: gây khó chịu hoặc chậm một chút, người dùng vẫn hoàn thành được | Nút nằm hơi xa nên phải cuộn thêm; thông báo lỗi chưa nói rõ cách sửa | Ưu tiên thấp; đưa vào backlog |
| **3** | Major | Vấn đề lớn: nhiều người dùng bị chặn lại, mất nhiều thời gian hoặc phải đi đường vòng | Không tìm ra nơi chia sẻ; phải nhập lại dữ liệu sau khi gặp lỗi | Quan trọng, ưu tiên cao; sửa trước khi launch, hoặc ghi rõ lý do chấp nhận |
| **4** | Catastrophe | Vấn đề nghiêm trọng đến mức người dùng không hoàn thành được việc chính, hoặc gây mất dữ liệu, mất tiền | Nút thanh toán không hoạt động; xoá nhầm mà không thể quay lại | **Bắt buộc sửa trước khi phát hành** |

## Cách quyết định một mức

Một vấn đề được chấm dựa trên ba yếu tố, nhìn chung chứ không cộng điểm:

| Yếu tố | Câu hỏi | Nghiêng về mức cao khi |
|---|---|---|
| **Frequency** (tần suất) | Vấn đề này xảy ra thường xuyên đến đâu? Bao nhiêu người gặp? | Hầu hết người dùng gặp, hoặc gặp ở việc chính |
| **Impact** (tác động) | Khi gặp, người dùng vượt qua dễ hay khó? | Họ bị chặn lại, mất dữ liệu, hoặc không biết cách tiếp tục |
| **Persistence** (độ dai dẳng) | Chỉ gặp một lần, hay lặp lại mãi? | Người dùng không học được cách né, mỗi lần đều gặp lại |

Ví dụ: một lỗi hiếm xảy ra nhưng làm mất toàn bộ dữ liệu có thể là mức 4. Một khó chịu xảy ra ở mọi lượt dùng nhưng chỉ tốn một giây có thể là mức 2.

## Cách chấm

1. **Chấm sau khi đã xem hết thiết kế,** không chấm giữa chừng. Bạn cần biết bức tranh tổng thể để so sánh các vấn đề với nhau.
2. **Mỗi người chấm riêng,** rồi mới so sánh. Một người chấm đơn lẻ thường lệch; lấy mức trung bình của 3 người trở lên đáng tin hơn.
3. **Chấm vấn đề, không chấm giải pháp.** Mức nghiêm trọng nói về tác động lên người dùng, không phải việc sửa dễ hay khó.
4. **Ghi lý do ngắn** cho mức 3 và 4, để người khác hiểu vì sao.

## Dùng thang này trong hub

- Mỗi finding là một file trong `insights/findings/` với property `severity` (0 đến 4) và `principle` (xem [Principle checks](principle-checks.md)). Báo cáo tự xếp finding theo mức, và trang Findings trong Stages hiện danh sách.
- Ở gate Deliver, check 4b yêu cầu findings được xếp theo mức độ quan trọng: dùng thang này.
- Mức **4** chặn handoff: báo cáo cảnh báo khi còn finding mức 4 có `resolution: open`, và đánh dấu decision bị ảnh hưởng.
- Mức **3** cần một quyết định rõ: sửa, hoặc chấp nhận như một trade-off và ghi vào `reference/case-log.md`.
- Mức **0 đến 2** có thể đưa vào backlog sau launch.

## Cách ghi một finding

| Finding | Principle bị vi phạm | Severity (0 đến 4) | Bằng chứng | Việc cần làm |
|---|---|---|---|---|
| Một câu mô tả vấn đề, từ góc nhìn người dùng | Mã principle, ví dụ P1 | 0 đến 4, kèm lý do ngắn nếu là 3 hoặc 4 | Mã evidence hoặc bản ghi | Sửa / chấp nhận / hoãn |

## Nguồn

- Nielsen, J. (1994). *Severity Ratings for Usability Problems.* Nielsen Norman Group.
- Nielsen, J. (1994). *How to Conduct a Heuristic Evaluation.* Nielsen Norman Group.
