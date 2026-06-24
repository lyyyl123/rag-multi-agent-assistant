from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """应用配置，从 .env 文件读取"""

    # OpenAI API 配置（对话模型）
    OPENAI_API_KEY: str = "tp-crbwd8r4b80paexd3d2jelhrvrhe7rh2snqyvso1c7lwk8xt"
    OPENAI_BASE_URL: str = "https://token-plan-cn.xiaomimimo.com/v1"
    OPENAI_MODEL: str = "mimo-v2.5-pro"

    # Ollama 配置（Embedding 模型）
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    EMBEDDING_MODEL: str = "qwen3"

    # PostgreSQL 配置
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "rag_agent"
    POSTGRES_USER: str = "rag_user"
    POSTGRES_PASSWORD: str = "rag_password"
    DATABASE_URL: str = "postgresql+psycopg://rag_user:rag_password@localhost:5432/rag_agent"

    # Redis 配置
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0

    # Chroma 配置
    CHROMA_PERSIST_DIR: str = "./storage/chroma"

    # 文件上传配置
    UPLOAD_DIR: str = "./storage/uploads"

    # 应用配置
    APP_NAME: str = "rag-multi-agent-assistant"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


settings = Settings()
