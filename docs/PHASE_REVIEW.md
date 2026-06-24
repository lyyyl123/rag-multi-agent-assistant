# 阶段性梳理

---

## 第一阶段：项目初始化（2026-06-23）

### 一、项目架构

```
rag-multi-agent-assistant/
├── backend/                    # FastAPI 后端
│   ├── app/
│   │   ├── core/              # 核心配置（已完成）
│   │   ├── api/               # API 路由（骨架）
│   │   ├── models/            # 数据库模型（已完成）
│   │   ├── schemas/           # Pydantic 模型（已完成）
│   │   ├── services/          # 业务服务（骨架）
│   │   ├── graph/             # LangGraph 图（骨架）
│   │   ├── rag/               # RAG 模块（骨架）
│   │   └── memory/            # 记忆模块（骨架）
├── frontend/                   # Vue3 前端
│   └── src/
│       ├── api/               # API 调用（已完成）
│       ├── views/             # 页面（骨架）
│       └── router/            # 路由（已完成）
├── docs/                       # 设计文档（已完成）
└── docker-compose.yml          # 基础设施（已完成）
```

### 二、已完成的模块

#### 1. 核心配置 (`backend/app/core/`)

| 文件 | 功能 |
|------|------|
| `config.py` | pydantic-settings 管理，从 `.env` 读取配置 |
| `database.py` | SQLAlchemy 引擎、会话工厂、`get_db()` 依赖 |
| `redis_client.py` | Redis 连接、`get_redis()` 依赖 |
| `llm.py` | `get_llm()` 和 `get_embeddings()` 工厂函数 |

#### 2. 数据模型 (`backend/app/models/`)

| 模型 | 表名 | 用途 |
|------|------|------|
| `Document` | document | 文档元数据（文件名、类型、状态） |
| `DocumentChunk` | document_chunk | 文档切片（内容、向量 ID） |
| `ChatSession` | chat_session | 聊天会话 |
| `ChatMessage` | chat_message | 聊天消息（角色、内容、token 数） |
| `AgentLog` | agent_log | Agent 执行日志（输入输出、耗时） |
| `LongTermMemory` | long_term_memory | 长期记忆（命名空间、类型、重要性） |

#### 3. Pydantic Schema (`backend/app/schemas/`)

| 文件 | 定义 |
|------|------|
| `chat.py` | `ChatRequest`、`ChatResponse`、`MessageResponse` |
| `document.py` | `DocumentUploadResponse`、`DocumentResponse`、`DocumentChunkResponse` |
| `session.py` | `SessionResponse`、`SessionListResponse`、`AgentLogResponse`、`AgentTraceResponse` |

#### 4. 前端基础 (`frontend/src/`)

| 文件 | 功能 |
|------|------|
| `api/index.js` | Axios 实例 + 6 个 API 调用函数 |
| `router/index.js` | 4 个路由（Chat/Upload/History/AgentTrace） |
| `App.vue` | 主布局（顶部导航 + 路由出口） |

#### 5. 基础设施

| 文件 | 功能 |
|------|------|
| `docker-compose.yml` | PostgreSQL 16 + Redis 7 |
| `requirements.txt` | 14 个 Python 依赖 |
| `.env.example` | 配置模板 |

#### 6. 设计文档 (`docs/`)

| 文件 | 内容 |
|------|------|
| `PROJECT_SPEC.md` | 项目目标、技术选型、核心模块、性能指标 |
| `API_DESIGN.md` | 6 个 API 接口设计（请求/响应格式） |
| `DATABASE_DESIGN.md` | 6 张表设计（字段、索引、关系） |

### 三、骨架模块（TODO 占位）

| 模块 | 文件 | 待实现 |
|------|------|--------|
| API | `chat.py`、`documents.py`、`sessions.py` | 接口逻辑 |
| Services | `chat_service.py`、`document_service.py` 等 | 业务逻辑 |
| Graph | `rag_graph.py` | LangGraph 多智能体图 |
| RAG | `loaders.py`、`splitter.py`、`vector_store.py` | 文档处理流程 |
| Memory | `checkpointer.py`、`long_term_memory.py` | 记忆存储逻辑 |
| 前端 | 4 个 Vue 页面 | 交互功能 |

