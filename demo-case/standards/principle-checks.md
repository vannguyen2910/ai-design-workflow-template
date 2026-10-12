# Principle checks

*Viết khi bắt đầu giai đoạn Define. Đây là bộ nguyên tắc dùng trong **Heuristic Evaluation**: kiểm tra một thiết kế với 10 usability heuristics của Nielsen. Biến mỗi principle thành một câu hỏi có/không cho sản phẩm của bạn. Thêm principle riêng của tổ chức ở dưới, đánh số từ P11.*

## Cách dùng

1. **Viết câu hỏi có/không cho sản phẩm của bạn** vào cột cuối của bảng dưới đây. Mỗi principle ở phần "Chi tiết" có sẵn các câu hỏi gợi ý: chọn, sửa lại theo sản phẩm, rồi ghi vào bảng.
2. **Đánh giá thiết kế:** với mỗi decision hoặc màn hình, đi qua từng câu hỏi. Câu trả lời "không" là một vi phạm.
3. **Ghi mỗi vi phạm kèm mức độ nghiêm trọng** (0 đến 4), theo [Severity levels](severity-levels.md).
4. **Đánh giá độc lập, rồi gộp lại:** một người thường chỉ tìm được một phần vấn đề. Nếu có thể, nhờ 3 đến 5 người đánh giá riêng, sau đó gộp kết quả.
5. **Nối về hub:** decision đạt thì ghi `follows` tới principle, decision vi phạm mà bạn chấp nhận thì ghi `pulls_against` và lý do (xem `_skills/how-the-hub-works.md`).

## Bảng principle

| ID | Principle | Yes/no check for my product |
|---|---|---|
| P1 | Visibility of system status | |
| P2 | Match between system and the real world | |
| P3 | User control and freedom | |
| P4 | Consistency and standards | |
| P5 | Error prevention | |
| P6 | Recognition rather than recall | |
| P7 | Flexibility and efficiency of use | |
| P8 | Aesthetic and minimalist design | |
| P9 | Help users recognise, diagnose and recover from errors | |
| P10 | Help and documentation | |
| P11 | (principle của tổ chức, nếu có) | |

---

# Chi tiết 10 heuristics

Mỗi mục có bốn phần: **Nghĩa là** (giải thích bằng lời thường), **Hỏi khi đánh giá** (câu hỏi có/không để chép vào bảng trên), **Dấu hiệu vi phạm**, và **Ví dụ**.

## P1 · Visibility of system status

**Nghĩa là:** hệ thống luôn cho người dùng biết chuyện gì đang xảy ra, qua phản hồi kịp thời và dễ thấy. Người dùng không phải đoán xem thao tác của mình đã có hiệu lực chưa.

**Hỏi khi đánh giá:**
- Sau mỗi thao tác, người dùng có thấy phản hồi ngay (đã lưu, đã gửi, đang tải) không?
- Với việc mất hơn vài giây, có hiển thị tiến độ hoặc trạng thái đang xử lý không?
- Người dùng có biết mình đang ở đâu trong một quy trình nhiều bước (bước mấy trên tổng số) không?
- Trạng thái hiện tại của một mục (đã chọn, đang tắt, đã xác nhận) có nhìn thấy được mà không cần mở ra không?

**Dấu hiệu vi phạm:** bấm nút mà không có gì xảy ra; trang trắng khi đang tải; người dùng bấm lại nhiều lần vì không chắc lần đầu đã được.

**Ví dụ:** thanh tiến độ khi tải tệp; nhãn "Đã lưu" xuất hiện sau khi bấm Lưu; chỉ báo "Bước 2/4" ở đầu form.

## P2 · Match between system and the real world

**Nghĩa là:** hệ thống nói ngôn ngữ của người dùng: từ ngữ, khái niệm, thứ tự quen thuộc với họ, không phải thuật ngữ nội bộ của hệ thống.

**Hỏi khi đánh giá:**
- Nhãn, nút và thông báo có dùng từ mà người dùng thật sự dùng không (không có thuật ngữ nội bộ, mã lỗi, tên kỹ thuật)?
- Thứ tự các bước có theo thứ tự tự nhiên của việc người dùng đang làm ngoài đời không?
- Biểu tượng và hình ẩn dụ có giống thứ người dùng đã biết không?
- Thông tin có xuất hiện theo logic của người dùng (ví dụ theo chuyến đi) thay vì theo cấu trúc dữ liệu của hệ thống không?

**Dấu hiệu vi phạm:** người dùng hỏi "chữ này nghĩa là gì?"; nhãn lấy từ tên bảng trong cơ sở dữ liệu; từ viết tắt không giải thích.

**Ví dụ:** dùng "Giỏ hàng" thay cho "Danh sách mục đã chọn"; sắp thẻ tín dụng đã lưu giống thẻ vật lý.

