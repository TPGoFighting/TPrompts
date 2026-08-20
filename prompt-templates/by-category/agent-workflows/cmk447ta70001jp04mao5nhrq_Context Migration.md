# Context Migration

**Description:** This prompt guides AI agents in creating a comprehensive context artifact that preserves all conversational context, progress, decisions, and project structures. It enables seamless continuation across AI sessions, platforms, or agents, acting as a "context USB" to prevent repetition or context loss.

see the sub-prompt for other workflow route 

**Type:** TEXT
**Author:** joembolinas
**Created:** 2026-01-07T14:30:04.543Z
**Votes:** 0
**Views:** 0

**Tags:** Agent, Product Management, Prompt Engineering

**Category:** Agent Workflows

## Prompt Content

```

# Context Preservation & Migration Prompt

[ for AGENT.MD pass THE `## SECTION` if NOT APPLICABLE ]

Generate a comprehensive context artifact that preserves all conversational context, progress, decisions, and project structures for seamless continuation across AI sessions, platforms, or agents. This artifact serves as a "context USB" enabling any AI to immediately understand and continue work without repetition or context loss.

## Core Objectives

Capture and structure all contextual elements from current session to enable:
1. **Session Continuity** - Resume conversations across different AI platforms without re-explanation
2. **Agent Handoff** - Transfer incomplete tasks to new agents with full progress documentation
3. **Project Migration** - Replicate entire project cultures, workflows, and governance structures

## Content Categories to Preserve

### Conversational Context
- Initial requirements and evolving user stories
- Ideas generated during brainstorming sessions
- Decisions made with complete rationale chains
- Agreements reached and their validation status
- Suggestions and recommendations with supporting context
- Assumptions established and their current status
- Key insights and breakthrough moments
- Critical keypoints serving as structural foundations

### Progress Documentation
- Current state of all work streams
- Completed tasks and deliverables
- Pending items and next steps
- Blockers encountered with mitigation strategies
- Rate limits hit and workaround solutions
- Timeline of significant milestones

### Project Architecture (when applicable)
- SDLC methodology and phases
- Agent ecosystem (main agents, sub-agents, sibling agents, observer agents)
- Rules, governance policies, and strategies
- Repository structures (.github workflows, templates)
- Reusable prompt forms (epic breakdown, PRD, architectural plans, system design)
- Conventional patterns (commit formats, memory prompts, log structures)
- Instructions hierarchy (project-level, sprint-level, epic-level variations)
- CI/CD configurations (testing, formatting, commit extraction)
- Multi-agent orchestration (prompt chaining, parallelization, router agents)
- Output format standards and variations

### Rules & Protocols
- Established guidelines with scope definitions
- Additional instructions added during session
- Constraints and boundaries set
- Quality standards and acceptance criteria
- Alignment mechanisms for keeping work on track

# Steps

1. **Scan Conversational History** - Review entire thread/session for all interactions and context
2. **Extract Core Elements** - Identify and categorize information per content categories above
3. **Document Progress State** - Capture what's complete, in-progress, and pending
4. **Preserve Decision Chains** - Include reasoning behind all significant choices
5. **Structure for Portability** - Organize in universally interpretable format
6. **Add Handoff Instructions** - Include explicit guidance for next AI/agent/session

# Output Format

Produce a structured markdown document with these sections:

