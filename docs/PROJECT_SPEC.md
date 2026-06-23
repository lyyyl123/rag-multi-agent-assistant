# 项目规格说明

## 项目目标

开发一个「基于 LangGraph 的 RAG 多智能体知识库问答系统」，作为应届生求职 AI Agent 应用开发 / 大模型应用开发岗位的作品集项目。

## 核心能力

1. **文档管理**
   - 支持用户上传 PDF / TXT / Markdown 文档
   - 文档解析、文本切分、Embedding、向量检索

2. **RAG 问答**
   - 基于知识库的 RAG 问答
   - 支持多轮对话
   - 上下文记忆管理

3. **多智能体编排**
   - 使用 LangGraph 实现多智能体编排
   - 支持 Agent 执行过程可视化
   - 支持 Agent 日志记录

4. **记忆系统**
   - PostgreSQL 作为核心持久化数据库
   - LangGraph checkpointer 能力
   - 长期记忆存储
   - Redis 短期缓存和会话临时状态

## 技术选型

### 后端技术栈

| 技术 | 用途 |
|------|------|
| Python 3.11+ | 主要编程语言 |
| FastAPI | Web 框架 |
| LangChain | LLM 应用开发框架 |
| LangGraph | 多智能体编排框架 |
| SQLAlchemy | ORM 框架 |
| PostgreSQL | 关系型数据库 |
| Redis | 缓存和会话存储 |
| Chroma | 向量数据库 |
| Pydantic | 数据验证 |

### 前端技术栈

| 技术 | 用途 |
|------|------|
| Vue 3 | 前端框架 |
| Vite | 构建工具 |
| Element Plus | UI 组件库 |
| Axios | HTTP 客户端 |
| Vue Router | 路由管理 |

### 基础设施

| 技术 | 用途 |
|------|------|
| Docker Compose | 容器编排 |
| PostgreSQL 16 | 数据库服务 |
| Redis 7 | 缓存服务 |

## 核心模块

### 1. 文档处理模块
- 文档加载器 (PDF/TXT/Markdown)
- 文本切分器
- Embedding 生成器
- 向量存储管理

### 2. RAG 检索模块
- 向量相似度检索
- 上下文构建
- 提示词模板

### 3. 多智能体模块
- Router Agent: 路由决策
- Knowledge Agent: 知识检索
- Review Agent: 质量审查
- Finalize Agent: 结果整合

### 4. 记忆管理模块
- 短期记忆 (Redis)
- 长期记忆 (PostgreSQL)
- 会话状态管理

### 5. API 服务模块
- 文档上传接口
- 聊天接口
- 会话管理接口
- Agent 日志接口

## 最终功能

### 用户功能
- 文档上传和管理
- 智能问答对话
- 历史记录查看
- Agent 执行过程查看

### 系统功能
- 多智能体协同工作
- 知识库自动构建
- 记忆系统管理
- 性能监控和日志

## 性能指标

- 单次问答响应时间: < 5 秒
- 文档处理速度: 10 页/秒
- 并发支持: 10 用户
- 知识库容量: 1000 文档

## 扩展性

### 可扩展模块
- 向量数据库: Chroma -> Milvus/Qdrant
- 缓存系统: Redis -> 分布式缓存
- 模型服务: OpenAI -> 私有化部署
- 搜索能力: 增加 BM25 + Rerank

### 预留接口
- MCP 服务接口
- 多后端服务拆分
- 复杂权限系统
- 写作子图
