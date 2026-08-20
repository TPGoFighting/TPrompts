# AWS Cloud Expert

**Description:** Designs and implements AWS cloud architectures with focus on Well-Architected Framework, cost optimization, and security. Use when: 1. Designing or reviewing AWS infrastructure architecture 2. Migrating workloads to AWS or between AWS services 3. Optimizing AWS costs (right-sizing, Reserved Instances, Savings Plans) 4. Implementing AWS security, compliance, or disaster recovery 5. Troubleshooting AWS service issues or performance problems

**Type:** SKILL
**Author:** izzetemre
**Created:** 2025-12-26T07:34:27.415Z
**Votes:** 1
**Views:** 0

**Tags:** Skill, AI Tools, DevOps, Backend, Testing

**Category:** Agent Skill

## Prompt Content

```
---
name: aws-cloud-expert
description: |
  Designs and implements AWS cloud architectures with focus on Well-Architected Framework, cost optimization, and security. Use when:
  1. Designing or reviewing AWS infrastructure architecture
  2. Migrating workloads to AWS or between AWS services
  3. Optimizing AWS costs (right-sizing, Reserved Instances, Savings Plans)
  4. Implementing AWS security, compliance, or disaster recovery
  5. Troubleshooting AWS service issues or performance problems
---

**Region**: ${region:us-east-1}
**Secondary Region**: ${secondary_region:us-west-2}
**Environment**: ${environment:production}
**VPC CIDR**: ${vpc_cidr:10.0.0.0/16}
**Instance Type**: ${instance_type:t3.medium}

# AWS Architecture Decision Framework

## Service Selection Matrix

| Workload Type | Primary Service | Alternative | Decision Factor |
|---------------|-----------------|-------------|-----------------|
| Stateless API | Lambda + API Gateway | ECS Fargate | Request duration >15min -> ECS |
| Stateful web app | ECS/EKS | EC2 Auto Scaling | Container expertise -> ECS/EKS |
| Batch processing | Step Functions + Lambda | AWS Batch | GPU/long-running -> Batch |
| Real-time streaming | Kinesis Data Streams | MSK (Kafka) | Existing Kafka -> MSK |
| Static website | S3 + CloudFront | Amplify | Full-stack -> Amplify |
| Relational DB | Aurora | RDS | High availability -> Aurora |
| Key-value store | DynamoDB | ElastiCache | Sub-ms latency -> ElastiCache |
| Data warehouse | Redshift | Athena | Ad-hoc queries -> Athena |

## Compute Decision Tree

```
Start: What's your workload pattern?
|
+-> Event-driven, <15min execution
|   +-> Lambda
|       Consider: Memory ${lambda_memory:512}MB, concurrent executions, cold starts
|
+-> Long-running containers
|   +-> Need Kubernetes?
|       +-> Yes: EKS (managed) or self-managed K8s on EC2
|       +-> No: ECS Fargate (serverless) or ECS EC2 (cost optimization)
|
+-> GPU/HPC/Custom AMI required
|   +-> EC2 with appropriate instance family
|       g4dn/p4d (ML), c6i (compute), r6i (memory), i3en (storage)
|
+-> Batch jobs, queue-based
    +-> AWS Batch with Spot instances (up to 90% savings)
```

## Networking Architecture

### VPC Design Pattern

```
${environment:production} VPC (${vpc_cidr:10.0.0.0/16})
|
+-- Public Subnets (${public_subnet_cidr:10.0.0.0/24}, 10.0.1.0/24, 10.0.2.0/24)
|   +-- ALB, NAT Gateways, Bastion (if needed)
|
+-- Private Subnets (${private_subnet_cidr:10.0.10.0/24}, 10.0.11.0/24, 10.0.12.0/24)
|   +-- Application tier (ECS, EC2, Lambda VPC)
|
+-- Data Subnets (${data_subnet_cidr:10.0.20.0/24}, 10.0.21.0/24, 10.0.22.0/24)
    +-- RDS, ElastiCache, other data stores
