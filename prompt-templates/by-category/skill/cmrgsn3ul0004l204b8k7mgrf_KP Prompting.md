# KP Prompting

**Description:** Build advanced prompts, task specs, verification criteria, and Claude Code setup using Andrej Karpathy's spec / verifier / environment method. Use this skill whenever you need to spec out a task or project, tighten or rewrite a prompt, define verification or success criteria for agent output, or set up/update a knowledge base, skill, or guardrails for an agent. 

**Type:** SKILL
**Author:** tomstools11
**Created:** 2026-07-11T20:04:59.325Z
**Votes:** 0
**Views:** 0

**Tags:** Prompt Engineering, System Prompt, prompt, Skill, agent-skill, skills

**Category:** Agent Skill

## Prompt Content

```
---
name: kp-prompting
description: Build advanced prompts, task specs, verification criteria, and Claude Code setup using Andrej Karpathy's spec / verifier / environment method. Use this skill whenever you need to spec out a task or project, tighten or rewrite a prompt, define verification or success criteria for agent output, or set up/update a knowledge base, skill, or guardrails for an agent. 
---
Spec — what's actually wanted, precisely enough that the model isn't guessing
Verifier — how you (or the model) will know the output is actually right
Environment — the persistent context and guardrails so the agent doesn't relearn everything from zero every time

The thread connecting all three: you can hand off the execution, but not the understanding. Every layer below should keep Tom in the loop on the actual judgment calls, not just produce polished-looking output that papers over gaps he never got asked about.
Two modes — figure out which one you're in before doing anything else
Coaching mode (default). Tom hands you a task, a rough prompt, or a request to write instructions for something specific. Tighten it using the three-layer lens below and hand back an improved version in chat — no files. This is the default for "help me write/improve a prompt for X."
Full setup mode. Tom is standing up a new project, tool, or recurring workflow and wants the actual scaffolding: a spec doc, verification criteria, and environment setup (CLAUDE.md additions, guardrails, knowledge base pointers). Trigger this on phrases like "spec out," "set up the environment for," "build out the Karpathy method for X," or an explicit ask for all three layers.
If it's genuinely unclear which one fits, ask ONE quick question rather than guessing — building the wrong one wastes more time than asking. Most of the time it's inferable: a single task or prompt draft in hand → coaching; a new project/feature with no prompt yet → full setup.

Layer 1: Spec
Why it matters
Karpathy's example: ask a frontier model whether to drive or walk to a car wash 50 meters away, and it says walk — missing the obvious fact that the car needs to get there too. Models are excellent at anything checkable and surprisingly bad at real-world judgment calls, because judgment calls are exactly what's missing from clean training signal. A spec's job is to hand the model the judgment it can't infer on its own, so it isn't reduced to guessing at context. Shallow high-level "plan mode" style prompting doesn't do this — it's too thin to carry real understanding.
How to build one

Find the actual goal, not just the task. "Write the end-of-month report" is a task. The goal is whatever decision that report is supposed to support. If it's not obvious from what Tom said, ask — a couple of quick questions here save a much bigger rewrite later.
Work in small checkpoints, not one big dump. Handing over everything and only reconvening at a finished result lets drift compound silently. Scope the spec into pieces small enough to check at each step, especially anywhere there's real ambiguity.
Be precise about what shouldn't be assumed. Every vague word in a spec becomes an assumption the model fills in — confidently, in whatever direction is statistically likely, not necessarily what Tom actually wants. Name the specific judgment calls (naming conventions, edge cases, what happens on conflicting data) instead of leaving them implicit. A line like "flag any assumption you're making instead of silently picking one" does real work here.

What a spec should contain
Goal (the decision/outcome this serves, not just the task), scope boundaries (explicitly in vs. out), the judgment calls to flag rather than silently resolve, and constraints split into non-negotiable vs. preference.

Layer 2: Verifier
Why it matters
Karpathy's framing: these models are closer to "ghosts" than animals — statistical simulators, not motivated agents. Yelling at a model, pleading with it, or telling it something matters a lot doesn't change output quality. What changes output quality is whether there's something that can actually check the work. It's also why models are superhuman at code and math (cleanly checkable) and unreliable at taste and judgment (nothing to check against) — so the more explicit and checkable "done well" is for a given task, the more the output can actually be trusted rather than skimmed with review-fatigue.
How to build one

Set pass/fail criteria up front, in the prompt itself, not after the fact. "Make the report look good" isn't checkable. "The report has three sections and each ends with a recommendation" is. Write criteria as things a second reader — human or model — could check without reading Tom's mind.
Use a second model as a critic where it's cheap to do. A different model (or the same model in a fresh context) grading the first model's output against the spec catches things the original run will rationalize past.
Pull in real external signal when it exists. For code: does it actually deploy, do the tests pass? For non-technical work: does it match the format/tone of examples already known to be good? A verifier that only checks internal consistency is weaker than one that checks against something real.

What a verifier should contain
The specific, checkable pass/fail criteria (not vibes), who or what does the checking (self-check, second model, deployment/test signal), and what happens on a fail (retry with what specific feedback, or escalate to Tom).

Layer 3: Environment
Why it matters
Most people rebuild context from scratch every session — re-explaining the project, re-stating the rules, hoping the agent remembers what it's not supposed to touch. Keeping chat history around isn't the same as a real environment. A workshop with the tools already in place beats re-explaining the whole shop on every visit.
How to build one

A CLAUDE.md the agent reads automatically. Cover: what this workspace/repo is, what custom skills exist and when to use them, where to find things (the knowledge architecture), and the rules that always apply. This is the single highest-leverage piece since it's read on every prompt without Tom repeating himself.
A personal knowledge base. A structured, retrievable place for reference material the agent can pull from instead of re-deriving or hallucinating it. Accumulated material is a moat; a well-organized retrieval structure over it compounds every time it's used.
Reusable skills for anything repeated. If Tom's doing something a second time, it should become a skill instead of a re-explained one-off.
Guardrails enforced at the tool level, not just the prompt level. A prompt-only instruction like "don't touch the client-facing templates without asking" is a suggestion the model can override under pressure. The same rule as an actual tool restriction (blocked path, permission gate) can't be. Sort rules into three tiers:

Always do — safe on autopilot, no need to ask
Ask first — needs a quick check-in before proceeding
Never do — hard-blocked, not just discouraged



What an environment setup should contain
Proposed CLAUDE.md additions (or a full CLAUDE.md if none exists), a short list of what belongs in the knowledge base vs. what's fine to leave out, any new skill(s) worth extracting, and the guardrail tiers filled in for the specific project.

Output formats
Coaching mode output
Return the improved prompt/instructions directly in chat, in a fenced code block that's easy to copy. Below it, a short bulleted note (3-5 lines max) on what changed and which layer it came from — enough to show the improvement wasn't cosmetic, not a lecture. Don't create files for this mode unless asked.
Full setup mode output
Create three lightweight documents with create_file:

SPEC.md — goal, scope, judgment calls, constraints
VERIFIER.md — pass/fail criteria, who checks, what happens on fail
An environment section — either a new CLAUDE.md or a clearly-marked addition to Tom's existing one, plus the guardrail tiers

Read references/templates.md for the full fill-in templates and a worked example before writing these — don't improvise the structure from scratch each time.
Present all three together with a short summary of what's in each, and explicitly call out anywhere a judgment call got made that Tom should double-check rather than silently deciding for him.

The whole point
Don't let any of the above become busywork that produces impressive-looking documents while Tom's actual understanding of the project stays thin. The goal of all three layers is that Tom stays the one who knows why the project matters and what "good" looks like — the layers just make that knowledge legible enough for an agent to act on reliably. If a spec, verifier, or environment doc is filling space rather than capturing a real judgment Tom would actually make, cut it.
FILE:templates.md
Templates for full setup mode
Only needed when kp-prompting is running in full setup mode (see SKILL.md). Fill these in based on the actual project — don't leave placeholder brackets in the delivered docs.
SPEC.md template
markdown# Spec: [Project/Task Name]

## Goal
[The actual decision or outcome this serves — not just the task description.
E.g. not "add day-parting to the bid logic" but "cut wasted spend during
historically low-conversion hours without also cutting volume during hours
that convert but just look slow at a glance."]

## Scope
**In scope:**
- [...]

**Out of scope (for now):**
- [...]

## Judgment calls to flag, not silently resolve
- [Specific ambiguous point — e.g. "what happens on a campaign with under
  2 weeks of data: apply category benchmarks immediately, or wait for
  campaign-specific data?"]
- [...]

## Constraints
**Non-negotiable:**
- [...]

**Preferences (can be traded off):**
- [...]

## Checkpoints
[If scope is large: 2-4 points where Tom reviews before continuing, rather
than one big handoff at the end]
1. [...]
2. [...]
VERIFIER.md template
markdown# Verifier: [Project/Task Name]

## Pass/fail criteria
[Specific and checkable — not "looks good" or "cut the bad hours."
E.g. "an hour is only flagged for reduced bidding if it has at least N
leads of history and a CPA more than X% above the account average."]
- [ ] [criterion 1]
- [ ] [criterion 2]

## Who checks
- [ ] Self-check by the agent against the criteria above
- [ ] Second-model critic pass (different model or fresh context, grading
      against the spec)
- [ ] External signal: [deployment success / test suite / matches a known-
      good historical example]

## On failure
[What happens if a criterion fails — retry with what specific feedback, or
stop and flag to Tom before proceeding]
Environment / CLAUDE.md addition template
markdown## [Project/Feature Name]

**What this is:** [one or two sentences]

**Where things live:** [file paths, data sources, related docs]

**Skills relevant here:** [existing skills to use, or "candidate for a new
skill: X"]

**Rules:**
- Always do: [...]
- Ask first: [...]
- Never do: [...]

Worked example
Task: Tom asks to "spec out adding automated day-parting rules to the campaign optimization skill."
SPEC.md excerpt:

Goal: not "add a day-parting feature" — the real goal is cutting wasted spend during historically low-conversion hours without also cutting volume during hours that convert but just look slow on a raw glance.
Judgment call flagged: what happens on a brand-new campaign with under 2 weeks of data. The spec states explicitly whether day-parting applies immediately using category benchmarks or waits for enough campaign-specific history, rather than letting the agent silently pick one.
Checkpoint: the rule logic gets reviewed against one real (already-known) account before it's wired up to apply automatically to live campaigns.

VERIFIER.md excerpt:

Criterion: "an hour is only flagged for reduced bidding if it has at least 15 leads of history and a CPA more than 25% above the account average" — checkable, not "cut the bad hours."
Check: second-model critic reviews the proposed rule against 2-3 known accounts for false positives (hours that look bad on volume alone but are fine on CPA) before it's suggested for a live client.

CLAUDE.md addition excerpt:

Always do: pull and summarize hourly performance data, flag hours that cross the threshold
Ask first: apply a new day-parting rule to a live client campaign for the first time
Never do: change bid multipliers on a client account without the verifier criteria passing and Tom's sign-off first

Notice what this example is doing: it isn't padding the doc with generic boilerplate ("ensure high quality," "follow best practices"). Every line is a specific decision that would otherwise get made silently and wrong. That's the actual job of all three layers together.
```

