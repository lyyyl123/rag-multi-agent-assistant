import redis
from .config import settings

# 创建 Redis 连接
redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    decode_responses=True,
)


def get_redis() -> redis.Redis:
    """获取 Redis 客户端"""
    return redis_client
