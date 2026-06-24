# RAG Multi-Agent Assistant

基于 LangGraph 的 RAG 多智能体知识库问答系统

## 项目简介

这是一个用于应届生求职 AI Agent 应用开发 / 大模型应用开发岗位的作品集项目。项目实现了基于 LangGraph 的多智能体编排，支持文档上传、知识库问答、Agent 执行过程展示等功能。

## 技术栈

### 后端
- Python 3.11+
- FastAPI
- LangChain
- LangGraph
- SQLAlchemy
- PostgreSQL
- Redis
- Chroma
- Pydantic

### 前端
- Vue 3
- Vite
- Element Plus
- Axios
- Vue Router

### 基础设施
- PostgreSQL 16
- Redis 7
- Docker Compose

## 项目架构

```
rag-multi-agent-assistant/
├── backend/                    # 后端服务
│   ├── app/
│   │   ├── api/               # API 接口
│   │   ├── agents/            # LangGraph 智能体
│   │   ├── graph/             # LangGraph 图定义
│   │   ├── rag/               # RAG 相关模块
│   │   ├── memory/            # 记忆管理
│   │   ├── models/            # 数据库模型
│   │   ├── schemas/           # Pydantic 模型
│   │   ├── services/          # 业务服务
│   │   └── core/              # 核心配置
│   └── requirements.txt
├── frontend/                  # 前端应用
│   └── src/
│       ├── api/               # API 调用
│       ├── views/             # 页面组件
│       ├── components/        # 通用组件
│       └── router/            # 路由配置
├── docs/                      # 项目文档
├── docker-compose.yml
└── README.md
```

## 已完成功能

### 第一阶段：项目初始化（2026-06-23）

- [x] 项目初始化和目录结构
- [x] 后端 FastAPI 骨架
- [x] 健康检查接口
- [x] 前端 Vue3 基础页面
- [x] Docker Compose 配置
- [x] PostgreSQL 和 Redis 服务
- [x] 项目文档

### 第二阶段：RAG 核心流程（2026-06-24）

- [x] 文档上传接口（支持 PDF/TXT/Markdown）
- [x] 文档解析器（pypdf + 文本读取）
- [x] 文本切分器（RecursiveCharacterTextSplitter）
- [x] Chroma 向量存储
- [x] Embedding 生成和存储
- [x] RAG 问答接口
- [x] 前端文档上传页面
- [x] 前端智能问答页面
- [x] 文档列表接口（GET /api/documents）
- [x] 失败文档重新上传支持
- [x] LLM 模型配置修复

## 本地启动方式

### 1. 启动 PostgreSQL 和 Redis

```bash
docker compose up -d
```

### 2. 启动后端

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # 编辑 .env 填入 API Key
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 3. 启动前端

```bash
cd frontend
npm install
npm run dev
```

### 4. 访问应用

- 前端: http://localhost:5173
- 后端 API: http://localhost:8000
- API 文档: http://localhost:8000/docs

## 测试健康检查

```bash
curl http://localhost:8000/api/health
```

预期响应：
```json
{
  "status": "ok",
  "service": "rag-multi-agent-assistant"
}
```

## 后续开发阶段规划

### 第二阶段：RAG 核心流程
- 文档上传接口
- PDF/TXT/Markdown 解析
- 文本切分
- Embedding 生成
- Chroma 向量存储
- 基础 RAG 问答

### 第三阶段：LangGraph 多智能体
- Router Agent
- Knowledge Agent
- Review Agent
- Finalize Agent
- 多智能体编排图
- Agent 执行日志

### 第四阶段：记忆系统
- 长期记忆存储
- 短期缓存
- 会话管理
- 上下文窗口

### 第五阶段：前端完善
- 聊天界面
- 文档上传组件
- 历史记录
- Agent 执行过程可视化

## 许可证

MIT
