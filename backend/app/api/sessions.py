"""
会话接口

第一阶段预留，后续实现
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/sessions")
async def get_sessions():
    """获取会话列表 - TODO: 第二阶段实现"""
    return {"sessions": []}


@router.get("/api/sessions/{session_id}/messages")
async def get_session_messages(session_id: str):
    """获取会话消息 - TODO: 第二阶段实现"""
    return {"session_id": session_id, "messages": []}


@router.get("/api/sessions/{session_id}/agent-logs")
async def get_agent_logs(session_id: str):
    """获取 Agent 执行日志 - TODO: 第二阶段实现"""
    return {"session_id": session_id, "logs": []}
