"""
LangGraph Checkpointer 配置

第一阶段预留接口，后续阶段实现
"""
from ..core.config import settings


def get_checkpointer():
    """
    获取 LangGraph PostgresSaver 实例

    TODO: 第二阶段实现，使用 langgraph-checkpoint-postgres
    """
    # from langgraph.checkpoint.postgres import PostgresSaver
    # return PostgresSaver.from_conn_string(settings.DATABASE_URL)
    return None
