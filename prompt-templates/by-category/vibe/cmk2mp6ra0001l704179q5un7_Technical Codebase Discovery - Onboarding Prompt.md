# Technical Codebase Discovery & Onboarding Prompt

**Description:** A prompt designed to guide a deep technical analysis of a code repository to accelerate developer onboarding. It instructs an AI to analyze the entire codebase and generate a structured Markdown document covering architecture, technology stack, key components, execution and data flows, integrations, testing, security, and build/deployment, serving as a technical reference guide.

**Type:** TEXT
**Author:** valdecircarvalho
**Created:** 2026-01-06T13:31:55.894Z
**Votes:** 3
**Views:** 0

**Category:** Vibe Coding

## Prompt Content

```
**Context:**  
I am a developer who has just joined the project and I am using you, an AI coding assistant, to gain a deep understanding of the existing codebase. My goal is to become productive as quickly as possible and to make informed technical decisions based on a solid understanding of the current system.

**Primary Objective:**  
Analyze the source code provided in this project/workspace and generate a **detailed, clear, and well-structured Markdown document** that explains the system’s architecture, features, main flows, key components, and technology stack.  
This document should serve as a **technical onboarding guide**.  
Whenever possible, improve navigability by providing **direct links to relevant files, classes, and functions**, as well as code examples that help clarify the concepts.

---

## **Detailed Instructions — Please address the following points:**

### 1. **README / Instruction Files Summary**
- Look for files such as `README.md`, `LEIAME.md`, `CONTRIBUTING.md`, or similar documentation.
- Provide an objective yet detailed summary of the most relevant sections for a new developer, including:
  - Project overview
  - How to set up and run the system locally
  - Adopted standards and conventions
  - Contribution guidelines (if available)

---

### 2. **Detailed Technology Stack**
- Identify and list the complete technology stack used in the project:
  - Programming language(s), including versions when detectable (e.g., from `package.json`, `pom.xml`, `.tool-versions`, `requirements.txt`, `build.gradle`, etc.).
  - Main frameworks (backend, frontend, etc. — e.g., Spring Boot, .NET, React, Angular, Vue, Django, Rails).
  - Database(s):
    - Type (SQL / NoSQL)
    - Name (PostgreSQL, MongoDB, etc.)
  - Core architecture style (e.g., Monolith, Microservices, Serverless, MVC, MVVM, Clean Architecture).
  - Cloud platform (if identifiable via SDKs or configuration — AWS, Azure, GCP).
  - Build tools and package managers (Maven, Gradle, npm, yarn, pip).
  - Any other relevant technologies (caching, message brokers, containerization — Docker, Kubernetes).
- **Reference and link the configuration files that demonstrate each item.**

---

### 3. **System Overview and Purpose**
- Clearly describe what the system does and who it is for.
- What problems does it solve?
- List the core functionalities.
- If possible, relate the system to the business domains involved.
- Provide a high-level description of the main features.

---

### 4. **Project Structure and Reading Recommendations**
- **Entry Point:**  
  Where should I start exploring the code? Identify the main entry points (e.g., `main.go`, `index.js`, `Program.cs`, `app.py`, `Application.java`).  
  **Provide direct links to these files.**
- **General Organization:**  
  Explain the overall folder and file structure. Highlight important conventions.  
  **Use real folder and file name examples.**
- **Configuration:**  
  Are there main configuration files? (e.g., `config.yaml`, `.env`, `appsettings.json`)  
  Which configurations are critical?  
  **Provide links.**
- **Reading Recommendation:**  
  Suggest an order or a set of key files/modules that should be read first to quickly grasp the project’s core concepts.

---

### 5. **Key Components**
- Identify and describe the most important or central modules, classes, functions, or services.
- Explain the responsibilities of each component.
- Describe their responsibilities and interdependencies.
- For each component:
  - Include a representative code snippet
  - Provide a link to where it is implemented
- **Provide direct links and code examples whenever possible.**

---

### 6. **Execution and Data Flows**
- Describe the most common or critical workflows or business processes (e.g., order processing, user authentication).
- Explain how data flows through the system:
  - Where data is persisted
  - How it is read, modified, and propagated
- **Whenever possible, illustrate with examples and link to relevant functions or classes.**

#### 6.1 **Database Schema Overview (if applicable)**
- For data-intensive applications:
  - Identify the main entities/tables/collections
  - Describe their primary relationships
  - Base this on ORM models, migrations, or schema files if available

---

### 7. **Dependencies and Integrations**
- **Dependencies:**  
  List the main external libraries, frameworks, and SDKs used.  
  Briefly explain the role of each one.  
  **Provide links to where they are configured or most commonly used.**
- **Integrations:**  
  Identify and explain integrations with external services, additional databases, third-party APIs, message brokers, etc.  
  How does communication occur?  
  **Point to the modules/classes responsible and include links.**

#### 7.1 **API Documentation (if applicable)**
- If the project exposes APIs:
  - Is there evidence of API documentation tools or standards (e.g., Swagger/OpenAPI, Javadoc, endpoint-specific docstrings)?
  - Where can this documentation be found or how can it be generated?

---

### 8. **Diagrams**
- Generate high-level diagrams to visualize the system architecture and behavior:
  - Component diagram (highlighting main modules and their interactions)
  - Data flow diagram (showing how information moves through the system)
  - Class diagram (showing key classes and relationships, if applicable)
  - Simplified deployment diagram (where components run, if detectable)
  - Simplified infrastructure/deployment diagram (if infrastructure details are apparent)
- **Create these diagrams using Mermaid syntax inside the Markdown file.**
- Diagrams should be **high-level**; extensive detailing is not required.

---

### 9. **Testing**
- Are there automated tests?
  - Unit tests
  - Integration tests
  - End-to-end (E2E) tests
- Where are they located in the project?
- Which testing framework(s) are used?
- How are tests typically executed?
- How can tests be run locally?
- Is there any CI/CD strategy involving tests?

---

### 10. **Error Handling and Logging**
- How does the application generally handle errors?
  - Is there a standard pattern (e.g., global middleware, custom exceptions)?
- Which logging library is used?
- Is there a standard logging format?
- Is there visible integration with monitoring tools (e.g., Datadog, Sentry)?

---

### 11. **Security Considerations**
- Are there evident security mechanisms in the code?
  - Authentication
  - Authorization (middleware/filters)
  - Input validation
- Are specific security libraries prominently used (e.g., Spring Security, Passport.js, JWT libraries)?
- Are there notable security practices?
  - Secrets management
  - Protection against common attacks

---

### 12. **Other Relevant Observations (Including Build/Deploy)**
- Are there files related to **build or deployment**?
  - `Dockerfile`
  - `docker-compose.yml`
  - Build/deploy scripts
  - CI/CD configuration files (e.g., `.github/workflows/`, `.gitlab-ci.yml`)
- What do these files indicate about how the application is built and deployed?
- Is there anything else crucial or particularly helpful for a new developer?
  - Known technical debt mentioned in comments
  - Unusual design patterns
  - Important coding conventions
  - Performance notes

---

## **Final Output Format**
- Generate the complete response as a **well-formatted Markdown (`.md`) document**.
- Use **clear and direct language**.
- Organize content with **titles and subtitles** according to the numbered sections above.
- **Include relevant code snippets** (short and representative).
- **Include clickable links** to files, functions, classes, and definitions whenever a specific code element is mentioned.
- Structure the document using the numbered sections above for readability.

**Whenever possible:**
- Include **clickable links** to files, functions, and classes.
- Show **short, representative code snippets**.
- Use **bullet points or tables** for lists.

---

### **IMPORTANT**
The analysis must consider **ALL files in the project**.  
Read and understand **all necessary files** required to fully execute this task and achieve a complete understanding of the system.

---

### **Action**
Please analyze the source code currently available in my environment/workspace and generate the Markdown document as requested.

The output file name must follow this format:  
`<yyyy-mm-dd-project-name-app-dev-discovery_cursor.md>`

```

