# Accessibility Testing Superpower

**Description:** Performs WCAG compliance audits and accessibility remediation for web applications. Use when: 1) Auditing UI for WCAG 2.1/2.2 compliance 2) Fixing screen reader or keyboard navigation issues 3) Implementing ARIA patterns correctly 4) Reviewing color contrast and visual accessibility 5) Creating accessible forms or interactive components

**Type:** SKILL
**Author:** izzetemre
**Created:** 2025-12-26T07:35:31.086Z
**Votes:** 1
**Views:** 0

**Tags:** Skill, AI Tools, JavaScript, Go, Backend

**Category:** Agent Skill

## Prompt Content

```
---
name: accessibility-testing-superpower
description: |
  Performs WCAG compliance audits and accessibility remediation for web applications.
  Use when: 1) Auditing UI for WCAG 2.1/2.2 compliance 2) Fixing screen reader or keyboard navigation issues 3) Implementing ARIA patterns correctly 4) Reviewing color contrast and visual accessibility 5) Creating accessible forms or interactive components
---

# Accessibility Testing Workflow

## Configuration

- **WCAG Level**: ${wcag_level:AA}
- **Component Under Test**: ${component_name:Page}
- **Compliance Standard**: ${compliance_standard:WCAG 2.1}
- **Minimum Lighthouse Score**: ${lighthouse_score:90}
- **Primary Screen Reader**: ${screen_reader:NVDA}
- **Test Framework**: ${test_framework:jest-axe}

## Audit Decision Tree

```
Accessibility request received
|
+-- New component/page?
|   +-- Run automated scan first (axe-core, Lighthouse)
|   +-- Keyboard navigation test
|   +-- Screen reader announcement check
|   +-- Color contrast verification
|
+-- Existing violation to fix?
|   +-- Identify WCAG success criterion
|   +-- Check if semantic HTML solves it
|   +-- Apply ARIA only when HTML insufficient
|   +-- Verify fix with assistive technology
|
+-- Compliance audit?
    +-- Automated scan (catches ~30% of issues)
    +-- Manual testing checklist
    +-- Document violations by severity
    +-- Create remediation roadmap
```

## WCAG Quick Reference

### Severity Classification

| Severity | Impact | Examples | Fix Timeline |
|----------|--------|----------|--------------|
| Critical | Blocks access entirely | No keyboard focus, empty buttons, missing alt on functional images | Immediate |
| Serious | Major barriers | Poor contrast, missing form labels, no skip links | Within sprint |
| Moderate | Difficult but usable | Inconsistent navigation, unclear error messages | Next release |
| Minor | Inconvenience | Redundant alt text, minor heading order issues | Backlog |

### Common Violations and Fixes

**Missing accessible name**
```html
<!-- Violation -->
<button><svg>...</svg></button>

<!-- Fix: aria-label -->
<button aria-label="Close dialog"><svg>...</svg></button>

<!-- Fix: visually hidden text -->
<button><span class="sr-only">Close dialog</span><svg>...</svg></button>
```

**Form label association**
```html
<!-- Violation -->
<label>Email</label>
<input type="email">

<!-- Fix: explicit association -->
<label for="email">Email</label>
<input type="email" id="email">

<!-- Fix: implicit association -->
<label>Email <input type="email"></label>
```

**Color contrast failure**
```
Minimum ratios (WCAG ${wcag_level:AA}):
- Normal text (<${large_text_size:18}px or <${bold_text_size:14}px bold): ${contrast_ratio_normal:4.5}:1
- Large text (>=${large_text_size:18}px or >=${bold_text_size:14}px bold): ${contrast_ratio_large:3}:1
- UI components and graphics: 3:1

Tools: WebAIM Contrast Checker, browser DevTools
```

**Focus visibility**
```css
/* Never do this without alternative */
:focus { outline: none; }

