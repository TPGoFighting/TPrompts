/* curated-data.js - 品味页策展数据（手动维护，编辑感来源）
 * 结构: window.CURATED_DATA.sections[]
 * 每条 item: { src: 'library'|'inspire', id: <条目id>, note: <策展语> }
 * library → #/p/<id>（查 PROMPTS_DATA），inspire → #/i/<id>（查 INSPIRE_DATA）
 */
window.CURATED_DATA = {
  updated: '2026-08-19',
  sections: [
    {
      name: '本周精选',
      tag: 'EDITOR PICK',
      note: '跨库 + 灵感，最值得先看的 4 条。',
      items: [
        { src: 'library', id: 'ai-workflow', note: '现代数字化产品官方的视觉锚点，动态光影排版教科书。' },
        { src: 'library', id: 'digital-director', note: '创意机构作品集的首选，高级感不靠花哨靠克制。' },
        { src: 'inspire', id: 'cmjwphuqd0001i3043hx6ewgf', note: '一句话讲清长文章，学生党与研究者的救星。' },
        { src: 'inspire', id: 'cmj1zb0y3000evl0rcqduac4u', note: '经典中的经典：翻译 + 润色 + 文学化，一鱼三吃。' }
      ]
    },
    {
      name: '写作与表达',
      tag: 'WORDS',
      note: '让文字有骨头也有肉。',
      items: [
        { src: 'inspire', id: 'cmj78iw840004zc0swraq0obl', note: '不满足于改写，带研究深度的文章增强术。' },
        { src: 'inspire', id: 'cmlu85d1v0004l804qy5fnq3f', note: 'SEO 博客建筑师：内容、结构、外链一肩挑。' },
        { src: 'inspire', id: 'cmk60pvav0001kx04xjcz6mg8', note: 'APA 第 7 版文献综述助手，毕业论文好搭子。' },
        { src: 'inspire', id: 'cmjh18y7e000bl904cpwc3lna', note: '职场邮件专业人士，把「已读不回」变成「收到谢谢」。' }
      ]
    },
    {
      name: '代码与效率',
      tag: 'CODE',
      note: '从搬砖到撬动杠杆。',
      items: [
        { src: 'inspire', id: 'cmjcylib30007xp0skiid83dk', note: '任意语言互译的代码翻译官，迁移项目不重写。' },
        { src: 'inspire', id: 'cmkc6yvpy0007jr044u5hm1t9', note: 'RPA 项目代码审查，自动化脚本的质检员。' },
        { src: 'library', id: 'rocket-cta', note: '暗黑系界面 CTA 组件，转化按钮的满分示范。' },
        { src: 'inspire', id: 'cmj1zb1jl00bqvl0rzhc15fdq', note: 'ASCII 艺术家，把「猫」画成代码块的浪漫。' }
      ]
    },
    {
      name: '图像与创意',
      tag: 'VISUAL',
      note: '视觉脑洞收集册。',
      items: [
        { src: 'inspire', id: 'cmqdpf4240001jv04m93hle15', note: '伊斯坦布尔街景的密集点绘，细节控狂喜。' },
        { src: 'inspire', id: 'cmjits8la000kl1042cjz4ism', note: '末日恐怖图像模拟器，越怕越想看。' },
        { src: 'library', id: 'daisy-wild', note: 'Bento 便当盒布局的金融电商范本，结构即设计。' },
        { src: 'library', id: 'place-saver', note: '移动端 App 界面模拟，产品稿快速出街。' }
      ]
    },
    {
      name: '求职与成长',
      tag: 'CAREER',
      note: '写给正在升级的你。',
      items: [
        { src: 'inspire', id: 'cmlpgu1c80001l504gb6j4f5p', note: 'ATS 简历扫描模拟器，先过机器这一关。' },
        { src: 'inspire', id: 'cmlzhdjsy0004l2041czx0u3o', note: '面试前情报卷宗，让准备变成降维打击。' },
        { src: 'inspire', id: 'cmjfd0fzq0001i5048f3fvaf4', note: '职业路径顾问，帮你把选择想清楚再跳。' }
      ]
    }
  ]
};
