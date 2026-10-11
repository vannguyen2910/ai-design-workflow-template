# Set Up Your Case

Guide này giúp bạn đặt tên case, hiểu từng folder dùng để làm gì, và biết cách làm việc với AI tool trong folder này.

## Step 1: Name your case

1. Đổi tên folder `my-case` theo case của bạn.
2. Dùng chữ thường, nối bằng dấu gạch ngang, không có dấu cách. Ví dụ: `onboarding-redesign`, `checkout-flow`.
3. Chọn tên mà nhìn vào là biết case nói về gì, vì bạn sẽ thấy nó ở đầu mọi đường dẫn.

Có hai case thì nhân đôi folder `my-case` và đặt tên cho từng bản.

## Step 2: Understand the folders

| Folder hoặc file | Dùng để | Khi nào |
|---|---|---|
| `00-context/` | Thông tin nền về sản phẩm và người dùng. Bạn đưa nó cho AI đọc trước tiên ở mọi bước | Từ tuần 1, bổ sung dần |
| `01-discover/` | Tìm hiểu vấn đề. Mỗi hoạt động một file. `sources/anonymised/` chứa dữ liệu đã ẩn danh, `sources/_raw-private/` chứa dữ liệu gốc | Tuần 2 |
| `02-define/` | `problem-brief.md`: vấn đề đáng giải, thống nhất với product và business | Tuần 3 |
| `03-develop/` | Các hướng giải quyết, alignment check, và `prototype/` | Tuần 4 đến 6 |
| `04-deliver/` | Kế hoạch test, kết quả test, handoff và kế hoạch đo | Tuần 6 và 7 |
| `hub/` | Knowledge Hub: một folder Markdown nối mọi quyết định về nhu cầu của người dùng | Cập nhật mỗi tuần |
| `case-log.md` | Mỗi quyết định một dòng, kèm lý do và chỗ AI đã giúp | Mỗi tuần |

Folder được đánh số để giữ đúng thứ tự, và mỗi hoạt động có một file riêng để AI nhận đúng thứ nó cần.

## Step 3: Fill in the first files

Tuần 1 bạn điền bốn file trong `00-context/` và một file riêng:

1. `product-and-users.md`: sản phẩm là gì, người dùng là ai, bạn biết gì và chưa biết gì.
2. `accessibility-rules.md`: các yêu cầu về accessibility mà thiết kế phải đạt.
3. `data-rules.md`: ba dòng bằng lời của bạn: được đưa gì cho AI, sẽ không đưa gì, dùng công cụ nào cho việc gì.
4. `open-questions.md`: các câu hỏi AI cho là nó cần biết thêm.
5. `_personal/my-direction.md`: hai đến ba dòng về hướng nghề bạn đang nghiêng về. File này là ghi chú riêng nên nằm ngoài `00-context/`, và không đưa cho AI.

Mỗi file có sẵn các dòng gợi ý. Bạn thay phần gợi ý bằng nội dung của mình, và giữ nguyên các tiêu đề.

## Step 4: Work with an AI tool

Folder này được dựng để AI tool tự biết phải làm gì, nhờ bốn thứ:

| Thứ | Là gì |
|---|---|
| `AGENTS.md` | Một file ghi sẵn "luật chơi". AI tool tự đọc nó khi bạn mở folder, nên bạn không phải nhắc lại luật mỗi lần. Nếu tool của bạn đọc file luật dưới tên khác, copy nội dung sang tên đó |
| `workflow/` | Các **step card**: mỗi bước ghi rõ ai làm (AI hay bạn), đọc file nào, ghi vào đâu |
| `01-discover/sources/` | `anonymised/` AI được đọc. `_raw-private/` không bao giờ đưa cho AI và không lên GitHub |
| `hub/` | Mỗi quyết định, giả thuyết, bài kiểm tra là một file. Các bảng tổng hợp do AI dựng lại |

Một lần làm việc với AI trông như sau:

1. **Mở đúng một case folder** làm project trong AI tool. Đừng mở folder gốc, và đừng mở cả `my-case` lẫn `demo-case` cùng lúc, vì dữ liệu của hai case sẽ lẫn vào nhau.
2. **Lưu một mốc trước khi AI ghi file.** Nếu bạn dùng GitHub Desktop, bấm Commit (xem [`03-github-basics.md`](03-github-basics.md)). Nếu không, copy folder case thành một bản `...-backup`. Nhờ vậy AI làm hỏng thì bạn quay lại được.
3. **Nói với tool một câu**, ví dụ: *"Chạy step 5 của `workflow/user-voice-synthesis.md`."* Tool chỉ đọc đúng các file mà step card liệt kê.
4. **Đọc kết quả và tự kiểm tra** ở step tiếp theo. Bản nháp của AI và bản bạn đã sửa nằm ở hai chỗ riêng.
5. **Ghi một dòng vào `case-log.md`:** bạn quyết định gì, vì sao, và AI đã giúp ở đâu.

## Step 5: Use the hub

Hub là nơi bạn trả lời câu hỏi: "Quyết định này dựa trên nhu cầu nào của người dùng?"

- **Mỗi quyết định thiết kế là một file riêng.** Ví dụ quyết định `D2` nằm ở `hub/decisions/D2.md`.
- **Bạn chỉ viết mỗi điều một chỗ.** Quyết định `D2` nói nó kiểm chứng giả thuyết nào; hub tự suy ra chiều ngược lại.
- **Cuối mỗi tuần,** nhờ AI tool chạy `workflow/refresh-hub.md` để dựng lại bảng tổng hợp và danh sách điểm cần xem lại.

Cách hub vận hành nằm ở `hub/how-the-hub-works.md` trong folder case của bạn.

## View markdown files

File `.md` là text thuần, nên mọi trình soạn thảo đều mở được. Để thấy bảng và link hiển thị đẹp, chọn một cách:

| Cách | Làm gì |
|---|---|
| **Obsidian** (miễn phí, khuyên dùng) | Mở cả folder case làm vault. Xem [`05-obsidian.md`](05-obsidian.md) |
| **VS Code** (miễn phí) | Cài từ [code.visualstudio.com](https://code.visualstudio.com), mở cả folder case, bấm vào file `.md`, rồi nhấn `Cmd+Shift+V` (Mac) hoặc `Ctrl+Shift+V` (Windows) để xem bản hiển thị |
| **GitHub** | Nếu bạn đã lưu folder lên repo Private, mở repo trên github.com; Markdown được hiển thị sẵn |
| **Trình duyệt** | Tạo một file báo cáo HTML rồi bấm đúp để mở. Xem [`04-share-your-hub.md`](04-share-your-hub.md) |

Hãy mở **cả folder**, không mở từng file lẻ: các link giữa các trang chỉ bấm được khi cả folder đang mở.

## Make it your own

| Bạn muốn | Cách làm |
|---|---|
| Thêm folder riêng (ghi chú, ảnh, bản ghi âm) | Tạo folder mới cùng cấp với `00-context`, ví dụ `05-notes/` |
| Bỏ một file không dùng | Xoá file đó. Nếu là trang hub, xoá luôn dòng của nó trong bảng Pages ở `hub/README.md`. Nếu là item, nhờ AI chạy lại `workflow/refresh-hub.md` |
| Thêm một trang hub | Copy một trang có sẵn, đổi tên, rồi thêm một dòng vào bảng Pages ở `hub/README.md` |
| Thêm một quyết định hoặc bài kiểm tra | Copy một file trong folder cùng loại, đặt tên theo mã mới (ví dụ `decisions/D4.md`), rồi nhờ AI chạy `workflow/refresh-hub.md` |
| Dùng design system của công ty | Viết `00-context/design-system-notes.md` của bạn và dùng `03-develop/prototype/` làm mẫu |
| Viết file bằng tiếng Việt | Được. Chỉ giữ tên file và tên folder bằng tiếng Anh |

## Keep it safe

- **Ẩn danh trước khi đưa cho AI tool hoặc mang vào lớp.**
- **Không để mật khẩu, dữ liệu cá nhân của người dùng hay số liệu tài chính chưa công bố trong folder này**, kể cả khi repo ở chế độ Private.
- Hub mặc định là riêng tư. Cách cho người khác xem nằm ở [`04-share-your-hub.md`](04-share-your-hub.md).
