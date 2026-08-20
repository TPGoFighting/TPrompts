# Professional Full-Stack Developer for Network Mapping & Monitoring Application

**Description:** Act as a professional full-stack developer tasked with building a web application for mapping and monitoring networks using Mikrotik Netwatch API. Implement multi-user role-based management to handle devices, monitor their status, and manage user subscriptions.

**Type:** TEXT
**Author:** lalsproject
**Created:** 2025-12-30T03:06:50.257Z
**Votes:** 0
**Views:** 0

**Tags:** Web Development, Full Stack

**Category:** Web Development

## Prompt Content

```
Act as a professional full-stack developer. You are tasked with developing a web application for **Mapping & Monitoring Networks** connected to the Mikrotik Netwatch API.

Your objectives include:
- Building a role-based multi-user system to manage devices and monitor their status (UP/DOWN).
- Mapping devices on an interactive map and managing user balances for device subscriptions.

Step-by-step instructions:

1. **Project Structure Setup**
   - Define tables: users, roles, devices, device_types, ports, connections, logs, routers, and user_balances.
   - Provide a normalized schema design with foreign key relationships.

2. **Authentication & Authorization**
   - Implement a multi-user system with login & session management.
   - Roles: Admin and User.
   - Admin can manage users, roles, and routers.
   - Users can only manage devices according to their balance.

3. **User & Balance Management**
   - CRUD operations for users (Admin only).
   - Each user has a balance.
   - Subscription model: Rp.250 per device/month.
   - Automatically deduct balance monthly based on device addition date.
   - Prevent device addition if balance is insufficient.

4. **Device Type Management (CRUD)**
   - Devices can be "manageable" or "unmanageable".
   - If manageable, assign IP addresses per port.

5. **Device Management (CRUD)**
   - Add devices with port count and name.
   - Assign IP addresses to each port if the device is manageable.
   - Add devices by clicking on a map (coordinates) → pop-up form appears.

6. **Connection Management**
   - Connect devices by selecting source & destination ports.
   - Assign IP addresses to connections.
   - Move connections to other available ports.
   - Remove connections.

7. **Integration with Mikrotik Netwatch API**
   - Monitor devices based on assigned IPs.
   - Retrieve UP/DOWN status.
   - Log device status changes.

8. **Monitoring Dashboard**
   - Display devices on a map with various view styles.
   - Use different icon colors for UP/DOWN status.
   - Show device status change history logs.

9. **Remote Device Access**
   - Add a "Remote" button for each device.
   - Clicking the button automatically creates a port forwarding rule in Mikrotik (src-port specified, dst-port random).
   - Add/remove port forwarding rules.

10. **Multi Router Implementation**
   - Each user can have more than one Mikrotik router as a Netwatch server.
   - Save router assignments per user.

11. **Interactive Map**
   - Visualize all devices and connections.
   - Support various map display styles.

12. **Logging & Audit Trail**
   - Save UP/DOWN history for each device.
   - Save user action history (add/remove device, connection, port forwarding).

13. **Security & Best Practices**
   - Validate all API requests.
   - Protect the application from SQL Injection, XSS, CSRF.
   - Use secure authentication for Mikrotik API.
```

**Source:** https://prompts.chat/prompts/cmjs0ack1000vjr04kvtdi1qe_professional-full-stack-developer-for-network-mapping-monitoring-application

## 中文翻译

### 标题
专业的网络测绘和监控应用全栈开发人员

### 提示词内容

```
充当专业的全栈开发人员。您的任务是为连接到 Mikrotik Netwatch API 的 **映射和监控网络** 开发 Web 应用程序。

您的目标包括：
- 构建基于角色的多用户系统来管理设备并监控其状态（UP/DOWN）。
- 在交互式地图上映射设备并管理设备订阅的用户余额。

分步说明：

1. **项目结构设置**
   - 定义表：用户、角色、设备、device_types、端口、连接、日志、路由器和 user_balances。
   - 提供具有外键关系的规范化模式设计。

2. **认证与授权**
   - 实施具有登录和会话管理的多用户系统。
   - 角色：管理员和用户。
   - 管理员可以管理用户、角色和路由器。
   - 用户只能根据余额管理设备。

3. **用户和余额管理**
   - 用户的 CRUD 操作（仅限管理员）。
   - 每个用户都有一个余额。
   - 订阅模式：每台设备每月 250 卢比。
   - 根据设备添加日期每月自动扣除余额。
   - 如果余额不足，防止添加设备。

4. **设备类型管理 (CRUD)**
   - 设备可以是“可管理的”或“不可管理的”。
   - 如果可管理，请为每个端口分配 IP 地址。

5. **设备管理（CRUD）**
   - 添加设备及其端口数和名称。
   - 如果设备可管理，则为每个端口分配 IP 地址。
   - 通过单击地图（坐标）→ 出现弹出窗口来添加设备。

6. **连接管理**
   - 通过选择源和目标端口连接设备。
   - 为连接分配 IP 地址。
   - 将连接移至其他可用端口。
   - 删除连接。

7. **与 Mikrotik Netwatch API 集成**
   - 根据分配的 IP 监控设备。
   - 检索 UP/DOWN 状态。
   - 记录设备状态变化。

8. **监控仪表板**
   - 在地图上以各种视图样式显示设备。
   - 使用不同的图标颜色表示向上/向下状态。
   - 显示设备状态更改历史日志。

9. **远程设备访问**
   - 为每个设备添加“远程”按钮。
   - 单击该按钮会自动在 Mikrotik 中创建端口转发规则（源端口指定，目标端口随机）。
   - 添加/删除端口转发规则。

10. **多路由器实施**
   - 每个用户可以拥有多个 Mikrotik 路由器作为 Netwatch 服务器。
   - 保存每个用户的路由器分配。

11. **互动地图**
   - 可视化所有设备和连接。
   - 支持多种地图显示样式。

12. **记录和审计跟踪**
   - 保存每个设备的向上/向下历史记录。
   - 保存用户操作历史记录（添加/删除设备、连接、端口转发）。

13. **安全与最佳实践**
   - 验证所有 API 请求。
   - 保护应用程序免受 SQL 注入、XSS、CSRF 攻击。
   - 对 Mikrotik API 使用安全身份验证。
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Act as a professional full-stack developer tasked with building a web application for mapping and monitoring networks using Mikrotik Netwatch API. Implement multi-user role-based management to handle devices, monitor their status, and manage user subscriptions.

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
