# Photography Trip Planning — Research-Backed Itinerary Builder

**Description:** 
A trip planning prompt for travel photographers. Filters every location against your shooting style before suggesting anything. Covers shot lists, unconventional perspectives, photography policy verification, light timing, Atlas Obscura picks, fatigue management, and local food/bar research. Optional production deliverables: PowerPoint deck, Excel workbook, and Google Maps CSVs. Works in lightweight (text only) or full production mode.

**Type:** TEXT
**Author:** elpicoso
**Created:** 2026-07-01T19:05:24.585Z
**Votes:** 0
**Views:** 0

**Tags:** Travel, Planning

## Prompt Content

```
# Photography Trip Planning Prompt
## Reusable Template for Travel Photographers
### v3.0

---

> **Two ways to use this template:**
>
> **Lightweight mode** — Skip all sections marked `[OPTIONAL]` and the entire Technical Notes section. Fill in your style profile and trip details, then ask Claude for a text-based research brief and day-by-day schedule. No scripting required.
>
> **Full production mode** — Use every section. Claude will produce a PowerPoint slide deck (via Node.js + pptxgenjs), an Excel workbook (via Python + openpyxl), and Google Maps CSVs — all color-coded and QA'd. Requires comfort running scripts from the command line.
>
> In both modes: fill in every section marked `[FILL IN]`. Sections marked `[EXAMPLE]` show what a completed entry looks like — replace them with your own details. Sections marked `[OPTIONAL]` can be removed if not relevant to your workflow.

---

## WHO I AM

I am a travel photographer planning a trip [with / without] a companion. My name is [FILL IN]. I shoot with [FILL IN — e.g., Canon EOS R5 and Sony A7IV]. My lens kit for travel: [FILL IN — e.g., 16-35mm wide, 24-70mm standard, 100mm macro]. I travel with [FILL IN — e.g., a carbon fiber travel tripod / no tripod / a compact gorilla-pod]. My carry system is [FILL IN — e.g., a chest rig with Peak Design clips to secure cameras to the straps / a camera backpack with a cube insert].

> [EXAMPLE]: I shoot with a Canon 5D Mark II and Canon EOS-R with EF adapter. Lens kit: 16-35mm (primary workhorse), 24-105mm (street/mid-range), 100mm macro (details/close work). Carry system: a Condor Stowaway chest rig with two Peak Design clips. No ND filters on this trip.

---

## MY PHOTOGRAPHIC STYLE

This is the most important section. Read it carefully before suggesting any locations.

**The core subject:** [FILL IN — Describe the through-line of your work. What do you photograph and why? What draws you to a subject?]

> [EXAMPLE]: I photograph things that endure — structures, landscapes, and moments that exist outside of time. The through-line across my work is things built or lived in that now outlive their original purpose, still standing.

**Technical signatures:** [FILL IN — List your consistent compositional and technical choices.]

> [EXAMPLE]:
> - Symmetrical or near-symmetrical composition with a strong central vanishing point
> - Low angle or looking straight up to exaggerate scale and eliminate horizon — I do this consistently
> - A single human figure used for scale, not as the primary subject
> - Long exposure or slow shutter to pull motion out of water, clouds, and crowds
> - B&W for structural, industrial, and decay subjects; color when the palette itself is the subject
> - Strong tonal contrast — I print dark
> - The underside, interior skeleton, and structural bones of things interest me more than facades

**Recurring subject categories:** [FILL IN — List the types of places and subjects you consistently seek out.]

> [EXAMPLE]:
> - Decay and abandonment — things that have outlived their purpose (plane wrecks, ruined churches, abandoned institutions)
> - Sacred spaces with weight and edge — not pretty churches, spaces where something happened
> - Old-meets-industrial juxtapositions (ancient marble in a power plant, Roman columns in a modern piazza)
> - Underground and subterranean spaces — crypts, tunnels, ancient layers beneath modern cities
> - Geometric structural form — bridges, piers, arches, repeating elements
> - Quiet and empty streets — I shoot before crowds arrive
> - Atlas Obscura-type locations — the unusual, the hidden, the forgotten

**What I consistently avoid:** [FILL IN — List what you do not want recommended.]

> [EXAMPLE]:
> - Postcard framing of famous places
> - Posed subjects
> - Soft or sentimental light
> - Crowded tourist spots as primary targets
> - Markets as planned stops (open to stumbling upon them)

---

## TRAVEL COMPANION [OPTIONAL]

[FILL IN or delete this section] — If you are traveling with a companion, describe their interests here so Claude can build a plan that works for both of you, not a photographer's itinerary with someone along for the ride.

> [EXAMPLE]: My partner travels with me for the entire trip. They enjoy boutique shopping, aperitivo culture, neighborhood wandering, and unusual cultural experiences including ossuaries and catacombs. They are game for unusual locations. Nearly all photography targets are shared experiences — they are present for the vast majority of shoots, not waiting elsewhere. The only genuinely solo time is pre-dawn sessions. Build shared experiences into the plan, not a parallel track.

**On adventure and physical effort:** By default, a fully researched, ticketed, pre-scheduled itinerary can feel risk-free and passive — nothing left to chance, no physical exertion, no uncertainty. If a harder, more physically engaged way to reach a location exists (climbing down to a site instead of taking a boat, hiking a trail instead of driving), surface it explicitly as a choice rather than silently defaulting to the easier option. Don't just describe the harder option — check the return logistics too (e.g., if hiking down from a summit, where does the car end up, and how do you get back to it?).

**On fatigue:** Don't assume unlimited energy across a multi-city trip. Calculate the cumulative load of pre-dawn shoots, jet lag, and daily walking distance, and flag when a trip has no genuine rest morning built in. A trip with five excellent pre-dawn sessions beats one with six mediocre ones. Recommend at least one no-alarm, fully unplanned rest morning roughly mid-trip, not just on arrival day.

---

## THE TRIP

**Destination:** [FILL IN — e.g., "Italy: Rome, Venice, Milan"]
**Departure:** [FILL IN — e.g., "LAX, Sept 16, 3:05 PM"]
**Return:** [FILL IN — e.g., "LIN (Milan Linate), Sept 28, 9:50 AM"]
**Outbound arrival:** [FILL IN — e.g., "FCO (Rome), Sept 17, 2:05 PM"]
**Cities and nights:** [FILL IN — e.g., "Rome 3 nights, Venice 3 nights, Milan 3 nights"]
**City-to-city transport:** [FILL IN — e.g., "Frecciarossa train, targeting ~5 PM arrival at each new city to protect the outgoing city's final morning"]
**Base neighborhoods:** [FILL IN, or ask Claude to recommend based on shooting targets and companion interests]

---

## WHAT I WANT CLAUDE TO BUILD

### 1. PowerPoint Slide Deck [OPTIONAL — requires Node.js and pptxgenjs]

> This deliverable is for users comfortable running Node.js scripts. If you want a simpler output, replace this section with a request for a formatted document or text plan.

**Format:** LAYOUT_WIDE (13.3 x 7.5 inches), built with pptxgenjs in Node.js. Dark navy background with gold accent text on divider and reference slides. Off-white background on content/schedule slides. Version number on cover and filename.

**Badges/flags on slide header or inline:**
- Red badge: "★ ADVANCE BOOKING REQUIRED" — for locations requiring pre-purchase tickets
- Green badge: "★ ATLAS OBSCURA" — for unusual/hidden locations in that spirit
- Gold banner: "SHARED EXPERIENCE" — for meaningful shared visits
- Dark red badge: "⊘ PHOTOGRAPHY PROHIBITED" — only after direct verification (see Location Research Standards)
- Dark red badge on High Viewpoints cards: "⊘ CONFIRMED CLOSED" — for viewpoints that no longer exist or have shut down

**Slides to include:**
- Cover (trip title, cities, dates, version number)
- Trip overview (card layout, one card per city stop with dates/nights/base)
- Photography approach (style summary, gear)
- Schedule color legend
- For each city:
  - City section divider (full dark background)
  - Light timing table (blue hour start, sunrise, golden hour AM, golden hour PM, sunset, blue hour end — calculated with Python astral library, exact coordinates, actual trip dates)
  - Base camp slide (why this neighborhood, proximity to shooting targets, highlights nearby, transit)
  - Location slides for each confirmed shooting target: About / Shot List (4–5 shots) / Unconventional Perspectives (3–4 angles), plus a Key Notes bar (hours, access, cost)
  - High Viewpoints slide (card layout, 3 viewpoints; flag confirmed closures; distinguish true post-sundown viewpoints from golden-hour-only ones that close before dark)
  - Daily schedule — combine all days for a city onto a single slide; only split to a continuation slide if the content would actually overflow the slide height. Do not split preemptively at a fixed row count.
- Time Allocation pie chart (hours by category, pulled from actual schedule data)
- Tickets and booking slide (3 columns: book in advance / pay on day / free)
- Gear list slide (cameras, lenses, support, carry system, accessories, notes on where tripods/photography are restricted)
- Aperitivo/food bars slide — specific named bars by city, local picks only, with address and description. These are options spread across multiple evenings, not a single-night bar crawl.
- Train/transport connections summary slide [OPTIONAL]
- **Appendix — Shot Diagrams:** plan-view and cross-section schematics for every photography location. Camera position (red dot), shooting direction (dashed line), field-of-view cone (dotted lines), recommended lens, all numbered to match the location's shot list. Every plan-view diagram must include a north arrow/compass indicator. Cross-section diagrams (showing vertical relationships like a flooded crypt or a cliff-face) don't need one.

**Schedule color coding (7 categories):**
- Pre-Dawn Shoot / Photography: dark navy bg, light blue text
- Aperitivo: dark purple bg, light purple text
- Shared Activity: dark gold bg, light gold text
- Free / Optional: dark green bg, light green text
- Travel / Arrival: dark gray bg, light gray text
- Rest / Checkout: medium gray bg, light gray text
- Advance Booking Required: dark red bg, light red text
- (Sunset/golden-hour blocks can get a dark-orange variant if useful)

---

### 2. Excel Workbook [OPTIONAL — requires Python and openpyxl]

**Master tab — ask which format the person wants:**
- **List format:** chronological rows (Date, Day, City, Time, Activity, Category, Duration, Notes), one row per activity across the whole trip.
- **Calendar grid format:** horizontal week view — all trip days as columns left to right, a shared time axis down both sides (e.g. 5:00 AM–10:30 PM in 30-minute rows), each activity rendered as a color-coded block merged vertically across the rows it spans. Travel/transition-day columns get a visually distinct header and background tint. Sunrise, sunset, blue hour, and golden hour rows are highlighted on the time axis (label as trip-average approximations with a footnote — point to per-city Light Timing slides for precision). One sheet, all days, no tab splits.

One tab per city (vertical day-by-day format regardless of which Master style is chosen), plus a Legend tab.

Same color coding as schedule slides. Freeze panes, hide gridlines, auto-filter on header rows where the sheet is a flat list. Include a Duration column.

---

### 3. Google Maps CSVs — one per city [OPTIONAL]

Columns: Name, Description, Category, Best Time, Latitude, Longitude, Address.

**Critical:** Use Python csv.writer with utf-8 encoding. No special characters — plain ASCII only, with explicit character substitution (e.g. é→e, —→--, '→'). Verify coordinates before including.

Categories: Shooting Location, Shared Activity, Base, High Viewpoint, Transit, Optional Day Trip, CLOSED - DO NOT USE, Atlas Obscura Optional.

**File naming convention:** [destination]-trip-[year]-v[N].pptx / .xlsx / [city]-locations-v[N].csv. Increment the version number on every rebuild, and keep the deck, workbook, and all CSVs at the same version number even if only one file changed — rename/re-copy unchanged files so the full deliverable set stays in sync.

---

## LOCATION RESEARCH STANDARDS

### For each shooting location, provide:
1. **Description** — what it is, why it matters photographically, best conditions, connection to my style profile where relevant
2. **Shot list** — 4–5 standard shots worth getting
3. **Unconventional perspectives** — 3–4 angles or approaches most photographers miss, matched to my style profile above
4. **Key notes** — hours, access, cost, transit, proximity to other targets
5. **Best time** — pre-dawn / early morning / morning / afternoon / golden hour

### Photography policy verification — non-negotiable:
Before listing any location as a photography target, **verify the actual photography policy directly** — official site, or by contacting the venue if the policy is ambiguous or high-stakes. Do not assume "no photography" or "photography allowed" based on general reputation or partial information. Two real examples: a location assumed fully off-limits turned out to allow personal use with equipment-timing restrictions once the venue was emailed directly; a separate underground site turned out to prohibit photography completely despite initially being treated as a shooting target. When a venue's written policy restricts *equipment* (tripods, DSLRs) to specific hours rather than restricting photography outright, treat it as a scheduling constraint, not a footnote.

### For each city, also research:
- The best base neighborhood (balancing proximity to shooting targets and companion interests)
- **High viewpoints — split into two categories:** (a) true post-sundown/night viewpoints that stay open into darkness, and (b) golden-hour-only viewpoints that close before true dark (many rooftop terraces do — check exact closing time against that city's actual sunset time before assuming a rooftop works for night photography). Confirm current open/closed status; flag confirmed permanent closures clearly rather than omitting them silently.
- Optional day trips (3–4 options matched to both your aesthetic and companion interests)
- Atlas Obscura locations that genuinely fit your style — filter carefully, not everything qualifies
- Specific aperitivo/food bars: local picks only, not tourist-facing, with name, address, and what makes them worth going to
- Self-drive or no-license rental options (boats, small vehicles) where they'd give more compositional control than a scheduled ferry/tour — verify pricing and access logistics directly, don't extrapolate from aggregated blog content [OPTIONAL]

### Research and verification requirements:
- **Verify all locations exist** before including — web search any location you are not certain about
- **Confirm current access status** — search for closures before recommending any viewpoint or attraction
- **Days of week:** always calculate with Python datetime for the actual trip year. Never guess.
- **Light timing:** always calculate with Python astral library using exact city coordinates and trip dates. Never estimate.
- **Ticket prices and booking windows:** search for current prices — do not rely on training data
- **Do not hallucinate** — if uncertain about a fact, search or say so. If asked directly "why did you hallucinate X," own it plainly rather than explaining it away.
- **When new information contradicts prior research** (e.g., an official email reply from a venue), propagate the correction across every affected deliverable in the same pass — schedule, location slide, booking slide, Excel notes, CSV — not just in conversation.

---

## ATLAS OBSCURA APPROACH

Filter Atlas Obscura picks strictly against your style profile. Use these as a guide for what typically works and what doesn't:

**Strong fits:**
- Underground or subterranean spaces (crypts, tunnels, ancient layers)
- Abandoned or decaying spaces (former institutions, industrial ruins) — verify current safety and legal access status before including; drop anything requiring trespass regardless of photographic appeal
- Bone chapels and ossuaries
- Hidden architectural anomalies (a spiral staircase down an alley, an alchemist's gate in a park)
- Sacred spaces that have crossed into the uncanny

**Weak fits — do not suggest:**
- Quirky museums without strong visual potential
- Locations that are historically interesting but not photographically compelling
- Anything requiring illegal or unsafe access — note if access is uncertain and flag for research rather than recommending

---

## APERITIVO/FOOD RESEARCH STANDARD

For each city, research 3–4 specific local bars or restaurants. Requirements:
- Local crowd, not tourist-facing
- Named venue with street address
- One-sentence description of what makes it worth going to
- Flag any important closures (day of week, time of day)
- Prioritize venues near shooting locations so the same place can be visited at dawn (shooting) and evening (aperitivo) — this is a strong pairing when possible
- Present these as a menu of options across the trip's evenings, not a single night's itinerary — don't imply nightly bar-hopping unless the person says that's what they want

---

## PLANNING PROCESS

Follow this order:

1. Ask for trip dates, cities, and transport if not provided
2. Verify days of week with Python before doing anything else
3. Calculate light timing with Python astral for all shooting days
4. Research and propose shooting locations — filter against my style profile — ask to confirm before building
5. Research and propose base neighborhoods per city — ask to confirm
6. Research Atlas Obscura picks per city — propose with honest assessment of fit
7. Research specific local food/drink venues per city
8. Research high viewpoints per city, split by post-sundown vs. golden-hour-only access
9. Identify advance booking requirements and booking windows
10. Build the schedule — pre-dawn shoots, shared experiences, food/aperitivo, free time, and at least one genuine unplanned rest morning
11. **Audit the built schedule before presenting it:** (a) does it contain any real physical effort or unplanned time, or is everything ticketed and passive? (b) does the cumulative pre-dawn + walking load leave room to actually enjoy the trip, or will fatigue compound by mid-trip?
12. Build all deliverables in one go: PowerPoint, Excel, CSVs
13. QA slides before delivering: convert to PDF via soffice, then pdftoppm -jpeg -r 120, review per-slide images

**Batch changes, then rebuild only when explicitly told to.** Confirm all changes before touching any files. Hold requested changes in a running list and rebuild everything together, rather than rebuilding after each individual change.

---

## TECHNICAL NOTES [OPTIONAL — relevant only if using the PowerPoint, Excel, or CSV deliverables]

### pptxgenjs:
- Never pass a lambda as a positional y argument to helper functions — use inline `s.addText()` with explicit coordinates
- Always add `valign: "top"` to bulleted list text boxes
- Every bullet array's last item must include `options: { bullet: true }` explicitly
- Never use `#` in hex color values — pass without the hash
- When building card grids where content length varies, don't assume uniform row heights — either measure/estimate per-card height from item count, or use independently-tracked running y-offsets per column so taller cards don't overlap the next row
- QA every rebuild: `soffice --headless --convert-to pdf`, then `pdftoppm -jpeg -r 120`, review before delivering

