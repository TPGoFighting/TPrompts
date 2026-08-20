# Multi-Audience Application Discovery & Documentation Prompt

**Description:** A prompt designed to analyze a codebase and generate comprehensive Markdown documentation tailored for executive, technical, product, and business audiences. It guides an AI to extract high-level system purpose, architecture, key components, workflows, product features, business domains, and limitations, producing an onboarding and discovery document suitable for both technical and non-technical stakeholders.

**Type:** TEXT
**Author:** valdecircarvalho
**Created:** 2026-01-06T13:33:29.902Z
**Votes:** 1
**Views:** 0

**Category:** Vibe Coding

## Prompt Content

```
# **Prompt for Code Analysis and System Documentation Generation**

You are a specialist in code analysis and system documentation. Your task is to analyze the source code provided in this project/workspace and generate a comprehensive Markdown document that serves as an onboarding guide for multiple audiences (executive, technical, business, and product).

## **Instructions**

Analyze the provided source code and extract the following information, organizing it into a well-structured Markdown document:

---

## **1. Executive-Level View: Executive Summary**

### **Application Purpose**
- What is the main objective of this system?
- What problem does it aim to solve at a high level?

### **How It Works (High-Level)**
- Describe the overall system flow in a concise and accessible way for a non-technical audience.
- What are the main steps or processes the system performs?

### **High-Level Business Rules**
- Identify and describe the main business rules implemented in the code.
- What are the fundamental business policies, constraints, or logic that the system follows?

### **Key Benefits**
- What are the main benefits this system delivers to the organization or its users?

---

## **2. Technical-Level View: Technology Overview**

### **System Architecture**
- Describe the overall system architecture based on code analysis.
- Does it follow a specific pattern (e.g., Monolithic, Microservices, etc.)?
- What are the main components or modules identified?

### **Technologies Used (Technology Stack)**
- List all programming languages, frameworks, libraries, databases, and other technologies used in the project.

### **Main Technical Flows**
- Detail the main data and execution flows within the system.
- How do the different components interact with each other?

### **Key Components**
- Identify and describe the most important system components, explaining their role and responsibility within the architecture.

### **Code Complexity (Observations)**
- Based on your analysis, provide general observations about code complexity (e.g., well-structured, modularized, areas of higher apparent complexity).

### **Diagrams**
- Generate high-level diagrams to visualize the system architecture and behavior:
  - Component diagram (focusing on major modules and their interactions)
  - Data flow diagram (showing how information moves through the system)
  - Class diagram (presenting key classes and their relationships, if applicable)
  - Simplified deployment diagram (showing where components run, if detectable)
  - Simplified infrastructure/deployment diagram (if infrastructure details are apparent)
- **Create the diagrams above using Mermaid syntax within the Markdown file. Diagrams should remain high-level and not overly detailed.**

---

## **3. Product View: Product Summary**

### **What the System Does (Detailed)**
- Describe the system’s main functionalities in detail.
- What tasks or actions can users perform?

### **Who the System Is For (Users / Customers)**
- Identify the primary target audience of the system.
- Who are the end users or customers who benefit from it?

### **Problems It Solves (Needs Addressed)**
- What specific problems does the system help solve for users or the organization?
- What needs does it address?

### **Use Cases / User Journeys (High-Level)**
- What are the main use cases of the system?
- How do users interact with the system to achieve their goals?

### **Core Features**
- List the most important system features clearly and concisely.

### **Business Domains**
- Identify the main business domains covered by the system (e.g., sales, inventory, finance).

---

## **Analysis Limitations**

- What were the main limitations encountered during the code analysis?
- Briefly describe what constrained your understanding of the code.
- Provide suggestions to reduce or eliminate these limitations.

---

## **Document Guidelines**

### **Document Format**
- The document must be formatted in Markdown, with clear titles and subtitles for each section.
- Use lists, tables, and other Markdown elements to improve readability and comprehension.

### **Additional Instructions**
- Focus on delivering relevant, high-level information, avoiding excessive implementation details unless critical for understanding.
- Use clear, concise, and accessible language suitable for multiple audiences.
- Be as specific as possible based on the code analysis.
- Generate the complete response as a **well-formatted Markdown (`.md`) document**.
- Use **clear and direct language**.
- Use **headings and subheadings** according to the sections above.

### **Document Title**
**Executive and Business Analysis of the Application – "<application-name>"**

### **Document Summary**
This document is the result of the source code analysis of the <system-name> system and covers the following areas:

- **Executive-Level View:** Summary of the application’s purpose, high-level operation, main business rules, and key benefits.
- **Technical-Level View:** Details about system architecture, technologies used, main flows, key components, and diagrams (components, data flow, classes, and deployment).
- **Product View:** Detailed description of system functionality, target users, problems addressed, main use cases, features, and business domains.
- **Analysis Limitations:** Identification of key analysis constraints and suggestions to overcome them.

The analysis was based on the available source code files.

---

## **IMPORTANT**
The analysis must consider **ALL project files**.  
Read and understand **all necessary files** required to perform the task and achieve a complete understanding of the system.

---

## **Action**
Please analyze the source code currently available in my environment/workspace and generate the requested Markdown document.

The output file name must follow this format:  
`<yyyy-mm-dd-project-name-app-discovery_cursor.md>`

```