```
# CONTEXT ARTIFACT: [Session/Project Title]
**Generated**: [Date/Time]
**Source Platform**: [AI Platform Name]
**Continuation Priority**: [Critical/High/Medium/Low]

## SESSION OVERVIEW
[2-3 sentence summary of primary goals and current state]

## CORE CONTEXT
### Original Requirements
[Initial user requests and goals]

### Evolution & Decisions
[Key decisions made, with rationale - bulleted list]

### Current Progress
- Completed: [List]
- In Progress: [List with % complete]
- Pending: [List]
- Blocked: [List with blockers and mitigations]

## KNOWLEDGE BASE
### Key Insights & Agreements
[Critical discoveries and consensus points]

### Established Rules & Protocols
[Guidelines, constraints, standards set during session]

### Assumptions & Validations
[What's been assumed and verification status]

## ARTIFACTS & DELIVERABLES
[List of files, documents, code created with descriptions]

## PROJECT STRUCTURE (if applicable)
### Architecture Overview
[SDLC, workflows, repository structure]

### Agent Ecosystem
[Description of agents, their roles, interactions]

### Reusable Components
[Prompt templates, workflows, automation scripts]

### Governance & Standards
[Instructions hierarchy, conventional patterns, quality gates]

## HANDOFF INSTRUCTIONS
### For Next Session/Agent
[Explicit steps to continue work]

### Context to Emphasize
[What the next AI must understand immediately]

### Potential Challenges
[Known issues and recommended approaches]

## CONTINUATION QUERY
[Suggested prompt for next AI: "Given this context artifact, please continue by..."]
```

# Examples

**Example 1: Session Continuity (Brainstorming Handoff)**

Input: "We've been brainstorming a mobile app for 2 hours. I need to switch to Claude. Generate context artifact."

Output:
```
# CONTEXT ARTIFACT: FitTrack Mobile App Planning
**Generated**: 2026-01-07 14:30
**Source Platform**: Google Gemini
**Continuation Priority**: High

## SESSION OVERVIEW
Brainstormed fitness tracking mobile app for busy professionals. Decided on minimalist design with AI coaching. Ready for technical architecture phase.

## CORE CONTEXT
### Original Requirements
- Target users: Working professionals 25-40, limited gym time
- Must sync with Apple Watch and Fitbit
- Budget: $50k for MVP
- Timeline: 3 months to launch

### Evolution & Decisions
- ✓ Name: "FitTrack Pro" (rejected: "QuickFit", "PowerHour")
- ✓ Core feature: 15-min AI-personalized workouts (not generic plans)
- ✓ Monetization: Freemium ($9.99/mo premium)
- ✓ Tech stack: React Native (for iOS+Android simultaneously)

### Current Progress
- Completed: Feature prioritization, user personas, monetization model
- In Progress: None yet
- Pending: Technical architecture, database schema, API design
- Blocked: None

## KNOWLEDGE BASE
### Key Insights & Agreements
- Users want "smart short" over "long complete" - brevity is premium feature
- AI coaching must feel conversational, not robotic commands
- Social features deferred to v2 to avoid scope creep

(... rest of structure follows)

## CONTINUATION QUERY
"Given this context artifact for FitTrack Pro app planning, please design the technical architecture including database schema, API endpoints, and third-party integration strategy for Apple Watch and Fitbit."
```

**Example 2: Agent Handoff (Rate-Limited Automation)**

Input: "Browser agent hit rate limit while scraping competitor pricing. Generate handoff doc."

Output:
```
# CONTEXT ARTIFACT: Competitor Pricing Automation (Incomplete)
**Generated**: 2026-01-07 09:15
**Source Platform**: Browser Agent v2.1
**Continuation Priority**: Critical

## SESSION OVERVIEW
Automated scraping of 50 competitor websites for pricing comparison. Completed 32/50 before rate limiting. Need immediate continuation to meet Friday deadline.

## CORE CONTEXT
### Original Requirements
- Scrape pricing for "wireless earbuds under $100" from 50 e-commerce sites
- Extract: product name, price, rating, review count
- Output: Single CSV for analysis
- Deadline: Friday 5pm

### Evolution & Decisions
- ✓ Added retry logic after initial failures on JS-heavy sites
- ✓ Switched to headless Chrome (from requests library) for better compatibility
- ✓ Implemented 3-second delays between requests per domain
- ✓ User added instruction: "Skip sites requiring login"

### Current Progress
- Completed: 32/50 sites successfully scraped (2,847 products)
- In Progress: None (halted at rate limit)
- Pending: 18 sites remaining (list in "Continuation Query" below)
- Blocked: Rate limited on domains: amazon.com, walmart.com, target.com (need 2-hour cooldown)

## KNOWLEDGE BASE
### Established Rules & Protocols
- Respect robots.txt without exception
- Max 1 request per 3 seconds per domain
- Skip products with no reviews (noise in data)
- Handle pagination up to 5 pages max per site

### Challenges & Mitigations
- Challenge: Dynamic pricing (changes during scraping)
  Mitigation: Timestamp each entry
- Challenge: Anti-bot CAPTCHAs on 3 sites
  Mitigation: User approved manual data entry for these 3
- Challenge: Rate limiting
  Mitigation: Implement exponential backoff, rotate user agents

## CONTINUATION QUERY
"Continue pricing scraping automation. 18 sites remaining: [bestbuy.com, newegg.com, ebay.com...]. Use existing CSV 'pricing_data_partial.csv' (2,847 entries). Rate-limited domains need 2hr wait. Prioritize non-blocked sites first. Apply all established rules: 3-sec delays, skip no-reviews, 5-page pagination limit. Deliver final CSV by Friday 5pm."
```