### openpyxl:
- Use `PatternFill("solid")` for all cell fills
- Freeze panes at the top-left of the scrollable data region (this shifts if using a calendar-grid Master with header rows and a day-column axis)
- Set `showGridLines = False` on all sheets
- Auto-filter on header rows where the sheet is a flat list; a calendar-grid Master doesn't need auto-filter
- For calendar-grid layouts: resolve overlapping time blocks within a day before merging cells (sort by start time, clip a block's end to the next block's start); named/approximate time-of-day labels need an explicit anchor-hour mapping since they have no literal clock time

### CSVs:
- Always use Python `csv.writer` with utf-8 encoding
- No special characters — plain ASCII only, with explicit character substitution (é→e, —→--, '→')
- Verify coordinates are accurate before including

### Schedule splits (PowerPoint):
- Do not split a city's daily schedule across slides by default. Combine all days for one city onto a single slide.
- Only split to a continuation slide if the actual rendered content would overflow the available slide height — check total row count against available vertical space, not a fixed threshold.

---

## STYLE PREFERENCES

[FILL IN — describe your general planning philosophy. Examples below.]

> [EXAMPLE]:
> - Quality over quantity — fewer, richer locations beat comprehensive lists
> - Minimal logistics friction — don't route across a city when targets can be clustered
> - Authentic over tourist-facing — if a less-visited equivalent exists, recommend it
> - Pre-dawn access is a priority — but nearly all photography targets are shared experiences with my companion
> - The unusual over the famous — Atlas Obscura sensibility throughout
> - Adventure and unplanned time deserve deliberate room, not just ticketed efficiency
> - When in doubt about a fact, search before answering — and say so if you can't verify something rather than presenting an inference as confirmed

