# _ai: step card và script cho AI

Folder này chứa hai thứ. **Step card** (file `.md`): định nghĩa quy trình AI-assisted dưới dạng file, để AI tool đọc được và quy trình được lưu cùng case. Mỗi file là một workflow, gồm các step có thứ tự, và mỗi step ghi rõ ai làm (AI hay bạn), đọc file nào và ghi vào đâu.

## Cards

| Workflow | Giai đoạn | Khi nào dùng | Trạng thái |
|---|---|---|---|
| [`competitor-analysis.md`](competitor-analysis.md) | Discover | Khi cần biết đối thủ đang làm gì | Bản nháp, chưa được thử nhiều |
| [`user-voice-synthesis.md`](user-voice-synthesis.md) | Discover | Khi có quote hoặc phỏng vấn người dùng để tổng hợp | Bản nháp, chưa được thử nhiều |
| [`add-insights.md`](add-insights.md) | Discover, Test | Khi có tài liệu nghiên cứu mới (phỏng vấn, khảo sát, kết quả test) cần biến thành item | Bản nháp |
| [`refresh-hub.md`](refresh-hub.md) | Mọi giai đoạn | Khi muốn AI rà soát những chỗ item chưa nối hoặc còn thiếu | Bản nháp |
| [`add-media.md`](add-media.md) | Mọi giai đoạn | Khi có ảnh, video, PDF hoặc tài liệu cần đưa vào báo cáo | Bản nháp |
| [`export-hub.md`](export-hub.md) | Mọi stage | Khi cần xem hub trong trình duyệt hoặc gửi cho người khác | Bản nháp |

**Script** (file `.py`): `export-hub.py` tạo báo cáo `index.html`, `serve-hub.py` xem báo cáo ngay khi bạn lưu file. Bạn thường nhờ AI chạy chúng thay vì mở tay.

Các card cho Frame, Explore, Prototype và Test sẽ được bổ sung. Bạn tự thêm card riêng theo hướng dẫn bên dưới.

## How to run a step

1. Mở cả folder case trong AI tool. Tool tự đọc `AGENTS.md` ở gốc.
2. Commit trước (nếu bạn dùng Git), để quay lại được.
3. Nói với tool: *"Chạy step 5 của `_ai/user-voice-synthesis.md`."*
4. Đọc kết quả, rồi tự kiểm tra ở step tiếp theo. Step có nhãn **(YOU)** là phần bạn vẫn tự làm.

## Card format

Mỗi step có các dòng cố định:

| Dòng | Ý nghĩa |
|---|---|
| **Who** | `YOU` hoặc `AI` |
| **Input** | Các file mà bước này được đọc, và chỉ các file đó |
| **Instruction** | Câu lệnh đưa cho AI (chỉ có ở step của AI) |
| **Output** | Section hoặc file được ghi |
| **Check** | Bạn kiểm tra điều gì trước khi sang step sau |
| **Failure sign** | Dấu hiệu bước này đã hỏng |

## Add your own workflow

Copy một card, đổi tên, giữ các dòng cố định ở trên. Mỗi workflow nên có tối đa 8 step, một working file duy nhất, và hai quy tắc: AI chỉ trả về section của nó, và bản nháp của AI luôn tách khỏi bản bạn đã kiểm tra.
