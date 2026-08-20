# Cinematic Ink & Color Illustration Generator — Gary Frank Style

**Description:** Generates hyper-detailed cinematic illustrations with bold black ink linework over rich, fully-rendered digital color. Inspired by prestige editorial illustration technique, dramatic golden-hour lighting, cool blue-violet shadows, obsessive material detail. User describes a scene, prompt produces the illustration.

**Type:** IMAGE
**Author:** eyupyusufa
**Created:** 2026-01-31T14:22:52.132Z
**Votes:** 2
**Views:** 0

**Tags:** Art, creative, design

**Category:** Image Generation

## Prompt Content

```
{
  "type": "illustration",
  "goal": "Create a single wide cinematic illustration of a lone cowboy sitting on a wooden chair in front of an Old West saloon at dusk. Rendered with meticulous hand-inked linework over rich digitally-painted color. The technique combines bold black ink contour drawing with deep, layered, fully-rendered color work — the kind of dramatic realism found in high-end editorial illustration and graphic novel art.",

  "work_surface": {
    "type": "Single illustration, landscape orientation",
    "aspect_ratio": "16:9 widescreen cinematic",
    "medium": "Black ink line drawing with full digital color rendering — the line art has the confident hand-drawn quality of traditional inking, the color has the depth of oil-painting-influenced digital work"
  },

  "rendering_technique": {
    "line_work": {
      "tool_feel": "Traditional dip pen and brush ink on paper — confident, deliberate strokes with natural line weight variation. Not vector-clean, not scratchy-loose. The sweet spot of controlled precision with organic warmth.",
      "outer_contours": "Bold black ink outlines (3-4pt equivalent) defining every figure and major object. These contour lines give the image its graphic punch — silhouettes read clearly even at thumbnail size.",
      "interior_detail": "Finer ink lines (1-2pt) for facial features, leather stitching, wood grain, fabric folds, wrinkles, hair strands. This interior detail is what separates high-end illustration from simple cartoon — obsessive attention to surface texture and form.",
      "spotted_blacks": "Large areas of solid black ink used strategically — deep shadows under the porch overhang, inside the hat brim, the darkest folds of the vest. These black shapes create dramatic graphic contrast and anchor the composition.",
      "hatching": "Minimal. Where it appears (underside of porch ceiling, deep fabric creases), it is tight, controlled, parallel lines. Never loose or decorative. Shadows are primarily defined through color, not line hatching."
    },

    "color_work": {
      "approach": "Fully rendered, multi-layered digital painting OVER the ink lines. Not flat fills. Not cel-shading. Every surface has continuous tonal gradation — as if each area was painted with the care of an oil study.",
      "skin": "Multi-tonal. Warm tan base with cooler shadows under jawline and eye sockets, subtle red warmth on nose and sun-exposed cheekbones, precise highlights on brow ridge and cheekbone. Skin looks weathered and alive.",
      "materials": "Each material rendered distinctly. Leather has a slight waxy sheen on smooth areas and matte roughness on worn patches. Denim shows a faint diagonal weave. Metal (buckle, gun, spurs) has sharp specular highlights. Wood shows grain pattern, dust accumulation, age patina. Cotton shirt has soft diffused light transmission.",
      "shadow_color": "CRITICAL: Shadows are NOT just darker versions of the base color. They shift toward cool blue-violet (#2d2d44, #3a3555). A brown leather vest's shadow is not dark brown — it is dark brown with a blue-purple undertone. This color-shifting in shadows creates atmospheric depth and cinematic richness.",
      "light_color": "Where direct sunset light hits, surfaces gain a warm amber-golden overlay (#FFD280, #E8A848). This is additive — the golden light sits on top of the local color, making sun-facing surfaces glow."
    },

    "detail_density": "Extremely high. The viewer should be able to zoom in and discover new details: individual nail heads in the porch planks, a specific pattern of cracks in the leather, the particular way dust has settled in the creases of the hat, a tiny nick in the whiskey glass rim, the wear pattern on the boot sole. This density of observed detail is what creates the feeling of a real place inhabited by a real person.",

    "DO_NOT": [
      "Do NOT use flat color fills — every surface needs tonal gradation",
      "Do NOT use cel-shading or hard-edged color blocks",
      "Do NOT use cartoon proportions or exaggeration",
      "Do NOT use anime or manga rendering conventions",
      "Do NOT use soft airbrush blending that erases the ink lines",
      "Do NOT use watercolor transparency or bleeding edges",
      "Do NOT use photorealistic rendering — the ink linework must remain visible and central",
      "Do NOT use sketchy, rough, or unfinished-looking line quality",
      "Do NOT use pastel or desaturated washed-out colors — the palette is rich and deep"
    ]
  },

  "color_palette": {
    "sky": {
      "upper": "#1a1a3e deep indigo — night approaching from above",
      "middle": "#6B3A5E dusty purple-mauve transition",
      "lower_horizon": "#E8A040 to #FF7B3A blazing amber-to-orange sunset glow"
    },
    "saloon_wood": {
      "lit": "#A0784C warm aged timber catching sunset",
      "shadow": "#5C3A20 dark brown under porch overhang",
      "weathered": "#8B7355 grey-brown bleached planks"
    },
    "ground": {
      "lit": "#D4B896 warm sandy dust in golden light",
      "shadow": "#7A6550 cool brown where light doesn't reach"
    },
    "cowboy": {
      "hat": "#6B5B4F dark dusty brown, lighter dusty edges #8B7B6F",
      "skin": "#B8845A sun-weathered tan, #8B6B42 in deep creases",
      "shirt": "#C8B8A0 faded off-white, yellowed with age and dust",
      "vest": "#3C2A1A dark worn leather, near-black in deepest folds",
      "jeans": "#4A5568 faded dark blue-grey denim, #7B8898 dusty highlights at knees",
      "boots": "#5C3A20 dark leather, #8B6B42 scuff marks",
      "buckle": "#D4A574 antique brass catching one sharp sunset point",
      "gun_metal": "#4A4A4A dark steel, single sharp highlight line"
    },
    "light_sources": {
      "sunset": "#FFD280 to #FF8C42 — dominant golden-hour warmth from left",
      "saloon_interior": "#FFA040 amber oil-lamp glow from behind swinging doors"
    }
  },

  "lighting": {
    "concept": "Golden hour — the sun sits just above the horizon to the left. Nearly horizontal rays of warm amber light rake across the scene. Every raised surface catches fire. Every shadow stretches long. The air itself has visible warmth. This is the most dramatic natural lighting condition — treated here with the gravity of a Renaissance chiaroscuro painting translated into ink and color.",

    "key_light": {
      "source": "Setting sun, low on horizon, from the left",
      "color": "#FFD280 warm amber-gold",
      "direction": "Nearly horizontal, raking from left to right",
      "effect_on_cowboy": "Right side of face and body warmly lit — every weathered wrinkle, every thread of stubble visible in the golden light. Left side falls into cool blue-violet shadow. Creates a dramatic half-lit, half-shadow portrait.",
      "effect_on_environment": "Long shadows stretching to the right across dusty ground. Sun-facing wood surfaces glow amber. Dust particles in the air catch light like floating golden sparks."
    },

    "fill_light": {
      "source": "Ambient sky light from the dusk sky above",
      "color": "#6B7B9B cool blue-purple",
      "effect": "Fills shadow areas with cool tone. Prevents pure black — you see detail in shadows, but it's all tinted blue-violet. This warm/cool contrast between key and fill is what creates the richness."
    },

    "accent_light": {
      "source": "Oil lamp glow from inside the saloon, spilling through swinging doors and windows",
      "color": "#FFA040 warm amber",
      "effect": "Rim light on the back of cowboy's hat and shoulders. Separates him from background. Also casts geometric window-light rectangles on the porch floor."
    },

    "shadow_treatment": {
      "coverage": "45-55% of image area in shadow",
      "cast_shadows": "Cowboy's long shadow stretches right across the street. Porch overhang throws a hard horizontal shadow across the saloon facade. Chair legs cast thin shadow lines.",
      "face_shadows": "Half-face lighting. Right side warm and detailed. Left side cool shadow — eye socket deep, cheekbone creates a sharp shadow edge, stubble dots visible in the light-to-shadow transition.",
      "atmospheric": "Visible dust motes floating in the sunset light beams. Golden in the light, invisible in the shadow. Creates a sense of thick warm air."
    }
  },

  "scene": {
    "composition": "Wide cinematic frame. The cowboy sits slightly left of center — the golden ratio point. The saloon facade fills the right two-thirds of the background. Open dusty street stretches left toward the horizon and setting sun. This asymmetry — solid structure on the right, open emptiness on the left — reinforces the emotional isolation. A single figure at the boundary between civilization (the saloon) and wilderness (the open desert).",

    "the_cowboy": {
      "position": "Seated on a rough wooden chair on the saloon's front porch",
      "pose": "Leaned back, weight on the chair's hind legs. Left boot flat on porch floor. Right ankle crossed over left knee — easy, unhurried. Right hand loosely holds a short whiskey glass resting on his right knee. The glass is half-empty. Left hand rests on the chair arm or thigh. Head tilted very slightly down, but eyes aimed forward at the horizon — the thousand-yard stare of accumulated experience. Shoulders broad but not tensed. The body language says: I am at rest, but I am never unaware.",
      "face": "This must be a SPECIFIC face, not a generic cowboy. Middle-aged, 40s-50s. Square jaw with defined jawline visible through the stubble. Deep-set eyes under a heavy brow ridge — intense, observant, slightly narrowed against the sunset glare. Three-day stubble, dark with threads of grey at the chin. Sun-weathered skin — deep crow's feet radiating from eye corners, horizontal forehead creases, nasolabial folds that have become permanent grooves. A healed scar across the left cheekbone — thin, white, old. Nose slightly crooked from a long-ago break, a bump on the bridge. Thin lips set in a neutral line — not a frown, not a smile. This face has lived decades of hard outdoor life and it shows in every crease.",
      "clothing_detail": "Wide-brimmed cowboy hat, dark dusty brown, battered — dents in the crown, brim slightly curled and frayed at edges, a sweat stain ring visible on the band. Faded off-white cotton shirt, sleeves rolled to mid-forearm exposing sun-tanned forearms with visible veins and tendons. Dark leather vest over the shirt, well-worn — surface cracked in places, stitching visible at seams, a few spots where the leather has gone matte from years of use. Faded dark blue-grey jeans, lighter at the knees and thighs from wear, dusty. Wide leather belt with an antique brass buckle — the buckle catches one sharp point of sunset light. Holstered revolver on the right hip — dark aged leather holster, the wooden pistol grip visible, a glint of steel. Dark brown leather boots, scuffed and scored, heels slightly worn down, spur straps buckled at the ankle."
    },

    "the_saloon": {
      "architecture": "Classic Old West frontier saloon. Two-story wooden building with a false front (the facade extends above the actual roofline to make it look grander). Built from rough-sawn timber planks, some warped with age. A painted sign above the entrance: 'SALOON' in faded gold lettering on a dark red background — the paint is cracking, peeling at the corners, one letter slightly more faded than the others.",
      "entrance": "Swinging batwing doors at the center, slightly ajar. Through the gap, warm amber light spills outward — the glow of oil lamps and activity inside. You don't see the interior clearly, just the suggestion of warmth and noise contained behind those doors.",
      "windows": "Two windows flanking the entrance. Dirty glass with a warm glow from inside. One pane has a crack running diagonally across it.",
      "porch": "Wooden porch running the width of the building. Planks are weathered — grey where the sun has bleached them, darker brown where foot traffic has worn them smooth. Some boards slightly warped, a few nail heads protruding. Rough-hewn timber posts support the porch overhang.",
      "details": "A hitching post in front with a horse's lead rope tied to it — the rope is taut, suggesting an animal just out of frame. A wooden water trough near the hitching post, its surface greenish. A barrel beside the door. Everything covered in a thin layer of desert dust."
    },
  "constraints": {
    "must_include": [
      "Bold black ink contour lines visible throughout — this is line art with color, not a painting",
      "Rich multi-layered color with tonal gradation on every surface",
      "Cool blue-violet shift in all shadow areas (not just darkened base color)",
      "Warm amber-golden light where sunset hits directly",
      "Extremely detailed face with specific individual features — scars, wrinkles, bone structure",
      "Material differentiation — leather, wood, metal, fabric, skin all look different",
      "Atmospheric dust particles in sunset light beams",
      "Long dramatic cast shadows on dusty ground",
      "Warm glow from saloon interior as rim/accent light",
      "Vast open space on left contrasting with solid saloon structure on right"
    ],
    "must_avoid": [
      "Cartoon or caricature style of any kind",
      "Anime or manga rendering conventions",
      "Flat color fills without gradation",
      "Soft airbrush that hides the ink linework",
      "Photographic realism — the ink drawing must be visible",
      "Generic featureless face — this must be a specific person",
      "Clean or new-looking anything — everything shows age and wear",
      "Muddy dark coloring — the sunset provides rich warm light",
      "Stiff posed figure — natural relaxed human body language",
      "Watercolor transparency or bleeding-edge technique"
    ]
  },

  "negative_prompt": "anime, manga, chibi, cartoon, caricature, flat colors, cel-shading, minimalist, photorealistic photograph, 3D CGI render, soft airbrush, watercolor, pastel colors, sketchy rough lines, generic face, clean new clothing, bright neon, blurry, low resolution, stiff pose, modern elements, vector art, simple illustration, children's book style, pop art, abstract"
}
```