---

## COMPANION PRIORITIES [OPTIONAL]

[FILL IN or delete this section] — If traveling with a companion, list what matters to them so their priorities are built into the shared activities and food/aperitivo slides, not treated as an afterthought.

> [EXAMPLE]:
> - Boutique shopping (not chain stores, not department stores)
> - Aperitivo culture — spread across the trip's evenings, not a nightly ritual by default
> - Neighborhood wandering in places that feel local
> - Unusual cultural experiences — game for ossuaries, catacombs, and the uncanny
> - Good food and local restaurants

Remember: the large majority of photography locations should already be shared experiences. Treat the schedule as a joint itinerary with a few solo pre-dawn windows, not a photographer's itinerary with a companion along for the ride.

---

*Template built from a real multi-city Italy trip planning workflow, refined across multiple full deliverable rebuild cycles. Works with Claude, ChatGPT, Gemini, or any modern LLM.*
```

**Source:** https://prompts.chat/prompts/cmr2g3yw90001l7048veoh3xd_photography-trip-planning-research-backed-itinerary-builder

## 中文翻译

### 标题
摄影旅行规划 — 研究支持的行程构建器

### 提示词内容

```
# 摄影旅行计划提示
## 旅行摄影师可重复使用的模板
### v3.0

---

> **使用此模板的两种方法：**
>
> **轻量级模式** — 跳过所有标记为“[可选]”的部分以及整个技术说明部分。填写您的风格简介和旅行详细信息，然后向克劳德询问基于文本的研究简介和日常时间表。无需编写脚本。 >
> **完整生产模式** — 使用每个部分。 Claude 将制作一个 PowerPoint 幻灯片（通过 Node.js + pptxgenjs）、一个 Excel 工作簿（通过 Python + openpyxl）和 Google 地图 CSV — 所有颜色编码并经过 QA。需要从命令行轻松运行脚本。 >
> 在两种模式下：填写标记为“[FILL IN]”的每个部分。标记为“[示例]”的部分显示了完整条目的外观 - 将其替换为您自己的详细信息。如果与您的工作流程不相关，则可以删除标记为“[可选]”的部分。 ---

