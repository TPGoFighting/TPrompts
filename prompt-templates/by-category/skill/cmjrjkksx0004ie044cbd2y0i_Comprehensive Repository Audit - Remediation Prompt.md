# Comprehensive Repository Audit & Remediation Prompt

**Type:** TEXT
**Author:** ykarateke
**Created:** 2025-12-29T19:18:54.033Z
**Votes:** 0
**Views:** 0

**Category:** Agent Skill

## Prompt Content

```
## Objective
Conduct a thorough analysis of the entire repository to identify, prioritize, fix, and document ALL verifiable bugs, security vulnerabilities, and critical issues across any programming language, framework, or technology stack.

## Phase 1: Initial Repository Assessment

### 1.1 Architecture Mapping
- Map complete project structure (src/, lib/, tests/, docs/, config/, scripts/, etc.)
- Identify technology stack and dependencies (package.json, requirements.txt, go.mod, pom.xml, Gemfile, etc.)
- Document main entry points, critical paths, and system boundaries
- Analyze build configurations and CI/CD pipelines
- Review existing documentation (README, API docs, architecture diagrams)

### 1.2 Development Environment Analysis
- Identify testing frameworks (Jest, pytest, PHPUnit, Go test, JUnit, RSpec, etc.)
- Review linting/formatting configurations (ESLint, Prettier, Black, RuboCop, etc.)
- Check for existing issue tracking (GitHub Issues, TODO/FIXME/HACK/XXX comments)
- Analyze commit history for recent problematic areas
- Review existing test coverage reports if available

## Phase 2: Systematic Bug Discovery

### 2.1 Bug Categories to Identify
**Critical Bugs:**
- Security vulnerabilities (SQL injection, XSS, CSRF, auth bypass, etc.)
- Data corruption or loss risks
- System crashes or deadlocks
- Memory leaks or resource exhaustion

**Functional Bugs:**
- Logic errors (incorrect conditions, wrong calculations, off-by-one errors)
- State management issues (race conditions, inconsistent state, improper mutations)
- Incorrect API contracts or data mappings
- Missing or incorrect validations
- Broken business rules or workflows

**Integration Bugs:**
- Incorrect external API usage
- Database query errors or inefficiencies
- Message queue handling issues
- File system operation problems
- Network communication errors

**Edge Cases & Error Handling:**
- Null/undefined/nil handling
- Empty collections or zero-value edge cases
- Boundary conditions and limit violations
- Missing error propagation or swallowing exceptions
- Timeout and retry logic issues

**Code Quality Issues:**
- Type mismatches or unsafe casts
- Deprecated API usage
- Dead code or unreachable branches
- Circular dependencies
- Performance bottlenecks (N+1 queries, inefficient algorithms)

### 2.2 Discovery Methods
- Static code analysis using language-specific tools
- Pattern matching for common anti-patterns
- Dependency vulnerability scanning
- Code path analysis for unreachable or untested code
- Configuration validation
- Cross-reference documentation with implementation

## Phase 3: Bug Documentation & Prioritization

### 3.1 Bug Report Template
For each identified bug, document:
```
BUG-ID: [Sequential identifier]
Severity: [CRITICAL | HIGH | MEDIUM | LOW]
Category: [Security | Functional | Performance | Integration | Code Quality]
File(s): [Complete file path(s) and line numbers]
Component: [Module/Service/Feature affected]

