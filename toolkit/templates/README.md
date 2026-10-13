# Templates

Mẫu rỗng cho tài liệu làm việc, dùng chung cho mọi case trong workspace này. **Không điền trực tiếp ở đây.**

## Cách dùng

1. Copy một file vào `work/` của case của bạn, đổi tên cho dễ nhận ra (ví dụ `work/pestel-analysis.md`).
2. Điền nội dung. Đổi `status` thành `verified` khi bạn đã kiểm tra.
3. Chạy lại báo cáo; tài liệu hiện ở mục **Work**.

Hoặc nhờ AI tool: *"Tạo tài liệu research plan trong `work/` từ mẫu `toolkit/templates/research-plan.md`."*

> Mẫu cho **item** (nhu cầu, hypothesis, decision, evidence, finding, metric) nằm riêng ở `insights/_templates/` trong từng case, vì `new-item.py` dùng chúng để tạo item.

## Danh sách

| Giai đoạn | Template | Dùng để |
|---|---|---|
| Discover | `research-plan.md` | Lên kế hoạch nghiên cứu: câu hỏi, phương pháp, người tham gia, timeline |
| Discover | `interview-guide.md` | Bộ câu hỏi và kịch bản một buổi phỏng vấn |
| Discover | `interview-synthesis.md` | Tổng hợp nhiều cuộc phỏng vấn thành chủ đề |
| Discover | `survey-results.md` | Kết quả khảo sát |
| Discover | `competitor-analysis.md` | So sánh đối thủ |
| Discover | `pestel-analysis.md` | Bối cảnh bên ngoài: chính trị, kinh tế, xã hội, công nghệ, môi trường, pháp lý |
| Discover | `assumptions-map.md` | Liệt kê và xếp hạng giả định cần kiểm tra |
| Discover | `heuristic-evaluation.md` | Đánh giá sản phẩm với 10 heuristic và thang severity |
| Discover | `stakeholder-map.md` | Ai quyết định, ai bị ảnh hưởng, họ cần gì |
| Discover | `persona.md` | Persona dựa trên bằng chứng |
| Define | `problem-brief.md` | Một trang: vấn đề, bằng chứng, outcome, phạm vi |
| Define | `journey-map.md` | Hành trình hiện tại, điểm đau, khoảnh khắc quan trọng |
| Define | `opportunity-solution-tree.md` | Nối outcome với opportunity, giải pháp và giả định |
| Define | `prioritization.md` | Xếp hạng opportunity theo impact, confidence, effort |
| Develop | `options.md` | So sánh ít nhất ba hướng giải pháp |
| Develop | `user-flow.md`, `ia-sitemap.md`, `prototype.md` | Flow, sơ đồ trang, prototype |
| Deliver | `usability-test-script.md` | Kịch bản chạy buổi usability test |
| Deliver | `test-report.md` | Báo cáo kết quả test |
| Deliver | `measurement-plan.md` | Cách đo kết quả sau phát hành |
| Mọi giai đoạn | `generic.md` | Loại tài liệu khác |
