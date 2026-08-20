# Candlestick Reversal Pattern Detector in Pine Script

**Description:** Create a TradingView indicator in Pine Script v5 to detect and label candlestick reversal patterns with trend and RSI filters.

**Type:** TEXT
**Author:** cutejsq
**Created:** 2025-12-28T17:37:40.340Z
**Votes:** 1
**Views:** 0

**Tags:** Finance, Automation, Investing

## Prompt Content

```
Act as a TradingView Pine Script v5 developer. You are tasked with creating an indicator that automatically detects and plots candlestick reversal patterns on the price chart. 

Your task is to:
- Identify and label the following candlestick patterns:
  - Bullish: Morning Star, Hammer
  - Bearish: Evening Star, Bearish Engulfing
- For each detected pattern:
  - Plot a green upward arrow below the candle for bullish patterns with the text “BUY: Pattern Name”
  - Plot a red downward arrow above the candle for bearish patterns with the text “SELL: Pattern Name”
- Add optional trend confirmation using a moving average (user-selectable length).
  - Only show bullish signals above the MA and bearish signals below the MA (toggleable).
- Include an optional RSI panel:
  - RSI length input
  - Overbought and oversold levels
  - Allow RSI to be used as an additional filter for signals (on/off)
- Ensure the indicator overlays signals on the price chart and uses clear labels and arrows 
- Allow user inputs to enable/disable each candlestick pattern individually
- Make sure the script is clean, optimized, and fully compatible with TradingView.
```

**Source:** https://prompts.chat/prompts/cmjq0ijn7000hji04hwbgmota_candlestick-reversal-pattern-detector-in-pine-script

## 中文翻译

### 标题
Pine 脚本中的烛台反转模式检测器

### 提示词内容

```
担任 TradingView Pine Script v5 开发人员。您的任务是创建一个指标，自动检测并在价格图表上绘制烛台反转模式。 

你的任务是：
- 识别并标记以下烛台形态：
  - 看涨：晨星、锤子
  - 看跌：黄昏之星、看跌吞没
- 对于每个检测到的模式：
  - 在看涨形态的蜡烛下方绘制一个绿色向上箭头，并带有文本“买入：形态名称”
  - 在看跌形态的蜡烛上方绘制一个红色向下箭头，并带有文本“卖出：形态名称”
- 添加使用移动平均线（用户可选择长度）的可选趋势确认。
  - 仅显示 MA 上方的看涨信号和 MA 下方的看跌信号（可切换）。
- 包括可选的 RSI 面板：
  - RSI长度输入
  - 超买和超卖水平
  - 允许 RSI 用作信号的附加过滤器（开/关）
- 确保指标覆盖价格图表上的信号并使用清晰的标签和箭头 
- 允许用户输入单独启用/禁用每个烛台图案
- 确保脚本干净、优化且与 TradingView 完全兼容。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**数据分析与可视化**类的提示词。Create a TradingView indicator in Pine Script v5 to detect and label candlestick reversal patterns with trend and RSI filters.

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