## 我是谁

我是一名旅行摄影师，计划[有/没有]同伴旅行。我的名字是[填写]。我使用 [FILL IN — 例如，佳能 EOS R5 和索尼 A7IV] 进行拍摄。我的旅行镜头套件：[填写 — 例如，16-35 毫米宽、24-70 毫米标准、100 毫米微距]。我旅行时会携带[填写——例如碳纤维旅行三脚架/无三脚架/紧凑型大猩猩脚架]。我的携带系统是[填写——例如，带有 Peak Design 夹子的胸部装备，用于将相机固定在肩带上/带有立方体插件的相机背包]。 > [示例]：我使用带 EF 适配器的佳能 5D Mark II 和佳能 EOS-R 进行拍摄。镜头套件：16-35mm（主要主力）、24-105mm（街道/中距离）、100mm 微距（细节/近距离工作）。携带系统：Condor Stowaway 胸部装备，配有两个 Peak Design 夹子。这次旅行没有使用ND滤镜。 ---

## 我的摄影风格

这是最重要的部分。在建议任何地点之前请仔细阅读。 **核心主题：** [填写 - 描述您工作的主线。你拍摄什么以及为什么？是什么吸引您关注某个主题？]

> [示例]：我拍摄那些经久不衰的事物——结构、风景和存在于时间之外的时刻。我作品的主线是建造或居住的事物，这些事物现在已经超出了它们最初的目的，但仍然存在。 **技术签名：** [填写 - 列出您一致的成分和技术选择。]

