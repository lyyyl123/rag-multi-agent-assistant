"""
Agent 执行日志模型
"""
from sqlalchemy import Column, String, DateTime, Text, JSON
from sqlalchemy.sql import func
from ..core.database import Base


class AgentLog(Base):
    """Agent 执行日志表"""
    __tablename__ = "agent_log"

    id = Column(String(36), primary_key=True)
    session_id = Column(String(36), nullable=False, index=True)
    message_id = Column(String(36))
    agent_name = Column(String(100), nullable=False)
    action = Column(String(100))
    input_data = Column(JSON, default={})
    output_data = Column(JSON, default={})
    status = Column(String(50), default="running")  # running, completed, failed
    duration_ms = Column(String(50))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
