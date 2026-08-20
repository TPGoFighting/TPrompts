# Generate a Plan for Building the Best UI/UX

**Description:** Generate a comprehensive, actionable development plan for building a responsive web application.

**Type:** TEXT
**Author:** ayoubelouardi3710
**Created:** 2026-03-10T05:19:47.436Z
**Votes:** 0
**Views:** 0

**Tags:** Frontend, Web Development, claude-code, codex, CLI

**Category:** Vibe Coding

## Prompt Content

```
You are a senior full-stack engineer and UX/UI architect with 10+ years of experience building 
production-grade web applications. You specialize in responsive design systems, modern UI/UX 
patterns, and cross-device performance optimization.

---

## TASK

Generate a **comprehensive, actionable development plan** for building a responsive web application 
that meets the following criteria:

### 1. RESPONSIVENESS & CROSS-DEVICE COMPATIBILITY
- Flawlessly adapts to: mobile (320px+), tablet (768px+), desktop (1024px+), large screens (1440px+)
- Define a clear **breakpoint strategy** with rationale
- Specify a **mobile-first vs desktop-first** approach with justification
- Address: touch targets, tap gestures, hover states, keyboard navigation
- Handle: notches, safe areas, dynamic viewport units (dvh/svh/lvh)
- Cover: font scaling, image optimization (srcset, art direction), fluid typography

### 2. PERFORMANCE & SMOOTHNESS
- Target: 60fps animations, <2.5s LCP, <100ms INP, <0.1 CLS (Core Web Vitals)
- Strategy for: lazy loading, code splitting, asset optimization
- Approach to: CSS containment, will-change, GPU compositing for animations
- Plan for: offline support or graceful degradation

### 3. MODERN & ELEGANT DESIGN SYSTEM
- Define a **design token architecture**: colors, spacing, typography, elevation, motion
- Specify: color palette strategy (light/dark mode support), font pairing rationale
- Include: spacing scale, border radius philosophy, shadow system
- Cover: iconography approach, illustration/imagery style guidance
- Detail: component-level visual consistency rules

### 4. MODERN UX/UI BEST PRACTICES
Apply and plan for the following UX/UI principles:
- **Hierarchy & Scannability**: F/Z pattern layouts, visual weight, whitespace strategy
- **Feedback & Affordance**: loading states, skeleton screens, micro-interactions, error states
- **Navigation Patterns**: responsive nav (hamburger, bottom nav, sidebar), breadcrumbs, wayfinding
- **Accessibility (WCAG 2.1 AA minimum)**: contrast ratios, ARIA roles, focus management, screen reader support
- **Forms & Input**: validation UX, inline errors, autofill, input types per device
- **Motion Design**: purposeful animation (easing curves, duration tokens), reduced-motion support
- **Empty States & Edge Cases**: zero data, errors, timeouts, permission denied

### 5. TECHNICAL ARCHITECTURE PLAN
- Recommend a **tech stack** with justification (framework, CSS approach, state management)
- Define: component architecture (atomic design or alternative), folder structure
- Specify: theming system implementation, CSS strategy (modules, utility-first, CSS-in-JS)
- Include: testing strategy for responsiveness (tools, breakpoints to test, devices)

---

## OUTPUT FORMAT

Structure your plan in the following sections:

1. **Executive Summary** – One paragraph overview of the approach
2. **Responsive Strategy** – Breakpoints, layout system, fluid scaling approach
3. **Performance Blueprint** – Targets, techniques, tooling
4. **Design System Specification** – Tokens, palette, typography, components
5. **UX/UI Pattern Library Plan** – Key patterns, interactions, accessibility checklist
6. **Technical Architecture** – Stack, structure, implementation order
7. **Phased Rollout Plan** – Prioritized milestones (MVP → polish → optimization)
8. **Quality Checklist** – Pre-launch verification across all devices and criteria

---

## CONSTRAINTS & STYLE

- Be **specific and actionable** — avoid vague recommendations
- Provide **concrete values** where applicable (e.g., "8px base spacing scale", "400ms ease-out for modals")
- Flag **common pitfalls** and how to avoid them
- Where multiple approaches exist, **recommend one with reasoning** rather than listing all options
- Assume the target is a **[INSERT APP TYPE: e.g., SaaS dashboard / e-commerce / portfolio / social app]**
- Target users are **[INSERT: e.g., non-technical consumers / enterprise professionals / mobile-first users]**

---

Begin with the Executive Summary, then proceed section by section.
```

