# Data Lineage Agent Skill

**Description:** A skill for creating an agent to analyze data lineage and linkage across database scripts and stored procedures.

**Type:** TEXT
**Author:** ajillell_uhg
**Created:** 2026-04-29T04:31:44.288Z
**Votes:** 0
**Views:** 0

**Tags:** Agent, Data Analysis, Automation, Business, database

**Category:** Agent Skill

## Prompt Content

```
---
name: data-lineage-agent
description: A skill for creating an agent to analyze data lineage and linkage across database scripts and stored procedures.
---

# Data Lineage Agent Skill

## Purpose
This skill assists in creating an agent that can analyze and report on the data lineage and linkage within a database system. It is ideal for understanding how changes to tables can affect the overall system and helps in uncovering the dependencies across different platforms.

## Steps to Create the Agent
1. **Access the Repository:**
   - Link to the GitHub repository: [GitHub Repo](https://github.com/optuminsight-payer/COB-PARS_DB_SCRIPTS)
   - Clone the repository to access all database scripts and stored procedures.

2. **Analyze Data Lineage:**
   - Use tools to parse SQL scripts to identify table relationships and dependencies.
   - Map out the data flow from source tables to final tables.

3. **Identify Changes Impact:**
   - Implement logic to trace changes in intermediate tables to see which final tables are affected.
   - Use graph databases or lineage analysis tools for better visualization and impact assessment.

4. **Host the Agent:**
   - Choose a hosting platform (e.g., AWS, Azure) to deploy the agent for continuous analysis and reporting.

## Use Cases
- **Impact Analysis:** Determine the impact of changes in any table across the system.
- **Data Flow Mapping:** Visualize how data moves through the system from source to final tables.
- **Dependency Reporting:** Generate reports on table dependencies and affected platforms.

## Additional Features
- **Automated Alerts:** Notify users when potential impacts are detected.
- **Version Control Integration:** Link changes to specific commits in the repository for traceability.

## Example Variables
- `${repositoryUrl}`: The URL of the GitHub repository.
- `${platforms}`: List of platforms involved in the data flow.

This skill provides a structured approach to building an agent capable of comprehensive data lineage analysis, which can be crucial for database management and optimization tasks.
```

**Source:** https://prompts.chat/prompts/cmojk5r4w0001jr04qby97hzv_data-lineage-agent-skill

## 中文翻译

### 标题
数据沿袭代理技能

### 提示词内容

```
---
名称：数据沿袭代理
描述：创建代理来分析数据库脚本和存储过程之间的数据沿袭和链接的技能。
---

# 数据血统代理技能

## 目的
此技能有助于创建一个可以分析和报告数据库系统内的数据沿袭和链接的代理。它非常适合了解表的更改如何影响整个系统，并有助于发现不同平台之间的依赖关系。

## 创建代理的步骤
1. **访问存储库：**
   - GitHub 存储库链接：[GitHub Repo](https://github.com/optuminsight-payer/COB-PARS_DB_SCRIPTS)
   - 克隆存储库以访问所有数据库脚本和存储过程。

2. **分析数据沿袭：**
   - 使用工具解析SQL脚本来识别表关系和依赖关系。
   - 绘制从源表到最终表的数据流。

3. **确定变更影响：**
   - 实施逻辑来跟踪中间表中的更改，以查看哪些最终表受到影响。
   - 使用图形数据库或谱系分析工具进行更好的可视化和影响评估。

4. **托管代理：**
   - 选择托管平台（例如 AWS、Azure）来部署代理以进行持续分析和报告。

## 用例
- **影响分析：** 确定整个系统中任何表中的更改的影响。
- **数据流映射：** 可视化数据如何通过系统从源表移动到最终表。
- **依赖关系报告：** 生成有关表依赖关系和受影响平台的报告。

## 附加功能
- **自动警报：** 当检测到潜在影响时通知用户。
- **版本控制集成：** 将更改链接到存储库中的特定提交以实现可追溯性。

## 变量示例
- `${repositoryUrl}`：GitHub 存储库的 URL。
- `${platforms}`：数据流涉及的平台列表。

这项技能提供了一种结构化方法来构建能够进行全面数据沿袭分析的代理，这对于数据库管理和优化任务至关重要。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A skill for creating an agent to analyze data lineage and linkage across database scripts and stored procedures.

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
- `${repositoryUrl}`: 需要您填写
- `${platforms}`: 需要您填写

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
