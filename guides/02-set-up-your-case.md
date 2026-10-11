# Set Up Your Case

Guide này giúp bạn đặt tên dự án, hiểu từng folder dùng để làm gì, và biết cách làm việc với AI tool trong folder này.

## Step 1: Name your case

1. Mở Terminal tại folder gốc của workspace và chạy:

   ```
   python3 tools/new-case.py onboarding-redesign
   ```

   Thêm `--title "Onboarding redesign"` nếu muốn tên hiển thị khác với tên folder.
2. Tên folder dùng chữ thường, nối bằng dấu gạch ngang, không có dấu cách. Ví dụ: `onboarding-redesign`, `checkout-flow`. Chọn tên mà nhìn vào là biết case nói về gì, vì bạn sẽ thấy nó ở đầu mọi đường dẫn.
3. Lệnh tạo một folder mới cạnh `my-case`, đã xoá sẵn các item `[EXAMPLE]`. `my-case` được giữ nguyên làm template.

Có hai case thì chạy lệnh hai lần với hai tên khác nhau.

**Không dùng được Terminal?** Đổi tên folder `my-case` theo case của bạn rồi tự xoá các item `[EXAMPLE]` trong `hub/`. Cách này làm mất template gốc, nên hãy giữ một bản ZIP sạch để lấy lại khi cần.

## Step 2: Understand the folders

Folder được đặt tên theo **việc bạn làm** ở đó:

| Folder | Dùng để | Khi nào dùng |
|---|---|---|
| `context/` | **Thông tin nền:** sản phẩm, người dùng, quy tắc dữ liệu, design system. Bạn đưa nó cho AI đọc trước tiên ở mọi bước | Khi khởi động dự án, bổ sung dần |
| `work/discover/` | Tìm hiểu vấn đề: scope, tổng hợp tiếng nói người dùng, phân tích đối thủ | Giai đoạn Discover |
| `work/define/` | `problem-brief.md`: vấn đề đáng giải, thống nhất với product và business | Giai đoạn Define |
| `work/develop/` | Các hướng giải quyết và alignment check | Giai đoạn Develop |
| `work/deliver/` | Kế hoạch test, kết quả test, handoff và kế hoạch đo | Giai đoạn Deliver |
| `work/sources/` | `anonymised/` chứa dữ liệu đã ẩn danh, `_raw-private/` chứa dữ liệu gốc | Discover |
| `work/prototype/` | Code prototype | Giai đoạn Develop |
| `hub/` | **Bản ghi quyết định:** mỗi item (nhu cầu, hypothesis, decision, evidence, metric) một file, nối về user need | Cập nhật khi có thay đổi |
| `reference/` | **Tra cứu:** gates, principle checks, severity levels, case log. Thả file `.md` mới vào đây là tự hiện ở báo cáo | Khi cần xem lại |
| `steps/` | Các bước làm việc với AI (step card) | Khi chạy một bước |
| `_scripts/` | Script tạo báo cáo `index.html` | Hiếm khi mở tay |
| `_personal/` | Ghi chú riêng, không đưa cho AI | Khi bạn muốn |

Trang `README.md` ở gốc folder dự án có bảng "Tôi muốn... mở..." cho từng việc, nên khi chưa biết bắt đầu từ đâu, hãy đọc nó.

## Step 4: Work with an AI tool

Folder này được dựng để AI tool tự biết phải làm gì, nhờ bốn thứ:

| Thứ | Là gì |
|---|---|
| `AGENTS.md` | Một file ghi sẵn "luật chơi". AI tool tự đọc nó khi bạn mở folder, nên bạn không phải nhắc lại luật mỗi lần. Nếu tool của bạn đọc file luật dưới tên khác, copy nội dung sang tên đó |
| `steps/*.md` | Các **step card**: mỗi bước ghi rõ ai làm (AI hay bạn), đọc file nào, ghi vào đâu |
| `work/sources/` | `anonymised/` AI được đọc. `_raw-private/` không bao giờ đưa cho AI và không lên GitHub |
| `hub/` | Mỗi decision, hypothesis, test là một file. Các bảng tổng hợp do AI dựng lại |

Một lần làm việc với AI trông như sau:

1. **Mở đúng một case folder** làm project trong AI tool. Đừng mở folder gốc, và đừng mở cả `my-case` lẫn `demo-case` cùng lúc, vì dữ liệu của hai case sẽ lẫn vào nhau.
2. **Lưu một mốc trước khi AI ghi file.** Nếu bạn dùng GitHub Desktop, bấm Commit (xem [`03-github-basics.md`](03-github-basics.md)). Nếu không, copy folder case thành một bản `...-backup`. Nhờ vậy AI làm hỏng thì bạn quay lại được.
3. **Nói với tool một câu**, ví dụ: *"Chạy step 5 của `steps/user-voice-synthesis.md`."* Tool chỉ đọc đúng các file mà step card liệt kê.
4. **Đọc kết quả và tự kiểm tra** ở step tiếp theo. Bản nháp của AI và bản bạn đã sửa nằm ở hai chỗ riêng.
5. **Ghi một dòng vào `reference/case-log.md`:** bạn quyết định gì, vì sao, và AI đã giúp ở đâu.

