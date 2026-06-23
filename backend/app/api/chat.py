"""
聊天接口

第一阶段预留，后续实现
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/chat")
async def chat():
    """聊天接口 - TODO: 第二阶段实现"""
    return {"message": "聊天接口开发中"}
