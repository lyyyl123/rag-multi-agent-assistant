# RAG Multi-Agent Assistant 开发规范

## 项目定位

这是一个应届生 AI Agent 作品集项目，代码要清晰、可解释、适合面试讲解。

## 配置管理

- 不要硬编码 API Key
- 所有配置从 .env 读取
- 使用 pydantic-settings 管理配置

## 架构原则

- 不要过早微服务化
- 第一版采用单体 FastAPI 后端
- LangGraph 节点要保持简单，每个节点职责单一

## 技术选型

### PostgreSQL
- 用于 LangGraph checkpointer
- 用于长期记忆存储
- 用于聊天记录持久化
- 用于文档元数据存储

### Redis
- 用于短期缓存
- 用于会话临时状态
- 用于速率限制

### Chroma
- 第一版向量数据库
- 存储文档 Embedding
- 支持相似度检索

## 开发流程

- 每完成一个阶段都要更新 README
- 每完成一个阶段都要给出运行和测试命令
- 代码提交前确保后端和前端都能正常启动

## 代码风格

- Python 使用 type hints
- 函数和类要有 docstring
- 异步函数使用 async/await
- 错误处理要清晰

## 前端规范

- 使用 Vue 3 Composition API
- 使用 Element Plus 组件库
- API 调用统一放在 src/api/
- 页面组件放在 src/views/
