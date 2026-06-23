"""
日志服务

第一阶段预留接口，后续实现
"""
from ..core.config import settings


class LogService:
    """日志服务"""

    async def log_agent_action(self, session_id: str, agent_name: str, action: str, input_data: dict, output_data: dict):
        """
        记录 Agent 执行日志

        TODO: 第二阶段实现
        """
        raise NotImplementedError


log_service = LogService()
