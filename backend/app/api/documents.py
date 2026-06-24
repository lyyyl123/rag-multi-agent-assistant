"""
文档接口
"""
from typing import List
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..services.document_service import document_service
from ..schemas.document import DocumentUploadResponse, DocumentResponse
from ..models.document import Document

router = APIRouter()


@router.post("/api/documents/upload", response_model=DocumentUploadResponse)
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    文档上传接口

    支持 PDF、TXT、Markdown 格式
    """
    return await document_service.upload_document(file, db)


@router.get("/api/documents", response_model=List[DocumentResponse])
async def list_documents(db: Session = Depends(get_db)):
    """获取已上传文档列表"""
    documents = db.query(Document).order_by(Document.created_at.desc()).all()
    return documents