> [示例]：
> - 具有强烈中心消失点的对称或近对称构图
> - 低角度或直视以夸大比例并消除地平线 - 我一贯这样做
> - 用于比例的单个人物，而不是作为主要主题
> - 长时间曝光或慢速快门可将水、云和人群中的运动拉出来
> - 用于结构、工业和腐烂主题的黑白；当调色板本身是主题时的颜色
> - 强烈的色调对比 - 我打印深色
> - 事物的底面、内部骨架和结构骨骼比正面更让我感兴趣

**重复主题类别：** [填写 - 列出您经常寻找的地点和主题的类型。]

> [示例]：
> - 腐烂和遗弃——已经失去其用途的东西（飞机失事、被毁的教堂、被遗弃的机构）
> - 有重量和边缘的神圣空间 - 不是漂亮的教堂，是发生过事情的空间
> - 旧与工业的并置（发电厂中的古老大理石，现代广场中的罗马柱）
> - 地下和地下空间——现代城市下方的地窖、隧道、古代地层
> - 几何结构形式——桥梁、桥墩、拱门、重复元素
> - 安静而空旷的街道——我在人群到来之前拍摄
> - Atlas Obscura 类型的地点 — 不寻常的、隐藏的、被遗忘的

**我一贯避免的：** [填写 - 列出您不希望推荐的内容。]

> [示例]：
> - 著名景点明信片装框
> - 摆出的主题
> - 柔和或感伤的灯光
> - 拥挤的旅游景点是主要目标
> - 市场按计划停止（可能会被绊倒）

---

## 旅行伴侣 [可选]

[填写或删除此部分] — 如果您与同伴一起旅行，请在此处描述他们的兴趣，以便 Claude 制定适合你们俩的计划，而不是与同行的摄影师的行程。 > [示例]：我的伴侣在整个旅程中与我同行。他们喜欢精品店购物、开胃酒文化、街区漫步以及不寻常的文化体验，包括骨库和地下墓穴。它们喜欢在不寻常的地方活动。 几乎所有的摄影目标都是共同的经历——它们出现在绝大多数拍摄中，而不是在其他地方等待。唯一真正的独处时间是黎明前的会议。将共同的经验纳入计划中，而不是平行的轨道。 **关于冒险和体力消耗：** 默认情况下，经过充分研究、订票、预先安排的行程可以让人感到无风险和被动——没有任何机会，没有体力消耗，没有不确定性。如果存在一种更困难、更需要体力的方式来到达某个地点（爬到某个地点而不是乘船，沿着小路徒步而不是开车），明确地将其作为一种选择，而不是默默地默认更容易的选择。不要只描述更困难的选择 - 还要检查返回物流（例如，如果从山顶徒步下来，汽车最终会到达哪里，以及如何返回？）。 **关于疲劳：** 不要假设在多城市旅行中能量无限。计算黎明前拍摄、时差和每日步行距离的累积负荷，并在旅行没有内置真正的早晨休息时进行标记。一次有五次出色的黎明前训练的旅行胜过一次有六次平庸的黎明前训练的旅行。建议在行程中途至少安排一个没有闹钟、完全计划外的休息早晨，而不仅仅是在抵达当天。 ---

## 旅行

**目的地：** [填写 — 例如，“意大利：罗马、威尼斯、米兰”]
**出发：** [填写 — 例如，“洛杉矶国际机场，9 月 16 日下午 3:05”]
**返回：** [填写 — 例如，“LIN (Milan Linate), Sep 28, 9:50 AM”]
**出境到达：** [填写 — 例如，“FCO（罗马），9 月 17 日下午 2:05”]
**城市和夜晚：** [填写 — 例如，“罗马 3 晚，威尼斯 3 晚，米兰 3 晚”]
**城市到城市的交通：** [填写 — 例如，“Frecciarossa 列车，目标是下午 5 点左右抵达每个新城市，以保护出发城市的最后一个早晨”]
**基地街区：** [填写，或请克劳德根据射击目标和同伴兴趣推荐]

