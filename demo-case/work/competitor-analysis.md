---
type: "competitor-analysis"
title: "Phân tích đối thủ và SWOT"
stage: "Discover"
status: "verified"
summary: "Năm đối thủ cùng AI chat tool, so sánh trên mười tiêu chí: không ai phủ cả ba trụ khám phá, kết nối và nhật ký, miễn phí."
takeaways:
  - "Không có đối thủ nào phủ cả ba trụ cùng lúc và miễn phí."
  - "TripAdvisor và Google Maps sở hữu khám phá nhưng không có kết nối hay nhật ký; Polarsteps làm tốt nhật ký nhưng không có khám phá."
  - "AI chat tool vừa là đối thủ vừa là cơ hội: lịch trình chúng sinh ra không có nơi để đi tiếp."
supports:
  - "[[O1]]"
  - "[[O2]]"
  - "[[O4]]"
  - "[[D3]]"
  - "[[D5]]"
media:
  - "sources/anonymised/03_Competitor_Research_SWOT.md"
---
# Competitor analysis

*Working file cho competitor flow. Các nguồn bạn đã lưu nằm trong `sources/anonymised/`.*

## Scope
- Decision mà phân tích này phục vụ: Travel Buddy nên đứng ở đâu so với các nền tảng đang có, và không nên cạnh tranh trực tiếp ở đâu
- Các tiêu chí quan trọng (tối đa 6): bao phủ ba trụ (khám phá, kết nối, lập kế hoạch và nhật ký); miễn phí; riêng tư; nội dung có đáng tin không; hoạt động offline; đầu ra có cấu trúc và lưu lại được
- Điều tôi đã tin: không nền tảng nào phủ cả ba trụ (RH1, RH3)

## Competitors
Năm đối thủ, theo vai trò trong hành trình của du khách:

| Đối thủ | Vai trò | Trụ bị chạm |
|---|---|---|
| TripAdvisor | Khám phá bằng review của người lạ | Discover |
| Google Maps | Khám phá và điều hướng | Discover |
| Foursquare | Tip theo ngữ cảnh | Discover |
| Polarsteps | Nhật ký chuyến đi, chia sẻ | Journal, Share |
| Airbnb Experiences | Kết nối với người địa phương (có phí) | Connect |
| *AI chat tool* (thêm sau phỏng vấn P1) | Soạn lịch trình; kết quả không lưu có cấu trúc | Plan |

## Evidence (AI draft)
*Không có.* Dự án gốc được làm trước khi có quy trình AI-assisted này, nên không có bản nháp của AI để so sánh với bản đã kiểm tra, và không tính được tỷ lệ lỗi.

## Evidence (verified)
Nguồn: `sources/anonymised/03_Competitor_Research_SWOT.md`, mục 3.4. Ký hiệu: có = bao phủ tốt, một phần, không.

| Tiêu chí | TripAdvisor | Google Maps | Foursquare | Polarsteps | Airbnb Exp. | AI chat tool |
|---|---|---|---|---|---|---|
| Khám phá địa phương | có | có | có | không | một phần | một phần |
| Tip chọn lọc, cá nhân | không | không | có | không | một phần | không |
| Kết nối với người địa phương | không | không | một phần | không | có | không |
| Lập kế hoạch chuyến đi | một phần | một phần | không | không | không | một phần |
| Nhật ký chuyến đi | không | không | một phần | có | không | không |
| Chia sẻ | không | không | một phần | có | không | không |
| Dùng được offline | không | có | không | có | không | không |
| Miễn phí | có | có | có | có | không | có |
| Thiết kế ưu tiên riêng tư | không | không | không | có | một phần | không |
| Đầu ra có cấu trúc, lưu lại | một phần | một phần | không | có | không | không |

## Patterns
- Không có đối thủ nào phủ cả ba trụ (khám phá, kết nối, nhật ký) cùng lúc, và miễn phí.
- TripAdvisor và Google Maps sở hữu khám phá nhưng không có kết nối hay nhật ký. Polarsteps làm tốt nhật ký nhưng không có khám phá. Airbnb Experiences có kết nối nhưng qua paywall. Foursquare chứng minh tip theo ngữ cảnh tốt hơn điểm sao, rồi rời thị trường người dùng cuối.
- Khoảng trống: một nền tảng phục vụ du khách theo thời gian thực, trên cả ba trụ, miễn phí.
- Phản biện: Google có hạ tầng để sao chép bất kỳ tính năng nào ở quy mô lớn.

## Insights + decision
1. **Khám phá bằng người thật, không bằng điểm sao.** Hỗ trợ: TripAdvisor bị mất lòng tin vì review giả; Foursquare cho thấy tip theo ngữ cảnh hiệu quả hơn.
2. **Kết nối phải phi giao dịch.** Hỗ trợ: sự chân thực là động lực chính của trải nghiệm tốt trên Airbnb Experiences, nhưng nó nằm sau paywall.
3. **Nhật ký phải tự động, riêng tư mặc định.** Hỗ trợ: Polarsteps tăng trưởng nhờ nhật ký ít công sức và thiết kế ưu tiên riêng tư.
4. **AI chat tool vừa là đối thủ, vừa là cơ hội.** Chúng sinh ra lịch trình dạng chữ không có nơi để đi tiếp; nhập lịch trình AI vào Travel Buddy biến nó thành điểm vào (SP-P6).

**Decision cho câu hỏi ở Scope:** Travel Buddy không nên cạnh tranh trực tiếp về dữ liệu bản đồ hay khối lượng review; nên đứng ở chỗ không ai phủ: tip từ người thật có danh tính, kết nối phi giao dịch, và lập kế hoạch cùng nhật ký trong một nơi, miễn phí.

**Giới hạn của phân tích này:** phân tích dựa trên nguồn công khai, chưa kiểm tra bằng người dùng thật; chỉ cho thấy đối thủ **làm gì**, không cho thấy vì sao người dùng chọn họ.