**Source:** https://prompts.chat/prompts/cml2eizmu0001ks04wda154zs_cinematic-ink-color-illustration-generator-gary-frank-style

## 中文翻译

### 标题
电影墨水和彩色插图生成器 — 加里·弗兰克风格

### 提示词内容

```
{
  “类型”：“插图”，
  "目标": "创作一幅宽幅电影插图，描绘黄昏时分，一个孤独的牛仔坐在老西部酒吧前的木椅上。通过细致的手绘线条和丰富的数字绘画色彩进行渲染。该技术将大胆的黑色墨水轮廓图与深沉、分层、完全渲染的色彩作品相结合 - 高端编辑插图和图画小说艺术中的那种戏剧性现实主义。",

  “工作表面”：{
    "type": "单幅插图，横向",
    "aspect_ratio": "16:9 宽屏电影",
    "medium": "黑色水墨线条画，全数字色彩渲染——线条艺术具有传统水墨的自信手绘品质，色彩具有受油画影响的数字作品的深度"
  },

  “渲染技术”：{
    “线路工作”：{
      "tool_feel": "纸上的传统浸笔和毛笔墨水 — 自信、深思熟虑的笔触，具有自然的线条粗细变化。不是矢量干净，不是潦草的松散。控制精度与有机温暖的最佳点。",
      "outer_contours": "粗体黑色墨水轮廓（相当于 3-4 磅）定义了每个图形和主要对象。这些轮廓线赋予图像图形冲击力 - 即使在缩略图大小下，轮廓也清晰可见。",
      "interior_detail": "更精细的墨线（1-2pt）用于面部特征、皮革缝合、木纹、织物褶皱、皱纹、发丝。这种内部细节是将高端插图与简单卡通区分开来的——对表面纹理和形式的过分关注。",
      "spotted_blacks": "战略性地使用了大面积的纯黑色墨水 — 门廊悬垂下的深阴影、帽檐内、背心最暗的褶皱。这些黑色形状创造了戏剧性的图形对比并固定了构图。",
      "hatching": "最小。它出现的地方（门廊天花板的底面，深织物折痕），是紧密的、受控的、平行的线条。决不松散或装饰性。阴影主要通过颜色定义，而不是线条阴影。"
    },

    “颜色工作”：{
      "approach": "在墨水线上进行完全渲染的多层数字绘画。不是平面填充。不是卡通着色。每个表面都有连续的色调渐变 - 就好像每个区域都是经过油画研究的精心绘制的。",
      "skin": "多色调。温暖的棕褐色底色，下巴和眼窝下有较冷的阴影，鼻子和暴露在阳光下的颧骨上有微妙的红色温暖，眉脊和颧骨上有精确的高光。皮肤看起来饱经风霜，充满活力。",
      "materials": "每种材料都渲染得清晰。皮革在光滑区域有轻微的蜡质光泽，在磨损的补丁上有哑光粗糙度。牛仔布显示出微弱的斜纹编织。金属（带扣、枪、马刺）有锐利的镜面高光。木材显示纹理图案、灰尘堆积、老化铜绿。棉衬衫具有柔和的漫射光传输。",
      "shadow_color": "关键：阴影不仅仅是基色的较暗版本。它们转向冷蓝紫色（#2d2d44、#3a3555）。棕色皮背心的阴影不是深棕色 - 它是带有蓝紫色底色的深棕色。阴影中的这种颜色变化创造了大气深度和电影丰富度。",
      “light_color”：“在夕阳直射的地方，表面会获得温暖的琥珀金色覆盖层（#FFD280，#E8A848）。这是附加的 - 金色的光位于局部颜色的顶部，使面向太阳的表面发光。”
    },

    "detail_密度": "极高。观看者应该能够放大并发现新的细节：门廊木板上的单个钉头、皮革上特定的裂纹图案、灰尘在帽子折痕中沉降的特殊方式、威士忌酒杯边缘上的小缺口、靴底上的磨损图案。 这种观察细节的密度创造了真人居住在真实地方的感觉。”,

    “不要”：[
      “不要使用平面颜色填充 - 每个表面都需要色调渐变”，
      “请勿使用卡通渲染或硬边色块”，
      “请勿使用卡通比例或夸张”，
      “请勿使用动漫或漫画渲染约定”，
      “请勿使用软喷枪混合来擦除墨线”，
      “请勿使用水彩透明或出血边缘”，
      “请勿使用真实感渲染 - 墨水线条必须保持可见且居中”，
      “请勿使用粗略、粗糙或未完成的线条质量”，
      “不要使用柔和的或不饱和的褪色颜色——调色板丰富而深沉”
    ]
  },

  “颜色调色板”：{
    “天空”：{
      "upper": "#1a1a3e 深靛蓝 — 夜幕从上方降临",
      "middle": "#6B3A5E 尘土飞扬的紫紫过渡",
      "lower_horizon": "#E8A040 到 #FF7B3A 闪耀的琥珀色到橙色的夕阳光芒"
    },
    “沙龙木”：{
      "lit": "#A0784C 温暖的老化木材捕捉日落",
      "shadow": "#5C3A20 门廊悬挑下的深棕色",
      "weather": "#8B7355 灰棕色漂白木板"
    },
    “地面”：{
      "lit": "#D4B896 金色光芒中温暖的沙尘",
      "shadow": "#7A6550 光线照射不到的冷棕色"
    },
    “牛仔”：{
      "hat": "#6B5B4F 深灰棕色，浅灰边缘 #8B7B6F",
      "skin": "#B8845A 晒黑，#8B6B42 深折痕",
      "shirt": "#C8B8A0 褪色为灰白色，因年龄和灰尘而泛黄",
      "vest": "#3C2A1A 深色磨损皮革，最深的褶皱接近黑色",
      "jeans": "#4A5568 褪色深蓝灰色牛仔布，#7B8898 膝盖处有灰尘的亮点",
      "boots": "#5C3A20 深色皮革，#8B6B42 磨损痕迹",
      "buckle": "#D4A574 古董黄铜捕捉一个尖锐的日落点",
      "gun_metal": "#4A4A4A 暗钢，单条锐利高光线"
    },
    “光源”：{
      "sunset": "#FFD280 到 #FF8C42 — 从左到右的黄金时段温暖",
      "saloon_interior": "#FFA040 琥珀色油灯从旋转门后面发出光芒"
    }
  },

  “照明”：{
    “concept”：“黄金时刻——太阳位于地平线上方左侧。几乎水平的温暖琥珀色光线掠过整个场景。每个凸起的表面都会着火。每一个影子都拉得很长。空气本身就有明显的温暖。这是最引人注目的自然光条件——这里用文艺复兴时期的明暗对比绘画的重力转化为墨水和颜色来处理。”,

    “键灯”：{
      "source": "夕阳，低在地平线上，从左边看",
      "color": "#FFD280 暖琥珀金",
      "direction": "接近水平，从左向右倾斜",
      "effect_on_cowboy": "脸部和身体的右侧被温暖地照亮——每一条风化的皱纹、每一根胡茬在金色的光芒下都清晰可见。左侧陷入凉爽的蓝紫色阴影中。创建戏剧性的半亮半影肖像。",
      "effect_on_environment": "长长的阴影在尘土飞扬的地面上向右延伸。面向阳光的木质表面发出琥珀色的光。空气中的灰尘颗粒会发光，就像漂浮的金色火花一样。”
    },

    “填充光”：{
      "source": "来自上方黄昏天空的环境天空光",
      "color": "#6B7B9B 冷蓝紫色",
      "effect": "用冷色调填充阴影区域。防止纯黑色 - 您可以看到阴影中的细节，但它都是蓝紫色的。主调和填充之间的这种暖/冷对比创造了丰富度。”
    },

    “口音灯”：{
      "source": "油灯从酒吧内发出光芒，从旋转的门窗中溢出",
      "color": "#FFA040 暖琥珀色",
      "effect": "牛仔帽背面和肩膀上有边缘光。将他与背景分开。还在门廊地板上投射几何窗光矩形。”
    },

    “阴影治疗”：{
      "coverage": "45-55% 的图像区域处于阴影中",
      "cast_shadows": "牛仔长长的影子一直延伸到街对面。悬垂的门廊在沙龙正面投射出坚硬的水平阴影。椅子腿投射出细细的阴影线。",
      "face_shadows": "半脸照明。右侧温暖而细致。左侧冷色阴影 - 眼窝深，颧骨形成锐利的阴影边缘，在光影过渡中可见胡茬点。",
      “atmospheric”：“日落光束中漂浮着可见的尘埃微粒。光里金黄，阴影里看不见。 营造出一种浓浓的温暖空气感。”
    }
  },

  “场景”：{
    “构图”：“宽阔的电影框架。牛仔位于中心稍偏左的位置——黄金比例点。沙龙正面占据了背景右侧三分之二的面积。开阔的尘土飞扬的街道向左延伸到地平线和夕阳。这种不对称——右侧的坚实结构，左侧的开放空虚——强化了情感上的孤立。文明（酒吧）和荒野（开阔的沙漠）之间边界上的一个人物。",

    “牛仔”：{
      "position": "坐在酒吧前廊的一张粗糙的木椅上",
      “pose”：“向后倾斜，重量落在椅子的后腿上。左靴子平放在门廊地板上。右脚踝交叉在左膝上——轻松、从容。右手松松地握着一个短威士忌酒杯，放在右膝上。杯子是半空的。左手放在椅子扶手或大腿上。头微微低垂，但眼睛却注视着地平线——积累经验的千米凝视。肩膀宽阔但不紧张。肢体语言说：我在休息，但我从来没有意识到。",
      "face": "这必须是一张特定的脸，而不是普通的牛仔。中年，40-50岁。方下巴，下巴轮廓分明，透过胡茬可见。浓重的眉脊下有一双深陷的眼睛——目光敏锐，善于观察，在夕阳的余晖下微微眯起。三天的胡茬，颜色深，下巴处有灰色的线。饱受阳光照射的皮肤——从眼角辐射出来的深深鱼尾纹、水平额头皱纹、已经成为永久性凹槽的法令纹。左颧骨上有一道已经愈合的伤疤——又薄又白又老。鼻子因很久以前的断裂而略微弯曲，鼻梁上有一个凹凸。薄唇呈中性线——不是皱眉，不是微笑。这张脸经历了数十年的艰苦户外生活，每一个折痕都体现了这一点。”,
      "clothing_detail": "宽边牛仔帽，深灰褐色，破旧——帽冠有凹痕，帽檐略微卷曲，边缘磨损，帽带上可见一圈汗渍。褪色的灰白色棉质衬衫，袖子卷至前臂中部，露出晒黑的前臂，血管和肌腱清晰可见。衬衫外面套着深色皮革背心，已经很破旧了——表面有些地方开裂，接缝处的缝线清晰可见，一些地方的皮革因多年使用而变得无光泽。褪色的深蓝灰色牛仔裤，膝盖和大腿处因磨损而变浅，布满灰尘。宽皮带配有古董黄铜带扣——带扣捕捉夕阳的一个锐角。右臀上有一把左轮手枪——深色做旧的皮革枪套，木制的手枪握把清晰可见，闪烁着钢铁的光芒。深棕色皮靴，有磨损和划痕，鞋跟略有磨损，马刺带在脚踝处扣住。”
    },

    “the_saloon”：{
      “architecture”：“经典的老西部边境沙龙。两层木结构建筑，有假正面（正面延伸到实际屋顶线上方，使其看起来更宏伟）。由粗锯木板制成，有些随着时间的推移而变形。入口上方有一个彩绘标志：深红色背景上褪色的金色字体“SALOON”——油漆开裂，角落剥落，其中一个字母比其他字母稍微褪色。”,
      "entrance": "中心有摆动的蝙蝠翼门，微开着。通过缝隙，温暖的琥珀色光线向外溢出——油灯的光芒和里面的活动。你看不清内部，只能看到那些门后面所包含的温暖和噪音。”,
      "windows": "入口两侧有两扇窗户。肮脏的玻璃，里面发出温暖的光芒。一块玻璃上有一条对角线的裂缝。",
      "porch": "与建筑物同宽的木制门廊。木板已经风化，被太阳晒白的地方变成灰色，人流磨得光滑的地方变成深棕色。有的木板轻微翘曲，有几个钉头突出。粗凿的木柱支撑着门廊的悬挑。",
      “details”：“前面有一根拴马的柱子，上面拴着一根马的牵绳——绳子拉紧，表明有一只动物刚刚脱离了画面。系结柱附近有一个木制水槽，表面呈绿色。门旁边有一个桶。 一切都覆盖着一层薄薄的沙漠灰尘。”
    },
  “约束”：{
    “必须包含”：[
      “大胆的黑色墨水轮廓线贯穿始终——这是带有色彩的线条艺术，而不是绘画”，
      “丰富的多层色彩，每个表面都有色调渐变”，
      “所有阴影区域的蓝紫色转变（不仅仅是变暗的基色）”，
      “夕阳直射的温暖琥珀金光”，
      “极其细致的脸部，具有特定的个人特征——疤痕、皱纹、骨骼结构”，
      “材质差异化——皮革、木材、金属、织物、皮肤看起来都不同”，
      “日落光束中的大气尘埃颗粒”，
      “长长的戏剧性的影子投射在尘土飞扬的地面上”，
      “作为边缘/强调光从轿车内部发出温暖的光芒”，
      “左侧广阔的开放空间与右侧坚固的轿车结构形成鲜明对比”
    ],
    “必须避免”：[
      “任何类型的卡通或漫画风格”，
      “动画或漫画渲染约定”，
      “纯色填充，无渐变”，
      “隐藏墨水线条的软喷枪”，
      “照相写实主义——水墨画必须是可见的”，
      “普通的无特征脸——这一定是一个特定的人”，
      “干净或新的东西——一切都显示出年龄和磨损”，
      “浑浊的深色——夕阳提供了丰富的温暖光线”，
      “僵硬的姿势——自然放松的人体语言”，
      “水彩透明度或尖端技术”
    ]
  },

  " Negative_prompt": "动漫、漫画、赤壁、卡通、漫画、平面色彩、卡通着色、极简主义、真实感照片、3D CGI 渲染、软喷枪、水彩、柔和的颜色、粗略的线条、普通的脸、干净的新衣服、明亮的霓虹灯、模糊、低分辨率、僵硬的姿势、现代元素、矢量艺术、简单的插图、儿童书籍风格、波普艺术、抽象"
}
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。Generates hyper-detailed cinematic illustrations with bold black ink linework over rich, fully-rendered digital color. Inspired by prestige editorial illustration technique, dramatic golden-hour lighting, cool blue-violet shadows, obsessive material detail. User describes a scene, prompt produces the illustration.

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
