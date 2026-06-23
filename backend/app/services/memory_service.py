"""
记忆服务

第一阶段预留接口，后续实现
"""
from ..core.config import settings


class MemoryService:
    """记忆服务"""

    async def save_memory(self, namespace: str, key: str, content: str, metadata: dict = None):
        """
        保存长期记忆

        TODO: 第三阶段实现
        """
        raise NotImplementedError

    async def retrieve_memory(self, namespace: str, key: str) -> str:
        """
        检索长期记忆

        TODO: 第三阶段实现
        """
        raise NotImplementedError


memory_service = MemoryService()
