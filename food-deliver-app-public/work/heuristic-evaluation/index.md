---
type: "heuristic-evaluation"
title: "Heuristic evaluation of the current experience"
stage: "Discover"
status: "draft"
summary: "Screen-by-screen check of the current Grab food delivery experience (29 screens, three journeys) against Nielsen's 10 heuristics, with a 0 to 4 severity for each problem. The findings are an AI draft from the screenshots only and still need the owner's check."
supports: []
embed: true
media:
  - "heuristic-whiteboard.html"
---

# Heuristic evaluation of the current experience

Grab food delivery, Vietnam · iPhone · app v33437965 · English interface · walk-through of 23 Nov 2026.

## 1. What this is

A first pass at validating the current experience of the app. Every screen of the three journeys is checked against Nielsen's 10 usability heuristics, and every problem is rated from 0 (not a problem) to 4 (catastrophe). Screen references such as J1 · 01 are the same as in the user flows.

**The whiteboard** on this page draws the same findings on the screens, one sticky note and one pin per finding. Use the Journey list to show one journey at a time. Open it in a normal browser for sharp screenshots.

**How it was made:** every screenshot was looked at one by one and checked against the Figma overview board. The result was also compared with the possible breakdowns written in the three flow diagrams.

## 2. Summary

| Severity | Count | What it means here |
|---|---|---|
| 4 Catastrophe | 0 | No screen blocks the main task by itself in the screenshots |
| 3 Major | 5 | Price shown as free but charged, fees that appear late, an expired-card message with no fix, a countdown sheet that covers the tracking screen, help that is split over four places |
| 2 Minor | 23 | Crowded screens, hidden or truncated information, unclear labels |
| 1 Cosmetic | 2 | Small inconsistencies |

## 3. Findings

### Journey 1: Find and order

