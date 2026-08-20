import json

data = json.load(open('/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_8.json'))

p28_orig = data[28]['prompt']

# Translate prompt 28 with high fidelity
p28_zh = """# 摄影旅行规划提示词
## 旅行摄影师可复用模板
### v3.0

---

> **本模板的两种使用方式：**
>
> **轻量模式** — 跳过所有标有 `[OPTIONAL]`（可选）的章节以及整个“技术说明”章节。填入你的风格画像和行程详情，然后让 Claude 生成基于文本的调研简报和逐日行程表。无需运行脚本。
>
> **全功能产出模式** — 使用所有章节。Claude 将生成 PowerPoint 演示文稿（通过 Node.js + pptxgenjs）、Excel 工作簿（通过 Python + openpyxl）以及 Google Maps CSV 文件——全部经过配色规范与质量检查（QA）。需要能够在命令行运行脚本。
>
> 两种模式下：请填写所有标有 `[FILL IN]`（填写）的章节。标有 `[EXAMPLE]`（示例）的章节展示了完整条目的样式——请替换为你自己的具体信息。标有 `[OPTIONAL]`（可选）的章节如果不符合你的工作流可以删除。

---

## 个人基本信息 (WHO I AM)

我是一名旅行摄影师，正在计划一次[有同行伴侣 / 无同行伴侣]的旅行。我的名字是 [FILL IN — 姓名]。

---

## 我的摄影风格 (MY PHOTOGRAPHIC STYLE)

[FILL IN — 描述你的摄影美学与偏好。参考下方示例。]

> [EXAMPLE]:
> - 核心审美：建筑、对称性、历史分层、地下与神秘空间、晨曦微光、大理石与石材肌理、光影明暗对比。
> - 视觉偏好：避免明显的现代杂乱元素；偏好庄严沉静、空灵神秘的画面而非人头攒动的经典明信片机位。
> - 拍摄时段：日出/黎明前（无游客、光线柔和）、蓝调时刻（夜景与环境光平衡）、金色时刻（若拍摄点有开阔西向视野）。
> - 常用焦段与题材：广角建筑内部透视、中焦局部几何构图、长焦压缩空间层次。

---

## 同行伴侣 (TRAVEL COMPANION) [OPTIONAL]

[FILL IN — 如果有伴侣同行，描述其偏好与旅行步调。若独自旅行请删除本节。]

> [EXAMPLE]:
> - 伴侣偏好：精品街区漫步、本地特色美食、小众独立咖啡馆、手工艺品店与特色集市。
> - 体能与节奏：清晨拍摄可偶尔独行，大部分白天的游览需兼顾双方兴趣，每天预留下午茶或休息时段。

---

## 行程概况 (THE TRIP)

[FILL IN — 填写旅行目的地、日期、主要交通方式等。]

> [EXAMPLE]:
> - 目的地城市：罗马、佛罗伦萨、威尼斯
> - 出行日期：2026年10月10日 — 2026年10月24日
> - 交通方式：城际高铁 + 市内步行与公共交通

---

## 期望 CLAUDE 生成的交付成果 (WHAT I WANT CLAUDE TO BUILD)

### 1. PowerPoint 演示文稿 [OPTIONAL — requires Node.js and pptxgenjs]
- 每个城市独立展示页：包含每日拍摄时序表、核心机位卡片、机位预览图占位与参数建议。
- 采用专业暗色或极简设计风格，所有文本框与网格自适应排版。

### 2. Excel 完整行程规划表 [OPTIONAL — requires Python and openpyxl]
- Master 标签页：按日历网格/时间轴展示全天计划（拍摄时段、公共活动、餐饮、空闲休息）。
- Shooting Locations 标签页：包含地点名称、经纬度、最佳光线时段、门票与拍摄许可要求、器材建议及机位要点。
- Logistics & Bookings 标签页：交通预订、门票预约窗口期及确认状态。

### 3. Google Maps CSV 地图标记文件 [OPTIONAL]
- 每个城市一个 CSV 文件，包含 Name, Latitude, Longitude, Description, Category 等标准字段，可直接导入 Google My Maps。

---

## 地点调研标准 (LOCATION RESEARCH STANDARDS)

### 对于每个拍摄地点，需提供：
- 精确名称与官方英文/当地语言名称
- 经纬度坐标（需严格验证）
- 最佳拍摄时段（基于太阳方位与光线角度分析，如黎明前、金色时刻、蓝调时刻）
- 拍摄角度与构图建议（主视角、特殊细节机位）
- 门票预订需求及开放时间
- 器材建议（如超广角、三脚架限制等）

### 摄影政策核验（非协商项）：
- 严查是否允许携带三脚架/单脚架
- 严查商业拍摄与个人摄影限制
- 室内拍摄是否允许背包或闪光灯

### 对于每个城市，还需调研：
- 推荐下榻街区（Base Neighborhoods）：优先兼顾日出机位步行可达性与周边生活便利度。
- 高处俯瞰视角（High Viewpoints）：区分日落金色时刻机位与天黑后开放的夜景观景台。
- 当地日落开胃酒/餐饮推荐（Aperitivo / Food）：每座城市推荐 3-4 家地道非游客导向的餐酒吧。

### 调研与验证要求：
- **拒绝幻觉**：若对某项事实不确定，先进行检索或如实说明。
- **信息修正同步**：当获得新的官方信息时，一次性同步修正所有交付物（PPT、Excel、CSV、对话）。

---

## ATLAS OBSCURA 小众探秘策略 (ATLAS OBSCURA APPROACH)

严格对照风格画像筛选 Atlas Obscura 推荐点：

**高度契合（优先推荐）：**
- 地下空间（地下墓穴、古地层遗迹、古代水利隧道）
- 废弃与历史遗迹（经合法且安全确认的废墟或古迹）
- 人骨礼拜堂与圣骨室（Ossuaries）
- 隐藏的建筑奇观（隐蔽螺旋楼梯、炼金术士之门等）
- 具有神秘/崇高感的特殊圣所空间

**不契合（不要推荐）：**
- 缺乏视觉冲击力的普通猎奇博物馆
- 历史意义虽重但摄影美学价值低的地点
- 涉及非法进入或安全风险的区域

---

## 开胃酒与地道美食调研标准 (APERITIVO/FOOD RESEARCH STANDARD)

每个城市调研 3–4 家具体的当地特色餐馆/酒吧：
- 面向本地居民，非游客扎堆网点
- 具备明确名称与街道地址
- 一句话说明其值得前往的核心特色
- 标明公休日期与营业时间段
- 优先选择邻近拍摄点的场所（实现晨曦拍摄与晚间小酌的空间结合）

---

## 规划工作流 (PLANNING PROCESS)

请遵循以下顺序执行：
1. 确认行程日期、城市及交通方式
2. 使用 Python 脚本核实具体星期几与公休日
3. 使用 Python astral 库计算所有拍摄日的准确日出、日落、晨昏蒙影时间
4. 调研并提议拍摄机位 — 经风格画像过滤后向用户确认
5. 调研并提议各城市下榻街区 — 向用户确认
6. 调研各城市 Atlas Obscura 小众探秘点
7. 调研各城市地道美食/酒吧
8. 调研高处俯瞰机位并按开放时段分类
9. 梳理需提前预约的门票与预订窗口
10. 构建完整日程表（黎明拍摄、共享活动、餐饮、自由探索及至少一个无计划休息日上午）
11. **在展示前对日程进行审查**：是否留有充足的体能缓冲与非计划探索空间
12. 一次性构建全部交付物：PowerPoint、Excel、CSVs
13. 对幻灯片进行 QA 验证（转 PDF 并渲染图片检查排版）

---

## 技术说明 [OPTIONAL — 仅在使用代码生成交付物时参考]

### pptxgenjs:
- 避免使用 lambda 作为 y 坐标；使用显式坐标参数
- 列表文本框添加 `valign: "top"`
- 项目符号数组最后一项需显式包含 `options: { bullet: true }`
- 十六进制颜色代码不要包含 `#` 前缀
- 针对变长卡片网格，动态计算 y 偏移防止重叠

### openpyxl:
- 单元格填充使用 `PatternFill("solid")`
- 在可滚动数据区域左上角冻结窗格
- 所有工作表设置 `showGridLines = False`
- 处理日历网格的时间块重叠与合并逻辑

### CSVs:
- 使用 Python `csv.writer` 配合 utf-8 编码
- 确保经纬度数据精确无误

---

## 风格偏好与设计哲学 (STYLE PREFERENCES)

[FILL IN — 描述你的旅行哲学]
- 质量胜过数量：宁要深度打磨的少量机位，不要泛泛打卡
- 低物流摩擦：同区域机位集中规划，减少城市往返折腾
- 真实小众胜过大众地标：有优质小众替代项时优先推荐

---

## 伴侣优先级 [OPTIONAL]

[FILL IN 或删除本节]
- 小众精品店与手工艺工坊
- 融入当地日常的街区漫步
- 特色餐饮与开胃酒文化
- 兼具视觉与趣味的文化奇观探索"""

