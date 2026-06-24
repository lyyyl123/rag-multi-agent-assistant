"""
聊天接口
"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..services.chat_service import chat_service
from ..schemas.chat import ChatRequest, ChatResponse

router = APIRouter()


@router.post("/api/chat", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    """
    聊天接口

    发送消息，返回回答内容 + agent_trace 执行链路
    """
    return await chat_service.chat(request.message, request.session_id, db)
