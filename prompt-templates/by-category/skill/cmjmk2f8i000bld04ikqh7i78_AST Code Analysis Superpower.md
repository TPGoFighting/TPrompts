# AST Code Analysis Superpower

**Description:** AST-based code pattern analysis using ast-grep for security, performance, and structural issues. Use when (1) reviewing code for security vulnerabilities, (2) analyzing React hook dependencies or performance patterns, (3) detecting structural anti-patterns across large codebases, (4) needing systematic pattern matching beyond manual inspection.

**Type:** SKILL
**Author:** izzetemre
**Created:** 2025-12-26T07:33:55.746Z
**Votes:** 1
**Views:** 0

**Tags:** Skill, AI Tools, JavaScript, TypeScript, React

**Category:** Agent Skill

## Prompt Content

```
---
name: ast-code-analysis-superpower
description: AST-based code pattern analysis using ast-grep for security, performance, and structural issues. Use when (1) reviewing code for security vulnerabilities, (2) analyzing React hook dependencies or performance patterns, (3) detecting structural anti-patterns across large codebases, (4) needing systematic pattern matching beyond manual inspection.
---

# AST-Grep Code Analysis

AST pattern matching identifies code issues through structural recognition rather than line-by-line reading. Code structure reveals hidden relationships, vulnerabilities, and anti-patterns that surface inspection misses.

## Configuration

- **Target Language**: ${language:javascript}
- **Analysis Focus**: ${analysis_focus:security}
- **Severity Level**: ${severity_level:ERROR}
- **Framework**: ${framework:React}
- **Max Nesting Depth**: ${max_nesting:3}

## Prerequisites

```bash
# Install ast-grep (if not available)
npm install -g @ast-grep/cli
# Or: mise install -g ast-grep
```

## Decision Tree: When to Use AST Analysis

```
Code review needed?
|
+-- Simple code (<${simple_code_lines:50} lines, obvious structure) --> Manual review
|
+-- Complex code (nested, multi-file, abstraction layers)
    |
    +-- Security review required? --> Use security patterns
    +-- Performance analysis? --> Use performance patterns
    +-- Structural quality? --> Use structure patterns
    +-- Cross-file patterns? --> Run with --include glob
```

## Pattern Categories

| Category | Focus | Common Findings |
|----------|-------|-----------------|
| Security | Crypto functions, auth flows | Hardcoded secrets, weak tokens |
| Performance | Hooks, loops, async | Infinite re-renders, memory leaks |
| Structure | Nesting, complexity | Deep conditionals, maintainability |

## Essential Patterns

### Security: Hardcoded Secrets

```yaml
# sg-rules/security/hardcoded-secrets.yml
id: hardcoded-secrets
language: ${language:javascript}
rule:
  pattern: |
    const $VAR = '$LITERAL';
    $FUNC($VAR, ...)
  meta:
    severity: ${severity_level:ERROR}
    message: "Potential hardcoded secret detected"
```

### Security: Insecure Token Generation

```yaml
# sg-rules/security/insecure-tokens.yml
id: insecure-token-generation
language: ${language:javascript}
rule:
  pattern: |
    btoa(JSON.stringify($OBJ) + '.' + $SECRET)
  meta:
    severity: ${severity_level:ERROR}
    message: "Insecure token generation using base64"
```

### Performance: ${framework:React} Hook Dependencies

```yaml
# sg-rules/performance/react-hook-deps.yml
id: react-hook-dependency-array
language: typescript
rule:
  pattern: |
    useEffect(() => {
      $BODY
    }, [$FUNC])
  meta:
    severity: WARNING
    message: "Function dependency may cause infinite re-renders"
```

### Structure: Deep Nesting

```yaml
# sg-rules/structure/deep-nesting.yml
id: deep-nesting
language: ${language:javascript}
rule:
  any:
    - pattern: |
        if ($COND1) {
          if ($COND2) {
            if ($COND3) {
              $BODY
            }
          }
        }
    - pattern: |
        for ($INIT) {
          for ($INIT2) {
            for ($INIT3) {
              $BODY
            }
          }
        }
  meta:
    severity: WARNING
    message: "Deep nesting (>${max_nesting:3} levels) - consider refactoring"
```

## Running Analysis

```bash
# Security scan
ast-grep run -r sg-rules/security/

# Performance scan on ${framework:React} files
ast-grep run -r sg-rules/performance/ --include="*.tsx,*.jsx"

# Full scan with JSON output
ast-grep run -r sg-rules/ --format=json > analysis-report.json

