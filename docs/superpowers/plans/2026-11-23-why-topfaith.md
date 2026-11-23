# Why Topfaith Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "Why Topfaith" page listing the school's 25 reasons in four themed groups, linked from the About page and footer.

**Architecture:** `index.html` is a single-file prototype: each page is a `<template id="tpl-Name">`, a `REG["Name"]` component class whose `renderVals()` feeds `{{ }}` bindings and `data-sc="for"/"if"` templates, and an entry in the `ROUTES` object; links of the form `Name.dc.html` route by hash. Copy the Anthem page (`tpl-Anthem`, `REG["Anthem"]`) as the pattern.

**Tech Stack:** Plain HTML/CSS/JS, no build step. Verification by a Python string check plus a headless check in Chrome against `python3 -m http.server`.

**Spec:** `docs/superpowers/specs/2026-11-23-why-topfaith-design.md`

## Global Constraints

- Staff-to-student ratio is **1:8** (never 1:7).
- Reason wording is the school's text, typos fixed ("Entrepreneurship", "e-teaching", "performances"); no invented claims or descriptions.
- Site system only: Bricolage Grotesque / Instrument Sans, `#062F4A`, `#0079AF`, `#FFD400`, square cards, inline styles like the rest of the file.
- No horizontal scroll at 375px width.
- Header renders with `current="about"`.

## Review Focus

- Phone width (375px): four-column card grid must collapse to one column; long reasons (power & water, academic standards) must wrap, not overflow.
- Direct load of `index.html#why` (no prior navigation) must render the page and set "Jump to" to `why`.
- Group jump links (`#teaching` etc.) must scroll, not trigger the router (router only treats `Name.dc.html`).
- Numbering must run 01–25 with no gaps or repeats across groups.
- "Read all 25" on About must land on this page, not Admissions.

---

### Task 1: Why Topfaith page, data and links

**Files:**
- Modify: `index.html` (new `tpl-Why` before `<script>`; `ROUTES`; `#pageJump` options; footer About nav; About "Read all 25" href; new `REG["Why"]` beside `REG["Anthem"]`)
- Test: `docs/superpowers/plans/check_why.py` (string checks)

**Interfaces:**
- Produces: route `Why` → id `why`, title `"Why Topfaith — Topfaith Schools"`; `REG["Why"].renderVals()` returns `{ groups: Array<{ id: string, title: string, reasons: Array<{ n: string, text: string }> }> }` where `n` is zero-padded `"01"`–`"25"`.

- [ ] **Step 1: Write failing check** `check_why.py` asserting in `index.html`: `id="tpl-Why"` present; `"Why": {"id": "why"` in ROUTES; `<option value="why">` present; footer has `href="Why.dc.html"`; the "Read all 25" anchor's href is `Why.dc.html`; `REG["Why"]` present; no `1:7` anywhere; 25 reason entries in the `REG["Why"]` block; group ids `teaching`, `care`, `campus`, `values`.
- [ ] **Step 2: Run** `python3 -I docs/superpowers/plans/check_why.py` → expect FAIL.
- [ ] **Step 3: Implement.** Group contents and order exactly as the spec's "Grouping" list (8/5/7/5); `n` computed by running index across groups. Page sections: navy banner (back-link "← About Topfaith", kicker "Why Topfaith", h1 "25 reasons to choose Topfaith."), on-this-page bar linking `#teaching #care #campus #values`, one `<section id="{{ g.id }}">` per group with numbered cards, closing band "See it for yourself" with **Book a visit** → `Admissions.dc.html` and **Apply** → `Apply.dc.html`. Footer About column: add "Why Topfaith" after "Anthem & pledge". Visual detail per the frontend-design skill within the Global Constraints.
- [ ] **Step 4: Run check** → expect PASS.
- [ ] **Step 5: Browser check** at `http://127.0.0.1:8765/index.html#why`: 25 cards rendered, numbers 01–25 in order, `#pageJump.value === 'why'`, no horizontal scroll at desktop and at 375px; click "Read all 25" from `#about` lands on `#why`.
- [ ] **Step 6: Commit** `index.html`, spec, plan and check script: `feat: add Why Topfaith page with 25 reasons`.
