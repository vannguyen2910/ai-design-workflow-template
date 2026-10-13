---
type: "test-plan"
title: "Kế hoạch usability test không điều phối"
stage: "Deliver"
status: "planned"
summary: "Kế hoạch cho 8 đến 12 người, năm task theo hành trình, đo bằng task success, SEQ và SUS. Chưa chạy."
takeaways:
  - "Task không dùng nhãn giao diện, để không dẫn đường."
  - "Ngưỡng: từ 80% là tốt; dưới 60% là ưu tiên thiết kế lại."
supports:
  - "[[E2]]"
  - "[[M1]]"
  - "[[M2]]"
  - "[[M3]]"
source: "original-docs/12_Unmoderated_Usability_Test_Plan.md"
---
# Test plan

*Deliver stage, before the test.*

> Kế hoạch đầy đủ: `work/original-docs/12_Unmoderated_Usability_Test_Plan.md`. Bản dưới đây là phần cốt lõi. Trạng thái: **chưa chạy**.

## What we are testing
Hypothesis: H1 đến H6 (xem `insights/hypotheses/`). Điều sẽ làm tôi đổi ý: nếu tỷ lệ hoàn thành task dưới 60%, hypothesis tương ứng bị coi là chưa đứng vững và flow đó được ưu tiên thiết kế lại.

## Tasks
*Each task is something the user tries to do, without being told how.*
1. "Bạn đang lên kế hoạch cho một chuyến tới Chiang Mai. Tìm một tip về đồ ăn từ một du khách khác và lưu vào một chuyến đi." (H2, H3)
2. "Bạn đã có một lịch trình thô do một chatbot viết. Đưa nó vào kế hoạch chuyến đi." (H1)
3. "Bạn muốn một gợi ý quán ăn thật từ người sống ở thành phố. Tìm một người địa phương tên Niran và liên hệ." (H4)
4. "Chuyến đi đã kết thúc. Tìm lại bản ghi những gì bạn đã làm." (H5)
5. "Chia sẻ nhật ký chuyến đi với bạn của bạn, chỉ riêng cô ấy, không công khai." (H6)

## Participants
8 đến 12 người, tuyển 12 đến 15 để bù tỷ lệ bỏ dở của test không điều phối. Tiêu chí: đã đi chơi trong 12 tháng, dùng điện thoại, tự hoàn thành một task trực tuyến không cần ai giúp; 18 đến 45 tuổi ưu tiên. Ghi lại sự đồng ý của người tham gia trước phiên.

## Script
Phần giới thiệu bằng văn bản, câu hỏi khởi động, năm task theo thứ tự cố định (theo hành trình: khám phá, lập kế hoạch, kết nối, nhớ lại), một câu hỏi SEQ sau mỗi task, bộ SUS sau task cuối. Câu hỏi hỏi về điều đã xảy ra, không hỏi ý kiến về ý tưởng. Chi tiết: `work/original-docs/12_...`, mục 5 đến 7.

## What we measure
| Metric | Baseline | Target |
|---|---|---|
| Task success (hoàn thành không cần trợ giúp) | chưa có | từ 80% mỗi task; dưới 60% là ưu tiên thiết kế lại |
| Time on task | chưa có | không đặt mục tiêu; so sánh tương đối, đánh dấu giá trị trên 2 lần trung vị |
| Errors (số lần chạm sai) | chưa có | không đặt mục tiêu |
| Satisfaction (System Usability Scale, SUS) | chưa có | từ 68 (trên trung bình); dùng như kiểm tra sức khoẻ chung, không phải ngưỡng đạt |
| First-click accuracy | chưa có | kiểm tra câu hỏi về nhãn điều hướng |
