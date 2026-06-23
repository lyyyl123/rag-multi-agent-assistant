"""
文档相关 Schema
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class DocumentUploadResponse(BaseModel):
    """文档上传响应"""
    id: str
    filename: str
    file_type: str
    file_size: int
    status: str
    message: str


class DocumentResponse(BaseModel):
    """文档响应"""
    id: str
    filename: str
    file_type: str
    file_size: int
    status: str
    chunk_count: int
    created_at: datetime

    class Config:
        from_attributes = True


class DocumentChunkResponse(BaseModel):
    """文档切片响应"""
    id: str
    document_id: str
    chunk_index: int
    content: str
    metadata: Optional[dict] = None

    class Config:
        from_attributes = True