```

### Security Group Rules

| Tier | Inbound From | Ports |
|------|--------------|-------|
| ALB | 0.0.0.0/0 | 443 |
| App | ALB SG | ${app_port:8080} |
| Data | App SG | ${db_port:5432} |

### VPC Endpoints (Cost Optimization)

Always create for high-traffic services:
- S3 Gateway Endpoint (free)
- DynamoDB Gateway Endpoint (free)
- Interface Endpoints: ECR, Secrets Manager, SSM, CloudWatch Logs

## Cost Optimization Checklist

### Immediate Actions (Week 1)
- [ ] Enable Cost Explorer and set up budgets with alerts
- [ ] Review and terminate unused resources (Cost Explorer idle resources report)
- [ ] Right-size EC2 instances (AWS Compute Optimizer recommendations)
- [ ] Delete unattached EBS volumes and old snapshots
- [ ] Review NAT Gateway data processing charges

### Cost Estimation Quick Reference

| Resource | Monthly Cost Estimate |
|----------|----------------------|
| ${instance_type:t3.medium} (on-demand) | ~$30 |
| ${instance_type:t3.medium} (1yr RI) | ~$18 |
| Lambda (1M invocations, 1s, ${lambda_memory:512}MB) | ~$8 |
| RDS db.${instance_type:t3.medium} (Multi-AZ) | ~$100 |
| Aurora Serverless v2 (${aurora_acu:8} ACU avg) | ~$350 |
| NAT Gateway + 100GB data | ~$50 |
| S3 (1TB Standard) | ~$23 |
| CloudFront (1TB transfer) | ~$85 |

## Security Implementation

### IAM Best Practices

```
Principle: Least privilege with explicit deny

1. Use IAM roles (not users) for applications
2. Require MFA for all human users
3. Use permission boundaries for delegated admin
4. Implement SCPs at Organization level
5. Regular access reviews with IAM Access Analyzer
```

### Example IAM Policy Pattern

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowS3BucketAccess",
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::${bucket_name:my-bucket}/*",
      "Condition": {
        "StringEquals": {"aws:PrincipalTag/Environment": "${environment:production}"}
      }
    }
  ]
}
```

### Security Checklist

- [ ] Enable CloudTrail in all regions with log file validation
- [ ] Configure AWS Config rules for compliance monitoring
- [ ] Enable GuardDuty for threat detection
- [ ] Use Secrets Manager or Parameter Store for secrets (not env vars)
- [ ] Enable encryption at rest for all data stores
- [ ] Enforce TLS 1.2+ for all connections
- [ ] Implement VPC Flow Logs for network monitoring
- [ ] Use Security Hub for centralized security view

## High Availability Patterns

### Multi-AZ Architecture (${availability_target:99.99%} target)

```
Region: ${region:us-east-1}
|
+-- AZ-a                    +-- AZ-b                    +-- AZ-c
    |                           |                           |
    ALB (active)                ALB (active)                ALB (active)
    |                           |                           |
    ECS Tasks (${replicas_per_az:2})  ECS Tasks (${replicas_per_az:2})  ECS Tasks (${replicas_per_az:2})
    |                           |                           |
    Aurora Writer               Aurora Reader               Aurora Reader
```

### Multi-Region Architecture (99.999% target)

```
Primary: ${region:us-east-1}              Secondary: ${secondary_region:us-west-2}
|                               |
Route 53 (failover routing)     Route 53 (health checks)
|                               |
CloudFront                      CloudFront
|                               |
Full stack                      Full stack (passive or active)
|                               |
Aurora Global Database -------> Aurora Read Replica
     (async replication)
```

### RTO/RPO Decision Matrix

| Tier | RTO Target | RPO Target | Strategy |
|------|------------|------------|----------|
| Tier 1 (Critical) | <${rto:15 min} | <${rpo:1 min} | Multi-region active-active |
| Tier 2 (Important) | <1 hour | <15 min | Multi-region active-passive |
| Tier 3 (Standard) | <4 hours | <1 hour | Multi-AZ with cross-region backup |
| Tier 4 (Non-critical) | <24 hours | <24 hours | Single region, backup/restore |

## Monitoring and Observability

### CloudWatch Implementation

| Metric Type | Service | Key Metrics |
|-------------|---------|-------------|
| Compute | EC2/ECS | CPUUtilization, MemoryUtilization, NetworkIn/Out |
| Database | RDS/Aurora | DatabaseConnections, ReadLatency, WriteLatency |
| Serverless | Lambda | Duration, Errors, Throttles, ConcurrentExecutions |
| API | API Gateway | 4XXError, 5XXError, Latency, Count |
| Storage | S3 | BucketSizeBytes, NumberOfObjects, 4xxErrors |

### Alerting Thresholds

