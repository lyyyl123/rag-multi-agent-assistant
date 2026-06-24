# 技术知识库

---

## 一、AI 框架类

### LangChain

**定义：** 用于构建 LLM 应用的开发框架，提供标准化的组件和链式调用能力。

**解决的核心问题：**
- LLM 原生 API 只是"文本进、文本出"
- 真实应用需要：检索、记忆、工具调用、多步推理
- LangChain 把这些能力封装成可复用的组件

**六大核心组件：**

| 组件 | 作用 | 代码示例 |
|------|------|----------|
| Models | 统一模型接口 | `ChatOpenAI`, `ChatAnthropic`, `OllamaLLM` |
| Prompts | 提示词模板化 | `ChatPromptTemplate.from_messages([...])` |
| Chains | 链式调用（LCEL） | `chain = prompt \| llm \| parser` |
| Retrieval | RAG 检索 | `retriever = vectorstore.as_retriever()` |
| Memory | 对话记忆 | `ConversationBufferMemory` |
| Agents | 工具调用 | `create_tool_calling_agent(llm, tools, prompt)` |

**架构演进：**
| 版本 | 架构 | 特点 |
|------|------|------|
| v0.1 | Chain 类继承 | 臃肿、难扩展 |
| v0.2 | LCEL 管道 | 灵活、可组合（当前主流） |
| v0.3 | 更轻量 | 持续优化 |

---

### LangGraph

**定义：** LangChain 生态中的状态机框架，用于构建有状态、可循环、可分支的多步骤 AI 工作流。

**解决的核心问题：**
- LangChain 的 Chain 是线性的（A → B → C）
- 真实应用需要：条件分支、循环重试、并行执行、人工介入
- LangGraph 用图结构解决这些问题

**核心概念：**
| 概念 | 作用 | 示例 |
|------|------|------|
| State | 共享数据容器 | `class AgentState(TypedDict)` |
| Node | 处理节点（纯函数） | `def retrieve(state): return {...}` |
| Edge | 连接边 | 普通边 / 条件边 |
| Graph | 图结构 | `StateGraph(AgentState)` |

**LangGraph vs LangChain：**
| 维度 | LangChain Chain | LangGraph |
|------|-----------------|-----------|
| 结构 | 线性管道 | 有向图 |
| 分支 | 不支持 | 条件边 |
| 循环 | 不支持 | 原生支持 |
| 状态 | 无状态 | 有状态 |
| 人工介入 | 困难 | 原生支持 |
| 适用场景 | 简单流水线 | 复杂工作流 |

**关键特性：**
1. **循环重试**：审核不通过可重新生成
2. **Human-in-the-loop**：`interrupt_before=["execute_tool"]`
3. **持久化**：`PostgresSaver` 保存状态到数据库
4. **流式输出**：`app.stream(input_data)`

---

## 二、知识表示类

### 知识图谱（Knowledge Graph）

**定义：** 用图结构表示知识的方法，由实体（节点）和关系（边）组成。

**核心概念：**
- **节点（实体）**：人、公司、地点、概念
- **边（关系）**：实体之间的连接
- **属性**：节点/边的附加信息

**存储方式：**
- 图数据库：Neo4j、ArangoDB
- 三元组：`(主语, 谓语, 宾语)` → `(张三, 任职于, 腾讯)`

**与 RAG 的关系：**
| 检索方式 | 擅长场景 | 示例 |
|----------|----------|------|
| 向量检索 | 语义相似 | "头疼怎么办" → 医疗文档 |
| 图检索 | 关系明确 | "张三的同事" → 精确查询 |

---

## 三、协议/工具类

### Ollama OpenAI 兼容 API

**定义：** Ollama 支持 OpenAI 兼容 API，地址：`http://localhost:11434/v1`

**作用：** 一套代码，多个后端，只需要改 `base_url` 就能切换模型服务：

| 场景 | base_url |
|------|----------|
| OpenAI 官方 | `https://api.openai.com/v1` |
| mimo 兼容服务 | `https://token-plan-cn.xiaomimimo.com/v1` |
| 本地 Ollama | `http://localhost:11434/v1` |
| vLLM 本地部署 | `http://localhost:8000/v1` |

**为什么是 OpenAI 协议：**
1. **先发优势**：OpenAI 最早推出商业化 API，成为事实标准
2. **生态锁定**：LangChain 等框架优先适配 OpenAI 接口
3. **兼容性**：其他服务主动兼容 OpenAI 协议才能接入生态

---

## 四、Web 框架类

### FastAPI

**定义：** 现代、快速的 Python Web 框架，基于 Starlette 和 Pydantic。

**核心特性：**
- **异步支持**：原生 async/await
- **自动文档**：Swagger UI + ReDoc
- **类型安全**：Pydantic 数据验证
- **高性能**：接近 Node.js/Go 的速度

