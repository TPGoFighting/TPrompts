# TPrompts · 项目完整介绍

> 一个纯前端、零依赖、双击即用的提示词检索站。孟菲斯设计风格。

## 一、项目定位

TPrompts 是 TP 的个人提示词站点，聚合三类内容：
1. **提示词库**：435 条网页组件提示词（Hero / Landing / 组件 / SaaS 等 8 大归并分类），带预览图，可直接投喂 AI 编码工具
2. **灵感**：2112 条来自 prompts.chat 的通用提示词（写作/编程/图像/求职等 55 个分类），双语对照 + 使用说明
3. **品味**：编辑精选策展（库 + 灵感混编，手动维护）

## 二、技术架构

- **纯静态单页应用**：单文件 `index.html`（约 66KB，CSS + JS 全内联）+ 数据 JS 文件，无框架、无构建、无依赖
- **Hash 路由**：`#/` `#/library` `#/inspire` `#/taste` `#/about` `#/cat/<分类>` `#/p/<id>` `#/i/<id>` `#/search?q=<词>`
- **数据层**（三个全局变量，`<script>` 直接加载，兼容 `file://` 协议双击打开）：
  | 文件 | 全局变量 | 内容 | 大小 |
  |------|---------|------|------|
  | `prompts-data.js` | `window.PROMPTS_DATA` | 435 条库提示词（含 zh/en/usage/图） | ~5MB |
  | `inspire-data.js` | `window.INSPIRE_DATA` | 2112 条灵感（含 titleZh/zh/usage/ai 标记） | ~8MB |
  | `curated-data.js` | `window.CURATED_DATA` | 品味策展（5 分区 19 条，手动维护） | ~3KB |

- **零 XSS 风险**：所有动态内容经 `esc()` 转义 + 自研轻量 Markdown 渲染器（`mdToHtml`，支持代码块/表格/列表/粗斜体）

## 三、功能清单

### 1. 首页（门户）
- 品牌 Hero：超大标题「GOOD PROMPTS DESERVE GOOD TASTE.」
- 双 CTA：进入提示词库 / 逛逛灵感
- **三大门户卡**（孟菲斯色块）：提示词库 435 · 灵感 2112 · 品味 N，点击直达
- **本周编辑推荐**：拉取品味页首个分区的 Top 3，跨板块直达详情

### 2. 提示词库 `#/library`
- 全库搜索（标题/描述/分类/类型/标签）
- 8 个归并分类 chips（带数量）→ 分类页
- 卡片网格：预览图（本地图/动图/视频悬停播放/波普色兜底）+ 标题 + 描述 + 标签 + 一键复制中文
- 24 条/页分页（智能页码省略）

### 3. 分类页 `#/cat/<分类>`
- type 归并筛选 chips（Hero/移动端/Landing/定价/社媒&博客/组件）
- 分类内搜索 + 分页

### 4. 库详情页 `#/p/<id>`
- 左：预览媒体（封面图/页面内播放 mp4/HLS 链接）；右：标题 + 描述 + 标签
- 三 Tab：🇨🇳 中文提示词 / 🇺🇸 英文原版 / 📖 使用说明，各带复制按钮
- 上一条/下一条导航

### 5. 灵感 `#/inspire`（本次新增）
- **文本优先卡片**（无封面图）：中文标题为主 + 英文原标题 + 中文摘要 + 分类 + 复制中文
- 55 个英文分类 → **中文映射**筛选 chips（带数量，按条数排序）
- 全字段搜索（标题/正文/说明，中英文都搜）
- 24 条/页分页
- **AI 翻译标记**：AI 翻译条目显示紫色「AI 译」徽章，机翻显示灰色「机翻待升级」

### 6. 灵感详情页 `#/i/<id>`（独立设计，与库详情区分）
- `.idp-*` 专属样式：720px 居中 + 左侧 coral 竖条 + 黑底分类 badge
- 头部：中文标题（大字）+ 英文原标题 + 分类 + 来源编号（INSPIRE ✦ 0001/2112）+ **AI 译徽章**
- 双复制按钮：复制中文 / Copy English
- 三 Tab：🇨🇳 中文翻译 / 🇺🇸 English Original / 📖 使用说明
- 上一条/下一条导航

### 7. 品味 `#/taste`（编辑策展）
- 策展人手记 + 更新时间
- 主题分区（本周精选/写作与表达/代码与效率/图像与创意/求职与成长），每区标签 badge + 一句话
- 策展卡：来源徽章（LIBRARY=蓝 / INSPIRE=绿）+ 标题 + **策展语**（引号样式）+ 分类，点击直达详情
- 数据在 `curated-data.js` 手动维护：`{src: 'library'|'inspire', id, note: 策展语}`

### 8. Roadmap `#/about`
- 三阶段时间线：✓ 已上线（带日期）/ 🔧 进行中 / ✦ 计划中
- 状态圆点 + 徽章 + 描述

### 9. 其他
- 键盘 `/` 聚焦搜索框
- Toast 复制反馈（clipboard API + execCommand 双 fallback）
- 移动端响应式（1024px 两列 / 600px 单列）
- 404 页

## 四、页面设计语言（孟菲斯风格）

- **色板**：`--coral:#ff6b57` `--sky:#a8ddff` `--pink:#ffc5d8` `--lime:#d9ef7f` `--grape:#d8cbff` `--sand:#ffd4a8`，米色底 `#fff9f1`，墨色 `#1f1b19`
- **特征**：2px 粗黑描边 + 3~5px 硬阴影（hover 时位移变大）+ 大圆角（12~20px）+ 950 字重标题
- **层级**：卡片 hover `translate(-2px,-4px)` + 阴影加深，按钮 hover 位移 + 阴影收缩
- **首页主界面**：孟菲斯（用户设定）；详情页沿用孟菲斯但结构独立（idp 布局）

## 五、数据管线（如何更新）

| 数据 | 来源 | 更新方式 |
|------|------|---------|
| 提示词库 | Obsidian Vault 提示词模板 | `node build-data.js`（解析 frontmatter + 中英提示词 + 使用说明 → prompts-data.js） |
| 灵感英文原文 | `~/Developer/ai-coding/prompt-templates/by-category/**/*.md` | 重新扫描即可 |
| 灵感翻译 | `inspire_zh.ndjson`（断点续传） | `python3 inspire_translate_gemini.py`（免费层）/ `python3 inspire_translate.py`（DeepSeek 付费） |
| 灵感数据汇总 | ndjson + md | `python3 build-inspire-data.py` → inspire-data.js（带 ai 标记） |
| 品味策展 | 手动 | 编辑 `curated-data.js` 的 sections |

## 六、当前数据状态（2026-08-19）

- 提示词库：435 条（含中英双语 + 使用说明 + 预览图）
- 灵感：2112 条
  - **281 条** DeepSeek 大模型翻译（`ai: true`，页面显示「AI 译」）
  - **1831 条** 旧机翻兜底（`ai: false`，页面显示「机翻待升级」）—— 待用 Gemini 免费层升级
- 品味：5 分区 19 条精选

## 七、已知注意点

- 旧机翻数据存在 JSON 引号被翻成中文引号的问题（复制代码类提示词会损坏），这正是 AI 重译要解决的
- 所有数据文件用 `file://` 打开即可运行，无需服务器
- 部署到服务器（如 tpgofighting.top 子域）走 rsync + nginx 静态托管即可