**Source:** https://prompts.chat/prompts/cmrgsn3ul0004l204b8k7mgrf_kp-prompting

## 中文翻译

### 标题
KP提示

### 提示词内容

```
---
名称：kp-提示
描述：使用 Andrej Karpathy 的规范/验证程序/环境方法构建高级提示、任务规范、验证标准和 Claude 代码设置。每当您需要指定任务或项目、收紧或重写提示、定义代理输出的验证或成功标准，或者为代理设置/更新知识库、技能或护栏时，请使用此技能。 ---
规格 - 实际想要的东西，足够精确以至于模型无法猜测
验证者——你（或模型）如何知道输出实际上是正确的
环境——持久的上下文和护栏，这样代理就不会每次都从零开始重新学习一切

连接这三者的线索：你可以移交执行，但不能移交理解。下面的每一层都应该让 Tom 参与实际的判断调用，而不仅仅是产生看起来精美的输出来掩盖他从未被问到的差距。两种模式——在做其他事情之前先弄清楚你处于哪一种模式
辅导模式（默认）。汤姆给你一个任务，一个粗略的提示，或者一个为特定的事情写说明的请求。使用下面的三层镜片将其拧紧，然后在聊天中交回改进版本 - 无文件。这是“帮我编写/改进 X 提示”的默认设置。
完整设置模式。 Tom 正在建立一个新项目、工具或重复工作流程，并需要实际的脚手架：规范文档、验证标准和环境设置（CLAUDE.md 添加、护栏、知识库指针）。在“规范输出”、“设置环境”、“为 X 构建 Karpathy 方法”等短语或对所有三个层的明确要求时触发此操作。如果确实不清楚哪一个适合，请快速提出一个问题，而不是猜测——构建错误的问题比询问更浪费时间。大多数时候这是可以推断的：一项任务或手头的即时草案→指导；没有提示的新项目/功能 → 完整设置。第 1 层：规格
为什么这很重要
卡帕蒂的例子：询问前沿模型是开车还是步行去 50 米外的洗车场，它说步行——忽略了一个明显的事实，即汽车也需要到达那里。模型在任何可检查的方面都表现出色，但在现实世界的判断调用方面却出人意料地糟糕，因为判断调用正是干净的训练信号中所缺少的。规范的工作是向模型提供它无法自行推断的判断，因此它不会简化为猜测上下文。浅薄的高级“计划模式”风格的提示并不能做到这一点——它太薄弱，无法承载真正的理解。如何建造一个

找到实际的目标，而不仅仅是任务。 “写月末报告”是一项任务。目标是报告应该支持的任何决定。如果从汤姆所说的内容中看不出来，就问——这里提出几个简单的问题，可以节省以后更大的重写。在小检查站工作，而不是在大垃圾场工作。交出一切，只有在完成结果后才重新召集，让漂移悄然复合。将规范范围划分为足够小的部分，以便在每个步骤中进行检查，尤其是在存在真正模糊性的地方。准确说明不应该假设的内容。规范中的每个模糊单词都会成为模型填充的假设——自信地，无论统计上可能的方向如何，不一定是汤姆真正想要的。命名具体的判断调用（命名约定、边缘情况、冲突数据上会发生什么），而不是让它们隐式存在。像“标记你所做的任何假设，而不是默默地选择一个”这样的台词在这里确实有效。规范应包含哪些内容
目标（所服务的决策/结果，而不仅仅是任务）、范围边界（明确的进与出）、标记而不是默默地解决的判断调用，以及分为不可协商与偏好的约束。第 2 层：验证者
为什么这很重要
卡帕蒂的框架：这些模型比动物更接近“幽灵”——统计模拟器，而不是有动机的代理人。对模型大喊大叫、恳求它或告诉它一些非常重要的事情不会改变输出质量。改变输出质量的是是否有东西可以真正检查工作。这也是为什么模型在代码和数学方面是超人的（可以完全检查），但在品味和判断方面却不可靠（没有什么可检查的）——因此，对于给定的任务来说，“做得好”越明确和可检查，输出就越可信，而不是因审查疲劳而被忽略。如何建造一个

在提示本身中预先设置通过/失败标准，而不是事后设置。 “让报告看起来不错”是不可检查的。 “报告分为三个部分，每个部分都以建议结尾”。将标准写成第二位读者（人类或模型）可以在不了解汤姆想法的情况下检查的内容。使用第二个模型作为批评家，这样做的成本低廉。不同的模型（或新环境中的相同模型）根据规范对第一个模型的输出进行评分，捕获原始运行将合理化过去的事情。当真实的外部信号存在时，将其拉入。对于代码：它是否实际部署，测试是否通过？对于非技术性工作：它是否符合已知的良好示例的格式/语气？仅检查内部一致性的验证器比检查真实事物的验证器要弱。验证者应该包含什么
具体的、可检查的通过/失败标准（不是振动）、谁或什么检查（自检、第二个模型、部署/测试信号）以及失败时会发生什么（使用什么具体反馈重试，或升级给 Tom）。第三层：环境
为什么这很重要
大多数人在每次会议时都会从头开始重建上下文——重新解释项目，重新陈述规则，希望代理记住不应该触及的内容。保存聊天记录与真实环境不同。工具已经就位的研讨会胜过每次访问时重新解释整个商店。如何建造一个

代理会自动读取 CLAUDE.md。封面：这个工作区/存储库是什么，存在哪些自定义技能以及何时使用它们，在哪里可以找到东西（知识架构）以及始终适用的规则。这是影响力最高的一篇文章，因为每次提示时都会阅读它，而汤姆不会重复自己的话。个人知识库。一个结构化的、可检索的参考材料位置，代理可以从中提取参考材料，而不是重新推导或产生幻觉。积累的物质是护城河；每次使用时，其上组织良好的检索结构都会复合。对于任何重复的事情都可以重复使用的技能。如果汤姆第二次做某事，它应该成为一种技能，而不是重新解释一次性的。护栏在工具级别强制执行，而不仅仅是提示级别。像“未经询问就不要触摸面向客户的模板”这样的仅提示指令是模型在压力下可以推翻的建议。与实际工具限制（阻止路径、权限门）相同的规则不可能是这样。将规则分为三层：

始终这样做——自动驾驶安全，无需询问
先询问——在继续之前需要快速登记
永远不要这样做——严格阻止，而不仅仅是气馁



环境设置应包含哪些内容
建议添加 CLAUDE.md（如果不存在，则添加完整的 CLAUDE.md）、属于知识库的内容与可以省略的内容的简短列表、任何值得提取的新技能以及为特定项目填写的护栏层。输出格式
教练模式输出
在易于复制的受隔离代码块中直接在聊天中返回改进的提示/说明。在它的下面，有一个简短的项目符号注释（最多 3-5 行），说明发生了什么变化以及它来自哪一层——足以表明改进不是表面的，而不是说教。除非有要求，否则不要为此模式创建文件。完整设置模式输出
使用 create_file 创建三个轻量级文档：

SPEC.md — 目标、范围、判断调用、约束
VERIFIER.md — 通过/失败标准，谁检查，失败时会发生什么
环境部分 — 可以是新的 CLAUDE.md，也可以是 Tom 现有部分的明确标记的附加部分，以及护栏层

在编写这些内容之前，请阅读references/templates.md以获取完整的填充模板和一个有效的示例——不要每次都从头开始即兴创作结构。将这三个内容一起呈现，并简要概述每个内容的内容，并明确指出任何做出判断的地方，汤姆应该仔细检查而不是默默地为他做出决定。整个要点
不要让上述任何事情成为生成令人印象深刻的文档的忙碌工作，而汤姆对项目的实际了解仍然很薄弱。所有三个层的目标是让 Tom 始终知道项目为何重要以及什么是“好”——这些层只是使这些知识足够清晰，以便代理能够可靠地采取行动。如果规范、验证者或环境文档正在填补空白，而不是捕获 Tom 实际做出的真实判断，请删除它。文件：模板.md
完整设置模式的模板
仅当 kp-prompting 在完整设置模式下运行时才需要（请参阅 SKILL.md）。 根据实际项目填写这些内容 - 不要在交付的文档中留下占位符括号。 SPEC.md 模板
markdown# 规范：[项目/任务名称]

## 目标
[这服务于实际的决定或结果——而不仅仅是任务描述。例如。不是“在出价逻辑中添加时段”，而是“减少期间的浪费支出”
历史上较低的转化时间，同时也没有减少交易量
转换但乍一看看起来很慢。”]

## 范围
**范围：**
- [...]

**超出范围（目前）：**
- [...]

## 判断调用flag，而不是默默解决
- [具体的歧义点——例如“在一场活动中会发生什么？
  2 周数据：立即应用类别基准，或等待
  活动特定数据？”]
- [...]

## 约束条件
**不可协商：**
- [...]

**偏好（可以权衡）：**
- [...]

## 检查点
[如果范围很大：汤姆在继续之前评论 2-4 点，而不是
比最后的一次大交接]
1. [...]
2. [...]
VERIFIER.md 模板
markdown# 验证者：[项目/任务名称]

## 通过/失败标准
[具体且可检查——不是“看起来不错”或“减少糟糕的时间”。
例如。 “只有当一个小时至少有 N 个时，才会被标记为降低出价
历史领先地位，每次转化费用 (CPA) 高于帐户平均水平 X% 以上。”]
- [ ] [标准 1]
- [ ] [标准 2]

## 谁检查
- [ ] 代理商根据上述标准进行自查
- [ ] 第二模型评论家通过（不同模型或新鲜背景，评分
      违反规范）
- [ ] 外部信号：[部署成功/测试套件/匹配已知-
      很好的历史例子]

## 失败时
[如果标准失败会发生什么 - 使用什么具体反馈重试，或者
在继续之前停下来并向汤姆招手]
环境/CLAUDE.md 添加模板
markdown## [项目/功能名称]

**这是什么：** [一两句话]

**事物所在的位置：** [文件路径、数据源、相关文档]

**此处相关的技能：** [要使用的现有技能，或“新技能的候选人”
技能：X”]

**规则：**
- 始终这样做：[...]
- 先问：[...]
- 永远不要这样做：[...]

工作示例
任务：Tom 要求“指定在营销活动优化技能中添加自动时段规则”。
SPEC.md 摘录：

目标：不是“添加日间休息功能”——真正的目标是在历史上转化率较低的时段减少浪费的支出，同时在转化但乍一看很慢的时段减少交易量。判断电话标记为：在不到两周的数据的全新营销活动中会发生什么。该规范明确规定了是否使用类别基准立即应用时段或等待足够的特定于活动的历史记录，而不是让代理默默地选择一个。检查点：在将规则逻辑连接到自动应用于实时营销活动之前，会根据一个真实（已知）帐户对规则逻辑进行审查。 VERIFIER.md 摘录：

标准：“只有在历史上至少有 15 个潜在客户且 CPA 高于账户平均水平 25% 以上的情况下，一个小时才会被标记为降低出价”——可检查，而不是“减少不良时间”。
检查：第二个模型评论家会根据 2-3 个已知帐户审查拟议的规则是否存在误报（仅在交易量上看起来很糟糕，但在每次转化费用上却很好），然后再建议实际客户。 CLAUDE.md 添加摘录：

始终这样做：提取并汇总每小时的性能数据，标记超过阈值的小时数
先问：首次将新的时段规则应用于实时客户活动
切勿这样做：在未通过验证者标准且 Tom 未先签字的情况下更改客户帐户的出价乘数

请注意此示例的作用：它没有用通用样板来填充文档（“确保高质量”、“遵循最佳实践”）。每一行都是一个具体的决定，否则就会默默地做出错误的决定。这就是所有三层共同完成的实际工作。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Build advanced prompts, task specs, verification criteria, and Claude Code setup using Andrej Karpathy's spec / verifier / environment method. Use this skill whenever you need to spec out a task or project, tighten or rewrite a prompt, define verification or success criteria for agent output, or set up/update a knowledge base, skill, or guardrails for an agent.

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
