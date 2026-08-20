# prompts.chat Promotional Video using Remotion

**Description:** This prompt guides the creation of a 30-second promotional video for prompts.chat using Remotion. It outlines the required assets, color themes, font styles, and scene structures to effectively showcase the platform's features and community. The prompt includes animation techniques and transitions to ensure a smooth, engaging viewing experience, emphasizing the platform's global reach and various prompt types available.

**Type:** VIDEO
**Author:** f
**Created:** 2026-01-24T14:02:32.070Z
**Votes:** 1
**Views:** 0

**Category:** Video Generation

## Prompt Content

```
Create a 30-second promotional video for prompts.chat                     
                                                                              
Required Assets                                                               
                                                                              
- https://prompts.chat/logo.svg - Logo SVG   
- https://raw.githubusercontent.com/flekschas/simple-world-map/refs/heads/master/world-map.svg - World map SVG for global community scene       
                                                                              
Color Theme (Light)                                                           
                                                                              
- Background: #ffffff                                                         
- Background Alt: #f8fafc                                                     
- Primary: #6366f1 (Indigo)                                                   
- Primary Light: #818cf8                                                      
- Accent: #22c55e (Green)                                                     
- Text: #0f172a                                                               
- Text Muted: #64748b                                                         
                                                                              
Font                                                                          
                                                                              
- Inter (weights: 400, 600, 700, 800)                                         
                                                                              
---                                                                           
Scene Structure (8 Scenes)                                                    
                                                                              
Scene 1: Opening (5s)                                                         
                                                                              
- Logo appears                           
- Logo centered, scales in with spring animation                              
- After animation: "prompts.chat" text reveals left-to-right below logo using 
clip-path                                                                     
- Tagline appears: "The Free Social Platform for AI Prompts"                  
                                                                              
Scene 2: Global Community (4s)                                                
                                                                              
- Full-screen world map (25% opacity) as background                           
- 16 pulsing activity dots at major cities (LA, NYC, Toronto, Sao Paulo,      
London, Paris, Berlin, Lagos, Moscow, Dubai, Mumbai, Beijing, Tokyo,          
Singapore, Sydney, Warsaw)                                                    
- Each dot has outer pulse ring, inner pulse, and center dot with glow        
- Title: "A global community of prompt creators"                              
- Stats row: 8k+ users, 3k+ daily visitors, 1k+ prompts, 300+ contributors,   
10+ languages                                                                 
- Gradient overlay at bottom for text readability                             
                                                                              
Scene 3: Solution (2.5s)                                                      
                                                                              
- Three words appear sequentially with spring animation: "Discover." "Share." 
"Collect."                                                                    
- Each word in different color (primary, accent, primary light)               
                                                                              
Scene 4: Built for Everyone (4s)                                              
                                                                              
- 8 floating persona icons around screen edges with sine/cosine wave floating 
animation                                                                     
- Personas: Students, Teachers, Researchers, Developers, Artists, Writers,    
Marketers, Entrepreneurs                                                      
- Each has 130x130 icon container with colored background/border              
- Center title: "Built for everyone"                                          
- Subtitle: "One prompt away from your next breakthrough."                    
                                                                              
Scene 5: Prompt Types (5s)                                                    
                                                                              
- Title: "Prompts for every need"                                             
- Browser-like frame (1400x800) with macOS traffic lights and URL bar showing 
"prompts.chat"                                                                
- A masonry skeleton screenshot scrolls vertically with eased animation (cubic ease-in-out)      
- 7 floating pill-shaped labels around edges with icons:                      
  - Text (purple), Image (pink), Video (amber), Audio (green), Workflows      
(violet), Skills (teal), JSON (red)                                           
                                                                              
Scene 6: Features (4s)                                                        
                                                                              
- 4 feature cards appearing sequentially with spring animation:               
  - Prompt Library (book icon) - "Thousands of prompts across all categories" 
  - Skills & Workflows (bolt icon) - "Automate multi-step AI tasks"           
  - Community (users icon) - "Share and discover from creators"               
  - Open Source (circle-plus icon) - "Self-host with complete privacy"        
                                                                              
Scene 7: Social Proof (4s)                                                    
                                                                              
- Animated GitHub star counter (0 → 143,000+)                                 
- Star icon next to count                                                     
- Badge: "The First Prompt Library — Since December 2022" with trophy icon    
- Text: "Endorsed by OpenAI co-founders • Used by Harvard, Columbia & more"   
                                                                              
Scene 8: CTA (3.5s)                                                           
                                                                              
- Background glow animation (pulsing radial gradient)                         
- Title: "Start exploring today"                                              
- Large button with logo + "prompts.chat" text (gradient background, subtle   
pulse)                                                                        
- Subtitle: "Free & Open Source"                                              
                                                                              
---                                                                           
Transitions (0.4s each)                                                       
                                                                              
- Scene 1→2: Fade                                                             
- Scene 2→3: Slide from right                                                 
- Scene 3→4: Fade                                                             
- Scene 4→5: Fade                                                             
- Scene 5→6: Slide from right                                                 
- Scene 6→7: Slide from bottom                                                
- Scene 7→8: Fade                                                             
                                                                              
Animation Techniques Used                                                     
                                                                              
- spring() for bouncy scale animations                                        
- interpolate() for opacity, position, and clip-path                          
- Easing.inOut(Easing.cubic) for smooth scroll                                
- Math.sin()/Math.cos() for floating animations                               
- Staggered delays for sequential element appearances                         
                                                                              
Key Components                                                                
                                                                              
- Custom SVG icon components for all icons (no emojis)                        
- Logo component with prompts.chat "P" path                                   
- FeatureCard reusable component                                              
- TransitionSeries for scene management                                       
```