| Tag | Screen | Where on the screen | What the user sees | Principle | Sev | Why this level |
|---|---|---|---|---|---|---|
| UX-01 | J1 · 01 Home | Service grid, bottom tab bar, floating bus button | About ten service icons in two rows plus a carousel (labels cut at the right edge: "Mal", "GrabCo…"), a rating card, two ad cards, red dots and a "5" badge on three tabs, and a floating bus button laid over an ad card | Aesthetic and minimalist design | 2 | Every user lands here. Food is still easy to see (top left), so it is a slowdown, not a block |
| UX-02 | J1 · 02 Food section | Top banner, bottom tab bar, section titles | A promo banner fills the top third before any category. The bottom tabs change from Home, Moments, Payment, Activity, Messages to Discover, Near Me, Offers, Order Again, Cart, with no Home tab. "Near Me" is both a tile and a tab. The same kind of carousel is called "Order Now" on Home and "Buy Now" here | Consistency and standards | 2 | Users must re-learn the navigation inside one app |
| UX-03 | J1 · 01 and J1 · 02 | Search field | The placeholder is "Search food" on Home and "What shall we deliver?" in the food section | Consistency and standards | 1 | Same job, two wordings |
| UX-04 | J1 · 02, J1 · 03, J1 · 04 | "Deliver now / Home ▾" at the top; the "Current location / Home" row | The delivery address and time sit in the smallest text at the top. In the address screen the row "Current location" carries the sub-label "Home", so it is not clear whether this is the GPS position or a saved address. The ⋮ menu on that row has no label. The keyboard covers most of the list | Match between system and the real world; Visibility of system status | 2 | A wrong address is costly, and nothing makes the user confirm it (breakdown 2 is confirmed) |
| UX-05 | J1 · 04, J1 · 06 | Filter chip row under the search | The chip "Under 18.000đ" has a scooter icon and no label saying it is the delivery fee. The row is clipped on the right, so the last chip cannot be read | Match between system and the real world; Recognition rather than recall | 2 | Users may read it as a food price limit |
| UX-06 | J1 · 04 | Voucher chip and restaurant names | "Min. spend 100.00…" is cut off, so the amount cannot be read. Restaurant names are cut ("Tiệm Nước Mát Vị Sâm - 337…") | Aesthetic and minimalist design; Recognition rather than recall | 2 | The cut part is exactly the information needed to decide |
| UX-07 | J1 · 06 Results | Small "Ad" tag left of the name; "Showing results in Delivery ▾" | The first two results for "Matcha" are both ads. The tag is small and grey. The search scope (Delivery) is a plain text dropdown | Match between system and the real world; Aesthetic and minimalist design | 2 | Breakdown 3 is confirmed. Users may take paid listings as the best match |
| UX-08 | J1 · 06, J1 · 07 | Fee line "Free ~~10.000đ~~ · From 17 mins" with the orange GrabUnlimited icon | The restaurant is shown as free delivery. At checkout (J2 · 01) the same order has "Delivery and applicable fees 17.000". The same page also offers "Join GrabUnlimited", which suggests the free price is the member price | Visibility of system status; Match between system and the real world | 3 | Most users see this, and it moves the price at the decisive moment. *To confirm: whether your account is a GrabUnlimited member* |
| UX-09 | J1 · 07, J1 · 08, J1 · 11 | Floating red pill ("GrabMore ⊕", "Two restaurants, one delivery fee") | The pill sits over the "For You" title (J1 · 07), over a dish name (J1 · 08) and over the "+" button of a dish (J1 · 11) | Aesthetic and minimalist design | 2 | It hides content and a button the user may want to tap, on every menu screen |
| UX-10 | J1 · 07, J1 · 08 | Chips and promo cards under the header; the "Today's Offer ▾" dropdown | Before any menu item the page shows Group Order, Order for Later, Menu language (cut off), three promo cards, Your Last Order, Today's Offer and For You. Categories are hidden in one dropdown, not shown as tabs | Aesthetic and minimalist design; Recognition rather than recall | 2 | Breakdown 5 is confirmed. A specific item is harder to find |
| UX-11 | J1 · 09, J1 · 10 Item detail and options | Option groups and their tags | "Optional, max 1" is shown with checkboxes, not radio buttons. When one option is ticked the others turn pale grey, so a change needs an untick first. The size group is tagged "Optional" but "Ly 500ml" is already ticked. Group names are Vietnamese in an English screen ("Loại Kem", "Chọn thêm 'Trà Đá, Ly đá'") | Consistency and standards; Error prevention; Match between system and the real world | 2 | Breakdown 4 is partly confirmed: every group captured is tagged Optional, so a required group was not seen |
| UX-12 | J1 · 09 | Grey italic line under the description | "Thông tin sản phẩm này được tạo bởi AI." (the product text was made by AI) is small, pale and only in Vietnamese | Match between system and the real world | 1 | The disclosure is there but easy to miss |
| UX-13 | J1 · 11 Basket → J2 · 01 Summary | Basket bar "Basket • 1 Item 47.000đ"; the fee lines at checkout | The basket shows 47.000đ. The next screen adds "Delivery and applicable fees" 17.000 and "Small order fee" 3.000, so the total is 67.000đ, about 42% above the basket. The reason and the threshold of the small order fee are not shown before this step | Visibility of system status | 3 | Every user meets it, and it is the moment of payment, when a surprise costs the most trust |

### Journey 2: Check out and pay