### 四、验证结果

- PostgreSQL: ✓ `localhost:5432`
- Redis: ✓ `localhost:6379`
- 后端: ✓ `http://localhost:8000`
- 前端: ✓ `http://localhost:5173`
- 健康检查: ✓ `{"status":"ok"}`

### 五、面试讲解要点

1. **技术选型理由**：LangGraph 做多智能体编排，PostgreSQL 做持久化，Redis 做缓存，Chroma 做向量存储
2. **架构设计**：单体 FastAPI，模块化分层（api/service/model），职责清晰
3. **数据库设计**：6 张表覆盖文档、聊天、Agent 日志、长期记忆，预留 JSONB 字段扩展
4. **前端设计**：Vue3 Composition API + Element Plus，4 个页面对应 4 个核心功能

---

## 第二阶段：RAG 核心流程（2026-06-24）

### 一、完成内容

#### 1. RAG 管道组件 (`backend/app/rag/`)

| 文件 | 功能 |
|------|------|
| `loaders.py` | 文档加载器，支持 PDF（pypdf）、TXT、Markdown |
| `splitter.py` | 文本切分器，使用 RecursiveCharacterTextSplitter |
| `vector_store.py` | Chroma 向量存储，支持 add_documents 和 search |
| `embeddings.py` | Embedding 模型（第一阶段已完成） |

#### 2. 服务层 (`backend/app/services/`)

| 文件 | 功能 |
|------|------|
| `document_service.py` | 文档上传全流程：保存文件 → 哈希去重 → 解析 → 切分 → Embedding → 存储 Chroma |
| `chat_service.py` | RAG 问答流程：创建会话 → 保存消息 → 向量检索 → 构建 Prompt → 调用 LLM |

#### 3. API 路由 (`backend/app/api/`)

| 文件 | 接口 |
|------|------|
| `documents.py` | `POST /api/documents/upload` - 文档上传 |
| `chat.py` | `POST /api/chat` - RAG 问答 |

#### 4. 前端页面 (`frontend/src/views/`)

| 文件 | 功能 |
|------|------|
| `Upload.vue` | 文档上传页面：拖拽上传、状态显示、文档列表 |
| `Chat.vue` | 智能问答页面：消息列表、输入框、Agent 轨迹展示 |

#### 5. 新增依赖

```
langchain-text-splitters>=0.2.0
chromadb>=0.4.0
langchain-chroma
```

### 二、核心流程

```
文档上传流程：
用户上传文件 → 保存到本地 → 计算哈希（去重）→ 创建 Document 记录
→ 解析文档内容 → 文本切分 → 生成 Embedding → 存储到 Chroma
→ 更新文档状态为 completed

RAG 问答流程：
用户发送消息 → 创建/获取会话 → 保存用户消息
→ 向量检索相关文档（k=4）→ 构建 RAG Prompt
→ 调用 LLM 生成回答 → 保存助手回复 → 返回结果 + agent_trace
```

### 三、验证结果

- 后端服务: ✓ 启动正常
- 前端服务: ✓ 启动正常
- 健康检查: ✓ `{"status":"ok"}`

### 四、面试讲解要点

1. **RAG 流程设计**：文档上传 → 解析 → 切分 → Embedding → 向量存储 → 检索 → 生成回答
2. **向量存储选型**：Chroma 作为第一版向量数据库，支持持久化和相似度检索
3. **文本切分策略**：RecursiveCharacterTextSplitter，chunk_size=500，chunk_overlap=50
4. **去重机制**：通过文件内容哈希实现文档去重

---

## 第三阶段：LangGraph 多智能体（待开发）

---

## 第四阶段：记忆系统（待开发）

---

## 第五阶段：前端完善（待开发）
