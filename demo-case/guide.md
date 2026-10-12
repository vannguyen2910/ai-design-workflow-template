# Hướng dẫn

## 1. Workspace này là gì, dành cho ai

**Là gì.** Một folder cho một sản phẩm, nơi bạn và AI tool cùng làm việc. Tài liệu, nghiên cứu, quyết định và kết quả đo nằm đúng chỗ và nối với nhau, nên AI luôn có đủ context.

**Dành cho.** PM, designer, researcher, hoặc người làm sản phẩm một mình. Không cần biết code.

| Bạn làm ở | Để làm gì |
|---|---|
| `work/` | Việc đã làm: phân tích, wireframe, prototype |
| `insights/` | Điều đã học và quyết định, nối về nhu cầu người dùng |
| `context/` | Thông tin nền để AI đọc trước tiên |
| Menu bên trái | Chỉ để **xem**: tự dựng từ ba folder trên |

## 2. Tôi có một sản phẩm hoặc dự án mới

| Bước | Làm gì | Nói với AI |
|---|---|---|
| 1 | Tạo dự án (mở folder workspace bằng AI tool) | `Tạo một dự án mới tên <tên-dự-án>` |
| 2 | Cho AI biết sản phẩm và người dùng | `Giúp tôi điền thông tin nền về sản phẩm và người dùng. Hỏi tôi từng câu một.` |
| 3 | Viết phạm vi của dự án | `Giúp tôi viết scope: câu hỏi của business, outcome mong muốn, người dùng chính.` |
| 4 | Đưa dữ liệu nghiên cứu (đã ẩn danh) vào | `Rút insight từ file <tên-file>. Đề xuất trước, đừng tạo.` |
| 5 | Xem hub | Bấm đúp `index.html` trong folder dự án |

Sau đó đi qua bốn giai đoạn:

| Giai đoạn | Bạn đang làm gì |
|---|---|
| **Discover** | Hiểu vấn đề và người dùng |
| **Define** | Chốt vấn đề đáng giải nhất |
| **Develop** | Khám phá hướng giải, vẽ wireframe, dựng prototype |
| **Deliver** | Test với người dùng và bàn giao |
| **Learn** | Đọc kết quả sau khi phát hành |

## 3. Tôi có một task hoặc work mới

| Tôi có | Làm gì | Nói với AI |
|---|---|---|
| Một buổi phỏng vấn hoặc khảo sát mới | Lưu file (đã ẩn danh) vào `work/` | `Rút insight từ file <tên-file>. Đề xuất trước, đừng tạo.` |
| Ảnh, wireframe, prototype | Thả vào một folder mới trong `work/` | `Thêm các file trong folder <tên-folder> vào báo cáo.` |
| Một quyết định thiết kế | Không cần file trước | `Ghi một quyết định: <một câu>. Nó kiểm chứng giả thuyết H1. Lý do: <...>. Chưa chấp nhận.` |
| Một nhu cầu hoặc hypothesis mới | Không cần file trước | `Ghi một nhu cầu người dùng: <một câu>. Mức tác động <cao/vừa/thấp>, vì <lý do>.` |
| Kết quả đo sau launch | Không cần file trước | `Chỉ số M1 đo được <số> ngày <ngày>, mục tiêu là <...>. Kết luận: <đạt / chưa đạt>.` |

**Quy tắc chọn chỗ:** việc đã làm thì ở `work/`; điều đã học và quyết định thì ở `insights/`. Mỗi thông tin chỉ ghi một chỗ.

## 4. Tôi muốn xem (preview) hub

| Cách | Khi nào | Làm gì |
|---|---|---|
| **Xem nhanh** | Chỉ cần nhìn | Bấm đúp `index.html` trong folder dự án: mở bằng trình duyệt, không cần cài gì |
| **Xem và tự cập nhật** | Đang sửa file liên tục | Nói với AI: *"Mở bản xem trước của hub, tự cập nhật khi tôi lưu file"*, rồi mở địa chỉ nó đưa |
| **Gửi cho người khác** | Chia sẻ | Nói với AI: *"Đóng gói báo cáo thành một file zip để gửi đi"* |

Báo cáo chỉ đổi khi được tạo lại. Vừa thêm file mà chưa thấy? Nói với AI: *"Tạo lại báo cáo"*, rồi tải lại trang.

## 5. Thuật ngữ để làm việc với AI

**Các thứ trong workspace**

| Từ | Nghĩa |
|---|---|
| **Hub** | Cả folder dự án và báo cáo `index.html` hiển thị nó |
| **Item** | Một nhu cầu, hypothesis, metric, decision, evidence hoặc finding. Mỗi item là một file trong `insights/` |
| **Working file** | File làm việc trong `work/` (ví dụ `scope.md`) |
| **Step card** | Một quy trình có sẵn để AI chạy (nằm trong `_skills/`). Bạn không cần gọi tên: nói việc cần làm, AI tự chọn đúng quy trình |
| **Context** | Các file trong `context/` mà AI đọc trước tiên ở mọi bước |

**Các từ bạn nói với AI**

| Bạn nói | AI hiểu là |
|---|---|
| "Đề xuất trước, đừng tạo" | Liệt kê để tôi duyệt, chưa ghi file nào |
| "Ẩn danh" | Thay tên người, tên công ty, số liệu thật bằng tên và số giả trước khi đưa cho AI |
| "assumed" | Con số này chưa ai xác nhận |
| "Draft" / "verified" | Chưa kiểm tra / tôi đã kiểm tra |
| "Proposed" / "accepted" | Quyết định mới đề xuất / đã được chấp nhận |
| "Nối với H1" | Ghi quan hệ về item H1 (ví dụ decision kiểm chứng hypothesis H1) |
| "Tạo lại báo cáo" | Cập nhật lại báo cáo từ các file hiện có, để menu và bảng khớp với thay đổi mới |

Muốn hiểu sâu hơn cách workspace vận hành, nói với AI: *"Giải thích cho tôi cách workspace này vận hành."*
