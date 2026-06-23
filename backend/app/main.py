from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.health import router as health_router
from .api.chat import router as chat_router
from .api.documents import router as documents_router
from .api.sessions import router as sessions_router
from .core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="基于 LangGraph 的 RAG 多智能体知识库问答系统",
    version="0.1.0",
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(health_router, tags=["health"])
app.include_router(chat_router, tags=["chat"])
app.include_router(documents_router, tags=["documents"])
app.include_router(sessions_router, tags=["sessions"])


@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "Welcome to RAG Multi-Agent Assistant",
        "docs": "/docs",
    }
