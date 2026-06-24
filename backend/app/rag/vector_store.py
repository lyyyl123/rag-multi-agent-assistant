"""
向量存储服务

使用 Chroma 向量数据库
"""
from typing import List, Optional
from langchain_chroma import Chroma
from ..core.config import settings
from ..core.llm import get_embeddings

# 全局 Chroma 实例
_vector_store: Optional[Chroma] = None


def get_vector_store() -> Chroma:
    """
    获取 Chroma 向量存储实例（单例）

    Returns:
        Chroma 向量存储实例
    """
    global _vector_store
    if _vector_store is None:
        _vector_store = Chroma(
            persist_directory=settings.CHROMA_PERSIST_DIR,
            embedding_function=get_embeddings(),
            collection_name="rag_documents",
        )
    return _vector_store


def add_documents(chunks: List[str], metadatas: List[dict]) -> List[str]:
    """
    添加文档切片到向量存储

    Args:
        chunks: 文本切片列表
        metadatas: 元数据列表

    Returns:
        向量 ID 列表
    """
    store = get_vector_store()
    ids = store.add_texts(texts=chunks, metadatas=metadatas)
    return ids


def search(query: str, k: int = 4) -> List[dict]:
    """
    相似度检索

    Args:
        query: 查询文本
        k: 返回结果数量

    Returns:
        检索结果列表，每项包含 content 和 metadata
    """
    store = get_vector_store()
    results = store.similarity_search_with_score(query=query, k=k)

    return [
        {
            "content": doc.page_content,
            "metadata": doc.metadata,
            "score": score,
        }
        for doc, score in results
    ]
