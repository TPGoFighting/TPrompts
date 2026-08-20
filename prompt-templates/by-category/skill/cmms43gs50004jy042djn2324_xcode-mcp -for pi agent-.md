# xcode-mcp (for pi agent)

**Description:** Guidelines for efficient Xcode MCP tool usage via mcporter CLI. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations. Use this skill whenever working with Xcode projects, iOS/macOS builds, SwiftUI previews, or Apple platform development.

**Type:** SKILL
**Author:** ilker
**Created:** 2026-03-15T18:52:34.613Z
**Votes:** 0
**Views:** 0

**Category:** Agent Skill

## Prompt Content

```
---
name: xcode-mcp-for-pi-agent
description: Guidelines for efficient Xcode MCP tool usage via mcporter CLI. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations. Use this skill whenever working with Xcode projects, iOS/macOS builds, SwiftUI previews, or Apple platform development.
---

# Xcode MCP Usage Guidelines

Xcode MCP tools are accessed via `mcporter` CLI, which bridges MCP servers to standard command-line tools. This skill defines when to use Xcode MCP and when to prefer standard tools.

## Setup

Xcode MCP must be configured in `~/.mcporter/mcporter.json`:

```json
{
  "mcpServers": {
    "xcode": {
      "command": "xcrun",
      "args": ["mcpbridge"],
      "env": {}
    }
  }
}
```

Verify the connection:
```bash
mcporter list xcode
```

---

## Calling Tools

All Xcode MCP tools are called via mcporter:

```bash
# List available tools
mcporter list xcode

# Call a tool with key:value args
mcporter call xcode.<tool_name> param1:value1 param2:value2

# Call with function-call syntax
mcporter call 'xcode.<tool_name>(param1: "value1", param2: "value2")'
```

---

## Complete Xcode MCP Tools Reference

### Window & Project Management
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| List open Xcode windows (get tabIdentifier) | `mcporter call xcode.XcodeListWindows` | Low ✓ |

### Build Operations
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| Build the Xcode project | `mcporter call xcode.BuildProject` | Medium ✓ |
| Get build log with errors/warnings | `mcporter call xcode.GetBuildLog` | Medium ✓ |
| List issues in Issue Navigator | `mcporter call xcode.XcodeListNavigatorIssues` | Low ✓ |

### Testing
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| Get available tests from test plan | `mcporter call xcode.GetTestList` | Low ✓ |
| Run all tests | `mcporter call xcode.RunAllTests` | Medium |
| Run specific tests (preferred) | `mcporter call xcode.RunSomeTests` | Medium ✓ |

### Preview & Execution
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| Render SwiftUI Preview snapshot | `mcporter call xcode.RenderPreview` | Medium ✓ |
| Execute code snippet in file context | `mcporter call xcode.ExecuteSnippet` | Medium ✓ |

### Diagnostics
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| Get compiler diagnostics for specific file | `mcporter call xcode.XcodeRefreshCodeIssuesInFile` | Low ✓ |
| Get SourceKit diagnostics (all open files) | `mcporter call xcode.getDiagnostics` | Low ✓ |

### Documentation
| Tool | mcporter call | Token Cost |
|------|---------------|------------|
| Search Apple Developer Documentation | `mcporter call xcode.DocumentationSearch` | Low ✓ |

### File Operations (HIGH TOKEN - NEVER USE)
| MCP Tool | Use Instead | Why |
|----------|-------------|-----|
| `xcode.XcodeRead` | `Read` tool / `cat` | High token consumption |
| `xcode.XcodeWrite` | `Write` tool | High token consumption |
| `xcode.XcodeUpdate` | `Edit` tool | High token consumption |
| `xcode.XcodeGrep` | `rg` / `grep` | High token consumption |
| `xcode.XcodeGlob` | `find` / `glob` | High token consumption |
| `xcode.XcodeLS` | `ls` command | High token consumption |
| `xcode.XcodeRM` | `rm` command | High token consumption |
| `xcode.XcodeMakeDir` | `mkdir` command | High token consumption |
| `xcode.XcodeMV` | `mv` command | High token consumption |

---

## Recommended Workflows

### 1. Code Change & Build Flow
```
1. Search code      → rg "pattern" --type swift
2. Read file        → Read tool / cat
3. Edit file        → Edit tool
4. Syntax check     → mcporter call xcode.getDiagnostics
5. Build            → mcporter call xcode.BuildProject
6. Check errors     → mcporter call xcode.GetBuildLog (if build fails)
```

### 2. Test Writing & Running Flow
```
1. Read test file   → Read tool / cat
2. Write/edit test  → Edit tool
3. Get test list    → mcporter call xcode.GetTestList
4. Run tests        → mcporter call xcode.RunSomeTests (specific tests)
5. Check results    → Review test output
```

### 3. SwiftUI Preview Flow
```
1. Edit view        → Edit tool
2. Render preview   → mcporter call xcode.RenderPreview
3. Iterate          → Repeat as needed
```

### 4. Debug Flow
```
1. Check diagnostics → mcporter call xcode.getDiagnostics
2. Build project     → mcporter call xcode.BuildProject
3. Get build log     → mcporter call xcode.GetBuildLog severity:error
4. Fix issues        → Edit tool
5. Rebuild           → mcporter call xcode.BuildProject
```

### 5. Documentation Search
```
1. Search docs       → mcporter call xcode.DocumentationSearch query:"SwiftUI NavigationStack"
2. Review results    → Use information in implementation
```

---

## Fallback Commands (When MCP or mcporter Unavailable)

If Xcode MCP is disconnected, mcporter is not installed, or the connection fails, use these xcodebuild commands directly:

### Build Commands
```bash
# Debug build (simulator) - replace <SchemeName> with your project's scheme
xcodebuild -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# Release build (device)
xcodebuild -scheme <SchemeName> -configuration Release -sdk iphoneos build

