# Trading & Investing Simulation Platform

**Description:** People want to practice before risking real money. The simulation sells the hope of being competent enough to invest eventually — and the journal analysis layer sells the hope of becoming the kind of person whose judgment improves over time. If simulation doesn't reflect real market mechanics, it feels like a toy and loses credibility. Slippage, transaction costs, and realistic price impact must be simulated.

**Type:** TEXT
**Author:** mmanisaligil
**Created:** 2026-03-19T19:12:16.822Z
**Votes:** 0
**Views:** 0

**Tags:** coding

**Category:** Vibe Coding

## Prompt Content

```
Build a paper trading simulation platform called "Paper" — a realistic, risk-free environment for learning to trade and invest.

Core features:
- Portfolio setup: user starts with $100,000 in virtual cash. Real-time stock and ETF prices via Yahoo Finance or Alpha Vantage API
- Trade execution: market and limit orders supported. Simulate 0.1% slippage on market orders. Commission of $1 per trade (realistic friction without being punitive)
- Performance dashboard: P&L chart (daily), total return, annualized return, win rate, average gain and loss, Sharpe ratio, and current sector exposure — all updated with each trade. Built with recharts
- Trade journal: required field on every position close — "What was my thesis entering this trade? What happened? What will I do differently?" Three fields, each max 200 characters. Cannot close a position without completing the journal
- Behavioral analysis: [LLM API] analyzes the last 20 trade journal entries and identifies recurring behavioral patterns — "You consistently exit winning positions early when they approach round-number price levels" — surfaced monthly
- Leaderboard: optional, weekly-resetting leaderboard among friend groups — ranked by risk-adjusted return, not raw P&L

Stack: React, Yahoo Finance or Alpha Vantage for market data, [LLM API] for behavioral analysis, recharts. Terminal-inspired design — data dense, no decorative elements.

```

**Source:** https://prompts.chat/prompts/cmmxuk7na0009ky04jgx2k8je_trading-investing-simulation-platform

## 中文翻译

### 标题
交易投资模拟平台

### 提示词内容

```
建立一个名为“Paper”的模拟交易平台——一个学习交易和投资的真实、无风险的环境。

核心特点：
- 投资组合设置：用户从 100,000 美元的虚拟现金开始。通过 Yahoo Finance 或 Alpha Vantage API 获取实时股票和 ETF 价格
- 交易执行：支持市价单和限价单。模拟市价订单的 0.1% 滑点。每笔交易佣金为 1 美元（现实摩擦，但不会受到惩罚）
- 绩效仪表板：盈亏图（每日）、总回报、年化回报、胜率、平均盈亏、夏普比率和当前行业风险敞口——每笔交易都会更新。使用重新图表构建
- 交易日志：每次平仓时必填字段 — “我进入此交易的论文是什么？发生了什么？我会采取什么不同的做法？”三个字段，每个字段最多 200 个字符。在未完成日志的情况下无法平仓
- 行为分析：[LLM API] 分析最近 20 个交易日志条目并识别重复出现的行为模式 — “当盈利头寸接近整数价格水平时，您始终会尽早退出” — 每月出现
- 排行榜：朋友群体中可选的、每周重置的排行榜——按风险调整回报排名，而不是原始损益排名

Stack：React、Yahoo Finance 或 Alpha Vantage 用于市场数据，[LLM API] 用于行为分析、图表。受终端启发的设计——数据密集，无装饰元素。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**UI/UX设计与视觉创作**类的提示词。People want to practice before risking real money. The simulation sells the hope of being competent enough to invest eventually — and the journal analysis layer sells the hope of becoming the kind of person whose judgment improves over time. If simulation doesn't reflect real market mechanics, it feels like a toy and loses credibility. Slippage, transaction costs, and realistic price impact must be simulated.

### 适用人群
开发者/程序员

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