---

## 我想要克劳德建造什么

### 1. PowerPoint 幻灯片 [可选 — 需要 Node.js 和 pptxgenjs]

> 此交付成果旨在让用户能够轻松运行 Node.js 脚本。如果您想要更简单的输出，请将此部分替换为对格式化文档或文本计划的请求。 **格式：** LAYOUT_WIDE（13.3 x 7.5 英寸），使用 Node.js 中的 pptxgenjs 构建。深海军蓝背景，分隔线和参考幻灯片上带有金色文字。内容/时间表幻灯片上的灰白色背景。封面上的版本号和文件名。 **幻灯片标题或内联上的徽章/标志：**
- 红色徽章：“★ 需要提前预订”——适用于需要预购门票的地点
- 绿色徽章：“★ ATLAS OBSCURA”——本着这种精神，代表不寻常/隐藏的地点
- 金横幅：“共享体验”——有意义的共享访问
- 深红色徽章：“⊘ 禁止拍照”——仅在直接验证后（请参阅位置研究标准）
- 高视点卡上的深红色徽章：“⊘ 已确认关闭”——适用于不再存在或已关闭的视点

**幻灯片包括：**
- 封面（行程标题、城市、日期、版本号）
- 行程概览（卡片布局，每个城市停靠一张卡片，注明日期/夜晚/基地）
- 摄影方法（风格总结、装备）
- 时间表颜色图例
- 对于每个城市：
  - 城市部分分隔线（全黑背景）
  - 灯光时间表（蓝色时间开始、日出、上午黄金时间、下午黄金时间、日落、蓝色时间结束——使用Python星体库计算、精确坐标、实际旅行日期）
  - 大本营幻灯片（为什么是这个街区、靠近射击目标、附近的亮点、交通）
  - 每个已确认拍摄目标的位置幻灯片：关于/拍摄列表（4-5 个镜头）/非常规视角（3-4 个角度），以及关键注释栏（时间、访问、成本）
  - 高视点幻灯片（卡片布局，3 个视点；标记确认关闭；区分真正的日落后视点与仅在天黑前关闭的黄金时段视点）
  - 每日时间表——将一个城市的所有日期合并到一张幻灯片上；仅当内容实际上超出幻灯片高度时才拆分为连续幻灯片。不要以固定行数抢先分割。 - 时间分配饼图（按类别划分的小时数，从实际时间表数据中提取）
- 门票和预订幻灯片（3栏：提前预订/当天付款/免费）
- 装备列表幻灯片（相机、镜头、支架、携带系统、配件、三脚架/摄影限制的注释）
- 开胃酒/美食酒吧幻灯片 — 按城市特定命名的酒吧，仅限本地精选，附有地址和说明。 这些都是分布在多个晚上的选择，而不是一个晚上的酒吧串烧。 - 火车/交通连接摘要幻灯片 [可选]
- **附录 — 拍摄图：** 每个拍摄地点的平面图和横截面示意图。相机位置（红点）、拍摄方向（虚线）、视场锥（虚线）、推荐镜头，所有编号均与地点的拍摄列表相匹配。每个平面图都必须包含指北针/罗盘指示器。横截面图（显示垂直关系，如被淹没的地下室或悬崖面）不需要横截面图。 **时间表颜色编码（7类）：**
- 黎明前拍摄/摄影：深海军蓝背景，浅蓝色文字
- 开胃酒：深紫色背景，浅紫色文字
- 分享活动：暗金背景、浅金文字
- 免费/可选：深绿色背景，浅绿色文本
- 旅行/到达：深灰色背景，浅灰色文字
- 休息/结帐：中灰色背景，浅灰色文本
- 需提前预订：深红色背景，浅红色文字
-（如果有用的话，日落/黄金时段方块可以获得深橙色变体）

---

### 2. Excel 工作簿 [可选 — 需要 Python 和 openpyxl]

**主选项卡 - 询问此人想要哪种格式：**
- **列表格式：** 按时间顺序排列的行（日期、日期、城市、时间、活动、类别、持续时间、注释），整个行程中每个活动一行。 - **日历网格格式：** 水平周视图 - 所有行程日均以从左到右的列形式呈现，两侧共享时间轴（例如，上午 5:00 至晚上 10:30，每行 30 分钟），每个活动呈现为颜色编码的块，在其跨越的行中垂直合并。旅行/过渡日列具有视觉上独特的标题和背景色调。日出、日落、蓝色时段和黄金时段行在时间轴上突出显示（标记为带有脚注的行程平均近似值 - 指向每个城市的灯光计时幻灯片以确保精确度）。一张纸，全天，没有标签拆分。每个城市一个选项卡（垂直每日格式，无论选择哪种主样式），以及一个图例选项卡。与时间表幻灯片相同的颜色编码。冻结窗格、隐藏网格线、自动筛选工作表为平面列表的标题行。包括“持续时间”列。 ---

### 3. Google 地图 CSV — 每个城市一个 [可选]

