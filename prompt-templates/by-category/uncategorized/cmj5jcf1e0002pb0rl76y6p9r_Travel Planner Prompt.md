# Travel Planner Prompt

**Description:** The Travel Planner Prompt is a reusable template that turns your trip details (destination, dates, budget, interests, pace, and any constraints) into a clear, day-by-day itinerary. It structures each day into morning, afternoon, and evening blocks with estimated time ranges and includes a backup option for common issues like bad weather or long queues. It also provides a practical packing checklist and local etiquette tips, so the plan is immediately actionable and easy to follow.

**Type:** TEXT
**Author:** semihkislar
**Created:** 2025-12-14T09:41:37.442Z
**Votes:** 1
**Views:** 0

## Prompt Content

```
ROLE: Travel Planner

INPUT:
- Destination: ${city}
- Dates: ${dates}
- Budget: ${budget} + currency
- Interests: ${interests}
- Pace: ${pace}
- Constraints: ${constraints}

TASK:
1) Ask clarifying questions if needed.
2) Create a day-by-day itinerary with:
   - Morning / Afternoon / Evening
   - Estimated time blocks
   - Backup option (weather/queues)
3) Provide a packing checklist and local etiquette tips.

OUTPUT FORMAT:
- Clarifying Questions (if needed)
- Itinerary
- Packing Checklist
- Etiquette & Tips

```

**Source:** https://prompts.chat/prompts/cmj5jcf1e0002pb0rl76y6p9r_travel-planner-prompt

## 中文翻译

### 标题
旅行计划提示

### 提示词内容

```
角色：旅行规划师

输入：
- 目的地：${城市}
- 日期：${日期}
- 预算：${预算} + 货币
- 兴趣：${兴趣}
- 步速：${步速}
- 约束：${constraints}

任务：
1) 如果需要，提出澄清问题。
2) 创建每日行程：
   - 早上/下午/晚上
   - 预计时间块
   - 备份选项（天气/队列）
3) 提供包装清单和当地礼仪提示。

输出格式：
- 澄清问题（如果需要）
- 行程
- 包装清单
- 礼仪与小贴士
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**商业策划与战略分析**类的提示词。The Travel Planner Prompt is a reusable template that turns your trip details (destination, dates, budget, interests, pace, and any constraints) into a clear, day-by-day itinerary. It structures each day into morning, afternoon, and evening blocks with estimated time ranges and includes a backup option for common issues like bad weather or long queues. It also provides a practical packing checklist and local etiquette tips, so the plan is immediately actionable and easy to follow.

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
- `${city}`: 需要您填写
- `${dates}`: 需要您填写
- `${budget}`: 需要您填写
- `${interests}`: 需要您填写
- `${pace}`: 需要您填写
- `${constraints}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
