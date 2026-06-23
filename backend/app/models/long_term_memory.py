"""
长期记忆模型
"""
from sqlalchemy import Column, String, DateTime, Text, JSON, Float
from sqlalchemy.sql import func
from ..core.database import Base


class LongTermMemory(Base):
    """长期记忆表"""
    __tablename__ = "long_term_memory"

    id = Column(String(36), primary_key=True)
    namespace = Column(String(255), nullable=False, index=True)
    memory_key = Column(String(255), nullable=False)
    memory_type = Column(String(50), nullable=False)  # fact, preference, context
    content = Column(Text, nullable=False)
    metadata_ = Column("metadata", JSON, default={})
    importance = Column(Float, default=0.5)
    source_session_id = Column(String(36))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
