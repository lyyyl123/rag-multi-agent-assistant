"""
文档服务

处理文档上传、解析、切分、Embedding、存储
"""
import hashlib
import uuid
from pathlib import Path
from typing import Optional
from fastapi import UploadFile
from sqlalchemy.orm import Session

from ..core.config import settings
from ..models.document import Document
from ..models.document_chunk import DocumentChunk
from ..rag.loaders import load_document
from ..rag.splitter import split_text
from ..rag.vector_store import add_documents
from ..schemas.document import DocumentUploadResponse


class DocumentService:
    """文档服务"""

    async def upload_document(self, file: UploadFile, db: Session) -> DocumentUploadResponse:
        """
        上传文档

        流程：保存文件 → 计算哈希（去重）→ 创建 Document 记录 → 解析 → 切分 → Embedding → 存储 Chroma → 更新状态

        Args:
            file: 上传的文件
            db: 数据库会话

        Returns:
            文档上传响应
        """
        # 1. 保存文件
        file_path = await self._save_file(file)

        # 2. 计算内容哈希
        content_hash = self._compute_hash(file_path)

        # 3. 检查是否已存在（去重）
        existing = db.query(Document).filter(Document.content_hash == content_hash).first()
        if existing:
            return DocumentUploadResponse(
                id=existing.id,
                filename=existing.filename,
                file_type=existing.file_type,
                file_size=existing.file_size,
                status=existing.status,
                message="文档已存在",
            )

        # 4. 创建 Document 记录
        doc_id = str(uuid.uuid4())
        file_type = Path(file.filename).suffix.lower().lstrip(".")
        document = Document(
            id=doc_id,
            filename=file.filename,
            file_type=file_type,
            file_size=file.size,
            file_path=file_path,
            content_hash=content_hash,
            status="processing",
        )
        db.add(document)
        db.commit()

        try:
            # 5. 解析文档
            text_content = load_document(file_path)

            # 6. 文本切分
            chunks = split_text(text_content)

            # 7. 存储切片到数据库
            chunk_records = []
            for i, chunk_text in enumerate(chunks):
                chunk_record = DocumentChunk(
                    id=str(uuid.uuid4()),
                    document_id=doc_id,
                    chunk_index=i,
                    content=chunk_text,
                )
                chunk_records.append(chunk_record)
                db.add(chunk_record)

            db.commit()

            # 8. Embedding 并存储到 Chroma
            metadatas = [{"document_id": doc_id, "chunk_index": i} for i in range(len(chunks))]
            embedding_ids = add_documents(chunks, metadatas)

            # 9. 更新切片的 embedding_id
            for chunk_record, embedding_id in zip(chunk_records, embedding_ids):
                chunk_record.embedding_id = embedding_id

            # 10. 更新文档状态
            document.status = "completed"
            document.chunk_count = len(chunks)
            db.commit()

            return DocumentUploadResponse(
                id=doc_id,
                filename=file.filename,
                file_type=file_type,
                file_size=file.size,
                status="completed",
                message=f"文档处理完成，共 {len(chunks)} 个切片",
            )

        except Exception as e:
            # 失败时更新状态
            document.status = "failed"
            db.commit()
            raise e

    async def _save_file(self, file: UploadFile) -> str:
        """保存上传的文件"""
        upload_dir = Path(settings.UPLOAD_DIR)
        upload_dir.mkdir(parents=True, exist_ok=True)

        # 生成唯一文件名
        file_ext = Path(file.filename).suffix
        unique_name = f"{uuid.uuid4()}{file_ext}"
        file_path = upload_dir / unique_name

        # 写入文件
        content = await file.read()
        with open(file_path, "wb") as f:
            f.write(content)

        return str(file_path)

    def _compute_hash(self, file_path: str) -> str:
        """计算文件内容哈希"""
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()


document_service = DocumentService()