**Example 3: Project Migration (Full Culture Transfer)**

(Input context: Entire project repository with SDLC, agents, governance)

Output: *(Condensed example showing structure - real output would be comprehensive)*
```
# CONTEXT ARTIFACT: "SmartInventory" Project Culture & Architecture
**Generated**: 2026-01-07 16:00
**Source Platform**: GitHub Copilot + Multi-Agent System
**Continuation Priority**: Medium (onboarding new AI agent framework)

## SESSION OVERVIEW
Enterprise inventory management system using AI-driven development culture. Need to replicate entire project structure, agent ecosystem, and governance for new autonomous AI agent setup.

## PROJECT STRUCTURE
### SDLC Framework
- Methodology: Agile with 2-week sprints
- Phases: Epic Planning → Development → Observer Review → CI/CD → Deployment
- All actions AI-driven: code generation, testing, documentation, commit narrative generation

### Agent Ecosystem
**Main Agents:**
- DevAgent: Code generation and implementation
- TestAgent: Automated testing and quality assurance
- DocAgent: Documentation generation and maintenance

**Observer Agent (Project Guardian):**
- Role: Alignment enforcer across all agents
- Functions: PR feedback, path validation, standards compliance
- Trigger: Every commit, PR, and epic completion

**CI/CD Agents:**
- FormatterAgent: Code style enforcement
- ReflectionAgent: Extracts commits → structured reflections, dev storylines, narrative outputs
- DeployAgent: Automated deployment pipelines

**Sub-Agents (by feature domain):**
- InventorySubAgent, UserAuthSubAgent, ReportingSubAgent

**Orchestration:**
- Multi-agent coordination via .ipynb notebooks
- Patterns: Prompt chaining, parallelization, router agents

### Repository Structure (.github)
```
.github/
├── workflows/
│   ├── epic_breakdown.yml
│   ├── epic_generator.yml
│   ├── prd_template.yml
│   ├── architectural_plan.yml
│   ├── system_design.yml
│   ├── conventional_commit.yml
│   ├── memory_prompt.yml
│   └── log_prompt.yml
├── AGENTS.md (agent registry)
├── copilot-instructions.md (project-level rules)
└── sprints/
    ├── sprint_01_instructions.md
    └── epic_variations/
```

### Governance & Standards
**Instructions Hierarchy:**
1. `copilot-instructions.md` - Project-wide immutable rules
2. Sprint instructions - Temporal variations per sprint
3. Epic instructions - Goal-specific invocations

**Conventional Patterns:**
- Commits: `type(scope): description` per Conventional Commits spec
- Memory prompt: Session state preservation template
- Log prompt: Structured activity tracking format

(... sections continue: Reusable Components, Quality Gates, Continuation Instructions for rebuilding with new AI agents...)
```

# Notes

- **Universality**: Structure must be interpretable by any AI platform (ChatGPT, Claude, Gemini, etc.)
- **Completeness vs Brevity**: Balance comprehensive context with readability - use nested sections for deep detail
- **Version Control**: Include timestamps and source platform for tracking context evolution across multiple handoffs
- **Action Orientation**: Always end with clear "Continuation Query" - the exact prompt for next AI to use
- **Project-Scale Adaptation**: For full project migrations (Case 3), expand "Project Structure" section significantly while keeping other sections concise
- **Failure Documentation**: Explicitly capture what didn't work and why - this prevents next AI from repeating mistakes
- **Rule Preservation**: When rules/protocols were established during session, include the context of WHY they were needed
- **Assumption Validation**: Mark assumptions as "validated", "pending validation", or "invalidated" for clarity

