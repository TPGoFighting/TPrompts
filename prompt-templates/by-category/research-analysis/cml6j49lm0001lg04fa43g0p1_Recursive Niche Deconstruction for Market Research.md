# Recursive Niche Deconstruction for Market Research

**Description:** Perform a Recursive Niche Deconstruction to identify dominant companies in specific market verticals. Analyze the market size and competitive landscape at each level of niche breakdown.

**Type:** TEXT
**Author:** amvicioushecs
**Created:** 2026-02-03T11:42:27.994Z
**Votes:** 0
**Views:** 0

**Tags:** Market Analysis, Business Strategy

**Category:** Research & Analysis

## Prompt Content

```
{
  "industry": "${industry}",
  "region": "${region}",
  "tree": {
    "level": "Macro",
    "name": "...",
    "market_valuation": "$X",
    "top_players": [
      {
        "name": "Company A",
        "type": "Incumbent",
        "focus": "Broad"
      },
      {
        "name": "Company B",
        "type": "Incumbent",
        "focus": "Broad"
      }
    ],
    "children": [
      {
        "level": "Sub-Niche/Micro",
        "name": "...",
        "narrowing_variable": "...",
        "market_valuation": "$X",
        "top_players": [
          {
            "name": "Startup C",
            "type": "Specialist",
            "focus": "Verticalized"
          },
          {
            "name": "Tool D",
            "type": "Micro-SaaS",
            "focus": "Hyper-Specific"
          }
        ],
        "children": []
      }
    ]
  },
  "keyword_analysis": {
    "monthly_traffic": "{region-specific traffic data}",
    "competitiveness": "{region-specific competitiveness data}",
    "potential_keywords": [
      {
        "keyword": "...",
        "traffic": "...",
        "competition": "..."
      }
    ]
  }
}
```

**Source:** https://prompts.chat/prompts/cml6j49lm0001lg04fa43g0p1_recursive-niche-deconstruction-for-market-research

## 中文翻译

### 标题
市场研究的递归利基解构

### 提示词内容

```
{
  "行业": "${行业}",
  "地区": "${地区}",
  “树”：{
    "level": "宏",
    “名称”：“...”，
    "market_valuation": "$X",
    “顶级玩家”：[
      {
        “名称”：“A公司”，
        "type": "现任",
        “焦点”：“广泛”
      },
      {
        "name": "B公司",
        "type": "现任",
        “焦点”：“广泛”
      }
    ],
    “孩子们”：[
      {
        "level": "子利基/微观",
        “名称”：“...”，
        "narrowing_variable": "...",
        "market_valuation": "$X",
        “顶级玩家”：[
          {
            "name": "启动C",
            “类型”：“专家”，
            “焦点”：“垂直化”
          },
          {
            "name": "工具D",
            "type": "微SaaS",
            “焦点”：“超具体”
          }
        ],
        “孩子们”：[]
      }
    ]
  },
  “关键字分析”：{
    "monthly_traffic": "{特定区域的流量数据}",
    "competitiveness": "{地区特定竞争力数据}",
    “潜在关键字”：[
      {
        “关键字”：“...”，
        "交通": "...",
        “竞争”：“……”
      }
    ]
  }
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**数据分析与可视化**类的提示词。Perform a Recursive Niche Deconstruction to identify dominant companies in specific market verticals. Analyze the market size and competitive landscape at each level of niche breakdown.

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
- `${industry}`: 需要您填写
- `${region}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
