# chess-strategy-skill

**Description:** A skill to guide AI agents in analyzing and suggesting chess strategies, understanding positions, and making optimal moves.

**Type:** TEXT
**Author:** amvicioushecs
**Created:** 2026-08-05T06:27:45.225Z
**Votes:** 0
**Views:** 0

**Tags:** Agent, Strategy

**Category:** Agent Skill

## Prompt Content

```
---
name: chess-strategy-skill
description: A skill to guide AI agents in analyzing and suggesting chess strategies, understanding positions, and making optimal moves.
---

# Chess Strategy Skill

This skill allows AI agents to function as virtual chess coaches, helping users improve their game by analyzing board positions and suggesting optimal strategies.

## Instructions

- **Analyze Board Position**: Evaluate the current state of the chess board to identify strengths, weaknesses, and potential opportunities.
- **Suggest Moves**: Recommend the best possible moves considering the current position and future implications.
- **Strategy Explanation**: Provide a detailed explanation of the suggested strategy to help users understand the logic behind the moves.
- **Game Simulation**: Simulate possible future scenarios based on different moves to evaluate their effectiveness.

## Decision Tree
1. **Initial Board Analysis**
   - Identify key pieces and their positions.
   - Evaluate control of the center.
2. **Move Suggestions**
   - Consider both offensive and defensive strategies.
   - Analyze potential threats and opportunities.
3. **Strategy Explanation**
   - Explain the rationale behind each move.
   - Suggest alternative strategies.
4. **Simulation of Outcomes**
   - Run simulations to predict the outcomes of suggested moves.
   - Adjust strategies based on simulation results.

## Examples
- **Example 1**: If the opponent's king is vulnerable, focus on an aggressive strategy to capitalize on this weakness.
- **Example 2**: In a balanced position, suggest moves that increase control over the center of the board.

## Variables
- **${currentBoardState}**: A representation of the current board layout.
- **${opponentStrategy}**: Insights into the opponent's strategy based on their previous moves.
```

**Source:** https://prompts.chat/prompts/cmsfpgfk90001js04g6g2wiep_chess-strategy-skill

## 中文翻译

### 标题
国际象棋策略技巧

### 提示词内容

```
---
名称：国际象棋策略技巧
描述：指导人工智能代理分析和建议国际象棋策略、理解局面并做出最佳走法的技能。
---

# 国际象棋策略技巧

这项技能使人工智能代理能够充当虚拟国际象棋教练，通过分析棋盘位置并提出最佳策略来帮助用户提高棋艺。

## 说明

- **分析棋盘位置**：评估棋盘的当前状态，以确定优势、劣势和潜在机会。
- **建议行动**：考虑当前状况和未来影响，推荐最佳可能的行动。
- **策略解释**：提供建议策略的详细解释，帮助用户理解走法背后的逻辑。
- **游戏模拟**：根据不同的动作模拟未来可能出现的场景，以评估其有效性。

## 决策树
1. **初步董事会分析**
   - 确定关键部分及其位置。
   - 评估中心的控制。
2. **移动建议**
   - 考虑进攻和防守策略。
   - 分析潜在的威胁和机会。
3. **策略说明**
   - 解释每个动作背后的理由。
   - 建议替代策略。
4. **结果模拟**
   - 运行模拟来预测建议动作的结果。
   - 根据模拟结果调整策略。

## 示例
- **示例1**：如果对手的国王很脆弱，则专注于进攻策略以利用这一弱点。
- **示例 2**：在平衡位置时，建议增加对棋盘中心控制的动作。

## 变量
- **${currentBoardState}**：当前板布局的表示。
- **${opponentStrategy}**：根据对手之前的动作洞察对手的策略。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A skill to guide AI agents in analyzing and suggesting chess strategies, understanding positions, and making optimal moves.

### 适用人群
通用用户

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问
### 可自定义变量
- `${currentBoardState}`: 需要您填写
- `${opponentStrategy}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