Description:
- Current behavior (what's wrong)
- Expected behavior (what should happen)
- Root cause analysis

Impact Assessment:
- User impact (UX degradation, data loss, security exposure)
- System impact (performance, stability, scalability)
- Business impact (compliance, revenue, reputation)

Reproduction Steps:
1. [Step-by-step instructions]
2. [Include test data/conditions if needed]
3. [Expected vs actual results]

Verification Method:
- [Code snippet or test that demonstrates the bug]
- [Metrics or logs showing the issue]

Dependencies:
- Related bugs: [List of related BUG-IDs]
- Blocking issues: [What needs to be fixed first]
```

### 3.2 Prioritization Matrix
Rank bugs using:
- **Severity**: Critical > High > Medium > Low
- **User Impact**: Number of affected users/features
- **Fix Complexity**: Simple < Medium < Complex
- **Risk of Regression**: Low < Medium < High

## Phase 4: Fix Implementation

### 4.1 Fix Strategy
**For each bug:**
1. Create isolated fix branch (if using version control)
2. Write failing test FIRST (TDD approach)
3. Implement minimal, focused fix
4. Verify test passes
5. Run regression tests
6. Update documentation if needed

### 4.2 Fix Guidelines
- **Minimal Change Principle**: Make the smallest change that correctly fixes the issue
- **No Scope Creep**: Avoid unrelated refactoring or improvements
- **Preserve Backwards Compatibility**: Unless the bug itself is a breaking API
- **Follow Project Standards**: Use existing code style and patterns
- **Add Defensive Programming**: Prevent similar bugs in the future

### 4.3 Code Review Checklist
- [ ] Fix addresses the root cause, not just symptoms
- [ ] All edge cases are handled
- [ ] Error messages are clear and actionable
- [ ] Performance impact is acceptable
- [ ] Security implications considered
- [ ] No new warnings or linting errors introduced

## Phase 5: Testing & Validation

### 5.1 Test Requirements
**For EVERY fixed bug, provide:**
1. **Unit Test**: Isolated test for the specific fix
2. **Integration Test**: If bug involves multiple components
3. **Regression Test**: Ensure fix doesn't break existing functionality
4. **Edge Case Tests**: Cover related boundary conditions

### 5.2 Test Structure
```[language-specific]
describe('BUG-[ID]: [Bug description]', () => {
  test('should fail with original bug', () => {
    // This test would fail before the fix
    // Demonstrates the bug
  });
  
  test('should pass after fix', () => {
    // This test passes after the fix
    // Verifies correct behavior
  });
  
  test('should handle edge cases', () => {
    // Additional edge case coverage
  });
});
```

### 5.3 Validation Steps
1. Run full test suite: `[npm test | pytest | go test ./... | mvn test | etc.]`
2. Check code coverage changes
3. Run static analysis tools
4. Verify performance benchmarks (if applicable)
5. Test in different environments (if possible)

## Phase 6: Documentation & Reporting

### 6.1 Fix Documentation
For each fixed bug:
- Update inline code comments explaining the fix
- Add/update API documentation if behavior changed
- Create/update troubleshooting guides
- Document any workarounds for unfixed issues

### 6.2 Executive Summary Report
```markdown
# Bug Fix Report - [Repository Name]
Date: [YYYY-MM-DD]
Analyzer: [Tool/Person Name]

## Overview
- Total Bugs Found: [X]
- Total Bugs Fixed: [Y]
- Unfixed/Deferred: [Z]
- Test Coverage Change: [Before]% → [After]%

## Critical Findings
[List top 3-5 most critical bugs found and fixed]

## Fix Summary by Category
- Security: [X bugs fixed]
- Functional: [Y bugs fixed]
- Performance: [Z bugs fixed]
- Integration: [W bugs fixed]
- Code Quality: [V bugs fixed]

## Detailed Fix List
[Organized table with columns: BUG-ID | File | Description | Status | Test Added]

## Risk Assessment
- Remaining High-Priority Issues: [List]
- Recommended Next Steps: [Actions]
- Technical Debt Identified: [Summary]

## Testing Results
- Test Command: [exact command used]
- Tests Passed: [X/Y]
- New Tests Added: [Count]
- Coverage Impact: [Details]
```

### 6.3 Deliverables Checklist
- [ ] All bugs documented in standard format
- [ ] Fixes implemented and tested
- [ ] Test suite updated and passing
- [ ] Documentation updated
- [ ] Code review completed
- [ ] Performance impact assessed
- [ ] Security review conducted (for security-related fixes)
- [ ] Deployment notes prepared

## Phase 7: Continuous Improvement

### 7.1 Pattern Analysis
- Identify common bug patterns
- Suggest preventive measures
- Recommend tooling improvements
- Propose architectural changes to prevent similar issues

### 7.2 Monitoring Recommendations
- Suggest metrics to track
- Recommend alerting rules
- Propose logging improvements
- Identify areas needing better test coverage

## Constraints & Best Practices

1. **Never compromise security** for simplicity
2. **Maintain audit trail** of all changes
3. **Follow semantic versioning** if fixes change API
4. **Respect rate limits** when testing external services
5. **Use feature flags** for high-risk fixes (if applicable)
6. **Consider rollback strategy** for each fix
7. **Document assumptions** made during analysis

## Output Format
Provide results in both:
- Markdown for human readability
- JSON/YAML for automated processing
- CSV for bug tracking systems import

## Special Considerations
- For monorepos: Analyze each package separately
- For microservices: Consider inter-service dependencies
- For legacy code: Balance fix risk vs benefit
- For third-party dependencies: Report upstream if needed
```

**Source:** https://prompts.chat/prompts/cmjrjkksx0004ie044cbd2y0i_comprehensive-repository-audit-remediation-prompt

## 中文翻译

### 标题
全面的存储库审核和修复提示

### 提示词内容

```
## 目标
对整个存储库进行彻底分析，以识别、确定优先级、修复和记录任何编程语言、框架或技术堆栈中的所有可验证错误、安全漏洞和关键问题。

## 第 1 阶段：初始存储库评估

### 1.1 架构映射
- 映射完整的项目结构（src/、lib/、tests/、docs/、config/、scripts/等）
- 识别技术堆栈和依赖项（package.json、requirements.txt、go.mod、pom.xml、Gemfile 等）
- 记录主要入口点、关键路径和系统边界
- 分析构建配置和 CI/CD 管道
- 查看现有文档（自述文件、API 文档、架构图）

### 1.2 开发环境分析
- 识别测试框架（Jest、pytest、PHPUnit、Go test、JUnit、RSpec 等）
- 检查 linting/格式化配置（ESLint、Prettier、Black、RuboCop 等）
- 检查现有问题跟踪（GitHub 问题、TODO/FIXME/HACK/XXX 评论）
- 分析最近有问题的区域的提交历史记录
- 审查现有的测试覆盖率报告（如果有）

## 第 2 阶段：系统性错误发现

### 2.1 要识别的错误类别
**严重错误：**
- 安全漏洞（SQL注入、XSS、CSRF、身份验证绕过等）
- 数据损坏或丢失风险
- 系统崩溃或死锁
- 内存泄漏或资源耗尽

**功能错误：**
- 逻辑错误（不正确的条件、错误的计算、相差一错误）
- 状态管理问题（竞争条件、状态不一致、突变不当）
- 不正确的API合约或数据映射
- 验证缺失或不正确
- 破坏业务规则或工作流程

**集成错误：**
- 外部API使用不正确
- 数据库查询错误或效率低下
- 消息队列处理问题
- 文件系统操作问题
- 网络通讯错误

**边缘情况和错误处理：**
- 空/未定义/零处理
- 空集合或零值边缘情况
- 边界条件和限制违规
- 丢失错误传播或吞噬异常
- 超时和重试逻辑问题

**代码质量问题：**
- 类型不匹配或不安全的强制转换
- 已弃用的 API 使用
- 死代码或无法访问的分支
- 循环依赖
- 性能瓶颈（N+1查询、低效算法）

### 2.2 发现方法
- 使用特定于语言的工具进行静态代码分析
- 常见反模式的模式匹配
- 依赖漏洞扫描
- 对无法访问或未经测试的代码进行代码路径分析
- 配置验证
- 交叉参考文档与实施

## 第 3 阶段：错误文档和优先级排序

### 3.1 错误报告模板
对于每个已识别的错误，记录：
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。它可以帮助你完成与Comprehensive Repository Audit & Remediation Prompt相关的任务。

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
