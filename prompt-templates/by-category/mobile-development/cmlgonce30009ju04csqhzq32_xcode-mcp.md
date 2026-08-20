# xcode-mcp

**Description:** Guidelines for efficient Xcode MCP tool usage. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations.

**Type:** SKILL
**Author:** ilker
**Created:** 2026-02-10T14:14:57.915Z
**Votes:** 2
**Views:** 0

**Tags:** Agent

**Category:** Mobile Development

## Prompt Content

```
---
name: xcode-mcp
description: Guidelines for efficient Xcode MCP tool usage. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations.
---

# Xcode MCP Usage Guidelines

Xcode MCP tools consume significant tokens. This skill defines when to use Xcode MCP and when to prefer standard tools.

## Complete Xcode MCP Tools Reference

### Window & Project Management
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__XcodeListWindows` | List open Xcode windows (get tabIdentifier) | Low ✓ |

### Build Operations
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__BuildProject` | Build the Xcode project | Medium ✓ |
| `mcp__xcode__GetBuildLog` | Get build log with errors/warnings | Medium ✓ |
| `mcp__xcode__XcodeListNavigatorIssues` | List issues in Issue Navigator | Low ✓ |

### Testing
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__GetTestList` | Get available tests from test plan | Low ✓ |
| `mcp__xcode__RunAllTests` | Run all tests | Medium |
| `mcp__xcode__RunSomeTests` | Run specific tests (preferred) | Medium ✓ |

### Preview & Execution
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__RenderPreview` | Render SwiftUI Preview snapshot | Medium ✓ |
| `mcp__xcode__ExecuteSnippet` | Execute code snippet in file context | Medium ✓ |

### Diagnostics
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__XcodeRefreshCodeIssuesInFile` | Get compiler diagnostics for specific file | Low ✓ |
| `mcp__ide__getDiagnostics` | Get SourceKit diagnostics (all open files) | Low ✓ |

### Documentation
| Tool | Description | Token Cost |
|------|-------------|------------|
| `mcp__xcode__DocumentationSearch` | Search Apple Developer Documentation | Low ✓ |

### File Operations (HIGH TOKEN - NEVER USE)
| Tool | Alternative | Why |
|------|-------------|-----|
| `mcp__xcode__XcodeRead` | `Read` tool | High token consumption |
| `mcp__xcode__XcodeWrite` | `Write` tool | High token consumption |
| `mcp__xcode__XcodeUpdate` | `Edit` tool | High token consumption |
| `mcp__xcode__XcodeGrep` | `rg` / `Grep` tool | High token consumption |
| `mcp__xcode__XcodeGlob` | `Glob` tool | High token consumption |
| `mcp__xcode__XcodeLS` | `ls` command | High token consumption |
| `mcp__xcode__XcodeRM` | `rm` command | High token consumption |
| `mcp__xcode__XcodeMakeDir` | `mkdir` command | High token consumption |
| `mcp__xcode__XcodeMV` | `mv` command | High token consumption |

---

## Recommended Workflows

### 1. Code Change & Build Flow
```
1. Search code      → rg "pattern" --type swift
2. Read file        → Read tool
3. Edit file        → Edit tool
4. Syntax check     → mcp__ide__getDiagnostics
5. Build            → mcp__xcode__BuildProject
6. Check errors     → mcp__xcode__GetBuildLog (if build fails)
```

### 2. Test Writing & Running Flow
```
1. Read test file   → Read tool
2. Write/edit test  → Edit tool
3. Get test list    → mcp__xcode__GetTestList
4. Run tests        → mcp__xcode__RunSomeTests (specific tests)
5. Check results    → Review test output
```

### 3. SwiftUI Preview Flow
```
1. Edit view        → Edit tool
2. Render preview   → mcp__xcode__RenderPreview
3. Iterate          → Repeat as needed
```

### 4. Debug Flow
```
1. Check diagnostics → mcp__ide__getDiagnostics (quick syntax check)
2. Build project     → mcp__xcode__BuildProject
3. Get build log     → mcp__xcode__GetBuildLog (severity: error)
4. Fix issues        → Edit tool
5. Rebuild           → mcp__xcode__BuildProject
```

### 5. Documentation Search
```
1. Search docs       → mcp__xcode__DocumentationSearch
2. Review results    → Use information in implementation
```

---

## Fallback Commands (When MCP Unavailable)

If Xcode MCP is disconnected or unavailable, use these xcodebuild commands:

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

### USE Xcode MCP For:
- ✅ `BuildProject` - Building
- ✅ `GetBuildLog` - Build errors
- ✅ `RunSomeTests` - Running specific tests
- ✅ `GetTestList` - Listing tests
- ✅ `RenderPreview` - SwiftUI previews
- ✅ `ExecuteSnippet` - Code execution
- ✅ `DocumentationSearch` - Apple docs
- ✅ `XcodeListWindows` - Get tabIdentifier
- ✅ `mcp__ide__getDiagnostics` - SourceKit errors