items = [
    {
        'id': 'cmpg3k4i90003lb04iwbgi9rb',
        'title_zh': '红发纹身女性肖像生成提示词',
        'zh': '我想要一个红发女性，身上有纹身，身材丰满迷人。',
        'usage': '该提示词适合 AI 绘画和数字艺术创作者使用，用于生成具有鲜明外貌特征（红发、纹身、丰满身材）的人物角色肖像。使用时可配合具体的艺术风格（如写实摄影、赛博朋克插画、动漫风等）和背景环境描述输入给 Midjourney 或 Stable Diffusion 等图像生成工具。'
    },
    {
        'id': 'cmpgzfwoa0005k0049301eozo',
        'title_zh': '简历标准化职业档案构建器 v1.1.3',
        'zh': '''# TITLE: Career Profile from Resume Builder
# VERSION: 1.1.3
# AUTHOR: Scott M
# LAST UPDATED: 2026-05-21
#
# CHANGELOG:
# · v1.1.3 (2026-05-21): Added filename normalization rules (no suffixes/certs, spaces to underscores) and strictly banned conversational filler between codeblocks.
# · v1.1.2 (2026-05-21): Isolated the suggested filename into its own independent codeblock at the start of output.
# · v1.1.1 (2026-05-21): Added standardized file naming convention output block before the main report.
# · v1.1.0 (2026-05-21): Added RESUME FORMAT & STRUCTURE AUDIT to catch ATS parsing risks and layout issues.
# · v1.0.1 (2026-05-21): Hardened PROFESSIONAL SUMMARY block to favor direct extraction and minimize semantic drift.
# · v1.0.0 (2026-05-21): Initial release. Canonical profile normalization and basic gap analysis.

============================================================
PROMPT PURPOSE
============================================================
将用户提供的简历转换为结构化、标准化的职业档案。

这是一个非交互式转换工具：
· 请勿提问
· 请勿进行面试交流
· 请勿请求进一步澄清
· 请勿与用户进行多轮迭代

输入 → 简历文本  
输出 → 文件名代码块 + 主档案报告代码块（严禁输出任何寒暄对话废话）

============================================================
CORE BEHAVIOR
============================================================
扮演一名精准的职业数据标准化专家。

你的职责是：
· 从简历中提取结构化的职业数据
· 将格式规范化为一致的档案模式（Schema）
· 保留所有客观事实信息，不篡改原意
· 仅将缺失或不明确的信息标记为缺陷（Gaps）
· 杜绝任何主观假设或虚构编造

如果某项信息缺失：
· 显式标记为 [NOT PROVIDED]
· 切勿擅自推断或猜测

============================================================
FORMATTING RULES
============================================================
· 所有无序列表使用中圆点（ · ）
· 输出必须精确包含两个 Markdown 代码块，且在代码块之前、之间或之后绝对不能出现任何闲聊文字或引导/结语
· 保持结构清晰且具备良好层级
· 请勿使用 Emoji 表情或多余修饰

============================================================
DATA NORMALIZATION RULES
============================================================
· 日期（Dates）→ "MMM YYYY – MMM YYYY" 或 "Present"
· 职位角色（Roles）→ "[Title] – [Company], [Dates]"
· 技能（Skills）→ 仅包含明确提及的技能
· 工具（Tools）→ 仅包含明确提及的工具
· 经验时长（Experience duration）→ 仅在明确说明时列出
· 文件名提取（Filename Extraction）→ 移除所有专业后缀或认证缩写（例如 CISSP、CEH、MBA）。将所有空格转换为下划线。格式必须严格为：Career_Profile_[First_Last].md

============================================================
OUTPUT STRUCTURE
============================================================
处理完成后，严格按顺序输出以下两个代码块，代码块周围或中间不得有任何文本：

[START FILENAME CODEBLOCK]
Career_Profile_[Normalized_First_Last].md
[END FILENAME CODEBLOCK]

[START REPORT CODEBLOCK]
Career Profile from Resume (Canonical Record)

USER JOB TARGET (if stated in resume):
· [or: NOT PROVIDED]

PROFESSIONAL SUMMARY:
· [Direct extraction of the existing summary. If no summary exists, synthesize a 2-sentence overview using only exact nouns and metrics from the history.]

JOB HISTORY (Recent First):
[Repeat the following block for each role found in the resume]
· Role: [Title] – [Company], [Dates]
  · Responsibilities:
  · Achievements:
  · Tools/Technologies:
  · Notes: [only factual extraction]

TECHNICAL SKILLS:
· [Skill list from resume only]

CERTIFICATIONS:
· [List or NOT PROVIDED]

EDUCATION:
· [List or NOT PROVIDED]

PROJECTS:
· [Only if explicitly present]

GAPS & MISSING INFORMATION:
· Metrics missing (impact, %, $, scale)
· Tool durations missing or unclear
· Timeline ambiguity present / not present
· Scope unclear (team size, systems, environment)
· STAR stories absent (if not present)

RESUME FORMAT & STRUCTURE AUDIT:
· ATS Parsing Risks: [Identify heavy tables, text boxes, headers/footers, or non-standard fonts that will break ATS]
· Hierarchy & Layout: [Report if section headers are non-standard, disorganized, or hard to scan]
· Formatting Consistency: [Flag mixed date formats, irregular bullet types, or sloppy alignment]

IMPORTANT NOTES:
· This profile is a structured transformation of provided resume content only
· No external enhancement has been applied
[END REPORT CODEBLOCK]

============================================================
INPUT DATA
============================================================
[PASTE RESUME BELOW THIS LINE]''',
        'usage': '该提示词适合求职者、猎头及职业规划师使用，用于将非结构化的杂乱简历文本无损提取并格式化为标准化的职业档案 Markdown 报告，同时进行 ATS 机器筛选风险审计与信息缺陷诊断。使用时将该提示词整段复制，并在底部的 [PASTE RESUME BELOW THIS LINE] 后粘贴简历正文即可。'
    },
    {
        'id': 'cmpndtobu0007l50476wb80tg',
        'title_zh': '光伏与储能系统工程方案设计',
        'zh': '''扮演一名专业的光储系统工程师。你负责为光伏电站、储能电站以及整体能量管控系统设计并生成综合规划方案。你的任务包括整合以下要素：

- 光伏与储能系统升压及降压变压器
- 并网柜（Grid-connected cabinets）
- 环网柜（Ring main units）
- 开关设备（Switches）
- 联络母线（Coupling busbars）

除上述内容外，请根据提供的系统配置、产品清单和项目名称生成系统电气主接线图/拓扑架构。

你将：
- 为每个系统组件创建详细原理图说明
- 确保组件之间高效的能量流动与电气连接
- 优化系统设计以实现最大化能效与可靠性

规则：
- 严格遵循行业技术标准与安全规范
- 采用最新技术与最佳工程实践
- 为不同规模的工程运营提供可灵活调整的解决方案

你的输出应包含清晰的系统架构图与落地实施技术规范。''',
        'usage': '该提示词适合新能源电气工程师、光伏储能方案设计师及微电网项目经理使用，用于设计高可靠性的光储一体化电站电气系统架构与技术方案。使用时提供具体的光伏装机容量、储能电池配置、并网电压等级及主要设备型号清单，AI 将据此输出包含主接线逻辑、变压与配电设备选型及安全规范的系统方案。'
    },
    {
        'id': 'cmpoqx1x20005ld04vdbg2hyy',
        'title_zh': '坚持长期主义的代码实现原则',
        'zh': '在代码实现时偏向于能够减少后期维护成本并提升代码质量的长期主义原则性解决方案。不要默认采用改动行数最少（Smallest-diff）的权宜补丁修法。',
        'usage': '该提示词适合软件工程师在与 AI 结对编程、重构系统或修复架构缺陷时作为系统级规则或即时约束使用。它能有效遏制 AI 倾向于为了完成任务而堆砌最小打补丁代码（Quick hack）的短视行为，促使 AI 采用更具可维护性、扩展性和遵循清晰设计模式的优质架构方案。'
    },
    {
        'id': 'cmppdtjmt0001l5042kt8txkk',
        'title_zh': '高效软件研发团队组织架构与协作规范',
        'zh': '''```markdown
# 综合编程研发团队组织架构
> **使命：** 通过清晰的角色定义、稳健的沟通机制与持续创新的文化，建立健全、高效的软件开发流程。

作为你的团队架构师，我构建了这支研发战队，以最大化效率、创新力与协作力。以下是涵盖五大核心角色（包括确保团队闭环所必需的质量保障角色）、使用工具及运营规范的完整指南。

---

## 👥 核心团队：角色、职责与 KPI

为确保目标清晰并避免任务交叉重叠，每个角色都严格定义了具体目标、职责和关键绩效指标（KPI）。

### 1. 团队大脑 (Lead Architect / Strategist 首席架构师/战略专家)
*   **目标：** 引领战略思考、技术创新与高层系统架构设计。
*   **职责：** 
    *   构建软件技术底座并做出核心技术选型。
    *   攻克复杂技术瓶颈并预先规划高扩展性。
    *   指导团队落地工程最佳实践与新技术。
*   **KPIs：** 系统可用性（Uptime）、技术债务比率、创新特性的成功落地率。

### 2. 任务分配者 (Scrum Master / Agile Coach 敏捷教练)
*   **目标：** 管理工作流、推进敏捷流程并确保合理均衡的工作负载。
*   **职责：**
    *   将项目里程碑拆解为可执行的工单（Tickets）。
    *   在团队成员间高效分发任务，防止人员倦怠。
    *   清除阻碍开发进度的各类阻碍（Blockers）。
*   **KPIs：** Sprint 完成率、周期时间（Cycle time）、团队速率（Team velocity）。

### 3. 程序员 (Software Engineer 软件工程师)
*   **目标：** 执行代码编写、构建业务功能并保障软件质量。
*   **职责：**
    *   根据分配的任务编写整洁、可维护且高效的代码。
    *   参与代码评审（Code Review），与架构师紧密协作。
    *   排查并修复软件缺陷。
*   **KPIs：** 代码行数/合并的 PR 数量、单功能缺陷率、代码评审周转时效。

### 4. 管理者 (Project / Product Manager 项目/产品经理)
*   **目标：** 把控项目时间线、管理干系人沟通及团队整体协作。
*   **职责：**
    *   定义产品路线图并梳理待办列表（Backlog）优先级。
    *   提供卓越领导力，引导团队达成共同商业目标。
    *   保持团队士气并争取必要资源。
*   **KPIs：** 里程碑按时交付率、干系人满意度评分、预算偏差度。

### 5. 质量保障专家 (QA / Tester 测试工程师)
*   **目标：** 确保所有交付成果在发布前达到最高质量标准。
*   **职责：**
    *   设计并实施自动化与手动测试协议。
    *   发现、记录并追踪缺陷直至完全解决。
    *   验证专业技术能力是否转化为完美无瑕的用户体验。
*   **KPIs：** 缺陷逃逸率（Defect escape rate）、测试覆盖率百分比、缺陷平均修复解决时长。

---

## 🛠️ 团队支撑体系与工具生态

为平衡工作负载并确保顺畅执行，团队依赖以下明确定义的运营生态：

| 类别 | 解决方案 / 策略 | 用途 |
| :--- | :--- | :--- |
| **项目管理** | Jira, Trello | 跟踪进度、管理 Backlog、指派日常任务。 |
| **共享工作区** | Slack, Microsoft Teams | 支持异步协作与每日同步。 |
| **技术栈基建** | Git, CI/CD Pipelines | 版本控制及开发与 QA 工作的无缝集成。 |

---

## ⚙️ 运营规范与工作流

### 1. 同步与例会
*   **每日站会（Daily Stand-ups）：** 由敏捷教练主持的 15 分钟严格会议，讨论*昨天完成了什么、今天计划做什么、当前有什么阻碍*。
*   **Sprint 规划与复盘会（Sprint Planning & Retrospectives）：** 由经理主导的双周会议，对齐目标、复盘 KPI 并持续改进流程。

### 2. 沟通与协作
*   **彻底坦诚（Radical Candor）：** 营造清晰、建设性反馈的沟通环境。
*   **文档化沉淀：** 所有架构决策（架构师）和流程规范（经理）必须沉淀在统一 Wiki（如 Confluence 或 Notion）中。

### 3. 持续学习与关怀
*   **技术提升时间：** 每周保留 10% 工时用于调研新技术、参加技术讲座或提升技能。
*   **知识分享会：** 每月举办“午餐分享会（Lunch & Learn）”，由成员分享新工具、设计模式或测试方法。
*   **负载监测：** 敏捷教练与经理主动监控看板，确保无单点过载，动态调配资源以维持高昂士气。
```''',
        'usage': '该提示词适合技术总监、工程主管、创业公司 CTO 及敏捷教练使用，用于为技术研发团队快速建立完备的五大角色职责定义、敏捷协作机制、工具链生态及 KPI 考核模型。可直接用于团队管理规范制定、新员工入职手册编写或组织架构重组。'
    },
    {
        'id': 'cmptw251o0001ib04gv9730bv',
        'title_zh': '尼日利亚国家发展问题智慧咨询',
        'zh': '我希望你扮演一名卓越的智囊专家，与我共同协作，针对尼日利亚的国家现状与挑战主动向我提问，以共同探寻解决当前问题的方案。让整个对话充满远见与智慧。',
        'usage': '该提示词适合公共政策研究者、国际发展学者及关心尼日利亚经济社会的学者使用。它让 AI 采取顾问式苏格拉底提问法，围绕尼日利亚面临的经济、安全、能源及治理挑战展开深度探讨与智慧启发。使用时直接发送提示词，AI 会主动发起关键提问引导你深入分析。'
    },
    {
        'id': 'cmpv7mzlw0001lf04k6rnobt5',
        'title_zh': '全国连锁门店员工两周基础电脑技能培训方案',
        'zh': '为一家在全国各地均设有连锁门店的企业，起草一份为期两周的基础计算机技能培训计划。',
        'usage': '该提示词适合企业 HR、培训主管、连锁零售运营总监使用，用于为全国分布式网点基层员工制定结构清晰、可落地的两周电脑入门培训大纲。使用时可直接获取覆盖操作系统基础、收银/进销存软件操作、办公协同软件及网络信息安全的系统化课程安排。'
    },
    {
        'id': 'cmpvf58ql0004jo04pb6do35f',
        'title_zh': '参数化定制电子邮件生成器',
        'zh': '''撰写一封关于 ${topic}、收件人为 ${recipient} 的 ${tone:professional|friendly} 风格电子邮件。

该邮件应：
- 字数约为 ${length:200} 字
- 包含明确的行动号召（Call to Action）
- 使用 ${language:English} 语言''',
        'usage': '该提示词适合职场人士、外贸业务员及跨部门沟通者使用，用于快速生成语气、字数与语言均可参数化定制的专业商务或日常邮件。使用时替换或保留默认参数（如语气 ${tone}、收件人 ${recipient}、主题 ${topic}、字数 ${length} 和语种 ${language}），AI 即可按规范生成结构完整的邮件。'
    },
    {
        'id': 'cmr2g3yw90001l7048veoh3xd',
        'title_zh': '旅行摄影师深度调研型行程规划模板 v3.0',
        'zh': p28_zh,
        'usage': '该提示词是一套专为风光与人文旅行摄影师打造的高保真行程规划系统模板（v3.0）。支持轻量文本模式与基于 Python/Node 自动化生成 PPT、Excel 日历看板及 Google Maps CSV 的全功能模式。使用时根据自身需求填写个人摄影风格、目的地、机位光影偏好与同行伴侣要求，AI 将依据太阳方位角计算与安全合规标准生成精准的逐日拍摄日程与交付物。'
    },
    {
        'id': 'cmr45e6wy0001ii04mbf4ewr5',
        'title_zh': '媒体精英训练营电影级宣传视频分镜生成',
        'zh': '''为“媒体素养卓越训练营”（Media Presence Excellence Camp）的发布创作一个 10 秒的极致电影级宣传视频脚本与视觉提示词。

视频在黑色背景与极具戏剧性的光影中开场。一只逼真的人手进入画面，手握一支专业麦克风。每过一秒，该物体平滑变形（Morph）转换为另一种高端媒体工具：广播级麦克风、专业单反相机、电影机、高级摄影镜头、无线领夹麦克风以及电视台转播摄像机。

运用无缝变形转场、动态特写镜头、慢动作细节与电影级布光。加入微妙的光斑条纹与现代视觉特效，以彰显创新、专业精神与媒体卓越品质。''',
        'usage': '该提示词适合视频编导、广告创意人及 AI 视频创作者（如 Runway Gen-2/Gen-3、Sora、Luma Dream Machine）使用，用于生成高端培训营发布的 10 秒快节奏无缝形变转场宣传片分镜。使用时可直接作为视频生成提示词或用于指导后期动态视觉设计。'
    }
]

out_file = '/Users/tylertang/Developer/ai-coding/tprompts-site/agent_chunks/agent_chunk_8_out.ndjson'
with open(out_file, 'a', encoding='utf-8') as f:
    for item in items:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
print(f'Appended {len(items)} items to {out_file}')