/* Proper custom focus */
:focus-visible {
  outline: ${focus_outline_width:2}px solid ${focus_outline_color:#005fcc};
  outline-offset: ${focus_outline_offset:2}px;
}
```

## ARIA Decision Framework

```
Need to convey information to assistive technology?
|
+-- Can semantic HTML do it?
|   +-- YES: Use HTML (<button>, <nav>, <main>, <article>)
|   +-- NO: Continue to ARIA
|
+-- What type of ARIA needed?
    +-- Role: What IS this element? (role="dialog", role="tab")
    +-- State: What condition? (aria-expanded, aria-checked)
    +-- Property: What relationship? (aria-labelledby, aria-describedby)
    +-- Live region: Dynamic content? (aria-live="${aria_live_mode:polite}")
```

### ARIA Patterns for Common Widgets

**Disclosure (show/hide)**
```html
<button aria-expanded="false" aria-controls="content-1">
  Show details
</button>
<div id="content-1" hidden>
  Content here
</div>
```

**Tab interface**
```html
<div role="tablist" aria-label="${component_name:Settings}">
  <button role="tab" aria-selected="true" aria-controls="panel-1" id="tab-1">
    General
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel-2" id="tab-2" tabindex="-1">
    Privacy
  </button>
</div>
<div role="tabpanel" id="panel-1" aria-labelledby="tab-1">...</div>
<div role="tabpanel" id="panel-2" aria-labelledby="tab-2" hidden>...</div>
```

**Modal dialog**
```html
<div role="dialog" aria-modal="true" aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirm action</h2>
  <p>Are you sure you want to proceed?</p>
  <button>Cancel</button>
  <button>Confirm</button>
</div>
```

## Keyboard Navigation Checklist

```
[ ] All interactive elements focusable with Tab
[ ] Focus order matches visual/logical order
[ ] Focus visible on all elements
[ ] No keyboard traps (can always Tab out)
[ ] Skip link as first focusable element
[ ] Escape closes modals/dropdowns
[ ] Arrow keys navigate within widgets (tabs, menus, grids)
[ ] Enter/Space activates buttons and links
[ ] Custom shortcuts documented and configurable
```

### Focus Management Patterns

**Modal focus trap**
```javascript
// On modal open:
// 1. Save previously focused element
// 2. Move focus to first focusable in modal
// 3. Trap Tab within modal boundaries

// On modal close:
// 1. Return focus to saved element
```

**Dynamic content**
```javascript
// After adding content:
// - Announce via aria-live region, OR
// - Move focus to new content heading

// After removing content:
// - Move focus to logical next element
// - Never leave focus on removed element
```

## Screen Reader Testing

### Announcement Verification

| Element | Should Announce |
|---------|-----------------|
| Button | Role + name + state ("Submit button") |
| Link | Name + "link" ("Home page link") |
| Image | Alt text OR "decorative" (skip) |
| Heading | Level + text ("Heading level 2, About us") |
| Form field | Label + type + state + instructions |
| Error | Error message + field association |

### Testing Commands (Quick Reference)

**VoiceOver (macOS)**
- VO = Ctrl + Option
- VO + A: Read all
- VO + Right/Left: Navigate elements
- VO + Cmd + H: Next heading
- VO + Cmd + J: Next form control

**${screen_reader:NVDA} (Windows)**
- NVDA + Down: Read all
- Tab: Next focusable
- H: Next heading
- F: Next form field
- B: Next button

## Automated Testing Integration

### axe-core in tests
```javascript
// ${test_framework:jest-axe}
import { axe, toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);

test('${component_name:component} is accessible', async () => {
  const { container } = render(<${component_name:MyComponent} />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

### Lighthouse CI threshold
```javascript
// lighthouserc.js
module.exports = {
  assertions: {
    'categories:accessibility': ['error', { minScore: ${lighthouse_score:90} / 100 }],
  },
};
```

## Remediation Priority Matrix

```
Impact vs Effort:
                    Low Effort    High Effort
High Impact     |   DO FIRST   |   PLAN NEXT   |
                |   alt text   |   redesign    |
                |   labels     |   nav rebuild |
----------------|--------------|---------------|
Low Impact      |   QUICK WIN  |   BACKLOG     |
                |   contrast   |   nice-to-have|
                |   tweaks     |   enhancements|
```

## Verification Checklist

Before marking accessibility work complete:

```
Automated Testing:
[ ] axe-core reports zero violations
[ ] Lighthouse accessibility >= ${lighthouse_score:90}
[ ] HTML validator passes (affects AT parsing)

Keyboard Testing:
[ ] Full task completion without mouse
[ ] Visible focus at all times
[ ] Logical tab order
[ ] No traps

Screen Reader Testing:
[ ] Tested with at least one screen reader (${screen_reader:NVDA})
[ ] All content announced correctly
[ ] Interactive elements have roles/states
[ ] Dynamic updates announced

Visual Testing:
[ ] Contrast ratios verified (${contrast_ratio_normal:4.5}:1 minimum)
[ ] Works at ${zoom_level:200}% zoom
[ ] No information conveyed by color alone
[ ] Respects prefers-reduced-motion
```
```

**Source:** https://prompts.chat/prompts/cmjmk4gsv000jld04pplcmo1e_accessibility-testing-superpower

## 中文翻译

### 标题
无障碍测试超能力

### 提示词内容

```
---
名称：可访问性测试超级大国
描述： |
  对 Web 应用程序执行 WCAG 合规性审核和可访问性修复。
  在以下情况下使用： 1) 审核 UI 是否符合 WCAG 2.1/2.2 合规性 2) 修复屏幕阅读器或键盘导航问题 3) 正确实施 ARIA 模式 4) 检查颜色对比度和视觉可访问性 5) 创建可访问的表单或交互式组件
---

# 辅助功能测试工作流程

## 配置

- **WCAG 级别**：${wcag_level:AA}
- **被测组件**：${component_name:Page}
- **合规标准**：${compliance_standard:WCAG 2.1}
- **最低灯塔分数**：${lighthouse_score:90}
- **主屏幕阅读器**：${screen_reader:NVDA}
- **测试框架**：${test_framework:jest-axe}

## 审计决策树
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Performs WCAG compliance audits and accessibility remediation for web applications. Use when: 1) Auditing UI for WCAG 2.1/2.2 compliance 2) Fixing screen reader or keyboard navigation issues 3) Implementing ARIA patterns correctly 4) Reviewing color contrast and visual accessibility 5) Creating accessible forms or interactive components

### 适用人群
通用用户

### 使用步骤
1. 复制下方完整的中文提示词内容
2. 打开任意AI工具（ChatGPT、Claude、Gemini、Copilot等）
3. 粘贴提示词到对话框
4. 根据需要修改变量部分（如有）
5. 发送并获取AI生成的响应
6. 根据结果进一步调整或追问
### 可自定义变量
- `${wcag_level}`: 可自定义（默认值: AA）
- `${component_name}`: 可自定义（默认值: Page）
- `${compliance_standard}`: 可自定义（默认值: WCAG 2.1）
- `${lighthouse_score}`: 可自定义（默认值: 90）
- `${screen_reader}`: 可自定义（默认值: NVDA）
- `${test_framework}`: 可自定义（默认值: jest-axe）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
