---
type: "task-analysis"
title: "Task analysis and user journey"
stage: "Discover"
status: "draft"
summary: "For each of the three core functions: the user's goal, the steps and where effort or friction may appear, plus one journey map across all three with assumed feelings and expectations. A draft built from my walk-through, to be tested."
supports: []
embed: true
media:
  - "user-journey-map.html"
---

# Task analysis and user journey

**The user:** one generic consumer who orders the food they like, waits for it to be delivered and enjoys it. There is no single age group or situation.

**Important:** the effort ratings, feelings and expectations below are my own assumptions from the walk-through and my understanding of the product. They are not test results. Each one is to be checked in the heuristic evaluation, the usability test and the interviews.

**Effort rating:** low means the step is quick and clear, medium means the user must think or compare, high means the step takes a lot of time or attention. All ratings are assumed.

## What the user expects from the app

These come from my own understanding, in this order of importance:

1. Find food easily and order it easily. Finding and ordering is the most important function.
2. Clear information and a clear preview of what they will get.
3. A visible reputation for each restaurant, and a delivery time.
4. Checking out and tracking the order are secondary, but should not get in the way.

In Vietnam, many people still like to pay in cash on delivery, while others use an e-wallet, a Visa or Mastercard, or a bank account. Many users live in houses or apartment buildings, so the way of receiving the order should be flexible for the user to choose.

## Task analysis 1: Find and order

**Goal:** find food I like and put it in my basket.

**Plan:** open the food section, check the address, find a restaurant, choose the food, add it to the basket, and repeat if more items are wanted.

| Step | What the user does | What the user needs | Effort | Possible friction |
|---|---|---|---|---|
| 1 | Open the app and go to the food section | Know where food delivery sits among the other services | Low | The home screen shows many services and promotions at once |
| 2 | Check the delivery address | Notice the address and judge if it is right | Low | The address is a small label, and changing it opens a separate screen with a keyboard |
| 3 | Decide how to find food: browse a category, search by keyword or take a suggestion | Know what they want and judge the suggestions | Medium | The suggestions lean towards restaurants already ordered from, with little that is new, so users search by keyword |
| 4 | Compare results and pick a restaurant | Read the rating, delivery time, fee and promotions, and tell sponsored listings from regular ones | High | A lot is shown at once, and reading reviews takes time |
| 5 | Browse the menu and open an item | Find a specific item, read the price and description | Medium | The menu opens with last order, offers and recommendations before the full menu |
| 6 | Choose options such as size, sweetness, toppings and a note | Understand which choices are required and which are optional | Medium | Option names written by the restaurant are in Vietnamese in an English interface |
| 7 | Add to the basket, decide whether to add more and review the basket | See a clear preview of what is in the basket and the price | Low | None expected |

## Task analysis 2: Check out and pay

**Goal:** pay for the order in the way I prefer and place it.

**Plan:** review the order, check the delivery details, choose delivery speed, keep or change the payment method, apply a promotion if there is one, and place the order.

| Step | What the user does | What the user needs | Effort | Possible friction |
|---|---|---|---|---|
| 1 | Open the order summary and check the items, fees and total | A clear total with the fees explained | Low | The summary mixes items, a promotion banner, fees and savings in one long screen |
| 2 | Check the delivery details such as address, meeting point and cutlery | Be able to choose how the food is handed over, for a house or an apartment building | Low | None expected |
| 3 | Choose the delivery speed | Understand what each speed costs and how long it takes | Medium | Priority and standard cost the same but take different times |
| 4 | Check the payment method | See which method is selected, such as cash, e-wallet or card | Low | None expected |
| 5 | Change the payment method, pick a linked one or add a new card | Know which methods work and how to add one | Medium | An expired card stays in the list, and the add-card form warns that the card may be charged to check it |
| 6 | Open offers and apply a promotion | See quickly which promotions apply to this order | Medium | Many offers are greyed out because of a minimum spend, and the user may feel upset when none applies |
| 7 | Place the order | Feel sure about the total and the details | Low | None expected |

## Task analysis 3: Track the order and resolve problems

**Goal:** know when my food arrives and receive it, or get help if something goes wrong.

**Plan:** see the order confirmed, wait while it is prepared, follow the driver, receive the food, rate the delivery, and get help or reorder if needed.

| Step | What the user does | What the user needs | Effort | Possible friction |
|---|---|---|---|---|
| 1 | See the order confirmed and the estimated time | A believable arrival time | Low | The time is a 15-minute window |
| 2 | Wait while the restaurant prepares the order | Know what stage the order is at | Low | None expected |
| 3 | Follow the driver on the map and check the order details | A clear, accurate arrival time, and a clear message if weather or traffic causes a delay | Low | A promotion banner with a countdown covers the bottom of the screen |
| 4 | Chat with, call or tip the driver if needed | Reach the driver quickly | Medium | None expected |
| 5 | Receive the food and confirm it arrived | Be able to say yes or report that it did not come | Low | None expected |
| 6 | Rate the delivery, give feedback and tip | A short, simple way to say how it went | Low | Rating, feedback and tip share one long screen |
| 7 | If something is wrong, find help | Know where to go for help | High | Help is in several places: contact the driver, Get help, and contact Grab or the restaurant from the order details |
| 8 | Later, find the order in the activity list and reorder | Find the past order and reorder easily | Low | The activity tab first shows an empty loading screen |

## User journey

The journey map covers all three functions as the middle stages, with a stage before (deciding to order) and a stage after (enjoying the food and following up). The lowest assumed feeling is while finding food, because there is a lot to look at and the suggestions repeat past orders. Checking out is assumed to feel clear and positive, and finding no promotion that applies is a small disappointment.

## What to check next

- Test the effort ratings in the usability test: do real users find steps 4 and 7 in the first task analysis hard?
- Ask in the interviews how users feel at each stage, and replace my assumed feelings with theirs.
- Check how users in Vietnam really pay and receive orders, using sources I can cite.
