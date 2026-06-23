"""
长期记忆服务

第一阶段预留接口，后续阶段实现
"""
from ..core.config import settings


class LongTermMemory:
    """
    长期记忆管理器

    TODO: 第三阶段实现，使用 PostgreSQL 存储长期记忆
    """

    def __init__(self):
        pass

    async def save_memory(self, namespace: str, key: str, content: str, metadata: dict = None):
        """保存长期记忆"""
        raise NotImplementedError

    async def retrieve_memory(self, namespace: str, key: str) -> str:
        """检索长期记忆"""
        raise NotImplementedError

    async def search_memories(self, namespace: str, query: str, limit: int = 5) -> list:
        """搜索相关记忆"""
        raise NotImplementedError