## P3 · User control and freedom

**Nghĩa là:** người dùng hay bấm nhầm. Họ cần một "lối thoát khẩn cấp" rõ ràng để rời khỏi trạng thái không mong muốn, mà không phải đi qua một quy trình dài.

**Hỏi khi đánh giá:**
- Người dùng có thể huỷ hoặc quay lại ở mọi bước của một quy trình không?
- Có hoàn tác (undo) cho các thao tác dễ nhầm không?
- Người dùng có thoát được khỏi cửa sổ hoặc chế độ đang mở mà không mất công việc đang làm không?
- Thao tác xoá hoặc ghi đè có thể quay lại được, hoặc có hỏi xác nhận trước không?

**Dấu hiệu vi phạm:** không có nút Huỷ; chỉ thoát được bằng cách đóng cả ứng dụng; xoá nhầm là mất vĩnh viễn.

**Ví dụ:** thông báo "Đã xoá. Hoàn tác" hiện vài giây; nút Quay lại giữ nguyên dữ liệu đã nhập.

## P4 · Consistency and standards

**Nghĩa là:** cùng một thứ thì trông và hoạt động giống nhau ở mọi nơi. Người dùng không phải tự hỏi hai từ hoặc hai hành động khác nhau có cùng nghĩa không. Tuân theo quy ước của nền tảng và của ngành.

**Hỏi khi đánh giá:**
- Cùng một hành động có cùng tên và cùng vị trí ở mọi màn hình không?
- Cùng một thành phần (nút, ô nhập, thẻ) có cùng hình dạng và cách hoạt động không?
- Sản phẩm có theo quy ước của nền tảng (iOS, Android, web) cho những thứ quen thuộc không?
- Một từ có luôn chỉ cùng một khái niệm không?

**Dấu hiệu vi phạm:** "Lưu" ở màn này nhưng "Xác nhận" ở màn khác cho cùng việc; hai kiểu nút chính khác nhau; biểu tượng một nghĩa nhưng dùng cho hai việc.

**Ví dụ:** nút chính luôn nằm ở góc dưới bên phải và cùng màu; logo ở góc trên trái dẫn về trang chủ.

## P5 · Error prevention

**Nghĩa là:** tốt hơn thông báo lỗi rõ ràng là thiết kế để lỗi không xảy ra. Loại bỏ các tình huống dễ gây lỗi, hoặc kiểm tra và hỏi xác nhận trước khi người dùng thực hiện.

**Hỏi khi đánh giá:**
- Với thao tác hệ trọng (xoá, thanh toán, gửi), có bước xác nhận hoặc cách hoàn tác không?
- Ô nhập có giúp người dùng nhập đúng (định dạng gợi ý, giá trị mặc định hợp lý, giới hạn) không?
- Hệ thống có ngăn lựa chọn không hợp lệ thay vì để người dùng chọn rồi báo lỗi không?
- Hai thao tác dễ nhầm có được đặt xa nhau, hoặc có phân biệt rõ về hình thức không?

**Dấu hiệu vi phạm:** để nhập ngày trong quá khứ rồi mới báo "ngày không hợp lệ"; nút Xoá nằm sát nút Lưu và cùng kiểu.

**Ví dụ:** bộ chọn ngày khoá những ngày không chọn được; nút Xoá có màu cảnh báo và hỏi xác nhận.

## P6 · Recognition rather than recall

**Nghĩa là:** giảm gánh nặng trí nhớ. Đưa các lựa chọn, thông tin và hành động ra ngay trước mắt để người dùng nhận ra, thay vì buộc họ phải nhớ từ màn hình trước.

**Hỏi khi đánh giá:**
- Thông tin cần cho một bước có hiển thị ngay ở bước đó không (không bắt người dùng nhớ từ bước trước)?
- Người dùng có chọn được từ một danh sách thay vì gõ lại từ trí nhớ không?
- Các hành động và lựa chọn có nhìn thấy được thay vì giấu sau các thao tác ẩn không?
- Nếu có lịch sử hoặc gợi ý (mục đã dùng gần đây, tự điền), người dùng có dùng được không?

**Dấu hiệu vi phạm:** bắt nhập lại mã đã thấy ở màn trước; chức năng chỉ có qua cử chỉ ẩn mà không có gợi ý.

**Ví dụ:** hiện các tìm kiếm gần đây; tóm tắt đơn hàng nằm cạnh bước thanh toán.

## P7 · Flexibility and efficiency of use

**Nghĩa là:** hệ thống phục vụ cả người mới và người dùng quen. Có đường tắt, tuỳ chỉnh và cách làm nhanh cho người dùng thường xuyên, mà không làm rối người mới.

