# [sigrex.io] Full Kitchen Sink

**Description:** This prompt is a comprehensive trading signal generator utilizing sentiment analysis and technical indicators. It fetches the Fear & Greed Index to determine market sentiment and uses RSI and MACD for technical confirmation. The strategy logic includes sentiment biasing, technical confirmation, position checks, and decision-making rules, ensuring a disciplined trading approach.

**Type:** TEXT
**Author:** sigrex
**Created:** 2026-05-11T22:33:43.991Z
**Votes:** 0
**Views:** 0

**Tags:** Strategy, trading

**Category:** Finance & Budgeting

## Prompt Content

```
{{val:symbol=SOLUSDT}}
{{val:rsi_ob=70}}
{{val:rsi_os=30}}
{{val:max_repeat=3}}

Symbol: {{symbol}} | Time: {{current_time}}
Last signal: {{last_trigger_action}} @ {{last_trigger_price}} | Executed: {{last_trigger_at}}

Full signal history:
{{trigger_history}}

{{comment: External sentiment — Fear & Greed}}
Fear & Greed Index:
{{get:https://api.alternative.me/fng/?limit=1&format=json}}

{{comment: Strategy master config in Toon format}}
Master config:
{{toon:{"name":"full_strategy","symbol":"SOLUSDT","bias_source":"fear_greed","technicals":["RSI","MACD"],"rsi":{"overbought":70,"oversold":30},"macd":{"signal":"histogram_cross"},"position_rules":{"max_open":1,"allow_same_direction_repeat":false},"safety":{"max_consecutive_non_exit":3}}}}

STRATEGY LOGIC:

Step 1 — Sentiment Bias (from Fear & Greed fetch):
  - 0–30: Favor LONG only
  - 31–50: Lean LONG, allow neutral
  - 51–74: Lean SHORT, allow neutral
  - 75–100: Favor SHORT only

Step 2 — Technical Confirmation (from chart):
  - LONG confirmed: RSI < {{rsi_os}} turning up + MACD positive cross
  - SHORT confirmed: RSI > {{rsi_ob}} turning down + MACD negative cross

Step 3 — Position Check (from trigger_history):
  - If last action was LONG or SHORT → must EXIT before new entry
  - If {{trigger_history}} shows {{max_repeat}} or more signals without EXIT → HOLD

Step 4 — Decision:
  - Sentiment and technicals agree → take signal
  - Sentiment and technicals disagree → HOLD
  - Open position with exit signal → EXIT
  - Open position without exit signal → HOLD
  - No position and no clear signal → HOLD

{{comment: max_repeat val used above as a safety cap on consecutive non-exit signals}}
```

**Source:** https://prompts.chat/prompts/cmp1s3fhy0004js04p0er6i4y_sigrexio-full-kitchen-sink

## 中文翻译

### 标题
[sigrex.io] 全套厨房水槽

### 提示词内容

```
{{val:symbol=SOLUSDT}}
{{val:rsi_ob=70}}
{{val:rsi_os=30}}
{{val:max_repeat=3}}

符号：{{符号}} |时间：{{current_time}}
最后信号：{{last_trigger_action}} @ {{last_trigger_price}} |执行：{{last_trigger_at}}

完整的信号历史记录：
{{trigger_history}}

{{评论：外部情绪——恐惧与贪婪}}
恐惧与贪婪指数：
{{获取：https://api.alternative.me/fng/?limit=1&format=json}}

{{comment: Toon 格式的策略主配置}}
主配置：
{{toon:{"name":"full_strategy","symbol":"SOLUSDT","bias_source":"fear_greed","technicals":["RSI","MACD"],"rsi":{"超买":70,"超卖":30}," MACD":{"signal":"histogram_cross"},"position_rules":{"max_open":1,"allow_same_direction_repeat":false},"safety":{"max_consecutive_non_exit":3}}}}

策略逻辑：

步骤 1 — 情绪偏差（来自恐惧和贪婪获取）：
  - 0–30：仅支持长
  - 31–50：倾向于做多，允许中立
  - 51–74：精简短线，允许中性
  - 75–100：仅支持短视频

第 2 步 — 技术确认（来自图表）：
  - 多头确认：RSI < {{rsi_os}} 向上 + MACD 正交叉
  - 空头确认：RSI > {{rsi_ob}} 向下 + MACD 负交叉

第 3 步 — 位置检查（来自trigger_history）：
  - 如果上次操作是长或短 → 必须在新条目之前退出
  - 如果 {{trigger_history}} 显示 {{max_repeat}} 或更多信号而没有 EXIT → HOLD

第 4 步 — 决定：
  - 情绪和技术面一致 → 发出信号
  - 情绪和技术面不一致 → 持有
  - 带有退出信号的开仓 → 退出
  - 没有退出信号的开仓 → 持有
  - 无仓位且无明确信号 → HOLD

{{评论：上面使用 max_repeat val 作为连续非退出信号的安全上限}}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。This prompt is a comprehensive trading signal generator utilizing sentiment analysis and technical indicators. It fetches the Fear & Greed Index to determine market sentiment and uses RSI and MACD for technical confirmation. The strategy logic includes sentiment biasing, technical confirmation, position checks, and decision-making rules, ensuring a disciplined trading approach.

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
