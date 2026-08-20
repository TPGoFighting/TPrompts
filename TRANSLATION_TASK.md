# 任务：批量翻译 TPrompts「灵感」板块剩余提示词

## 你的角色
你是 TPrompts 网站的数据翻译工程师，负责把一批英文 AI 提示词翻译成高质量中文，并撰写使用说明。

## 项目背景
TPrompts（/Users/tylertang/Developer/ai-coding/tprompts-site/）是一个纯前端提示词检索站，包含：
- 提示词库（435 条网页组件提示词，已完成）
- **灵感板块**（2112 条来自 prompts.chat 的英文提示词）：每条需要「中文标题翻译 + 中文正文翻译 + 中文使用说明」，供中文用户复制使用。

目前已有 **281 条**由大模型高质量翻译完成，**剩余 1831 条**还是旧的机器翻译（质量差、JSON 引号损坏），需要你接手翻译。

## 数据位置
- 英文原文（1831 条待翻译）: `/Users/tylertang/Developer/ai-coding/prompt-templates/by-category/**/*.md`
  - 每条 md 的 id = 文件名第一个下划线前（如 `cmj1zb1jl00bqvl0rzhc15fdq_Ascii Artist.md` → id `cmj1zb1jl00bqvl0rzhc15fdq`）
  - 标题 = 首行 `# Title`
  - 分类 = 所在目录名（如 `coding`、`image-generation`）
  - 英文正文 = `## Prompt Content` 下的代码块内容
- 已完成翻译（**不要重复翻译，断点续传**）: `/Users/tylertang/Developer/ai-coding/tprompts-site/inspire_zh.ndjson`
  - 每行一条 JSON：`{"id","title_zh","zh","usage"}`
- 数据汇总脚本（翻译完成后运行）: `/Users/tylertang/Developer/ai-coding/tprompts-site/build-inspire-data.py`
  - 合并 ndjson + md → 生成 `inspire-data.js`（带 `ai: true/false` 标记），输出到站点目录

## 已有翻译脚本（推荐直接用，别重写轮子）
两个脚本都支持断点续传（自动跳过已完成的 id），都输出到同一个 `inspire_zh.ndjson`：

1. **免费方案（强烈推荐，0 成本）**: `python3 inspire_translate_gemini.py`
   - 用 Google AI Studio 免费层（GEMINI_API_KEY 在 ~/.hermes/.env，模型 gemini-3.7-flash，每天 1500 次请求额度）
   - 默认每批 4 条、2 并发，失败自动拆半重试，不会触发限流
   - 预计剩余 1831 条约需 1.5~2 小时，完全免费

2. **付费方案（备用）**: `python3 inspire_translate.py`
   - DeepSeek 官方 API（deepseek-chat），效果也很好但花钱，能不用就不用

## 翻译质量要求（最高优先级）
1. 忠实原意，语言自然流畅，符合中文表达习惯，不要机翻腔
2. **【关键】如果提示词包含代码/JSON/配置文件/结构化数据，必须完整保留结构**：
   - 代码、JSON 键名、变量名、函数名、URL、文件路径、技术标识符一律**不翻译**
   - 所有字符串值中的引号必须保持半角英文引号 `"`（绝不能改成中文引号“”）
   - 花括号、方括号、冒号等标点保持半角
3. 标题翻译简洁准确（不超过 30 个汉字）
4. 使用说明（usage）用中文写 100~200 字，**贴合本条提示词的具体内容**，说明：它能让 AI 做什么、适合什么人用、具体怎么用（步骤要点）、注意什么。不要空话套话，不要每条雷同
5. 输出 JSON 数组：`[{"id","title_zh","zh","usage"}]`，id 必须与输入一一对应

## 执行步骤
1. 先 `cd /Users/tylertang/Developer/ai-coding/tprompts-site`
2. 检查现状：`python3 inspire_translate_gemini.py --dry`（会显示总数/已完成/剩余）
3. 启动免费翻译：`python3 inspire_translate_gemini.py`（后台跑，定期查看进度）
4. 若脚本因网络/限流中断，直接重新运行同一命令，它会自动跳过已完成的继续
5. 翻译全部完成后，确认 `wc -l inspire_zh.ndjson` = 2112
6. 运行 `python3 build-inspire-data.py` 重新生成 `inspire-data.js`
7. 验证生成结果里 `ai: true` 的数量 = 2112（应全部是 AI 翻译，无机翻兜底）

## 红线
- **不要**修改/删除 `inspire_zh.ndjson` 里已有的 281 条（那是 DeepSeek 高质量翻译，直接复用）
- **不要**动 `prompt-templates/` 里的任何 md 原文件
- **不要**用付费 API 大批量翻译（Gemini 免费层够用；成本超预期前先停手问用户）
- 单条反复失败的（极端长文本），可以单独用更小的批次重试；仍失败的记录 id 和原因，不要静默丢弃
- 翻译脚本的 API key 从 ~/.hermes/.env 读取，不要打印、不要外传 key

## 交付
翻译完成后汇报：翻译条数、耗时、失败/跳过明细、inspire-data.js 是否已重新生成、页面是否需要刷新验证。