**Hỏi khi đánh giá:**
- Người dùng quen có đường tắt (phím tắt, thao tác nhanh, thao tác hàng loạt) không?
- Hệ thống có nhớ lựa chọn, thiết lập hoặc dữ liệu lặp lại để khỏi phải làm lại không?
- Người mới có đi được con đường đầy đủ, rõ ràng không?
- Người dùng có thể tuỳ chỉnh những phần thường dùng không?

**Dấu hiệu vi phạm:** người dùng lâu năm phải đi qua cùng năm bước mỗi lần; không có cách làm nhiều mục một lúc.

**Ví dụ:** phím tắt cho thao tác thường dùng; "mua lại" từ đơn trước; thao tác chọn nhiều mục.

## P8 · Aesthetic and minimalist design

**Nghĩa là:** giao diện không chứa thông tin thừa hoặc ít liên quan. Mỗi đơn vị thông tin thêm vào đều cạnh tranh sự chú ý với thông tin quan trọng và làm nó khó thấy hơn.

**Hỏi khi đánh giá:**
- Mỗi màn hình có một việc chính rõ ràng, và nó nổi bật hơn phần còn lại không?
- Mọi thành phần trên màn hình có phục vụ việc người dùng đang làm không?
- Chữ có ngắn gọn, và thông tin ít dùng có được giấu bớt (mở rộng khi cần) không?
- Phần trang trí có làm người dùng chậm hoặc khó đọc hơn không?

**Dấu hiệu vi phạm:** màn hình đầy chữ và nút ngang hàng nhau; banner, popup và biểu tượng cạnh tranh nhau; chữ giải thích dài mà không ai đọc.

**Ví dụ:** màn hình thanh toán chỉ giữ các trường cần thiết; tính năng nâng cao nằm sau mục "Thêm tuỳ chọn".

## P9 · Help users recognise, diagnose and recover from errors

**Nghĩa là:** thông báo lỗi dùng ngôn ngữ thường (không mã lỗi), nói rõ vấn đề là gì và đề xuất cách giải quyết một cách mang tính xây dựng.

**Hỏi khi đánh giá:**
- Thông báo lỗi có viết bằng lời thường, không có mã lỗi hay thuật ngữ kỹ thuật không?
- Nó có nói rõ cái gì sai và ở đâu (chỉ đúng ô hoặc bước) không?
- Nó có nói người dùng cần làm gì tiếp theo, và có nút để làm việc đó không?
- Công việc người dùng đã nhập có được giữ lại để họ sửa mà không phải làm lại không?

**Dấu hiệu vi phạm:** "Đã xảy ra lỗi. Mã 500."; lỗi hiện đỏ ở đầu trang mà không chỉ ô nào sai; xoá hết form sau khi báo lỗi.

**Ví dụ:** "Email này đã được dùng. Đăng nhập hoặc dùng email khác." kèm nút Đăng nhập.

## P10 · Help and documentation

**Nghĩa là:** tốt nhất là hệ thống dùng được không cần giải thích. Nhưng khi cần, trợ giúp phải dễ tìm, gắn với việc đang làm, có các bước cụ thể và không quá dài.

**Hỏi khi đánh giá:**
- Người dùng có tìm được trợ giúp đúng lúc và đúng chỗ họ cần (ngay trong ngữ cảnh) không?
- Nội dung trợ giúp có tìm kiếm được và theo việc người dùng muốn làm, không theo cấu trúc tính năng không?
- Nó có các bước ngắn, cụ thể, dễ làm theo không?
- Với những thứ người dùng lần đầu gặp, có gợi ý ngắn (onboarding, mẹo) không?

**Dấu hiệu vi phạm:** trợ giúp là một tài liệu PDF dài; phải rời khỏi màn hình đang làm để tìm; không có cách nào tìm kiếm.

**Ví dụ:** biểu tượng "?" cạnh trường khó hiểu mở ra một dòng giải thích; tìm kiếm trong trung tâm trợ giúp theo việc cần làm.

---

# Nguồn

- Nielsen, J. (1994). *10 Usability Heuristics for User Interface Design.* Nielsen Norman Group. Nielsen tinh chỉnh bộ 10 heuristics này năm 1994 từ phân tích 249 vấn đề usability; Nielsen Norman Group đã cập nhật phần giải thích từ đó.
- Nielsen, J. (1994). *How to Conduct a Heuristic Evaluation.* Nielsen Norman Group.
- Nielsen, J., & Molich, R. (1990). *Heuristic evaluation of user interfaces.* Proceedings of ACM CHI'90.

Phần giải thích và câu hỏi ở trên được viết lại bằng lời thường để dùng ngay trong dự án. Khi cần trích dẫn chính xác, hãy đọc nguồn gốc ở Nielsen Norman Group.
