# 开发日志

## 2026-06-24

### 第二阶段完成：RAG 核心流程

**完成内容：**

后端实现：
- `backend/app/rag/loaders.py` - 文档加载器（支持 PDF/TXT/Markdown）
- `backend/app/rag/splitter.py` - 文本切分器（RecursiveCharacterTextSplitter）
- `backend/app/rag/vector_store.py` - Chroma 向量存储（add_documents/search）
- `backend/app/services/document_service.py` - 文档服务（上传、解析、切分、Embedding、存储）
- `backend/app/services/chat_service.py` - 聊天服务（RAG 问答流程）
- `backend/app/api/documents.py` - 文档上传接口
- `backend/app/api/chat.py` - 聊天接口

前端实现：
- `frontend/src/views/Upload.vue` - 文档上传页面（拖拽上传、状态显示）
- `frontend/src/views/Chat.vue` - 智能问答页面（消息列表、输入框、Agent 轨迹）

新增依赖：
- langchain-text-splitters
- chromadb
- langchain-chroma

**验证结果：**
- 后端服务启动正常
- 前端服务启动正常
- 健康检查接口正常

---

## 2026-06-23

### 第一阶段验证完成

**验证内容：**
- PostgreSQL 16 容器启动正常
- Redis 7 容器启动正常
- 后端 FastAPI 服务启动正常
- 前端 Vue3 开发服务器启动正常
- `/api/health` 接口返回 `{"status":"ok","service":"rag-multi-agent-assistant"}`

**环境配置：**
- 配置 Docker 镜像源（docker.1ms.run, docker.xuanyuan.me）
- 升级 Python 至 3.11（原 3.8 不兼容 langgraph）
- 创建后端虚拟环境并安装依赖

**启动命令：**
```powershell
# 1. 启动数据库
docker compose up -d

# 2. 启动后端
cd backend; .\.venv\Scripts\Activate.ps1; uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 3. 启动前端
cd frontend; npm run dev
```

**服务地址：**
- 前端: http://localhost:5173
- 后端: http://localhost:8000
- API 文档: http://localhost:8000/docs

---

## 第一阶段：项目初始化

**完成内容：**
- 项目目录结构搭建
- FastAPI 后端骨架
- Vue3 + Element Plus 前端骨架
- Docker Compose 配置（PostgreSQL + Redis）
- SQLAlchemy 数据库模型定义
- Pydantic 配置管理
- 项目文档（README + 设计文档）