| Tag | Screen | Where on the screen | What the user sees | Principle | Sev | Why this level |
|---|---|---|---|---|---|---|
| UX-14 | J2 · 01 Order summary | Cross-sell block and its red button; the banner under the fees | A large "Two restaurants, one delivery fee" block with a dark red "See more options" button sits between the fees and the green "Place order". A GrabUnlimited banner follows. Items, promotions, fees and savings are in one long screen | Aesthetic and minimalist design | 2 | Breakdown 1 is confirmed. The red button pulls a user who is ready to pay back to browsing |
| UX-15 | J2 · 02, J2 · 03 Delivery options | Option cards, "VIP upgrade (12 remaining)", (i) icons | Priority (17 mins) and Standard (24 mins) both cost 12.000, and Standard is the pre-selected one. "VIP upgrade (12 remaining)" does not say 12 of what. "With On-Time Promise" is not explained. The (i) icons are small. "Order for later" is styled like a speed option but has no time or price | Match between system and the real world; Help and documentation | 2 | Breakdown 2 is confirmed. A faster option for the same price is not the default |
| UX-16 | J2 · 02, J2 · 06 | "Use offers and more" row; GrabCoins toggle | The row that leads to vouchers and the code field is labelled "Save VND3.000 using points". The GrabCoins toggle (90 coins) is half hidden behind the sticky total bar | Match between system and the real world; Aesthetic and minimalist design | 2 | A user looking for a voucher may not tap a row about points |
| UX-17 | J2 · 04 Payment methods | Grey box at the top; the grey radio at the end of the linked list | "Your linked card has expired. Visit Help Centre" does not say which card, and the only action takes the user out of the flow. The expired card itself shows only as a grey, unselectable radio | Help users recognise, diagnose and recover from errors; Visibility of system status | 3 | Breakdown 3 is confirmed. The user must leave the payment step to fix a payment problem. *To test: can the expired card still be the default?* |
| UX-18 | J2 · 04 | "Swipe left to set your default"; the Linked Methods list | Setting a default is a hidden swipe, while the same list already has radio buttons. It is not clear what a radio tap does (this order or the default). Cash and MoMo sit under "Linked Methods" | Recognition rather than recall; Consistency and standards; Match between system and the real world | 2 | Two ways to do one thing, one of them invisible |
| UX-19 | J2 · 05 Add card | Grey paragraph under "Your card details will be saved securely" | "Your card may be charged to make sure it's valid" is small grey text and does not say how much. The reassurance line comes first and the money line second | Error prevention; Visibility of system status | 2 | Breakdown 4 is confirmed. It may stop a user before they add a card |
| UX-20 | J2 · 07 Offers | Whole list; the field at the top | Of the 10 rows visible, 8 are greyed out ("Spend 172.500đ more to enjoy this offer" on an order of 46.500đ). "Enter promo or gift code here" looks like a search field (magnifier icon). "Use GrabGifts: Have a gift code?" repeats it right below | Aesthetic and minimalist design; Match between system and the real world | 2 | Breakdown 5 is confirmed. It is hard to see what can be used now |

### Journey 3: Track and resolve

| Tag | Screen | Where on the screen | What the user sees | Principle | Sev | Why this level |
|---|---|---|---|---|---|---|
| UX-21 | J3 · 01 to J3 · 06 | Red bottom sheet "GrabMore and save on delivery" | A sheet with a countdown covers the lower part of every tracking screen. The timer runs in real time (19:53 at 15:55, 12:42 at 16:02, 03:20 at 16:11). It cuts the order total ("₫67." in J3 · 01). Only a drag handle is visible, no close button | Aesthetic and minimalist design; User control and freedom | 3 | Breakdown 2 is confirmed. It is on screen the whole wait, it presses the user with a timer, and the user cannot clearly dismiss it |
| UX-22 | J3 · 02, J3 · 06 | "Check this out while you wait" card | Hotel membership ads (Modern Village, IHG) appear between the status and the order or driver details. They are unrelated to a food order. The way to hide them is a small ⋮ | Aesthetic and minimalist design | 2 | Together with the GrabUnlimited banner and the Favourites prompt, the status competes with four promotions |
| UX-23 | J3 · 01, J3 · 02, J3 · 03, J3 · 05 | Progress bar under the ETA | Four icons (G, pot, scooter, house) with no text. Progress is shown only by green fill. The text above changes, but the bar alone does not name the stage | Visibility of system status; Match between system and the real world | 2 | Meaning rests on icon and colour only (the accessibility rules say meaning must not rest on colour alone) |
| UX-24 | J3 · 01 to J3 · 05 | ETA "4:12 - 4:27 PM" | A 15-minute window stays unchanged from "We've got your order" to "Your order's ready for delivery" (16:02). It becomes a point ("Arriving by 4:17 PM") only on the map screen. The app shows 12-hour time while the phone clock is 24-hour | Visibility of system status; Consistency and standards | 2 | Breakdown 1 is confirmed. Hard to plan around, but the user is still informed |
| UX-25 | J3 · 04 | Order card under the status | The order appears only as one thumbnail with a "View order summary" link. A Favourites prompt and an "Offers" row with a chevron sit inside the card of an order that is already placed | Recognition rather than recall; Match between system and the real world | 2 | The user cannot check the items at a glance. It is unclear what "Offers" can do after paying |
| UX-26 | J3 · 05 Map | Map edges; teal tag "GF-091"; speech bubble on the right | The driver icon is cut by the left edge and the address bubble ("[address hidden]") by the right edge, so the map does not frame the driver and the destination. "GF-091" has no label. Many shop names clutter the map | Visibility of system status; Match between system and the real world | 2 | The map is the part users look at most while waiting |
| UX-27 | J3 · 03, J3 · 06, J3 · 08 | Tip card | The same tip card (5.000đ, 10.000đ, 20.000đ, Custom) appears three times, including before a driver is assigned (J3 · 03). The "Custom" chip is cut off. What a tap does (charge now or ask first) is not visible | Error prevention; Consistency and standards | 2 | Provisional: it is a money action, so test it before keeping this level |
| UX-28 | J3 · 01 to J3 · 11 | "Get help"; headset icon; "Haven't received your order? Contact driver"; "Chat with merchant" and "Contact Grab" | Help has four labels in three places: blue "Get help" (J3 · 01 to 06), headset icon plus a small link "Contact driver" (J3 · 07), two buttons "Chat with merchant" and "Contact Grab" (J3 · 11). No screen offers a direct "report a problem" or refund route | Consistency and standards; Help and documentation; Help users recognise, diagnose and recover from errors | 3 | Breakdown 3 is confirmed. It matters most when the order failed and the user is already stressed. Needs the test to confirm how often users get lost |
| UX-29 | J3 · 07, J3 · 08 | Blue link under "Total paid"; the video block; "Submit" | Rating, feedback chips ("Attitu…" cut off), tip and "Submit" share one long screen, and a large video ad fills the lower half of J3 · 07. "GrabCoins +0" has no explanation. "Submit" does not show whether a tip is included | Aesthetic and minimalist design; Visibility of system status; Error prevention | 2 | Breakdown 4 is partly confirmed |
| UX-30 | J3 · 09, J3 · 10, J3 · 11 | Blue text links; "Booking ID"; fee line; "Profile" | "Rate order", "Reorder" and "View details" are small blue text links. "Rate order" is still shown at 16:14, the same minute as the rating, with no confirmation seen. "Booking ID [hidden]" and "GF-091" are internal codes. "Applicable fees 20.000" merges the two fees from checkout. "Profile: Personal" is not explained | Visibility of system status; Match between system and the real world; Recognition rather than recall | 2 | Small targets and unclear labels on the screen users return to for reorder and help |

