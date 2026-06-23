"""
文档切片模型
"""
from sqlalchemy import Column, String, Integer, DateTime, Text, JSON, ForeignKey
from sqlalchemy.sql import func
from ..core.database import Base


class DocumentChunk(Base):
    """文档切片表"""
    __tablename__ = "document_chunk"

    id = Column(String(36), primary_key=True)
    document_id = Column(String(36), ForeignKey("document.id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)
    metadata_ = Column("metadata", JSON, default={})
    embedding_id = Column(String(255))  # Chroma 中的向量 ID
    created_at = Column(DateTime(timezone=True), server_default=func.now())
