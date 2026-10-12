# Stages

Mỗi giai đoạn của dự án có một trang trong báo cáo, ở mục **Stages**. **Bạn không viết trang giai đoạn.** Mỗi trang được báo cáo tự ghép từ hai nguồn:

- các file làm việc trong `work/` (cột **Từ work**), kèm trạng thái `status` của file đó (verified, draft...);
- các bảng item lấy từ `insights/` (cột **Bảng item**): opportunities, hypotheses, metrics, decisions, evidence, findings.

Muốn đổi nội dung: sửa file ở `work/` hoặc item ở `insights/`, rồi tạo lại `index.html`. Muốn đổi thứ tự hay thêm một giai đoạn: sửa bảng dưới đây (thứ tự các dòng là thứ tự trong báo cáo).

## Pages

| Id | Page | Giai đoạn | Nội dung | Từ work | Bảng item |
|---|---|---|---|---|---|
| `scope` | Scope | Discover | Business question, outcome, agreement | `scope.md` | |
| `evidence` | Evidence | Discover | Điều đã học từ nguồn, mỗi claim một nguồn | `user-voice-synthesis.md`, `competitor-analysis.md` | |
| `problem-brief` | Problem brief | Define | Opportunity, hypothesis, metric, principle | `problem-brief.md` | opportunities, hypotheses, metrics |
| `develop` | Options, flows, prototype | Develop | Các hướng đã khám phá, decision | `options.md`, `prototype/` | decisions |
| `alignment` | Alignment check | Develop | Principle audit, verdict | `alignment.md` | |
| `findings` | Findings | Deliver | Kết quả test với người dùng | `findings.md` | evidence, findings |
| `handoff` | Handoff and measurement | Deliver | Handoff pack, measurement plan | `handoff.md`, `measurement-plan.md` | |
| `learning` | Learning | Learn | Điều đã học sau launch: metric so với target, dẫn ngược về opportunity | `learning.md` | outcomes |
| `decision-log` | Decision log | Mọi giai đoạn | Mỗi quyết định một dòng, kèm lý do | `insights/case-log.md` | |

## Cách đọc bảng

| Cột | Ý nghĩa |
|---|---|
| **Id** | Tên ngắn, chữ thường, không dấu. Dùng làm địa chỉ trang. |
| **Từ work** | File trong `work/` (viết tên file, ví dụ `scope.md`) hoặc folder có `index.md` (ví dụ `prototype/`). Có thể nhiều file, ngăn bằng dấu phẩy. |
| **Bảng item** | Bảng nào hiện ở trang này: `opportunities`, `hypotheses`, `metrics`, `decisions`, `evidence`, `findings`, hoặc `outcomes` (metric, kết quả đo và opportunity phía sau). Để trống nếu không cần. |

Mỗi file nguồn hiện kèm trạng thái của nó. Một file còn `draft` vẫn hiện, nhưng được gắn nhãn "Bản nháp, chưa kiểm tra" để người đọc biết đó chưa phải điều đã kiểm tra: đổi `status` thành `verified` khi bạn đã kiểm tra xong.