**Source:** https://prompts.chat/prompts/cmksdpvk60004l404t37q90xr_promptschat-promotional-video-using-remotion

## 中文翻译

### 标题
prompts.聊天 Promotional Video using Remotion

### 提示词内容

```
【中文翻译说明】以下为英文提示词的中文翻译（部分技术术语保留英文原文），请参考下方使用说明了解其用途和用法。

创建 一个 30-second promotional video 用于 prompts.chat                     
                                                                              
Required Assets                                                               
                                                                              
- https://prompts.chat/logo.svg - Logo SVG   
- https://raw.githubusercontent.com/flekschas/simple-world-映射/refs/heads/master/world-映射.svg - World 映射 SVG 用于 global community scene       
                                                                              
Color Theme (Light)                                                           
                                                                              
- Background: #ffffff                                                         
- Background Alt: #f8fafc                                                     
- Primary: #6366f1 (Indigo)                                                   
- Primary Light: #818cf8                                                      
- Accent: #22c55e (Green)                                                     
- Text: #0f172a                                                               
- Text Muted: #64748b                                                         
                                                                              
Font                                                                          
                                                                              
- Inter (weights: 400, 600, 700, 800)                                         
                                                                              
---                                                                           
Scene 结构 (8 Scenes)                                                    
                                                                              
Scene 1: Opening (5s)                                                         
                                                                              
- Logo appears                           
- Logo centered, scales in 使用 spring animation                              
- After animation: "prompts.chat" text reveals left-to-right below logo using 
clip-path                                                                     
- Tagline appears: "（定冠词） Free Social 平台 用于 AI Prompts"                  
                                                                              
Scene 2: Global Community (4s)                                                
                                                                              
- Full-屏幕 world 映射 (25% opacity) as background                           
- 16 pulsing activity dots at major cities (LA, NYC, Toronto, Sao Paulo,      
London, Paris, Berlin, Lagos, Moscow, Dubai, Mumbai, Beijing, Tokyo,          
Singapore, Sydney, Warsaw)                                                    
- Each dot has outer pulse ring, inner pulse, 和 center dot 使用 glow        
- Title: "一个 global community of prompt creators"                              
- Stats row: 8k+ users, 3k+ daily visitors, 1k+ prompts, 300+ contributors,   
10+ languages                                                                 
- Gradient overlay at bottom 用于 text readability                             
                                                                              
Scene 3: 解决方案 (2.5s)                                                      
                                                                              
- Three words appear sequentially 使用 spring animation: "Discover." "Share." 
"Collect."                                                                    
- Each word in different color (primary, accent, primary light)               
                                                                              
Scene 4: Built 用于 Everyone (4s)                                              
                                                                              
- 8 floating persona icons around 屏幕 edges 使用 sine/cosine wave floating 
animation                                                                     
- Personas: Students, Teachers, Researchers, Developers, Artists, Writers,    
Marketers, Entrepreneurs                                                      
- Each has 130x130 icon 容器 使用 colored background/border              
- Center title: "Built 用于 everyone"                                          
- Subtitle: "One prompt away from your next breakthrough."                    
                                                                              
Scene 5: Prompt Types (5s)                                                    
                                                                              
- Title: "Prompts 用于 every need"                                             
- 浏览器-like frame (1400x800) 使用 macOS traffic lights 和 URL 栏 showing 
"prompts.chat"                                                                
- 一个 masonry skeleton screenshot scrolls vertically 使用 eased animation (cubic ease-in-out)      
- 7 floating pill-shaped labels around edges 使用 icons:                      
  - Text (purple), Image (pink), Video (amber), Audio (green), Workflows      
(violet), Skills (teal), JSON (red)                                           
                                                                              
Scene 6: 功能 (4s)                                                        
                                                                              
- 4 功能 cards appearing sequentially 使用 spring animation:               
  - Prompt 库 (book icon) - "Thousands of prompts across all categories" 
  - Skills & Workflows (bolt icon) - "Automate multi-step AI tasks"           
  - Community (users icon) - "Share 和 discover from creators"               
  - Open Source (circle-plus icon) - "Self-host 使用 complete privacy"        
                                                                              
Scene 7: Social 概念 (4s)                                                    
                                                                              
- Animated GitHub star counter (0 → 143,000+)                                 
- Star icon next to count                                                     
- Badge: "（定冠词） First Prompt 库 — Since December 2022" 使用 trophy icon    
- Text: "Endorsed by OpenAI co-founders • Used by Harvard, Columbia & more"   
                                                                              
Scene 8: CTA (3.5s)                                                           
                                                                              
- Background glow animation (pulsing radial gradient)                         
- Title: "Start exploring today"                                              
- Large 按钮 使用 logo + "prompts.chat" text (gradient background, subtle   
pulse)                                                                        
- Subtitle: "Free & Open Source"                                              
                                                                              
---                                                                           
Transitions (0.4s each)                                                       
                                                                              
- Scene 1→2: Fade                                                             
- Scene 2→3: Slide from right                                                 
- Scene 3→4: Fade                                                             
- Scene 4→5: Fade                                                             
- Scene 5→6: Slide from right                                                 
- Scene 6→7: Slide from bottom                                                
- Scene 7→8: Fade                                                             
                                                                              
Animation Techniques Used                                                     
                                                                              
- spring() 用于 bouncy scale animations                                        
- interpolate() 用于 opacity, position, 和 clip-path                          
- Easing.inOut(Easing.cubic) 用于 smooth scroll                                
- Math.sin()/Math.cos() 用于 floating animations                               
- Staggered delays 用于 sequential 元素 appearances                         
                                                                              
键 Components                                                                
                                                                              
- Custom SVG icon components 用于 all icons (no emojis)                        
- Logo 组件 使用 prompts.chat "P" path                                   
- FeatureCard reusable 组件                                              
- TransitionSeries 用于 scene 管理
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**创意写作与故事创作**类的提示词。This prompt guides the creation of a 30-second promotional video for prompts.chat using Remotion. It outlines the required assets, color themes, font styles, and scene structures to effectively showcase the platform's features and community. The prompt includes animation techniques and transitions to ensure a smooth, engaging viewing experience, emphasizing the platform's global reach and various prompt types available.

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