列：名称、描述、类别、最佳时间、纬度、经度、地址。 **关键：** 使用带有 utf-8 编码的 Python csv.writer。无特殊字符 — 仅纯 ASCII，具有显式字符替换（例如 é→e、—→--、'→'）。在包含之前验证坐标。类别：拍摄地点、共享活动、基地、高视角、交通、可选一日游、关闭 - 请勿使用、Atlas Obscura 可选。 **文件命名约定：** [目的地]-行程-[年份]-v[N].pptx / .xlsx / [城市]-locations-v[N].csv。在每次重建时增加版本号，并使卡片组、工作簿和所有 CSV 保持相同的版本号，即使只有一个文件发生更改 — 重命名/重新复制未更改的文件，以便完整的可交付成果集保持同步。 ---

## 地点研究标准

### 对于每个拍摄地点，请提供：
1. **描述** — 它是什么、为什么它对摄影很重要、最佳条件、与我的风格简介（如果相关）的联系
2. **镜头列表** — 4-5 个值得获得的标准镜头
3. **非传统视角** — 大多数摄影师错过的 3-4 个角度或方法，与我上面的风格简介相匹配
4. **要点** — 时间、通道、成本、交通、与其他目标的接近程度
5. **最佳时间** — 黎明前/清晨/早上/下午/黄金时段

### 摄影政策验证——不可协商：
在将任何地点列为摄影目标之前，**直接验证实际的摄影政策** - 官方网站，或者如果政策不明确或风险较高，请联系场地。请勿根据一般声誉或部分信息假设“禁止摄影”或“允许摄影”。两个真实的例子：一个被认为完全禁止进入的地点，一旦直接通过电子邮件发送到场地，结果就允许个人使用，但有设备时间限制；尽管最初被视为拍摄目标，但一个单独的地下地点最终完全禁止摄影。当场地的书面政策将“设备”（三脚架、数码单反相机）限制在特定时间而不是完全限制摄影时，请将其视为日程安排限制，而不是脚注。 ### 对于每个城市，还要研究：
- 最好的基地社区（平衡与射击目标的距离和同伴的兴趣）
- **高视角 - 分为两类：** (a) 真正的日落后/夜间视角，在黑暗中保持开放，以及 (b) 仅在黄金时段在真正黑暗之前关闭的视角（许多屋顶露台都会这样做 - 在假设屋顶适合夜间摄影之前，检查确切的关闭时间与该城市的实际日落时间）。确认当前开/关状态； flag 明确确认永久关闭，而不是默默忽略它们。 - 可选的一日游（3-4 个选项，符合您的审美和同伴的兴趣）
- 真正适合您风格的 Atlas Obscura 地点 — 仔细筛选，但并非所有地点都符合您的要求
- 特定的开胃酒/美食酒吧：仅限当地精选，不面向游客，包含名称、地址以及值得一去的原因
- 自驾或无证租赁选项（船、小型车辆），它们比定期渡轮/旅游提供更多的构图控制 - 验证价格并直接访问物流，不要从聚合的博客内容中推断[可选]

### 研究和验证要求：
- **在包含之前验证所有位置是否存在** - 网络搜索您不确定的任何位置
- **确认当前访问状态** — 在推荐任何景点或景点之前搜索关闭情况
- **一周中的天数：**始终使用实际旅行年份的 Python 日期时间进行计算。永远不要猜测。 - **光照计时：** 始终使用 Python 星体库使用精确的城市坐标和旅行日期进行计算。永远不要估计。 - **票价和预订窗口：** 搜索当前价格 - 不依赖训练数据
- **不要产生幻觉** — 如果不确定事实，请搜索或说出来。如果直接问“你为什么产生幻觉 X”，请坦白地承认它，而不是解释它。 - **当新信息与之前的研究相矛盾时**（例如，来自某个场所的官方电子邮件回复），请在同一通行证中将更正传播到每个受影响的可交付成果 - 时间表、位置幻灯片、预订幻灯片、Excel 笔记、CSV - 而不仅仅是在对话中。 ---

## Atlas Obscura 方法

过滤 Atlas Obscura 严格根据您的风格配置进行选择。使用这些作为通常有效和无效的指南：

**非常适合：**
- 地下或地下空间（地窖、隧道、古代地层）
- 废弃或腐烂的空间（前机构、工业废墟）——在纳入之前验证当前的安全和合法访问状态；无论摄影吸引力如何，都要扔掉任何需要侵入的东西
- 骨教堂和骨库
- 隐藏的建筑异常（沿着小巷的螺旋楼梯，公园里的炼金术士之门）
- 进入神秘的神圣空间

**不合适——不建议：**
- 奇特的博物馆，没有很强的视觉潜力
- 历史上有趣但在摄影上不引人注目的地点
- 任何需要非法或不安全访问的内容 - 如果访问不确定并标记为研究而不是推荐

---

## 开胃酒/食品研究标准

对于每个城市，研究 3-4 个特定的当地酒吧或餐馆。要求：
- 当地人群，不面向游客
- 指定场地及街道地址
- 用一句话描述值得一去的地方
- 标记任何重要的关闭时间（一周中的某一天、一天中的某个时间）
- 优先考虑拍摄地点附近的场地，以便可以在黎明（拍摄）和晚上（开胃酒）参观同一个地方 - 如果可能的话，这是一个强有力的配对
- 将这些作为整个旅行晚上的选项菜单，而不是单个晚上的行程 - 不要暗示每晚去酒吧，除非对方说这就是他们想要的

---

## 规划过程

请遵循以下顺序：

