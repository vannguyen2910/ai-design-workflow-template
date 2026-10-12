# Set Up Your Case

Guide này giúp bạn đặt tên dự án, hiểu từng folder dùng để làm gì, và biết cách làm việc với AI tool trong folder này.

## Step 1: Name your case

1. Mở Terminal tại folder gốc của workspace và chạy:

   ```
   python3 tools/new-case.py onboarding-redesign
   ```

   Thêm `--title "Onboarding redesign"` nếu muốn tên hiển thị khác với tên folder.
2. Tên folder dùng chữ thường, nối bằng dấu gạch ngang, không có dấu cách. Ví dụ: `onboarding-redesign`, `checkout-flow`. Chọn tên mà nhìn vào là biết case nói về gì, vì bạn sẽ thấy nó ở đầu mọi đường dẫn.
3. Lệnh tạo một folder mới cạnh `my-case`, sạch và sẵn để điền. `my-case` được giữ nguyên làm template.

Có hai case thì chạy lệnh hai lần với hai tên khác nhau.

**Không dùng được Terminal?** Đổi tên folder `my-case` theo case của bạn rồi điền vào đó. Cách này làm mất template gốc, nên hãy giữ một bản ZIP sạch để lấy lại khi cần.

## Step 2: Understand the folders

Folder được đặt tên theo **việc bạn làm** ở đó:

| Folder | Dùng để | Khi nào dùng |
|---|---|---|
| `context/` | **Thông tin nền:** sản phẩm, người dùng, quy tắc dữ liệu, design system. Bạn đưa nó cho AI đọc trước tiên ở mọi bước | Khi khởi động dự án, bổ sung dần |
| `work/` | **File làm việc của từng giai đoạn:** `scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` (Discover), `problem-brief.md` (Define), `options.md`, `alignment.md` (Develop), `test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` (Deliver). Trang giai đoạn ở `stages/` tự ghép từ các file này | Suốt dự án |
| `work/sources/` | `anonymised/` chứa dữ liệu đã ẩn danh, `_raw-private/` chứa dữ liệu gốc | Discover |
| `work/prototype/` | Code prototype | Giai đoạn Develop |
| `stages/` | **Mỗi giai đoạn một trang**, tự dựng từ `work/` và `insights/` theo bảng Pages ở `stages/README.md`; bạn không viết ở đây | Chỉ sửa bảng khi đổi thứ tự hoặc thêm giai đoạn |
| `insights/` | **Các item nối với nhau:** nhu cầu, hypothesis, decision, evidence, finding, metric; mỗi item một file trong folder loại của nó | Cập nhật khi có thay đổi |
| `standards/` | **Tra cứu:** gates, principle checks, severity levels, case log. Thả file `.md` mới vào đây là tự hiện ở báo cáo | Khi cần xem lại |
| `_skills/` | Step card (các bước làm việc với AI) và script tạo báo cáo `index.html` | Khi chạy một bước; hiếm khi mở tay |
| `_personal/` | Ghi chú riêng, không đưa cho AI | Khi bạn muốn |

Trang `README.md` ở gốc folder dự án có bảng "Bạn muốn làm gì?" với câu nói mẫu cho từng việc, nên khi chưa biết bắt đầu từ đâu, hãy đọc nó.

## Step 3: Fill in the first files

Khi khởi động dự án, bạn điền bốn file trong `context/` và một file riêng:

1. `context/product-and-users.md`: sản phẩm là gì, người dùng là ai, bạn biết gì và chưa biết gì.
2. `context/accessibility-rules.md`: các yêu cầu về accessibility mà thiết kế phải đạt.
3. `context/data-rules.md`: ba dòng bằng lời của bạn: được đưa gì cho AI, sẽ không đưa gì, dùng công cụ nào cho việc gì.
4. `context/open-questions.md`: các câu hỏi AI cho là nó cần biết thêm.
5. `_personal/my-direction.md`: hai đến ba dòng về hướng nghề bạn đang nghiêng về. File này là ghi chú riêng nên nằm ngoài các folder làm việc, và không đưa cho AI.

Mỗi file có sẵn các dòng gợi ý. Bạn thay phần gợi ý bằng nội dung của mình, và giữ nguyên các tiêu đề.

## Step 4: Work with an AI tool

Folder này được dựng để AI tool tự biết phải làm gì, nhờ bốn thứ:

| Thứ | Là gì |
|---|---|
| `AGENTS.md` | Một file ghi sẵn "luật chơi". AI tool tự đọc nó khi bạn mở folder, nên bạn không phải nhắc lại luật mỗi lần. Nếu tool của bạn đọc file luật dưới tên khác, copy nội dung sang tên đó |
| `_skills/*.md` | Các **step card**: mỗi bước ghi rõ ai làm (AI hay bạn), đọc file nào, ghi vào đâu |
| `work/sources/` | `anonymised/` AI được đọc. `_raw-private/` không bao giờ đưa cho AI và không lên GitHub |
| `insights/` | Mỗi decision, hypothesis, evidence là một file. Các bảng tổng hợp do AI dựng lại |

Một lần làm việc với AI trông như sau:

