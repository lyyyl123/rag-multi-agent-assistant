"""
文档接口

第一阶段预留，后续实现
"""
from fastapi import APIRouter

router = APIRouter()


@router.post("/api/documents/upload")
async def upload_document():
    """文档上传接口 - TODO: 第二阶段实现"""
    return {"message": "文档上传接口开发中"}
