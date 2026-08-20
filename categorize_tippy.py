import json
from pathlib import Path

# 我们为关键形象设定清晰的语义映射，并在交互舞台中调用
tippy_scenes = {
    "hero_radar": "assets/tippy/tippy_02.png",       # 提仔抱着 TP Core 站立，雷达探索
    "hero_float": "assets/tippy/tippy_11.png",       # 提仔飞越星空寻找信号
    "tp_partner": "assets/tippy/tippy_12.png",       # 提仔与 TP 一起写代码
    "card_library": "assets/tippy/tippy_03.png",     # 敲代码/组件
    "card_inspire": "assets/tippy/tippy_07.png",     # 穿梭灵感星球
    "card_taste": "assets/tippy/tippy_10.png",       # 戴眼镜戴帽子严选
    
    # 工作流 7 大角色态
    "wf_discover": {"img": "assets/tippy/tippy_06.png", "title": "01. DISCOVER 灵感雷达", "desc": "Prompt Radar 捕捉微弱未成型的模糊想法与需求信号", "quote": "“好强的灵感信号！这是什么？让我试试！”"},
    "wf_search": {"img": "assets/tippy/tippy_17.png", "title": "02. SEARCH 知识库检索", "desc": "钻进 Library 比对前人经验与已有结构，拒绝重复造轮子", "quote": "“有没有人已经写过类似的 Prompt？先查一查。”"},
    "wf_craft": {"img": "assets/tippy/tippy_08.png", "title": "03. CRAFT 结构重组", "desc": "装入 TP Core 整理出 Goal、Context、Role、Constraint、Output 5维框架", "quote": "“把模糊的想法整理成清晰、好用的 Prompt。”"},
    "wf_checklist": {"img": "assets/tippy/tippy_18.png", "title": "04. CHECKLIST 规范质检", "desc": "目标明确？标点半角？无机翻腔？Ready to generate ✓", "quote": "“等等，我觉得还能再改一下，细节决定成败。”"},
    "wf_generate": {"img": "assets/tippy/tippy_09.png", "title": "05. GENERATE 投喂生成", "desc": "认真紧盯屏幕等待 AI 生成结果，检验代码执行与视觉呈现", "quote": "“Preparing your prompt… 见证奇迹的时刻！”"},
    "wf_learn": {"img": "assets/tippy/tippy_19.png", "title": "06. LEARN 深度复盘", "desc": "戴上学士帽研究模型特性，吸收最新 Prompt Engineering 方法", "quote": "“为什么这个效果不够好？原来是因为少了约束条件。”"},
    "wf_share": {"img": "assets/tippy/tippy_13.png", "title": "07. SHARE 纸飞机传播", "desc": "坐上纸飞机，将经过实测验证的极佳 Prompt 发布至社区共享", "quote": "“Good ideas deserve good prompts! 分享给所有人！”"},
    "wf_celebrate": {"img": "assets/tippy/tippy_20.png", "title": "08. GOOD PROMPT!", "desc": "每一个想法变成可运行现实的瞬间，能量球闪耀爆发", "quote": "“GOOD PROMPT! 我们再做一个！”"},

    # 故事连环画 4 幕
    "story_chapters": [
        {"act": "ACT 01", "img": "assets/tippy/tippy_05.png", "title": "一个奇怪的信号", "text": "雷达闪烁，提仔在星球边缘发现一颗地球掉下的光点，里面只有一句话：“我想做点东西。” 既无上下文也无格式，但这正是一切的开端。"},
        {"act": "ACT 02", "img": "assets/tippy/tippy_12.png", "title": "TP 抱着电脑走来", "text": "黑色T恤、乱糟糟头发的 TP 出现了：“做网站、做产品，或者一个 AI 工具，先做出来看看。” 提仔啪的一声打开 TP Core：“好，我们从 Prompt 开始。”"},
        {"act": "ACT 03", "img": "assets/tippy/tippy_04.png", "title": "屏幕亮起的瞬间", "text": "重新排列 5 维要素，按下 Enter，一个真正可运行的页面瞬间亮起！提仔跳起来大喊：“GOOD PROMPT!”，TP 笑着说：“再做一个。”"},
        {"act": "ACT 04", "img": "assets/tippy/tippy_01.png", "title": "TP makes Prompts.", "text": "卡片堆满了房间，他们创立了 TPrompts：“世界上从来不缺想法，真正困难的，是把脑子里的那点灵感，变成真正存在的东西。”"}
    ],

    # 提仔互动百态（点击/悬浮可切换提仔状态）
    "moods": [
        {"name": "探索模式", "tag": "DISCOVER", "img": "assets/tippy/tippy_24.png", "quote": "“这是什么？让我试试！”", "desc": "头顶雷达高频运转，寻找新的 AI 技巧与提示词灵感。"},
        {"name": "打磨模式", "tag": "CRAFTING", "img": "assets/tippy/tippy_25.png", "quote": "“Crafting better prompts…”", "desc": "坐在 TP Core 前，专注编写结构化提示词与清晰约束。"},
        {"name": "严苛质检", "tag": "AUDIT", "img": "assets/tippy/tippy_27.png", "quote": "“等等，这里的变量还能更精准一点。”", "desc": "戴上放大镜，逐行检查 JSON 引号与上下文完整性。"},
        {"name": "兴奋交付", "tag": "SUCCESS", "img": "assets/tippy/tippy_28.png", "quote": "“GOOD PROMPT! 完美生成！”", "desc": "看到代码成功运行或画面惊艳生成时的专属庆祝姿态。"},
        {"name": "学术研讨", "tag": "RESEARCH", "img": "assets/tippy/tippy_30.png", "quote": "“不断学习新的模型架构与思维链机制。”", "desc": "佩戴学士帽，沉浸于深入的 Prompt Engineering 研究。"}
    ]
}

Path('tippy_scenes.json').write_text(json.dumps(tippy_scenes, ensure_ascii=False, indent=2), encoding='utf-8')
print("提仔场景语义字典构建成功！")