# Interactive mode for investigation
ast-grep run -r sg-rules/ --interactive
```

## Pattern Writing Checklist

- [ ] Pattern matches specific anti-pattern, not general code
- [ ] Uses `inside` or `has` for context constraints
- [ ] Includes `not` constraints to reduce false positives
- [ ] Separate rules per language (JS vs TS)
- [ ] Appropriate severity (${severity_level:ERROR}/WARNING/INFO)

## Common Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Too generic patterns | Many false positives | Add context constraints |
| Missing `inside` | Matches wrong locations | Scope with parent context |
| No `not` clauses | Matches valid patterns | Exclude known-good cases |
| JS patterns on TS | Type annotations break match | Create language-specific rules |

## Verification Steps

1. **Test pattern accuracy**: Run on known-vulnerable code samples
2. **Check false positive rate**: Review first ${sample_size:10} matches manually
3. **Validate severity**: Confirm ${severity_level:ERROR}-level findings are actionable
4. **Cross-file coverage**: Verify pattern runs across intended scope

## Example Output

```
$ ast-grep run -r sg-rules/
src/components/UserProfile.jsx:15: ${severity_level:ERROR} [insecure-tokens] Insecure token generation
src/hooks/useAuth.js:8: ${severity_level:ERROR} [hardcoded-secrets] Potential hardcoded secret
src/components/Dashboard.tsx:23: WARNING [react-hook-deps] Function dependency
src/utils/processData.js:45: WARNING [deep-nesting] Deep nesting detected

Found 4 issues (2 errors, 2 warnings)
```

## Project Setup

```bash
# Initialize ast-grep in project
ast-grep init

# Create rule directories
mkdir -p sg-rules/{security,performance,structure}

# Add to CI pipeline
# .github/workflows/lint.yml
# - run: ast-grep run -r sg-rules/ --format=json
```

## Custom Pattern Templates

### ${framework:React} Specific Patterns

```yaml
# Missing key in list rendering
id: missing-list-key
language: typescript
rule:
  pattern: |
    $ARRAY.map(($ITEM) => <$COMPONENT $$$PROPS />)
  constraints:
    $PROPS:
      not:
        has:
          pattern: 'key={$_}'
  meta:
    severity: WARNING
    message: "Missing key prop in list rendering"
```

### Async/Await Patterns

```yaml
# Missing error handling in async
id: unhandled-async
language: ${language:javascript}
rule:
  pattern: |
    async function $NAME($$$) {
      $$$BODY
    }
  constraints:
    $BODY:
      not:
        has:
          pattern: 'try { $$$ } catch'
  meta:
    severity: WARNING
    message: "Async function without try-catch error handling"
```

## Integration with CI/CD

```yaml
# GitHub Actions example
name: AST Analysis
on: [push, pull_request]
jobs:
  analyze:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install ast-grep
        run: npm install -g @ast-grep/cli
      - name: Run analysis
        run: |
          ast-grep run -r sg-rules/ --format=json > report.json
          if grep -q '"severity": "${severity_level:ERROR}"' report.json; then
            echo "Critical issues found!"
            exit 1
          fi
```
```

**Source:** https://prompts.chat/prompts/cmjmk2f8i000bld04ikqh7i78_ast-code-analysis-superpower

## 中文翻译

### 标题
AST 代码分析超能力

### 提示词内容

```
---
名称：ast-代码分析-超能力
描述：使用 ast-grep 进行基于 AST 的代码模式分析，以解决安全性、性能和结构问题。在以下情况下使用：(1) 检查代码是否存在安全漏洞；(2) 分析 React 钩子依赖性或性能模式；(3) 检测大型代码库中的结构反模式；(4) 需要超出手动检查的系统模式匹配。
---

# AST-Grep 代码分析

AST 模式匹配通过结构识别而不是逐行读取来识别代码问题。代码结构揭示了表面检查遗漏的隐藏关系、漏洞和反模式。

## 配置

- **目标语言**：${语言：javascript}
- **分析焦点**：${analysis_focus:security}
- **严重级别**：${severity_level:ERROR}
- **框架**：${框架：React}
- **最大嵌套深度**：${max_nesting:3}

## 先决条件
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。AST-based code pattern analysis using ast-grep for security, performance, and structural issues. Use when (1) reviewing code for security vulnerabilities, (2) analyzing React hook dependencies or performance patterns, (3) detecting structural anti-patterns across large codebases, (4) needing systematic pattern matching beyond manual inspection.

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
- `${language}`: 可自定义（默认值: javascript）
- `${analysis_focus}`: 可自定义（默认值: security）
- `${severity_level}`: 可自定义（默认值: ERROR）
- `${framework}`: 可自定义（默认值: React）
- `${max_nesting}`: 可自定义（默认值: 3）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
