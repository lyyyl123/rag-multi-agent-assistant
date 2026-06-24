"""
文档接口
"""
from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from ..core.database import get_db
from ..services.document_service import document_service
from ..schemas.document import DocumentUploadResponse

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
