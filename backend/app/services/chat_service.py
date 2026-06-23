"""
聊天服务

第一阶段预留接口，后续实现
"""
from ..core.config import settings


class ChatService:
    """聊天服务"""

    async def chat(self, message: str, session_id: str = None) -> dict:
        """
        处理聊天请求

        TODO: 第二阶段实现，调用 LangGraph 执行 RAG 流程
        """
        raise NotImplementedError


chat_service = ChatService()
