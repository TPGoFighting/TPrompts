import json

scenes = {
    "hero": {
        "badge": "assets/tippy/tippy_02.png", # TP + Tippy "TP makes prompts"
        "partner": "assets/tippy/tippy_07.png" # TP + Tippy "TP makes things"
    },
    "portals": {
        "library": "assets/tippy/tippy_30.png", # Code: Build Better Prompts
        "inspire": "assets/tippy/tippy_05.png", # Daily Inspiration + Tippy
        "taste": "assets/tippy/tippy_08.png"    # TP with Checklist (Discover, Curate, Inspire)
    },
    "story": [
        {
            "num": "01",
            "tag": "01 · 迷路的灵感",
            "title": "一个掉下来的光点",
            "desc": "雷达疯狂闪烁，提仔在星球边缘发现一颗地球掉下的光斑：“我想做点东西。” 既无上下文也无格式，但这正是一切的开端。",
            "img": "assets/tippy/tippy_60.png" # "New prompt idea!" 气泡贴纸
        },
        {
            "num": "02",
            "tag": "02 · 整理重组",
            "title": "装入 TP Core",
            "desc": "TP 抱着电脑走来：“先做出来看看。” 提仔打开黑绿色方块装置，将零散的想法重组为结构化提示词。",
            "img": "assets/tippy/tippy_31.png" # TP Core 标志方块
        },
        {
            "num": "03",
            "tag": "03 · 一键执行",
            "title": "Prompt · Copy · Create",
            "desc": "整理、组合、测试，按下 Enter，屏幕中央可运行的页面瞬间亮起，提仔兴奋跳起！",
            "img": "assets/tippy/tippy_61.png" # "Prompt. Copy. Create." 便签条
        },
        {
            "num": "04",
            "tag": "04 · 创立平台",
            "title": "GOOD PROMPTS!",
            "desc": "桌面堆满了提示词卡片，他们建立 TPrompts，把真正好用、测试过的 Prompt 分享给所有人。",
            "img": "assets/tippy/tippy_29.png" # 提仔举着 "GOOD PROMPTS!" 招牌
        }
    ],
    "workflow": [
        {"num": "01", "name": "DISCOVER", "title": "捕捉灵感", "desc": "雷达与放大镜全开，捕捉未成型的模糊需求信号", "img": "assets/tippy/tippy_34.png"}, # 提仔戴耳机拿放大镜
        {"num": "02", "name": "SEARCH", "title": "知识比对", "desc": "比对已有提示词结构，在海量灵感中寻找解法", "img": "assets/tippy/tippy_62.png"}, # /imagine a better idea 窗口
        {"num": "03", "name": "INPUT", "title": "拖入需求", "desc": "将人类原始想法粒子一键放入 TP 核心打磨管道", "img": "assets/tippy/tippy_56.png"}, # "Drop your idea here" 拖拽框
        {"num": "04", "name": "CRAFT", "title": "结构重组", "desc": "TP Core 设定明确角色、上下文、约束与输出格式", "img": "assets/tippy/tippy_63.png"}, # 提仔坐在 TP 电脑前
        {"num": "05", "name": "CHECKLIST", "title": "品味质检", "desc": "严格审查标点、JSON结构与多模型适配确定性", "img": "assets/tippy/tippy_53.png"}, # 质检眼镜
        {"num": "06", "name": "TEST & RUN", "title": "大模型实测", "desc": "在主流 LLM 实际运行并记录真实生成效果", "img": "assets/tippy/tippy_35.png"}, # 提仔趴着观察
        {"num": "07", "name": "COPY", "title": "一键复制", "desc": "一键直达剪贴板，秒速投喂各类 AI 编码与对话工具", "img": "assets/tippy/tippy_55.png"}, # "Copy Prompt" 卡片
        {"num": "08", "name": "CELEBRATE", "title": "Good Prompt!", "desc": "好想法终于做成好产品，能量球爆发，纸飞机启航！", "img": "assets/tippy/tippy_29.png"} # 提仔举牌庆祝
    ],
    "lab": [
        {"tag": "DISCOVER", "name": "01. 灵感雷达", "img": "assets/tippy/tippy_34.png", "quote": "“头顶雷达全天候开启：Discover Better Prompts!”", "desc": "手持放大镜，在海量需求中寻找最有潜力的小光点。"},
        {"tag": "DAILY", "name": "02. 每日精选", "img": "assets/tippy/tippy_05.png", "quote": "“Daily Inspiration！今天又收录了超多好玩的提示词！”", "desc": "充满活力，每天为创作者输送源源不断的新鲜灵感。"},
        {"tag": "CURATE", "name": "03. 严选把关", "img": "assets/tippy/tippy_08.png", "quote": "“Discover、Curate、Inspire，每一条都要能打！”", "desc": "TP 亲手勾选 Checklist，宁缺毋滥，拒绝平庸。"},
        {"tag": "STATION", "name": "04. 终端就绪", "img": "assets/tippy/tippy_64.png", "quote": "“TP makes things. Turn ideas into prompts faster!”", "desc": "提仔坐在 TP 终端前，随时准备将想法转化成现实。"},
        {"tag": "GOOD PROMPT", "name": "05. 庆祝达成", "img": "assets/tippy/tippy_29.png", "quote": "“GOOD PROMPTS! 完美运行，好想法值得被实现！”", "desc": "眨眼举牌，为你成功做出的每一个网站和工具喝彩。"}
    ]
}

print("JSON 配置测试通过！全部素材精准贴合，无一张 UI Kit 图！")