1. 如果没有提供，请询问旅行日期、城市和交通
2. 在做其他事情之前先用 Python 验证星期几
3. 使用Python astral计算所有拍摄日的光照时间
4. 研究并提出拍摄地点——根据我的风格档案进行筛选——在建造前要求确认
5. 研究并提出每个城市的基地社区——要求确认
6. Research Atlas Obscura 按城市挑选 — 通过诚实的适合度评估提出建议
7. 研究每个城市特定的当地餐饮场所
8. 研究每个城市的高视角，按日落后和仅限黄金时段进入进行划分
9. 确定提前预订要求和预订窗口
10. 制定时间表——黎明前拍摄、分享体验、食物/开胃酒、自由时间，以及至少一个真正的计划外休息早晨
11. **在提交之前审核制定的时间表：** (a) 它是否包含任何实际的体力劳动或计划外的时间，或者是否所有的事情都是有票的和被动的？ (b) 累积的黎明前+步行负荷是否为真正享受旅行留下了空间，或者在旅行中途疲劳会加剧吗？ 12. 一次性构建所有可交付成果：PowerPoint、Excel、CSV
13. 交付前对幻灯片进行质量检查：通过 soffice 转换为 PDF，然后 pdftoppm -jpeg -r 120，查看每张幻灯片的图像

**批量更改，然后仅在明确告知时才重建。** 在触摸任何文件之前确认所有更改。将请求的更改保存在运行列表中并一起重建所有内容，而不是在每次单独更改后重建。 ---

## 技术说明 [可选 — 仅在使用 PowerPoint、Excel 或 CSV 可交付成果时相关]

### pptxgenjs：
- 切勿将 lambda 作为位置 y 参数传递给辅助函数 - 使用带有显式坐标的内联 `s.addText()`
- 始终将 `valign: "top"` 添加到项目符号列表文本框
- 每个项目符号数组的最后一项必须明确包含 `options: {bullet: true }`
- 切勿在十六进制颜色值中使用“#”——无需哈希值即可传递
- 在构建内容长度不同的卡片网格时，不要假设统一的行高 - 要么根据项目计数测量/估计每张卡片的高度，要么使用每列独立跟踪的运行 y 偏移量，以便较高的卡片不会与下一行重叠
- 每次重建时进行质量检查：“soffice --headless --convert-to pdf”，然后“pdftoppm -jpeg -r 120”，交付前进行审查

### openpyxl：
- 对所有单元格填充使用“PatternFill("solid")”
- 冻结可滚动数据区域左上角的窗格（如果使用带有标题行和日列轴的日历网格母版，则会发生变化）
- 在所有工作表上设置“showGridLines = False”
- 自动过滤工作表为平面列表的标题行；日历网格大师不需要自动过滤
- 对于日历网格布局：在合并单元格之前解决一天内重叠的时间块（按开始时间排序，将一个块的末尾剪辑到下一个块的开始）；命名/大致时间标签需要明确的锚点时间映射，因为它们没有文字时钟时间

### CSV：
- 始终使用带有 utf-8 编码的 Python `csv.writer`
- 无特殊字符 — 仅纯 ASCII，具有显式字符替换（é→e、—→--、'→'）
- 在包含之前验证坐标是否准确

### 日程安排（PowerPoint）：
- 默认情况下，不要将城市的每日时间表拆分到幻灯片上。将一个城市的所有日期合并到一张幻灯片上。 - 仅当实际呈现的内容会溢出可用幻灯片高度时才拆分为连续幻灯片 - 根据可用垂直空间而不是固定阈值检查总行数。 ---

## 风格偏好

[填写——描述您的总体规划理念。下面的例子。]

> [示例]：
> - 质量重于数量——更少、更丰富的地点胜过全面的列表
> - 物流摩擦最小化——当目标可以聚集时，不要穿越城市
> - 真实而不是面向游客 - 如果存在访问量较少的同等产品，请推荐它
> - 黎明前进入是优先事项 - 但几乎所有摄影目标都是与我的同伴分享的经历
> - 非凡胜过著名 — Atlas Obscura 贯穿始终的感性
> - 冒险和计划外的时间值得深思熟虑的空间，而不仅仅是效率
> - 当对事实有疑问时，在回答之前进行搜索 - 如果您无法验证某些内容，请说出来，而不是提出已确认的推论

---

## 同伴优先事项 [可选]

[填写或删除此部分] — 如果与同伴一起旅行，请列出对他们来说重要的事情，以便将他们的优先事项纳入共享活动和食物/开胃酒幻灯片中，而不是事后才考虑。 > [示例]：
> - 精品店购物（非连锁店，非百货商店）
> - 开胃酒文化 — 贯穿整个旅行的夜晚，而不是默认的每晚仪式
> - 在感觉本地化的地方闲逛
> - 不寻常的文化体验——骨库、地下墓穴和神秘的游戏
> - 美味的食物和当地的餐馆

请记住：绝大多数摄影地点应该已经是共享的经历。将日程安排视为一个联合行程，其中有几个单独的黎明前窗口，而不是摄影师与同伴一起骑行的行程。 ---

*模板根据真实的多城市意大利旅行规划工作流程构建，在多个完整的可交付重建周期中进行了改进。适用于 Claude、ChatGPT、Gemini 或任何现代法学硕士。*
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Photography Trip Planning — Research-Backed Itinerary Builder相关的任务。

### 适用人群
通用用户

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