| Resource | Warning | Critical | Action |
|----------|---------|----------|--------|
| EC2 CPU | >${cpu_warning:70%} 5min | >${cpu_critical:90%} 5min | Scale out, investigate |
| RDS CPU | >${rds_cpu_warning:80%} 5min | >${rds_cpu_critical:95%} 5min | Scale up, query optimization |
| Lambda errors | >1% | >5% | Investigate, rollback |
| ALB 5xx | >0.1% | >1% | Investigate backend |
| DynamoDB throttle | Any | Sustained | Increase capacity |

## Verification Checklist

### Before Production Launch

- [ ] Well-Architected Review completed (all 6 pillars)
- [ ] Load testing completed with expected peak + 50% headroom
- [ ] Disaster recovery tested with documented RTO/RPO
- [ ] Security assessment passed (penetration test if required)
- [ ] Compliance controls verified (if applicable)
- [ ] Monitoring dashboards and alerts configured
- [ ] Runbooks documented for common operations
- [ ] Cost projection validated and budgets set
- [ ] Tagging strategy implemented for all resources
- [ ] Backup and restore procedures tested
```

**Source:** https://prompts.chat/prompts/cmjmk33o70005l404f9tvj19h_aws-cloud-expert

## 中文翻译

### 标题
AWS 云专家

### 提示词内容

```
---
名称：aws-云专家
描述： |
  设计和实施 AWS 云架构，重点关注架构完善的框架、成本优化和安全性。使用时：
  1. 设计或审查AWS基础设施架构
  2. 将工作负载迁移到 AWS 或在 AWS 服务之间迁移
  3. 优化 AWS 成本（调整规模、预留实例、节省计划）
  4. 实施 AWS 安全性、合规性或灾难恢复
  5. 排查 AWS 服务问题或性能问题
---

**区域**：${region:us-east-1}
**次要区域**：${secondary_region:us-west-2}
**环境**：${环境：生产}
**VPC CIDR**：${vpc_cidr:10.0.0.0/16}
**实例类型**：${instance_type:t3.medium}

# AWS 架构决策框架

## 服务选择矩阵

|工作负载类型 |主要服务|另类|决定因素|
|--------------|-----------------|------------------------|-----------------|
|无状态API | Lambda + API 网关 | ECS 法门 |请求持续时间 >15 分钟 -> ECS |
|有状态的 Web 应用程序 | ECS/EKS | EC2 自动缩放 |容器专业知识 -> ECS/EKS |
|批量处理 | Step 函数 + Lambda | AWS 批处理 | GPU/长时间运行 -> 批处理 |
|实时串流 | Kinesis 数据流 | MSK（卡夫卡）|现有 Kafka -> MSK |
|静态网站| S3 + CloudFront |放大|全栈 -> 放大 |
|关系型数据库 |极光 | RDS |高可用性 -> 极光 |
|键值存储 | DynamoDB |弹性缓存 |亚毫秒级延迟 -> ElastiCache |
|数据仓库|红移|雅典娜|即席查询 -> Athena |

## 计算决策树
```

## 使用说明
### 这个提示词能帮你做什么
这是一个**编程代码生成与审查**类的提示词。Designs and implements AWS cloud architectures with focus on Well-Architected Framework, cost optimization, and security. Use when: 1. Designing or reviewing AWS infrastructure architecture 2. Migrating workloads to AWS or between AWS services 3. Optimizing AWS costs (right-sizing, Reserved Instances, Savings Plans) 4. Implementing AWS security, compliance, or disaster recovery 5. Troubleshooting AWS service issues or performance problems

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
- `${region}`: 可自定义（默认值: us-east-1）
- `${secondary_region}`: 可自定义（默认值: us-west-2）
- `${environment}`: 可自定义（默认值: production）
- `${vpc_cidr}`: 可自定义（默认值: 10.0.0.0/16）
- `${instance_type}`: 可自定义（默认值: t3.medium）

### 使用技巧
- 如果AI生成的结果不满意，可以提供更多上下文或具体要求
- 可以要求AI用不同的风格或角度重新生成
- 对于复杂任务，可以分步骤进行，先让AI理解需求再执行
- 保留变量的默认值通常就能获得不错的效果，如需个性化可修改

### 注意事项
- 不同AI模型可能产生不同效果，可以多尝试对比
- 对于专业领域内容，建议人工审核AI输出
- 提示词中的变量可以根据实际需求自由调整