**Source:** https://prompts.chat/prompts/cmmk5uygc0001jv04g4yuguhi_generate-a-plan-for-building-the-best-uiux


## 中文翻译

### 标题
Generate a 计划 for Building the Best 用户界面/用户体验

### 提示词内容

```
【中文翻译说明】以下为英文提示词原文，请参考下方使用说明了解其用途和用法。

You are a senior full-stack engineer and UX/UI architect with 10+ years of experience building 
production-grade web applications. You specialize in responsive design systems, modern UI/UX 
patterns, and cross-device performance optimization.

---

## TASK

Generate a **comprehensive, actionable development plan** for building a responsive web application 
that meets the following criteria:

### 1. RESPONSIVENESS & CROSS-DEVICE COMPATIBILITY
- Flawlessly adapts to: mobile (320px+), tablet (768px+), desktop (1024px+), large screens (1440px+)
- Define a clear **breakpoint strategy** with rationale
- Specify a **mobile-first vs desktop-first** approach with justification
- Address: touch targets, tap gestures, hover states, keyboard navigation
- Handle: notches, safe areas, dynamic viewport units (dvh/svh/lvh)
- Cover: font scaling, image optimization (srcset, art direction), fluid typography

### 2. PERFORMANCE & SMOOTHNESS
- Target: 60fps animations, <2.5s LCP, <100ms INP, <0.1 CLS (Core Web Vitals)
- Strategy for: lazy loading, code splitting, asset optimization
- Approach to: CSS containment, will-change, GPU compositing for animations
- Plan for: offline support or graceful degradation

### 3. MODERN & ELEGANT DESIGN SYSTEM
- Define a **design token architecture**: colors, spacing, typography, elevation, motion
- Specify: color palette strategy (light/dark mode support), font pairing rationale
- Include: spacing scale, border radius philosophy, shadow system
- Cover: iconography approach, illustration/imagery style guidance
- Detail: component-level visual consistency rules

### 4. MODERN UX/UI BEST PRACTICES
Apply and plan for the following UX/UI principles:
- **Hierarchy & Scannability**: F/Z pattern layouts, visual weight, whitespace strategy
- **Feedback & Affordance**: loading states, skeleton screens, micro-interactions, error states
- **Navigation Patterns**: responsive nav (hamburger, bottom nav, sidebar), breadcrumbs, wayfinding
- **Accessibility (WCAG 2.1 AA minimum)**: contrast ratios, ARIA roles, focus management, screen reader support
- **Forms & Input**: validation UX, inline errors, autofill, input types per device
- **Motion Design**: purposeful animation (easing curves, duration tokens), reduced-motion support
- **Empty States & Edge Cases**: zero data, errors, timeouts, permission denied

### 5. TECHNICAL ARCHITECTURE PLAN
- Recommend a **tech stack** with justification (framework, CSS approach, state management)
- Define: component architecture (atomic design or alternative), folder structure
- Specify: theming system implementation, CSS strategy (modules, utility-first, CSS-in-JS)
- Include: testing strategy for responsiveness (tools, breakpoints to test, devices)

---

## OUTPUT FORMAT

Structure your plan in the following sections:

1. **Executive Summary** – One paragraph overview of the approach
2. **Responsive Strategy** – Breakpoints, layout system, fluid scaling approach
3. **Performance Blueprint** – Targets, techniques, tooling
4. **Design System Specification** – Tokens, palette, typography, components
5. **UX/UI Pattern Library Plan** – Key patterns, interactions, accessibility checklist
6. **Technical Architecture** – Stack, structure, implementation order
7. **Phased Rollout Plan** – Prioritized milestones (MVP → polish → optimization)
8. **Quality Checklist** – Pre-launch verification across all devices and criteria

---

## CONSTRAINTS & STYLE

- Be **specific and actionable** — avoid vague recommendations
- Provide **concrete values** where applicable (e.g., "8px base spacing scale", "400ms ease-out for modals")
- Flag **common pitfalls** and how to avoid them
- Where multiple approaches exist, **recommend one with reasoning** rather than listing all options
- Assume the target is a **[INSERT APP TYPE: e.g., SaaS dashboard / e-commerce / portfolio / social app]**
- Target users are **[INSERT: e.g., non-technical consumers / enterprise professionals / mobile-first users]**

---

Begin with the Executive Summary, then proceed section by section.
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Generate a comprehensive, actionable development plan for building a responsive web application.

### 适用人群
开发者/程序员

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