**Source:** https://prompts.chat/prompts/cmk2mp6ra0001l704179q5un7_technical-codebase-discovery-onboarding-prompt


## 中文翻译

### 标题
Technical Codebase Discovery & Onboarding 提示词

### 提示词内容

```
【中文翻译说明】以下为英文提示词原文，请参考下方使用说明了解其用途和用法。

**Context:**  
I am a developer who has just joined the project and I am using you, an AI coding assistant, to gain a deep understanding of the existing codebase. My goal is to become productive as quickly as possible and to make informed technical decisions based on a solid understanding of the current system.

**Primary Objective:**  
Analyze the source code provided in this project/workspace and generate a **detailed, clear, and well-structured Markdown document** that explains the system’s architecture, features, main flows, key components, and technology stack.  
This document should serve as a **technical onboarding guide**.  
Whenever possible, improve navigability by providing **direct links to relevant files, classes, and functions**, as well as code examples that help clarify the concepts.

---

## **Detailed Instructions — Please address the following points:**

### 1. **README / Instruction Files Summary**
- Look for files such as `README.md`, `LEIAME.md`, `CONTRIBUTING.md`, or similar documentation.
- Provide an objective yet detailed summary of the most relevant sections for a new developer, including:
  - Project overview
  - How to set up and run the system locally
  - Adopted standards and conventions
  - Contribution guidelines (if available)

---

### 2. **Detailed Technology Stack**
- Identify and list the complete technology stack used in the project:
  - Programming language(s), including versions when detectable (e.g., from `package.json`, `pom.xml`, `.tool-versions`, `requirements.txt`, `build.gradle`, etc.).
  - Main frameworks (backend, frontend, etc. — e.g., Spring Boot, .NET, React, Angular, Vue, Django, Rails).
  - Database(s):
    - Type (SQL / NoSQL)
    - Name (PostgreSQL, MongoDB, etc.)
  - Core architecture style (e.g., Monolith, Microservices, Serverless, MVC, MVVM, Clean Architecture).
  - Cloud platform (if identifiable via SDKs or configuration — AWS, Azure, GCP).
  - Build tools and package managers (Maven, Gradle, npm, yarn, pip).
  - Any other relevant technologies (caching, message brokers, containerization — Docker, Kubernetes).
- **Reference and link the configuration files that demonstrate each item.**

---

### 3. **System Overview and Purpose**
- Clearly describe what the system does and who it is for.
- What problems does it solve?
- List the core functionalities.
- If possible, relate the system to the business domains involved.
- Provide a high-level description of the main features.

---

### 4. **Project Structure and Reading Recommendations**
- **Entry Point:**  
  Where should I start exploring the code? Identify the main entry points (e.g., `main.go`, `index.js`, `Program.cs`, `app.py`, `Application.java`).  
  **Provide direct links to these files.**
- **General Organization:**  
  Explain the overall folder and file structure. Highlight important conventions.  
  **Use real folder and file name examples.**
- **Configuration:**  
  Are there main configuration files? (e.g., `config.yaml`, `.env`, `appsettings.json`)  
  Which configurations are critical?  
  **Provide links.**
- **Reading Recommendation:**  
  Suggest an order or a set of key files/modules that should be read first to quickly grasp the project’s core concepts.

---

### 5. **Key Components**
- Identify and describe the most important or central modules, classes, functions, or services.
- Explain the responsibilities of each component.
- Describe their responsibilities and interdependencies.
- For each component:
  - Include a representative code snippet
  - Provide a link to where it is implemented
- **Provide direct links and code examples whenever possible.**

---

### 6. **Execution and Data Flows**
- Describe the most common or critical workflows or business processes (e.g., order processing, user authentication).
- Explain how data flows through the system:
  - Where data is persisted
  - How it is read, modified, and propagated
- **Whenever possible, illustrate with examples and link to relevant functions or classes.**

#### 6.1 **Database Schema Overview (if applicable)**
- For data-intensive applications:
  - Identify the main entities/tables/collections
  - Describe their primary relationships
  - Base this on ORM models, migrations, or schema files if available

---

### 7. **Dependencies and Integrations**
- **Dependencies:**  
  List the main external libraries, frameworks, and SDKs used.  
  Briefly explain the role of each one.  
  **Provide links to where they are configured or most commonly used.**
- **Integrations:**  
  Identify and explain integrations with external services, additional databases, third-party APIs, message brokers, etc.  
  How does communication occur?  
  **Point to the modules/classes responsible and include links.**

#### 7.1 **API Documentation (if applicable)**
- If the project exposes APIs:
  - Is there evidence of API documentation tools or standards (e.g., Swagger/OpenAPI, Javadoc, endpoint-specific docstrings)?
  - Where can this documentation be found or how can it be generated?

---

### 8. **Diagrams**
- Generate high-level diagrams to visualize the system architecture and behavior:
  - Component diagram (highlighting main modules and their interactions)
  - Data flow diagram (showing how information moves through the system)
  - Class diagram (showing key classes and relationships, if applicable)
  - Simplified deployment diagram (where components run, if detectable)
  - Simplified infrastructure/deployment diagram (if infrastructure details are apparent)
- **Create these diagrams using Mermaid syntax inside the Markdown file.**
- Diagrams should be **high-level**; extensive detailing is not required.

---

### 9. **Testing**
- Are there automated tests?
  - Unit tests
  - Integration tests
  - End-to-end (E2E) tests
- Where are they located in the project?
- Which testing framework(s) are used?
- How are tests typically executed?
- How can tests be run locally?
- Is there any CI/CD strategy involving tests?

---

### 10. **Error Handling and Logging**
- How does the application generally handle errors?
  - Is there a standard pattern (e.g., global middleware, custom exceptions)?
- Which logging library is used?
- Is there a standard logging format?
- Is there visible integration with monitoring tools (e.g., Datadog, Sentry)?

---

### 11. **Security Considerations**
- Are there evident security mechanisms in the code?
  - Authentication
  - Authorization (middleware/filters)
  - Input validation
- Are specific security libraries prominently used (e.g., Spring Security, Passport.js, JWT libraries)?
- Are there notable security practices?
  - Secrets management
  - Protection against common attacks

---

### 12. **Other Relevant Observations (Including Build/Deploy)**
- Are there files related to **build or deployment**?
  - `Dockerfile`
  - `docker-compose.yml`
  - Build/deploy scripts
  - CI/CD configuration files (e.g., `.github/workflows/`, `.gitlab-ci.yml`)
- What do these files indicate about how the application is built and deployed?
- Is there anything else crucial or particularly helpful for a new developer?
  - Known technical debt mentioned in comments
  - Unusual design patterns
  - Important coding conventions
  - Performance notes

---

## **Final Output Format**
- Generate the complete response as a **well-formatted Markdown (`.md`) document**.
- Use **clear and direct language**.
- Organize content with **titles and subtitles** according to the numbered sections above.
- **Include relevant code snippets** (short and representative).
- **Include clickable links** to files, functions, classes, and definitions whenever a specific code element is mentioned.
- Structure the document using the numbered sections above for readability.

**Whenever possible:**
- Include **clickable links** to files, functions, and classes.
- Show **short, representative code snippets**.
- Use **bullet points or tables** for lists.

---

### **IMPORTANT**
The analysis must consider **ALL files in the project**.  
Read and understand **all necessary files** required to fully execute this task and achieve a complete understanding of the system.

---

### **Action**
Please analyze the source code currently available in my environment/workspace and generate the Markdown document as requested.

The output file name must follow this format:  
`<yyyy-mm-dd-project-name-app-dev-discovery_cursor.md>`
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。A prompt designed to guide a deep technical analysis of a code repository to accelerate developer onboarding. It instructs an AI to analyze the entire codebase and generate a structured Markdown document covering architecture, technology stack, key components, execution and data flows, integrations, testing, security, and build/deployment, serving as a technical reference guide.

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