**Source:** https://prompts.chat/prompts/cmk2mr7am0007js04m77z03jm_multi-audience-application-discovery-documentation-prompt


## 中文翻译

### 标题
Multi-Audience Application Discovery & 文档 提示词

### 提示词内容

```
【中文翻译说明】以下为英文提示词原文，请参考下方使用说明了解其用途和用法。

# **Prompt for Code Analysis and System Documentation Generation**

You are a specialist in code analysis and system documentation. Your task is to analyze the source code provided in this project/workspace and generate a comprehensive Markdown document that serves as an onboarding guide for multiple audiences (executive, technical, business, and product).

## **Instructions**

Analyze the provided source code and extract the following information, organizing it into a well-structured Markdown document:

---

## **1. Executive-Level View: Executive Summary**

### **Application Purpose**
- What is the main objective of this system?
- What problem does it aim to solve at a high level?

### **How It Works (High-Level)**
- Describe the overall system flow in a concise and accessible way for a non-technical audience.
- What are the main steps or processes the system performs?

### **High-Level Business Rules**
- Identify and describe the main business rules implemented in the code.
- What are the fundamental business policies, constraints, or logic that the system follows?

### **Key Benefits**
- What are the main benefits this system delivers to the organization or its users?

---

## **2. Technical-Level View: Technology Overview**

### **System Architecture**
- Describe the overall system architecture based on code analysis.
- Does it follow a specific pattern (e.g., Monolithic, Microservices, etc.)?
- What are the main components or modules identified?

### **Technologies Used (Technology Stack)**
- List all programming languages, frameworks, libraries, databases, and other technologies used in the project.

### **Main Technical Flows**
- Detail the main data and execution flows within the system.
- How do the different components interact with each other?

### **Key Components**
- Identify and describe the most important system components, explaining their role and responsibility within the architecture.

### **Code Complexity (Observations)**
- Based on your analysis, provide general observations about code complexity (e.g., well-structured, modularized, areas of higher apparent complexity).

### **Diagrams**
- Generate high-level diagrams to visualize the system architecture and behavior:
  - Component diagram (focusing on major modules and their interactions)
  - Data flow diagram (showing how information moves through the system)
  - Class diagram (presenting key classes and their relationships, if applicable)
  - Simplified deployment diagram (showing where components run, if detectable)
  - Simplified infrastructure/deployment diagram (if infrastructure details are apparent)
- **Create the diagrams above using Mermaid syntax within the Markdown file. Diagrams should remain high-level and not overly detailed.**

---

## **3. Product View: Product Summary**

### **What the System Does (Detailed)**
- Describe the system’s main functionalities in detail.
- What tasks or actions can users perform?

### **Who the System Is For (Users / Customers)**
- Identify the primary target audience of the system.
- Who are the end users or customers who benefit from it?

### **Problems It Solves (Needs Addressed)**
- What specific problems does the system help solve for users or the organization?
- What needs does it address?

### **Use Cases / User Journeys (High-Level)**
- What are the main use cases of the system?
- How do users interact with the system to achieve their goals?

### **Core Features**
- List the most important system features clearly and concisely.

### **Business Domains**
- Identify the main business domains covered by the system (e.g., sales, inventory, finance).

---

## **Analysis Limitations**

- What were the main limitations encountered during the code analysis?
- Briefly describe what constrained your understanding of the code.
- Provide suggestions to reduce or eliminate these limitations.

---

## **Document Guidelines**

### **Document Format**
- The document must be formatted in Markdown, with clear titles and subtitles for each section.
- Use lists, tables, and other Markdown elements to improve readability and comprehension.

### **Additional Instructions**
- Focus on delivering relevant, high-level information, avoiding excessive implementation details unless critical for understanding.
- Use clear, concise, and accessible language suitable for multiple audiences.
- Be as specific as possible based on the code analysis.
- Generate the complete response as a **well-formatted Markdown (`.md`) document**.
- Use **clear and direct language**.
- Use **headings and subheadings** according to the sections above.

### **Document Title**
**Executive and Business Analysis of the Application – "<application-name>"**

### **Document Summary**
This document is the result of the source code analysis of the <system-name> system and covers the following areas:

- **Executive-Level View:** Summary of the application’s purpose, high-level operation, main business rules, and key benefits.
- **Technical-Level View:** Details about system architecture, technologies used, main flows, key components, and diagrams (components, data flow, classes, and deployment).
- **Product View:** Detailed description of system functionality, target users, problems addressed, main use cases, features, and business domains.
- **Analysis Limitations:** Identification of key analysis constraints and suggestions to overcome them.

The analysis was based on the available source code files.

---

## **IMPORTANT**
The analysis must consider **ALL project files**.  
Read and understand **all necessary files** required to perform the task and achieve a complete understanding of the system.

---

## **Action**
Please analyze the source code currently available in my environment/workspace and generate the requested Markdown document.

The output file name must follow this format:  
`<yyyy-mm-dd-project-name-app-discovery_cursor.md>`
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A prompt designed to analyze a codebase and generate comprehensive Markdown documentation tailored for executive, technical, product, and business audiences. It guides an AI to extract high-level system purpose, architecture, key components, workflows, product features, business domains, and limitations, producing an onboarding and discovery document suitable for both technical and non-technical stakeholders.

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
