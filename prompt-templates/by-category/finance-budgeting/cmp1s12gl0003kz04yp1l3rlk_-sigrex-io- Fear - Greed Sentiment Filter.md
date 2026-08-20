# [sigrex.io] Fear & Greed Sentiment Filter

**Description:** This prompt uses the Fear & Greed Index as a sentiment filter to provide trading signals for cryptocurrencies. It defines rules for entering and exiting positions based on market sentiment and technical indicators like RSI and MACD. Customize parameters like the trading symbol and RSI thresholds to fit your strategy.

**Type:** TEXT
**Author:** sigrex
**Created:** 2026-05-11T22:31:53.781Z
**Votes:** 0
**Views:** 0

**Tags:** Strategy, trading

**Category:** Finance & Budgeting

## Prompt Content

```
{{val:symbol=BTCUSDT}}
{{val:rsi_ob=68}}
{{val:rsi_os=32}}

Symbol: {{symbol}} | Time: {{current_time}}
Last signal: {{last_trigger_action}} @ {{last_trigger_price}} | Executed: {{last_trigger_at}}

Signal history:
{{trigger_history}}

Current market sentiment data:
{{get:https://api.alternative.me/fng/?limit=1&format=json}}

STRATEGY RULES:
Use the Fear & Greed value fetched above as a sentiment filter:
- Value 0–30 = Extreme Fear → favor LONG setups only
- Value 31–50 = Fear → allow LONG, avoid SHORT
- Value 51–74 = Greed → allow SHORT, be cautious with LONG
- Value 75–100 = Extreme Greed → favor SHORT setups only

LONG when:
  - Sentiment is Extreme Fear or Fear
  - RSI is below {{rsi_os}} and turning up
  - MACD histogram crosses positive
  - No open position

SHORT when:
  - Sentiment is Extreme Greed or Greed
  - RSI is above {{rsi_ob}} and turning down
  - MACD histogram crosses negative
  - No open position

EXIT when:
  - RSI crosses back to neutral (45–55 range)
  - OR sentiment flips against current position direction

HOLD if sentiment and technicals disagree, or no clear signal.
```

**Source:** https://prompts.chat/prompts/cmp1s12gl0003kz04yp1l3rlk_sigrexio-fear-greed-sentiment-filter

## 中文翻译

### 标题
[sigrex.io] 恐惧与贪婪情绪过滤器

### 提示词内容

```
{{val:symbol=BTCUSDT}}
{{val:rsi_ob=68}}
{{val:rsi_os=32}}

符号：{{符号}} |时间：{{current_time}}
最后信号：{{last_trigger_action}} @ {{last_trigger_price}} |执行：{{last_trigger_at}}

信号历史：
{{trigger_history}}

当前市场情绪数据：
{{获取：https://api.alternative.me/fng/?limit=1&format=json}}

策略规则：
使用上面获取的恐惧和贪婪值作为情绪过滤器：
- 值 0–30 = 极度恐惧 → 仅支持长设置
- 值 31–50 = 恐惧 → 允许做多，避免做空
- 值 51–74 = 贪婪 → 允许 SHORT，谨慎使用 LONG
- 值 75–100 = 极度贪婪 → 仅支持短设置

长时：
  - 情绪是极度恐惧或恐惧
  - RSI 低于 {{rsi_os}} 并出现上升
  - MACD柱状图正向交叉
  - 没有未平仓头寸

短路时：
  - 情绪是极度贪婪还是贪婪
  - RSI 高于 {{rsi_ob}} 并向下
  - MACD柱状图与负相交叉
  - 没有未平仓头寸

退出时：
  - RSI 交叉回到中性（45-55 范围）
  - 或情绪与当前头寸方向相反

如果情绪与技术面不一致或没有明确信号，则持有。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。This prompt uses the Fear & Greed Index as a sentiment filter to provide trading signals for cryptocurrencies. It defines rules for entering and exiting positions based on market sentiment and technical indicators like RSI and MACD. Customize parameters like the trading symbol and RSI thresholds to fit your strategy.

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
