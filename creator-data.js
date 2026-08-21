/* creator-data.js - 「他们在用」博主来源与提示词整理数据
 * 约定：prompt.status = 「整理稿」表示基于公开内容重新编排，不冒充原文逐字引用。
 */
window.CREATOR_DATA = {
  updated: '2026-08-21',
  creators: [
    {
      id: 'khazix',
      name: '数字生命卡兹克',
      avatar: 'assets/creators/khazix.jpg',
      handle: '@Khazix0918',
      focus: 'Agent · Skills · 工作流',
      bio: '把 AI 从一次性对话，变成可以重复调用的工作流。',
      accent: 'lime',
      sourceLabel: '开源 Skills 合集',
      sourceUrl: 'https://github.com/KKKKhazix/Khazix-Skills',
      sourceVerified: true
    },
    {
      id: 'aiwarts',
      name: '卡尔的 AI 沃茨',
      avatar: 'assets/creators/aiwarts.jpg',
      handle: '@aiwarts',
      focus: '提问 · 反思 · 表达',
      bio: '先把问题说清楚，再让模型开始做事，减少“它替我猜”的情况。',
      accent: 'sky',
      sourceLabel: '公开文章',
      sourceUrl: 'https://kaerai.club/articles/fable-find-your-unknowns',
      sourceVerified: true
    },
    {
      id: 'nomad',
      name: '数字游牧人 Samuel',
      avatar: 'assets/creators/samuel.jpg',
      handle: '',
      focus: '效率 · 生活 · 迁徙',
      bio: '收录位已建，等一条可核对的文章、视频或原帖再正式入库。',
      accent: 'pink',
      sourceLabel: '待补出处',
      sourceUrl: '',
      sourceVerified: false
    },
  ],
  prompts: [
    {
      id: 'creator-khazix-01',
      creatorId: 'khazix',
      title: '把一次性提示词变成可复用 Skill',
      desc: '把重复任务拆成输入、步骤、产物与验收标准，适合交给 Agent 长期执行。',
      category: '工作流',
      tags: ['Agent', 'Skills', '自动化'],
      status: '整理稿',
      sourceNote: '基于公开 Skills 实践方向整理；非原文逐字引用。',
      prompt: `请把下面这项重复工作设计成一个可复用的 AI Skill。

目标任务：{{任务描述}}
使用者：{{谁会调用它}}
输入材料：{{输入}}

请按以下结构输出：
1. Skill 的一句话职责
2. 需要的输入字段，以及缺失时要追问的问题
3. 可执行的步骤清单，每一步写明产物
4. 失败、歧义和越权时的处理方式
5. 最终输出格式
6. 3 条验收标准，让我能判断它是否真的可复用

要求：把不确定的地方标成“需要确认”，不要替我补造背景。`
    },
    {
      id: 'creator-khazix-02',
      creatorId: 'khazix',
      title: '让 Agent 先做任务拆解，再开始执行',
      desc: '适合复杂研究、代码和内容任务：先暴露计划与依赖，再进入实际执行。',
      category: 'Agent',
      tags: ['拆解', '验收', '复杂任务'],
      status: '整理稿',
      sourceNote: '根据公开 Agent / Skills 方法论整理；非原文逐字引用。',
      prompt: `你现在是任务编排器，不要立即开始执行。

任务：{{任务描述}}

先输出：
- 你对目标的理解
- 已知信息与缺失信息
- 按依赖关系排序的执行步骤
- 每一步的完成判据
- 可能失败的地方与备选方案

只有在我回复“开始”后，才进入执行。执行过程中每完成一个步骤，都用“已完成 / 产出 / 下一步”三行更新进度。遇到超出任务范围的动作先停下来询问。`
    },
    {
      id: 'creator-aiwarts-01',
      creatorId: 'aiwarts',
      title: '帮我找到自己还没意识到的盲区',
      desc: '把模糊问题交给 AI 反向追问，先找缺失的变量，再给判断或方案。',
      category: '思考',
      tags: ['反问', '盲区', '决策'],
      status: '整理稿',
      sourceNote: '基于公开文章《7 个提示词技巧》整理；非原文逐字引用。',
      prompt: `我正在思考这个问题：{{问题}}
背景信息：{{已知背景}}

不要马上给我答案。请先像一位严谨的提问教练一样：
1. 列出你认为我可能忽略的 5 个关键变量
2. 说明每个变量为什么会改变结论
3. 按重要性只问我最值得先回答的 3 个问题
4. 如果我的问题本身带有未经验证的假设，请直接指出

等我回答后，再基于新信息给出结论、依据和仍然存在的不确定性。`
    },
    {
      id: 'creator-aiwarts-02',
      creatorId: 'aiwarts',
      title: '让 AI 在行动前先确认“我要什么”',
      desc: '适合需求不清、交付标准模糊的任务，减少模型按“常见答案”自作主张。',
      category: '表达',
      tags: ['需求', '确认', '输出标准'],
      status: '整理稿',
      sourceNote: '基于公开文章中的提问与澄清方法整理；非原文逐字引用。',
      prompt: `当我提出一个任务时，请先不要执行。

请用下面的格式复述你理解的需求：
- 我要达成的目标：
- 交付给谁：
- 我希望得到的形式：
- 不能改变的约束：
- 你仍然不确定的地方：

如果存在 3 个以上合理解释，先列出它们并让我选择；如果只有一个关键缺口，只问一个最小必要问题。得到确认后，再执行并在结尾检查结果是否满足上述标准。`
    },
    {
      id: 'creator-seo-01', creatorId: 'khazix', title: '按意图扩展关键词', desc: '按信息型、商业型、交易型和导航型意图建立真实关键词清单。', category: 'SEO', tags: ['关键词', '搜索意图', '内容策略'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Act as an SEO strategist. For the topic [TOPIC], generate 40 keyword ideas grouped by intent: informational, commercial, transactional, and navigational. Include a mix of short-tail, mid-tail, and long-tail queries. Avoid branded terms and avoid vague “best” queries unless they include a clear qualifier.`
    },
    {
      id: 'creator-seo-02', creatorId: 'khazix', title: '生成长尾问题词', desc: '从真实提问方式出发，寻找更容易匹配点击与精选摘要的查询。', category: 'SEO', tags: ['长尾词', '问题词', 'CTR'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Generate 25 long-tail, question-based keywords (5+ words) for [SEED KEYWORD]. Include variations starting with: “how to”, “what is”, “why”, “best way to”, “how much”. For each, label the likely intent and the ideal content type (blog post, landing page, FAQ, comparison).`
    },
    {
      id: 'creator-seo-03', creatorId: 'khazix', title: '把关键词聚成主题集群', desc: '把杂乱关键词整理成支柱页、支持文章和内链锚文本。', category: 'SEO', tags: ['聚类', '主题集群', '内链'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Cluster the following keywords into topic clusters. For each cluster, propose: 1 pillar page title, 6 supporting article titles, and recommended internal link anchor text. Keywords: [PASTE LIST].`
    },
    {
      id: 'creator-seo-04', creatorId: 'khazix', title: '拆解 SERP 搜索意图', desc: '先判断搜索结果奖励的内容形态，再规划更匹配意图的页面。', category: 'SEO', tags: ['SERP', '搜索意图', '页面结构'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Based on the keyword [KEYWORD], infer the dominant SERP intent. List the “likely top-ranking page patterns” (format, content depth, angle, entities, and common sections). Then give me a checklist for a page that would satisfy the same intent better.`
    },
    {
      id: 'creator-seo-05', creatorId: 'khazix', title: '生成 SEO 内容简报', desc: '把关键词、受众和目标整理成可以直接交给作者的写作 brief。', category: '内容', tags: ['Brief', '大纲', 'E-E-A-T'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Create an SEO content brief for [PRIMARY KEYWORD]. Audience: [AUDIENCE]. Goal: [GOAL]. Include: working title (5 options), search intent, H1/H2/H3 outline, key talking points per section, examples to include, objections to address, and suggested internal links (generic placeholders). Add an E-E-A-T plan (where to add experience, proof, and citations).`
    },
    {
      id: 'creator-seo-06', creatorId: 'khazix', title: '按段落写作，避免泛泛废话', desc: '限制每次生成的范围、可读性和实例，让文章更容易逐段打磨。', category: '写作', tags: ['分段写作', '可读性', '示例'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `You are writing section [SECTION NAME] of an article targeting [PRIMARY KEYWORD]. Constraints: 120–180 words, Grade 8 readability, include 1 practical example, avoid filler, and end with a 2-bullet takeaway list.`
    },
    {
      id: 'creator-seo-07', creatorId: 'khazix', title: '生成 Meta 标题与描述', desc: '围绕点击率写出多组长度受控、角度不同的 Meta 标题与描述。', category: 'SEO', tags: ['Meta', 'CTR', '标题'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Write 10 meta titles (max 58 characters) and 10 meta descriptions (max 155 characters) for a page targeting [PRIMARY KEYWORD]. Use an honest benefit, avoid clickbait, include a number when natural, and create variation in angle (speed, checklist, template, mistakes).`
    },
    {
      id: 'creator-seo-08', creatorId: 'khazix', title: '通读并优化页面内容', desc: '优化已有内容的清晰度、标题、内链和语义覆盖，同时标记风险。', category: '内容', tags: ['优化', '语义', '内容审校'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Optimize the following content for [PRIMARY KEYWORD] without changing meaning. Improve clarity, headings, internal linking opportunities, and semantic coverage. Flag: keyword stuffing risk, missing sections, and places to add examples. Content: [PASTE DRAFT].`
    },
    {
      id: 'creator-seo-09', creatorId: 'khazix', title: '绘制内链地图', desc: '根据 URL、目标关键词和搜索意图，规划页面之间的自然连接。', category: 'SEO', tags: ['内链', '锚文本', '信息架构'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `I have these URLs and targets: [PASTE URL LIST + TARGET KEYWORD]. Build an internal linking plan: which page links to which, suggested anchor text (natural), and where in the content it should appear. Prioritize pages with similar intent and avoid repetitive anchors.`
    },
    {
      id: 'creator-seo-10', creatorId: 'khazix', title: '生成并约束 Schema 草稿', desc: '按页面类型生成 JSON-LD，并要求模型只使用页面上确实存在的信息。', category: '技术 SEO', tags: ['Schema', 'JSON-LD', '校验'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Generate JSON-LD schema for a page about [TOPIC]. Page type: [Article/FAQ/HowTo/Product/LocalBusiness]. Include only fields that can be supported by visible on-page content. Return valid JSON-LD and a checklist of what must appear on the page to support it.`
    },
    {
      id: 'creator-seo-11', creatorId: 'khazix', title: '修剪并刷新旧内容', desc: '找出过时、重复或单薄的段落，给出删除、重写、合并和刷新大纲建议。', category: '内容', tags: ['内容刷新', '修剪', '搜索意图'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Review this article and identify sections that are outdated, redundant, or thin. Recommend what to remove, rewrite, or merge. Then propose a refreshed outline that better matches search intent for [PRIMARY KEYWORD]. Article: [PASTE].`
    },
    {
      id: 'creator-seo-12', creatorId: 'khazix', title: '挖掘 GSC 排名 8–20 的机会', desc: '从 Search Console 导出中找高曝光、接近首页的关键词，给出最小修改建议。', category: '数据驱动', tags: ['GSC', '排名', '增长机会'], status: '原文整理', sourceUrl: 'https://mp.weixin.qq.com/s/NAdhdFrUq9-BKelqzqpwBQ', sourceLabel: '微信原文', sourceNote: '来自你提供的微信文章；提示词主体保留英文原式。', prompt: `Analyze the following Google Search Console export. Identify keywords ranking positions 8–20 with high impressions. For each, recommend the smallest on-page change likely to move it to top 5 (heading tweak, section add, internal link, meta rewrite, intent alignment). Data: [PASTE GSC EXPORT].`
    }
  ]
};

/* SEO 12 条：保留英文原式，同时补齐中文可执行版本与场景说明。 */
const CREATOR_SEO_LOCALES = {
  'creator-seo-01': {
    zh: '请扮演 SEO 策略师。针对主题【主题】，生成 40 个关键词，并按信息型、商业型、交易型和导航型意图分组。混合短尾、中尾和长尾查询。避免品牌词；除非有明确限定词，否则不要生成含糊的“最佳”类查询。',
    usage: '适合从一个主题快速建立关键词池。把【主题】替换成产品、行业或内容主题，拿到结果后再用真实搜索数据验证，不要把模型生成的关键词量当成搜索量。'
  },
  'creator-seo-02': {
    zh: '请针对【种子关键词】生成 25 个长尾、问题型关键词，每个至少 5 个词。覆盖“how to”“what is”“why”“best way to”“how much”等提问变体，并为每个关键词标注可能的搜索意图和适合的内容类型（博客文章、落地页、FAQ 或对比页）。',
    usage: '适合发现用户真实会问的问题，尤其适合 FAQ、教程和精选摘要选题。先替换【种子关键词】，再按受众和业务相关性筛选。'
  },
  'creator-seo-03': {
    zh: '请把下面的关键词整理成主题集群。为每个集群提供：1 个支柱页标题、6 个支持文章标题，以及推荐的内链锚文本。关键词： 【粘贴关键词列表】。',
    usage: '适合把关键词清单转成内容架构。输入前先去重并统一关键词语言，输出后检查每个集群是否服务同一个搜索意图。'
  },
  'creator-seo-04': {
    zh: '请根据关键词【关键词】推断主导的 SERP 搜索意图。列出可能排名靠前的页面模式（内容形式、深度、角度、实体和常见章节），然后给出一份清单，说明怎样做出更好满足同一意图的页面。',
    usage: '适合写作前判断应该做教程、清单、对比还是产品页。最好同时提供当前排名页面的观察结果，让模型的推断有真实依据。'
  },
  'creator-seo-05': {
    zh: '请为【核心关键词】创建一份 SEO 内容简报。目标受众：【受众】；目标：【目标】。请包含：5 个工作标题、搜索意图、H1/H2/H3 大纲、各章节要点、应加入的案例、需要回应的异议、建议内链（使用通用占位符），以及 E-E-A-T 计划（在哪里加入经验、证据和引用）。',
    usage: '适合把策略交给作者或团队执行。先填写受众和目标，再根据业务事实补充案例、证据与引用来源。'
  },
  'creator-seo-06': {
    zh: '请撰写文章中关于【章节名称】的一节，目标关键词是【核心关键词】。限制：120–180 个词，达到八年级阅读难度，包含 1 个实用例子，避免废话，并以 2 条要点总结结尾。',
    usage: '适合逐段生成和审校长文，能减少一次性生成整篇文章带来的空泛表达。每次只处理一个章节，生成后人工确认事实和语气。'
  },
  'creator-seo-07': {
    zh: '请为一个以【核心关键词】为目标的页面，写出 10 个 Meta 标题（最多 58 个字符）和 10 个 Meta 描述（最多 155 个字符）。使用诚实的收益表达，避免标题党；自然时加入数字，并在速度、清单、模板、错误等角度之间做变化。',
    usage: '适合已有页面的点击率优化。输出后用实际 SERP 展示长度再检查一次，并确保标题与页面正文真实匹配。'
  },
  'creator-seo-08': {
    zh: '在不改变原意的前提下，针对【核心关键词】优化下面的内容。改善清晰度、标题、内链机会和语义覆盖，并标记：关键词堆砌风险、缺失章节以及适合补充案例的位置。内容：【粘贴草稿】。',
    usage: '适合刷新已经写好的页面，不适合让模型凭空重写整篇文章。保留原文事实，重点让模型指出缺口和可执行的修改点。'
  },
  'creator-seo-09': {
    zh: '我有以下 URL 和目标关键词：【粘贴 URL 列表 + 目标关键词】。请建立一份内链计划：哪个页面链接到哪个页面、建议使用什么自然锚文本，以及链接应出现在正文什么位置。优先连接搜索意图相近的页面，并避免重复锚文本。',
    usage: '适合主题集群完成后的内链规划。输入 URL 时同时写明页面主题和目标词，避免模型只按 URL 字符串猜测页面内容。'
  },
  'creator-seo-10': {
    zh: '请为关于【主题】的页面生成 JSON-LD Schema。页面类型：【Article/FAQ/HowTo/Product/LocalBusiness】。只包含页面可见内容能够支持的字段。返回有效的 JSON-LD，并附上一份清单，说明页面必须出现哪些内容才能支撑这些字段。',
    usage: '适合生成结构化数据初稿。发布前必须对照页面实际内容并使用 Google Rich Results Test 等工具验证，不能把模型输出直接上线。'
  },
  'creator-seo-11': {
    zh: '请审阅这篇文章，找出过时、重复或内容单薄的章节。建议哪些内容应删除、重写或合并，然后针对【核心关键词】提出一份更符合搜索意图的刷新大纲。文章：【粘贴文章】。',
    usage: '适合内容更新和减法优化。输入旧文章与目标关键词，优先处理事实过期、重复回答和无法满足搜索意图的段落。'
  },
  'creator-seo-12': {
    zh: '请分析下面的 Google Search Console 导出数据。找出排名在 8–20 位且曝光量较高的关键词。针对每个关键词，推荐最小的页面修改，以提高进入前 5 名的可能性（标题调整、增加章节、内链、Meta 重写或搜索意图对齐）。数据：【粘贴 GSC 导出】。',
    usage: '适合做低成本 SEO 迭代。输入真实 GSC 导出并保留曝光、点击、排名等字段，输出建议后一次只测试少量改动，便于判断效果。'
  }
};

window.CREATOR_DATA.prompts.forEach(item => {
  if (item.id.startsWith('creator-seo-')) {
    item.en = item.prompt;
    item.zh = CREATOR_SEO_LOCALES[item.id].zh;
    item.usage = CREATOR_SEO_LOCALES[item.id].usage;
  } else {
    item.zh = item.zh || item.prompt;
    item.en = item.en || '';
    item.usage = item.usage || item.desc;
  }
});
