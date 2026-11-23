# Why Topfaith page: design

**Date:** 2026-11-23 · **Size:** small change · **File:** `index.html` (single-file prototype)

## Intent
Give the school's "25 Reasons to Choose Topfaith" list a proper home. It is a statement
about who Topfaith is, but prospective parents and students are expected to read it, so
it should be easy to scan and end with a clear next step for a family.

## Approaches considered
- **A. Own "Why Topfaith" page under About (chosen).** Room to design all 25, keeps the
  already-long About page as it is, and gives the school a link it can send to parents.
  Costs one more page to maintain.
- **B. Full section on the About page.** One place for everything, but About already holds
  story, values, 11 board members and 19 staff; the list would be buried at the bottom.
- **C. Teaser band that opens in place.** No new page, but hidden by default and can't be
  linked to directly.

## Design
- **New page** `Why` (route id `why`, title "Why Topfaith — Topfaith Schools"), built the
  same way as the Anthem & Pledge page: own `<template>`, `REG` entry, `ROUTES` entry and a
  "Jump to" option. Main nav keeps **About** highlighted.
- **Wiring:** the About page's "Read all 25" button (currently pointing at Admissions, which
  has no list) goes to this page; the footer's About column gains a "Why Topfaith" link.
- **Layout (top to bottom):**
  1. Banner: "← About Topfaith" back-link, kicker, headline "25 reasons to choose Topfaith."
  2. Short "on this page" bar linking to the four groups.
  3. Four groups, each a heading plus a grid of numbered reason cards (large 01–25 numerals).
  4. Closing band: "See it for yourself" with **Book a visit** and **Apply** buttons.
- **Grouping (builder's call, approved by the school here):** numbered 01–25 continuously
  through the groups, so the order differs from the source list.
  - *Teaching & curriculum (8):* qualified staff; Total Quality Education approach; small
    classes and staff ratio; developing talents; WASSCE, Cambridge O Level, SAT, IELTS;
    audio-visual and e-learning; ICT and science emphasis; excursions and field trips.
  - *Care, boarding & welfare (5):* full boarding, co-educational; counselling, leadership
    and entrepreneurship training; security consciousness; staff live on campus; healthcare
    centre.
  - *Campus & facilities (7):* expansive campus; serene, nature-friendly environment; sports
    arena; science and computer labs; library; Food & Nutrition lab; uninterrupted power
    and water.
  - *Values & standards (5):* discipline and core values; high academic and moral standards;
    Board of Governors' commitment; passion for excellence; nurturing for service.
- **Wording:** the school's text, with typos fixed ("Entrepreneurship", "e-teaching",
  "performances") and light tidying for headline length. No new claims or descriptions
  are invented.
- **Look:** existing site system only: Bricolage Grotesque / Instrument Sans, navy `#062F4A`,
  blue `#0079AF`, gold `#FFD400`, square cards. Must fit at phone width with no sideways
  scroll.

## Goals / non-goals
- Goal: every one of the 25 reasons visible without clicking; scannable in under a minute.
- Non-goal: photos or long descriptions per reason (none supplied).
- Anti-goal: anything that contradicts facts elsewhere on the site.

## Resolved
- Staff-to-student ratio is **1:8** (confirmed 2026-11-23). The reason reads 1:8, matching
  the home page stat; the source list's 1:7 is superseded.

**Status:** approved 2026-11-23.
