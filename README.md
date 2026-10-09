# TPrompts

TPrompts 是一个简体中文静态提示词模板站（页面标题为「TPrompts · 提示词模板库」）。整个站点是一个用 URL hash 切换的单页：提示词库收录带预览图的网页与界面组件提示词，灵感板块收录带中文译文的通用提示词，品味页做人工精选，另外还有「他们在用」和 Roadmap。页面、样式和交互都在 `index.html` 里，数据通过 `window.*_DATA` 放在几个 JavaScript 文件中。仓库里写明的公开地址是 [https://prompts.tpgofighting.top/](https://prompts.tpgofighting.top/)。

## 功能

- **首页**（`#/`）：介绍 Prompt Planet 和角色「提仔 Tippy」，包括世界观、故事、八步工作流、可切换的插画展台，以及右下角可点的提仔挂件。首页同时链到提示词库、灵感和品味。
- **提示词库**（`#/library`，分类页 `#/cat/…`，详情 `#/p/…`）：760 条，分为 8 类：创意 & 3D、组件模块、金融 & 电商、Hero 首屏、SaaS & 商业、Landing Page、生活方式、其他页面。分类页还可按 Hero、移动端、Landing、定价、社媒 & 博客、组件筛选。搜索匹配标题、简介、分类、类型和标签，每页 24 条。详情可在中文、英文和使用说明之间切换并复制。`free` 为 `false` 的 290 条显示「待开放」，不能复制。
- **封面**：435 条使用 `images/` 里的本地图，列表优先请求 `images/thumbs/` 中的 WebP 缩略图，失败时回退原图。455 条带有远程动图或视频地址；MP4 进入视口后播放，离开视口暂停。
- **灵感**（`#/inspire`，详情 `#/i/…`）：2112 条。数据里有 53 个来源分类，页面收成 10 个主题。可查看中文、英文原文和使用说明，搜索匹配标题、正文和说明，每页 24 条。页面文案注明这些条目来自 prompts.chat，并附有中文翻译。
- **品味**（`#/taste`）：`curated-data.js` 手工维护，现有 5 个栏目、19 条，条目来自提示词库或灵感，并带编辑批注。
- **他们在用**（`#/creators`，详情 `#/c/…`）：3 份创作者资料、16 条提示词。可按人筛选，也可按标题、简介、分类和标签搜索。条目状态为「整理稿」或「原文整理」。
- **Roadmap**（`#/about`）：列出已上线、进行中和计划中的事项。进行中的「全站搜索」和计划中的收藏、投稿尚未实现；提示词库和灵感目前各自搜索。
- 从卡片打开详情时，详情层会从卡片位置展开。窄屏下导航改为横向滚动。在非输入框里按 `/` 会聚焦当前页的搜索框。

## 技术栈

- 纯静态 HTML、CSS 和 JavaScript，没有前端框架，当前仓库也没有 `package.json`。
- 路由使用 `location.hash`。数据挂在 `window.PROMPTS_DATA`、`window.INSPIRE_DATA`、`window.CURATED_DATA`、`window.CREATOR_DATA`。
- `prompts-data.js` 和 `inspire-data.js` 在进入对应页面时再动态插入脚本；策展和创作者数据随页面一并加载。
- 字体使用系统字体（Inter、苹方、微软雅黑等），样式写在 `index.html` 内。
- `robots.txt`、`sitemap.xml`、`llms.txt`，以及 `index.html` 里的 description、canonical、Open Graph 和 JSON-LD，指向同一站点地址。

## 项目结构

```text
index.html            页面、样式、路由与交互
prompt-access.js      待开放判断，以及把待开放条目排到后面
prompts-data.js       提示词库数据
inspire-data.js       灵感数据
curated-data.js       品味策展
creator-data.js       「他们在用」
images/               提示词封面原图（GIF、WebP、PNG、SVG、JPG）
images/thumbs/        封面 WebP 缩略图
assets/               Logo、提仔插画（PNG 与 WebP）、创作者头像
提仔/                 提仔 PNG 原图；index.html 不引用这个目录
tippy_manifest.json   提仔图片文件名与尺寸清单
tippy_scenes.json     提仔场景文案和 assets/tippy 下的图片路径
llms.txt              给检索引用用的站点说明
robots.txt
sitemap.xml
```

`tippy_manifest.json` 和 `tippy_scenes.json` 不由 `index.html` 加载。

## 本地运行

克隆后在仓库根目录启动静态文件服务即可，不需要安装依赖：

```bash
python3 -m http.server 4173 --bind 127.0.0.1
```

浏览器打开 <http://127.0.0.1:4173/>。提示词库和灵感的数据文件各约 9 MB，第一次进入这两个页面时会再请求一次。

## 构建与部署

当前仓库没有构建脚本、依赖清单、容器配置或 CI。发布时把仓库根目录当作静态站点的根目录即可，入口文件是 `index.html`。`index.html`、`robots.txt`、`sitemap.xml` 和 `llms.txt` 中的线上地址都是 <https://prompts.tpgofighting.top/>。
