from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaEmbeddings
from .config import settings


def get_llm() -> ChatOpenAI:
    """获取 LLM 实例"""
    return ChatOpenAI(
        model=settings.OPENAI_MODEL,
        api_key=settings.OPENAI_API_KEY,
        base_url=settings.OPENAI_BASE_URL,
        temperature=0.7,
    )


def get_embeddings() -> OllamaEmbeddings:
    """获取 Embeddings 实例"""
    return OllamaEmbeddings(
        model=settings.EMBEDDING_MODEL,
        base_url=settings.OLLAMA_BASE_URL,
    )