**项目中的应用：**
```python
from fastapi import FastAPI, UploadFile, File
from app.api import chat, documents

app = FastAPI()
app.include_router(chat.router, prefix="/api")
app.include_router(documents.router, prefix="/api")
```

---

## 五、数据库类

### PostgreSQL

**定义：** 开源关系型数据库，支持 JSON、全文搜索、向量扩展。

**项目中的应用：**
- LangGraph checkpointer（状态持久化）
- 长期记忆存储
- 聊天记录持久化
- 文档元数据存储

**连接方式：**
```python
from sqlalchemy import create_engine
DATABASE_URL = "postgresql+psycopg://user:pass@localhost:5432/db"
```

### Redis

**定义：** 内存数据结构存储，用作缓存、消息队列、会话存储。

**项目中的应用：**
- 短期缓存
- 会话临时状态
- 速率限制

**连接方式：**
```python
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
```

### Chroma

**定义：** 开源向量数据库，专为 AI 应用设计。

**项目中的应用：**
- 存储文档 Embedding
- 支持相似度检索

**使用方式：**
```python
from langchain_chroma import Chroma
vectorstore = Chroma(persist_directory="./storage/chroma", embedding_function=embeddings)
```

### SQLAlchemy

**定义：** Python SQL 工具包和 ORM。

**核心概念：**
- **Engine**：数据库连接
- **Session**：会话管理
- **Model**：ORM 映射

**项目中的应用：**
```python
from sqlalchemy.orm import DeclarativeBase, Session

class Base(DeclarativeBase):
    pass

class Document(Base):
    __tablename__ = "document"
    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
```

---

## 六、前端类

### Vue 3

**定义：** 渐进式 JavaScript 框架，Composition API 是当前主流。

**核心概念：**
- **响应式**：`ref()`, `reactive()`
- **生命周期**：`onMounted()`, `onUnmounted()`
- **组件化**：SFC (Single File Component)

**项目中的应用：**
```vue
<script setup>
import { ref, onMounted } from 'vue'

const messages = ref([])
onMounted(() => { /* 初始化 */ })
</script>
```

### Element Plus

**定义：** Vue 3 组件库，提供丰富的企业级 UI 组件。

**项目中的应用：**
```vue
<template>
  <el-upload action="/api/documents/upload" />
  <el-input v-model="input" @keyup.enter="send" />
</template>
```

### Axios

**定义：** 基于 Promise 的 HTTP 客户端。

**项目中的应用：**
```javascript
import axios from 'axios'

const api = axios.create({ baseURL: '/api' })
export const uploadDocument = (file) => api.post('/documents/upload', file)
export const sendMessage = (data) => api.post('/chat', data)
```

---

## 七、配置管理类

### pydantic-settings

**定义：** Pydantic 的配置管理扩展，支持从环境变量和 .env 文件读取配置。

**项目中的应用：**
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "gpt-3.5-turbo"
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
```

**优势：**
- 类型安全
- 自动读取 .env
- 支持默认值
- IDE 自动补全

---

## 八、容器化类

### Docker & Docker Compose

**定义：** 容器化技术，实现环境一致性。

**项目中的应用：**
```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: rag_agent
      POSTGRES_USER: rag_user
      POSTGRES_PASSWORD: rag_password

  redis:
    image: redis:7-alpine
```

**优势：**
- 开发/生产环境一致
- 一键启动所有服务
- 依赖隔离

---

## 九、面试高频问题

### 框架类

**Q1: LangChain 和 LangGraph 的区别？**
> LangChain 是组件框架，提供标准化的 LLM 调用接口；LangGraph 是编排框架，用图结构组织复杂工作流。LangChain 适合简单链式调用，LangGraph 适合需要分支、循环、状态管理的场景。

**Q2: 为什么需要 LangGraph？**
> 真实 AI 应用很少是线性的。比如一个 Agent 需要：判断问题类型 → 选择工具 → 执行 → 验证 → 重试。这种逻辑用 LangChain Chain 很难实现，LangGraph 的图结构天然支持。

**Q3: LangGraph 的状态是什么？**
> 状态是一个 TypedDict 对象，在图中所有节点间共享。每个节点接收当前状态，返回状态更新，LangGraph 自动合并更新。

**Q4: 什么是 Human-in-the-loop？**
> 在关键节点设置断点，暂停执行等待人工确认。比如 Agent 要执行危险操作（删除文件、发送邮件）前，先让人审批。LangGraph 原生支持 `interrupt_before` / `interrupt_after`。

**Q5: LangGraph 如何实现持久化？**
> 通过 Checkpointer（检查点）机制。每次状态变化都保存到数据库（PostgreSQL 等），可以从任意检查点恢复执行。适合长时间运行的任务或需要断点续传的场景。

### 知识表示类

**Q6: 知识图谱和向量数据库的区别？**
> 知识图谱存储结构化的"实体-关系"网络，支持精确关系查询；向量数据库存储高维向量，支持语义相似度检索。两者可结合使用。
