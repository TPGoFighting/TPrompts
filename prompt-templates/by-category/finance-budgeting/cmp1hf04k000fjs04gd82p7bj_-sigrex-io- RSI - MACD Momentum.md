# [sigrex.io] RSI + MACD Momentum

**Description:** This prompt analyzes the ${symbol} cryptocurrency using RSI and MACD indicators. It determines entry and exit points for trading based on specific conditions. Users can customize RSI overbought and oversold levels to tailor the analysis to their strategy.

**Type:** TEXT
**Author:** sigrex
**Created:** 2026-05-11T17:34:48.164Z
**Votes:** 0
**Views:** 0

**Tags:** trading, Strategy

**Category:** Finance & Budgeting

## Prompt Content

```
{{val:symbol=BTCUSDT}}
{{val:rsi_ob=70}}
{{val:rsi_os=30}}

You are analyzing {{symbol}} at {{current_time}}.

Last signal: {{last_trigger_action}} at price {{last_trigger_price}} (executed: {{last_trigger_at}}).

Recent signal history:
{{trigger_history}}

STRATEGY RULES:
- Look at the RSI indicator on the chart.
- Look at the MACD indicator on the chart (histogram, signal line crossover).

LONG conditions (all must be met):
  1. RSI is below {{rsi_os}} and turning upward
  2. MACD histogram is crossing from negative to positive
  3. No position is currently open

SHORT conditions (all must be met):
  1. RSI is above {{rsi_ob}} and turning downward
  2. MACD histogram is crossing from positive to negative
  3. No position is currently open

EXIT conditions (any is enough):
  1. RSI crosses the opposite extreme (e.g., was SHORT, RSI now below {{rsi_os}})
  2. MACD gives a reversal crossover against current position

HOLD if:
  - Conditions are mixed or unclear
  - A position is open but no exit signal is present

Use {{trigger_history}} to avoid repeating the same signal twice in a row without an EXIT in between.
```

**Source:** https://prompts.chat/prompts/cmp1hf04k000fjs04gd82p7bj_sigrexio-rsi-macd-momentum

## 中文翻译

### 标题
[sigrex.io] RSI + MACD 动量

### 提示词内容

```
{{val:symbol=BTCUSDT}}
{{val:rsi_ob=70}}
{{val:rsi_os=30}}

您正在 {{current_time}} 分析 {{symbol}}。

最后信号：{{last_trigger_action}}，价格为 {{last_trigger_price}}（执行：{{last_trigger_at}}）。

最近的信号历史记录：
{{trigger_history}}

策略规则：
- 查看图表上的 RSI 指标。
- 查看图表上的 MACD 指标（柱状图、信号线交叉）。

LONG 条件（必须满足所有条件）：
  1. RSI 低于 {{rsi_os}} 并向上
  2. MACD柱状图由负向正交叉
  3. 目前没有持仓

简短条件（必须满足所有条件）：
  1. RSI 高于 {{rsi_ob}} 并转向向下
  2. MACD柱状图由正向负交叉
  3. 目前没有持仓

退出条件（任意即可）：
  1. RSI 穿过相反的极端（例如，之前是空头，RSI 现在低于 {{rsi_os}}）
  2. MACD 给出与当前位置的反转交叉

持有如果：
  - 条件混杂或不明确
  - 持仓已开，但没有退出信号

使用 {{trigger_history}} 可以避免连续两次重复相同的信号而中间没有 EXIT。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。This prompt analyzes the ${symbol} cryptocurrency using RSI and MACD indicators. It determines entry and exit points for trading based on specific conditions. Users can customize RSI overbought and oversold levels to tailor the analysis to their strategy.

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