1. **Mở đúng một case folder** làm project trong AI tool. Đừng mở folder gốc, và đừng mở cả `my-case` lẫn `demo-case` cùng lúc, vì dữ liệu của hai case sẽ lẫn vào nhau.
2. **Lưu một mốc trước khi AI ghi file.** Nếu bạn dùng GitHub Desktop, bấm Commit (xem [`03-github-basics.md`](03-github-basics.md)). Nếu không, copy folder case thành một bản `...-backup`. Nhờ vậy AI làm hỏng thì bạn quay lại được.
3. **Nói với tool một câu**, ví dụ: *"Chạy step 5 của `_skills/user-voice-synthesis.md`."* Tool chỉ đọc đúng các file mà step card liệt kê.
4. **Đọc kết quả và tự kiểm tra** ở step tiếp theo. Bản nháp của AI và bản bạn đã sửa nằm ở hai chỗ riêng.
5. **Ghi một dòng vào `insights/case-log.md`:** bạn quyết định gì, vì sao, và AI đã giúp ở đâu.

## Step 5: Use the hub

Hub là nơi bạn trả lời câu hỏi: "Decision này dựa trên nhu cầu nào của người dùng?"

- **Mỗi design decision là một file riêng.** Ví dụ decision `D2` nằm ở `insights/decisions/D2.md`.
- **Bạn chỉ viết mỗi điều một chỗ.** Decision `D2` nói nó kiểm chứng hypothesis nào; hub tự suy ra chiều ngược lại.
- **Sau mỗi lần cập nhật,** chạy `python3 _skills/export-hub.py` (hoặc nhờ AI tool chạy) để báo cáo dựng lại bảng tổng hợp và warnings.

Cách hub vận hành nằm ở `_skills/how-the-hub-works.md` trong folder case của bạn.

## View markdown files

File `.md` là text thuần, nên **công cụ nào mở được folder đều dùng được**. Chọn theo việc bạn cần:

| Công cụ | Làm gì |
|---|---|
| **AI coding tool** | Mở cả folder case làm project. Tool đọc `AGENTS.md`, đọc và sửa file trực tiếp, và chạy các step card. Đây là cách bạn làm việc với AI |
| **Obsidian** (miễn phí) | Mở cả folder case làm vault. Thêm Graph view, Backlinks và bảng theo loại item. Xem [`05-obsidian.md`](05-obsidian.md) |
| **VS Code** (miễn phí) | Cài từ [code.visualstudio.com](https://code.visualstudio.com), mở cả folder case, bấm vào file `.md`, rồi nhấn `Cmd+Shift+V` (Mac) hoặc `Ctrl+Shift+V` (Windows) để xem bản hiển thị |
| **GitHub** | Nếu bạn đã lưu folder lên repo Private, mở repo trên github.com; Markdown được hiển thị sẵn |
| **Trình duyệt** (không cài gì) | Bấm đúp file `index.html` ở gốc case folder: đó là trang chủ của hub. Sau khi sửa hub, nhờ AI tool chạy `python3 _skills/export-hub.py` để tạo lại. Xem [`04-share-your-hub.md`](04-share-your-hub.md) |

Hãy mở **cả folder**, không mở từng file lẻ: các link giữa các trang chỉ bấm được khi cả folder đang mở.

**Lưu ý về liên kết:** các item nối với nhau bằng dấu `[[ ]]` trong khối properties ở đầu file. Chỉ Obsidian biến chúng thành link bấm được. Các công cụ khác vẫn đọc và sửa được vì đó chỉ là text, và AI coding tool hiểu chúng bình thường.

## Make it your own

| Bạn muốn | Cách làm |
|---|---|
| Thêm folder riêng (ghi chú, ảnh, bản ghi âm) | Tạo folder mới cùng cấp với `work/`, ví dụ `notes/` |
| Bỏ một file không dùng | Xoá file đó. Nếu file đó được một trang ở `stages/` dùng, xoá nó khỏi cột Từ work trong bảng Pages ở `stages/README.md`. Nếu là item, chạy lại `python3 _skills/export-hub.py` |
| Thêm một trang giai đoạn | Thêm một dòng vào bảng Pages ở `stages/README.md`: đặt Id, chọn file ở cột Từ work và bảng item muốn hiện. Không cần viết file mới |
| Thêm một item (nhu cầu, hypothesis, decision...) | Chạy `python3 _skills/new-item.py` trong folder dự án: lệnh hỏi từng câu, chọn mã tiếp theo và nối quan hệ giúp bạn |
| Thêm một tài liệu (phân tích đối thủ, persona, flow, prototype...) | Copy một template trong `work/_templates/` ra `work/`, hoặc tạo folder và thả ảnh, PDF, HTML vào. Xem `work/README.md` |
| Thêm một decision hoặc test | Chạy `python3 _skills/new-item.py D` (hoặc `E`): lệnh chọn mã mới và nối quan hệ giúp bạn |
| Dùng design system của công ty | Viết `context/design-system-notes.md` của bạn và dùng `work/prototype/` làm mẫu |
| Viết file bằng tiếng Việt | Được. Chỉ giữ tên file và tên folder bằng tiếng Anh |

## Keep it safe

- **Ẩn danh trước khi đưa cho AI tool hoặc chia sẻ ra ngoài.**
- **Không để mật khẩu, dữ liệu cá nhân của người dùng hay số liệu tài chính chưa công bố trong folder này**, kể cả khi repo ở chế độ Private.
- Hub mặc định là riêng tư. Cách cho người khác xem nằm ở [`04-share-your-hub.md`](04-share-your-hub.md).
