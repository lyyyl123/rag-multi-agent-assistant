"""
聊天会话模型
"""
from sqlalchemy import Column, String, DateTime, JSON
from sqlalchemy.sql import func
from ..core.database import Base


class ChatSession(Base):
    """聊天会话表"""
    __tablename__ = "chat_session"

    id = Column(String(36), primary_key=True)
    title = Column(String(255), default="新对话")
    metadata_ = Column("metadata", JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