# Build with workspace (for CocoaPods projects)
xcodebuild -workspace <ProjectName>.xcworkspace -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# Build with project file
xcodebuild -project <ProjectName>.xcodeproj -scheme <SchemeName> -configuration Debug -sdk iphonesimulator build

# List available schemes
xcodebuild -list
```

### Test Commands
```bash
# Run all tests
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -configuration Debug

# Run specific test class
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -only-testing:<TestTarget>/<TestClassName>

# Run specific test method
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -destination "platform=iOS Simulator,name=iPhone 16" \
  -only-testing:<TestTarget>/<TestClassName>/<testMethodName>

# Run with code coverage
xcodebuild test -scheme <SchemeName> -sdk iphonesimulator \
  -configuration Debug -enableCodeCoverage YES

# List available simulators
xcrun simctl list devices available
```

### Clean Build
```bash
xcodebuild clean -scheme <SchemeName>
```

---

## Quick Reference

### USE mcporter + Xcode MCP For:
- ✅ `xcode.BuildProject` — Building
- ✅ `xcode.GetBuildLog` — Build errors
- ✅ `xcode.RunSomeTests` — Running specific tests
- ✅ `xcode.GetTestList` — Listing tests
- ✅ `xcode.RenderPreview` — SwiftUI previews
- ✅ `xcode.ExecuteSnippet` — Code execution
- ✅ `xcode.DocumentationSearch` — Apple docs
- ✅ `xcode.XcodeListWindows` — Get tabIdentifier
- ✅ `xcode.getDiagnostics` — SourceKit errors

### NEVER USE Xcode MCP For:
- ❌ `xcode.XcodeRead` → Use `Read` tool / `cat`
- ❌ `xcode.XcodeWrite` → Use `Write` tool
- ❌ `xcode.XcodeUpdate` → Use `Edit` tool
- ❌ `xcode.XcodeGrep` → Use `rg` or `grep`
- ❌ `xcode.XcodeGlob` → Use `find` / `glob`
- ❌ `xcode.XcodeLS` → Use `ls` command
- ❌ File operations → Use standard tools

---

## Token Efficiency Summary

| Operation | Best Choice | Token Impact |
|-----------|-------------|--------------|
| Quick syntax check | `mcporter call xcode.getDiagnostics` | 🟢 Low |
| Full build | `mcporter call xcode.BuildProject` | 🟡 Medium |
| Run specific tests | `mcporter call xcode.RunSomeTests` | 🟡 Medium |
| Run all tests | `mcporter call xcode.RunAllTests` | 🟠 High |
| Read file | `Read` tool / `cat` | 🟢 Low |
| Edit file | `Edit` tool | 🟢 Low |
| Search code | `rg` / `grep` | 🟢 Low |
| List files | `ls` / `find` | 🟢 Low |
```

**Source:** https://prompts.chat/prompts/cmms43gs50004jy042djn2324_xcode-mcp-for-pi-agent

## 中文翻译

### 标题
xcode-mcp（用于 pi 代理）

### 提示词内容

```
---
名称： xcode-mcp-for-pi-agent
描述：通过 mcporter CLI 高效使用 Xcode MCP 工具的指南。此技能应用于了解何时使用 Xcode MCP 工具与标准工具。 Xcode MCP 消耗许多令牌 - 仅用于构建、测试、模拟器、预览和 SourceKit 诊断。切勿用于文件读/写/grep 操作。每当处理 Xcode 项目、iOS/macOS 构建、SwiftUI 预览或 Apple 平台开发时，请使用此技能。
---

# Xcode MCP 使用指南

Xcode MCP 工具可通过“mcporter” CLI 访问，它将 MCP 服务器与标准命令行工具桥接起来。此技能定义何时使用 Xcode MCP 以及何时首选标准工具。

## 设置

Xcode MCP 必须在 `~/.mcporter/mcporter.json` 中配置：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Guidelines for efficient Xcode MCP tool usage via mcporter CLI. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations. Use this skill whenever working with Xcode projects, iOS/macOS builds, SwiftUI previews, or Apple platform development.

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
