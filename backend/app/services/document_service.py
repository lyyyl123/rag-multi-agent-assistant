"""
文档服务

第一阶段预留接口，后续实现
"""
from ..core.config import settings


class DocumentService:
    """文档服务"""

    async def upload_document(self, file) -> dict:
        """
        上传文档

        TODO: 第二阶段实现，解析文档、切分、Embedding、存储
        """
        raise NotImplementedError


document_service = DocumentService()