## Step 5: Use the hub

Hub là nơi bạn trả lời câu hỏi: "Decision này dựa trên nhu cầu nào của người dùng?"

- **Mỗi design decision là một file riêng.** Ví dụ decision `D2` nằm ở `hub/decisions/D2.md`.
- **Bạn chỉ viết mỗi điều một chỗ.** Decision `D2` nói nó kiểm chứng hypothesis nào; hub tự suy ra chiều ngược lại.
- **Sau mỗi lần cập nhật,** nhờ AI tool chạy `steps/refresh-hub.md` để dựng lại bảng tổng hợp và danh sách warnings.

Cách hub vận hành nằm ở `hub/how-the-hub-works.md` trong folder case của bạn.

## View markdown files

File `.md` là text thuần, nên **công cụ nào mở được folder đều dùng được**. Chọn theo việc bạn cần:

| Công cụ | Làm gì |
|---|---|
| **AI coding tool** | Mở cả folder case làm project. Tool đọc `AGENTS.md`, đọc và sửa file trực tiếp, và chạy các step card. Đây là cách bạn làm việc với AI |
| **Obsidian** (miễn phí) | Mở cả folder case làm vault. Thêm Graph view, Backlinks và bảng theo loại item. Xem [`05-obsidian.md`](05-obsidian.md) |
| **VS Code** (miễn phí) | Cài từ [code.visualstudio.com](https://code.visualstudio.com), mở cả folder case, bấm vào file `.md`, rồi nhấn `Cmd+Shift+V` (Mac) hoặc `Ctrl+Shift+V` (Windows) để xem bản hiển thị |
| **GitHub** | Nếu bạn đã lưu folder lên repo Private, mở repo trên github.com; Markdown được hiển thị sẵn |
| **Trình duyệt** (không cài gì) | Bấm đúp file `index.html` ở gốc case folder: đó là trang chủ của hub. Sau khi sửa hub, nhờ AI tool chạy `python3 _scripts/export-hub.py` để tạo lại. Xem [`04-share-your-hub.md`](04-share-your-hub.md) |

Hãy mở **cả folder**, không mở từng file lẻ: các link giữa các trang chỉ bấm được khi cả folder đang mở.

**Lưu ý về liên kết:** các item nối với nhau bằng dấu `[[ ]]` trong khối properties ở đầu file. Chỉ Obsidian biến chúng thành link bấm được. Các công cụ khác vẫn đọc và sửa được vì đó chỉ là text, và AI coding tool hiểu chúng bình thường.

## Make it your own

| Bạn muốn | Cách làm |
|---|---|
| Thêm folder riêng (ghi chú, ảnh, bản ghi âm) | Tạo folder mới cùng cấp với `work/`, ví dụ `notes/` |
| Bỏ một file không dùng | Xoá file đó. Nếu là trang hub, xoá luôn dòng của nó trong bảng Pages ở `hub/README.md`. Nếu là item, nhờ AI chạy lại `steps/refresh-hub.md` |
| Thêm một trang hub | Copy một trang có sẵn, đổi tên, rồi thêm một dòng vào bảng Pages ở `hub/README.md` |
| Thêm một tài liệu (phân tích đối thủ, persona, flow, prototype...) | Copy một template trong `hub/artifacts/_templates/` ra `hub/artifacts/`, hoặc tạo folder và thả ảnh, PDF, HTML vào. Xem `hub/artifacts/README.md` |
| Thêm một decision hoặc test | Copy một file cùng loại trong `hub/`, đặt tên theo mã mới (ví dụ `D4.md`), rồi nhờ AI chạy `steps/refresh-hub.md` |
| Dùng design system của công ty | Viết `context/design-system-notes.md` của bạn và dùng `work/prototype/` làm mẫu |
| Viết file bằng tiếng Việt | Được. Chỉ giữ tên file và tên folder bằng tiếng Anh |

## Keep it safe

- **Ẩn danh trước khi đưa cho AI tool hoặc chia sẻ ra ngoài.**
- **Không để mật khẩu, dữ liệu cá nhân của người dùng hay số liệu tài chính chưa công bố trong folder này**, kể cả khi repo ở chế độ Private.
- Hub mặc định là riêng tư. Cách cho người khác xem nằm ở [`04-share-your-hub.md`](04-share-your-hub.md).
