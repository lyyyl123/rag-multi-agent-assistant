from fastapi import APIRouter
from ..core.config import settings

router = APIRouter()


@router.get("/api/health")
async def health_check():
    """健康检查接口"""
    return {
        "status": "ok",
        "service": settings.APP_NAME,
    }
