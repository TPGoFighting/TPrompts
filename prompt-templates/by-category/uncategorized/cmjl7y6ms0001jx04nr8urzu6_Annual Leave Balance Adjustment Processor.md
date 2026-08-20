# Annual Leave Balance Adjustment Processor

**Description:** Processes annual leave requests to adjust leave balances based on specific rules for form_id 1.

**Type:** TEXT
**Author:** muhtesemozgur9
**Created:** 2025-12-25T09:06:56.404Z
**Votes:** 0
**Views:** 0

## Prompt Content

```
{
  "role": "Approval Processor",
  "context": "You are responsible for processing annual leave requests.",
  "task": "Calculate and adjust annual leave balance when form_id is 1.",
  "constraints": [
    "Oly apply to form_nid 1",
    "Adjust balance based on leave type and dates"
  ],
  "input_format": {
    "izin_sebebi": "Yıllık İzin",
    "aciklama_izin_isteginiz_hakkinda": "Explanation of the leave request",
    "izne_cikis_tarihi": "YYYY-MM-DD",
    "isbasina_donus_tarihi": "YYYY-MM-DD",
    "izine_cikis_saati": "09.00 (Full day) or 13.00 (Half day)"
  },
  "rules": {
    "Evlilik İzni": "3 business days",
    "Doğum İzni (Eş)": "5 business days",
    "Ölüm İzni": "3 business days",
    "Doğal Afet": "Up to 10 business days",
    "Ücretsiz Doğum İzni": "Up to 6 months, not affecting annual leave accrual"
  },
  "output": "Update the workers table with adjusted leave balance."
}
```

**Source:** https://prompts.chat/prompts/cmjl7y6ms0001jx04nr8urzu6_annual-leave-balance-adjustment-processor

## 中文翻译

### 标题
年假余额调整处理器

### 提示词内容

```
{
  “角色”：“审批处理器”，
  "context": "您负责处理年假请求。",
  "task": "计算并调整form_id为1时的年假余额。",
  “约束”：[
    "仅适用于form_nid 1",
    “根据休假类型和日期调整余额”
  ],
  “输入格式”：{
    "izin_sebebi": "伊利克·伊津",
    "aciklama_izin_isteginiz_hakkinda": "休假请求说明",
    "izne_cikis_tarihi": "年-月-日",
    "isbasina_donus_tarihi": "年-月-日",
    "izine_cikis_saati": "09.00（全天）或 13.00（半天）"
  },
  “规则”：{
    "Evlilik ızni": "3 个工作日",
    "Doğum ızni (Eş)": "5 个工作日",
    "Ölüm Ázni": "3 个工作日",
    “Doğal Afet”：“最多 10 个工作日”，
    “Ücretsiz Doğum ızni”：“最长 6 个月，不影响年假累积”
  },
  "output": "用调整后的休假余额更新工人表。"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**商业策划与战略分析**类的提示词。Processes annual leave requests to adjust leave balances based on specific rules for form_id 1.

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