- - FOR GEMINI / GEMINI-CLI / ANTIGRAVITY

Here are ultra-concise versions:

GEMINI.md
"# Gemini AI Agent across platform

workflow/agent/sample.toml
"# antigravity prompt template


MEMORY.md
"# Gemini Memory

**Session**: 2026-01-07 | Sprint 01 (7d left) | Epic EPIC-001 (45%)  
**Active**: TASK-001-03 inventory CRUD API (GET/POST done, PUT/DELETE pending)  
**Decisions**: PostgreSQL + JSONB, RESTful /api/v1/, pytest testing  
**Next**: Complete PUT/DELETE endpoints, finalize schema"

```

**Source:** https://prompts.chat/prompts/cmk447ta70001jp04mao5nhrq_context-migration



---

## 中文翻译

### 标题
上下文迁移

### 提示词内容

```
# 上下文保存和迁移提示

[对于 AGENT.MD，如果不适用，请传递 `## SECTION` ]

生成一个全面的上下文工件，保留所有对话上下文、进度、决策和项目结构，以便跨 AI 会话、平台或代理无缝延续。该工件充当“上下文 USB”，使任何人工智能都能立即理解并继续工作，而不会重复或丢失上下文。

## 核心目标

捕获并构建当前会话中的所有上下文元素，以实现：
1. **会话连续性** - 跨不同人工智能平台恢复对话，无需重新解释
2. **座席交接** - 将未完成的任务转移给新座席并提供完整的进度文档
3. **项目迁移** - 复制整个项目文化、工作流程和治理结构

## 要保留的内容类别

### 对话上下文
- 初始需求和不断发展的用户故事
- 头脑风暴会议期间产生的想法
- 根据完整的理由链做出的决策
- 达成的协议及其验证状态
- 具有支持背景的建议和建议
- 已建立的假设及其现状
- 关键见解和突破时刻
- 作为结构基础的关键点

### 进度文档
- 所有工作流的当前状态
- 已完成的任务和可交付成果
- 待处理项目和后续步骤
- 遇到缓解策略的阻碍者
- 速率限制命中和解决方法
- 重要里程碑的时间表

### 项目架构（如果适用）
- SDLC 方法和阶段
- 代理生态系统（主代理、子代理、兄弟代理、观察代理）
- 规则、治理政策和策略
- 存储库结构（.github 工作流程、模板）
- 可重复使用的提示表单（史诗般的故障、PRD、架构计划、系统设计）
- 常规模式（提交格式、内存提示、日志结构）
- 指令层次结构（项目级、冲刺级、史诗级变体）
- CI/CD 配置（测试、格式化、提交提取）
- 多代理编排（提示链接、并行化、路由器代理）
- 输出格式标准和变化

### 规则和协议
- 制定了范围定义的指南
- 会议期间添加的附加说明
- 设定约束和界限
- 质量标准和验收标准
- 保持工作步入正轨的协调机制

# 步骤

1. **扫描对话历史记录** - 查看整个线程/会话的所有交互和上下文
2. **提取核心元素** - 根据上述内容类别对信息进行识别和分类
3. **文档进度状态** - 捕获已完成、正在进行和待处理的内容
4. **保留决策链** - 包括所有重要选择背后的推理
5. **可移植性结构** - 以通用可解释的格式组织
6. **添加切换说明** - 包括对下一个 AI/代理/会话的明确指导

# 输出格式

生成包含以下部分的结构化 Markdown 文档：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。This prompt guides AI agents in creating a comprehensive context artifact that preserves all conversational context, progress, decisions, and project structures. It enables seamless continuation across AI sessions, platforms, or agents, acting as a "context USB" to prevent repetition or context loss.

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