## 4. Cross-check with your possible breakdowns

| Flow | Your breakdown | Result from the screens | See |
|---|---|---|---|
| Find and order | 1 Many services at once, food entry may be missed | Partly: the screen is crowded, but Food is the first icon | UX-01 |
| | 2 Address is a small label | Confirmed, and the "Current location / Home" row adds doubt | UX-04 |
| | 3 Ads look like results | Confirmed | UX-07 |
| | 4 Vietnamese options, required and optional look alike | Partly: no required group was captured | UX-11 |
| | 5 Menu opens with last order, offers, recommendations | Confirmed | UX-10 |
| Check out and pay | 1 One long summary | Confirmed. Note: the item list at the top of the screen is not in the screenshot | UX-13, UX-14 |
| | 2 Priority and Standard same price | Confirmed | UX-15 |
| | 3 Expired card stays in the list | Confirmed, and the message gives no fix | UX-17 |
| | 4 Card may be charged | Confirmed | UX-19 |
| | 5 Many greyed offers | Confirmed | UX-20 |
| Track and resolve | 1 ETA window too wide | Confirmed | UX-24 |
| | 2 GrabMore countdown covers the screen | Confirmed, rated 3 | UX-21 |
| | 3 Help in several places | Confirmed, rated 3 | UX-28 |
| | 4 Rating, feedback, tip on one screen | Partly confirmed | UX-29 |
| | 5 Empty loading screen in Activity | Not checkable: no screenshot of that state. J3 · 09 shows a clipped "Let's talk about…" card, which may be a loading state | not rated |

**New problems that were not in your list:** UX-08, UX-09, UX-13, UX-16, UX-18, UX-22, UX-23, UX-25, UX-26, UX-27, UX-30.

## 5. Findings (verified)

*Empty. Your checked version goes here after you review section 3: which findings you keep, change or drop, your own severity, and a second evaluator if you have one. Then ask the AI tool to create the finding items.*
