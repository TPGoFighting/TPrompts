# Web Application Testing Skill (Imported)

**Description:** Toolkit for interacting with and testing local web applications using Playwright.

**Type:** SKILL
**Author:** daiyigr
**Created:** 2026-03-13T09:05:11.877Z
**Votes:** 0
**Views:** 0

**Tags:** UI, Playwright, Automation, Testing

## Prompt Content

```
---
name: web-application-testing-skill
description: A toolkit for interacting with and testing local web applications using Playwright.
---

# Web Application Testing

This skill enables comprehensive testing and debugging of local web applications using Playwright automation.

## When to Use This Skill

Use this skill when you need to:
- Test frontend functionality in a real browser
- Verify UI behavior and interactions
- Debug web application issues
- Capture screenshots for documentation or debugging
- Inspect browser console logs
- Validate form submissions and user flows
- Check responsive design across viewports

## Prerequisites

- Node.js installed on the system
- A locally running web application (or accessible URL)
- Playwright will be installed automatically if not present

## Core Capabilities

### 1. Browser Automation
- Navigate to URLs
- Click buttons and links
- Fill form fields
- Select dropdowns
- Handle dialogs and alerts

### 2. Verification
- Assert element presence
- Verify text content
- Check element visibility
- Validate URLs
- Test responsive behavior

### 3. Debugging
- Capture screenshots
- View console logs
- Inspect network requests
- Debug failed tests

## Usage Examples

### Example 1: Basic Navigation Test
```javascript
// Navigate to a page and verify title
await page.goto('http://localhost:3000');
const title = await page.title();
console.log('Page title:', title);
```

### Example 2: Form Interaction
```javascript
// Fill out and submit a form
await page.fill('#username', 'testuser');
await page.fill('#password', 'password123');
await page.click('button[type="submit"]');
await page.waitForURL('**/dashboard');
```

### Example 3: Screenshot Capture
```javascript
// Capture a screenshot for debugging
await page.screenshot({ path: 'debug.png', fullPage: true });
```

## Guidelines

1. **Always verify the app is running** - Check that the local server is accessible before running tests
2. **Use explicit waits** - Wait for elements or navigation to complete before interacting
3. **Capture screenshots on failure** - Take screenshots to help debug issues
4. **Clean up resources** - Always close the browser when done
5. **Handle timeouts gracefully** - Set reasonable timeouts for slow operations
6. **Test incrementally** - Start with simple interactions before complex flows
7. **Use selectors wisely** - Prefer data-testid or role-based selectors over CSS classes

## Common Patterns

### Pattern: Wait for Element
```javascript
await page.waitForSelector('#element-id', { state: 'visible' });
```

### Pattern: Check if Element Exists
```javascript
const exists = await page.locator('#element-id').count() > 0;
```

### Pattern: Get Console Logs
```javascript
page.on('console', msg => console.log('Browser log:', msg.text()));
```

### Pattern: Handle Errors
```javascript
try {
  await page.click('#button');
} catch (error) {\n  await page.screenshot({ path: 'error.png' });
  throw error;
}
```

## Limitations

- Requires Node.js environment
- Cannot test native mobile apps (use React Native Testing Library instead)
- May have issues with complex authentication flows
- Some modern frameworks may require specific configuration
```

**Source:** https://prompts.chat/prompts/cmmoo8dz80002lc04ys17mj0u_web-application-testing-skill-imported

## 中文翻译

### 标题
Web应用测试技能（引进）

### 提示词内容

```
---
名称：网络应用程序测试技能
描述：使用 Playwright 与本地 Web 应用程序交互并测试本地 Web 应用程序的工具包。
---

# Web 应用程序测试

此技能可以使用 Playwright 自动化对本地 Web 应用程序进行全面测试和调试。

## 何时使用此技能

当您需要执行以下操作时，请使用此技能：
- 在真实浏览器中测试前端功能
- 验证 UI 行为和交互
- 调试网络应用程序问题
- 捕获屏幕截图以用于文档或调试
- 检查浏览器控制台日志
- 验证表单提交和用户流程
- 检查跨视口的响应式设计

## 先决条件

- 系统上安装了 Node.js
- 本地运行的 Web 应用程序（或可访问的 URL）
- 如果不存在，剧作家将自动安装

## 核心能力

### 1. 浏览器自动化
- 导航至 URL
- 单击按钮和链接
- 填写表单字段
- 选择下拉菜单
- 处理对话框和警报

### 2.验证
- 断言元素存在
- 验证文本内容
- 检查元素可见性
- 验证 URL
- 测试响应行为

### 3.调试
- 捕获屏幕截图
- 查看控制台日志
- 检查网络请求
- 调试失败的测试

## 用法示例

### 示例 1：基本导航测试
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Toolkit for interacting with and testing local web applications using Playwright.

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