### NEVER USE Xcode MCP For:
- ❌ `XcodeRead` → Use `Read` tool
- ❌ `XcodeWrite` → Use `Write` tool
- ❌ `XcodeUpdate` → Use `Edit` tool
- ❌ `XcodeGrep` → Use `rg` or `Grep` tool
- ❌ `XcodeGlob` → Use `Glob` tool
- ❌ `XcodeLS` → Use `ls` command
- ❌ File operations → Use standard tools

---

## Token Efficiency Summary

| Operation | Best Choice | Token Impact |
|-----------|-------------|--------------|
| Quick syntax check | `mcp__ide__getDiagnostics` | 🟢 Low |
| Full build | `mcp__xcode__BuildProject` | 🟡 Medium |
| Run specific tests | `mcp__xcode__RunSomeTests` | 🟡 Medium |
| Run all tests | `mcp__xcode__RunAllTests` | 🟠 High |
| Read file | `Read` tool | 🟠 High |
| Edit file | `Edit` tool | 🟠 High|
| Search code | `rg` / `Grep` | 🟢 Low |
| List files | `ls` / `Glob` | 🟢 Low |
```

**Source:** https://prompts.chat/prompts/cmlgonce30009ju04csqhzq32_xcode-mcp

## 中文翻译

### 标题
xcode-mcp

### 提示词内容

```
---
名称：xcode-mcp
描述：高效 Xcode MCP 工具使用指南。此技能应用于了解何时使用 Xcode MCP 工具与标准工具。 Xcode MCP 消耗许多令牌 - 仅用于构建、测试、模拟器、预览和 SourceKit 诊断。切勿用于文件读/写/grep 操作。
---

# Xcode MCP 使用指南

Xcode MCP 工具消耗大量令牌。此技能定义何时使用 Xcode MCP 以及何时首选标准工具。

## 完整的 Xcode MCP 工具参考

### 窗口和项目管理
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__XcodeListWindows` |列出打开的 Xcode 窗口（获取 tabIdentifier）|低 ✓ |

### 构建操作
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__BuildProject` |构建 Xcode 项目 |中等 ✓ |
| `mcp__xcode__GetBuildLog` |获取包含错误/警告的构建日志 |中等 ✓ |
| `mcp__xcode__XcodeListNavigatorIssues` |在问题导航器中列出问题 |低 ✓ |

### 测试
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__GetTestList` |从测试计划中获取可用测试 |低 ✓ |
| `mcp__xcode__RunAllTests` |运行所有测试 |中等|
| `mcp__xcode__RunSomeTests` |运行特定测试（首选）|中等 ✓ |

### 预览和执行
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__RenderPreview` |渲染 SwiftUI 预览快照 |中等 ✓ |
| `mcp__xcode__ExecuteSnippet` |在文件上下文中执行代码片段 |中等 ✓ |

### 诊断
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__XcodeRefreshCodeIssuesInFile` |获取特定文件的编译器诊断 |低 ✓ |
| `mcp__ide__getDiagnostics` |获取 SourceKit 诊断（所有打开的文件）|低 ✓ |

### 文档
|工具|描述 |代币成本 |
|------|-------------|------------|
| `mcp__xcode__DocumentationSearch` |搜索 Apple 开发者文档 |低 ✓ |

### 文件操作（高令牌 - 切勿使用）
|工具|另类|为什么 |
|------|-------------|-----|
| `mcp__xcode__XcodeRead` | ‘阅读’工具 |高代币消耗 |
| `mcp__xcode__XcodeWrite` | ‘写入’工具 |高代币消耗 |
| `mcp__xcode__XcodeUpdate` | ‘编辑’工具 |高代币消耗 |
| `mcp__xcode__XcodeGrep` | `rg` / `Grep` 工具 |高代币消耗 |
| `mcp__xcode__XcodeGlob` | `Glob` 工具 |高代币消耗 |
| `mcp__xcode__XcodeLS` | `ls` 命令 |高代币消耗 |
| `mcp__xcode__XcodeRM` | `rm` 命令 |高代币消耗 |
| `mcp__xcode__XcodeMakeDir` | `mkdir` 命令 |高代币消耗 |
| `mcp__xcode__XcodeMV` | `mv` 命令 |高代币消耗 |

---

## 推荐的工作流程

### 1. 代码更改和构建流程
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Guidelines for efficient Xcode MCP tool usage. This skill should be used to understand when to use Xcode MCP tools vs standard tools. Xcode MCP consumes many tokens - use only for build, test, simulator, preview, and SourceKit diagnostics. Never use for file read/write/grep operations.

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
