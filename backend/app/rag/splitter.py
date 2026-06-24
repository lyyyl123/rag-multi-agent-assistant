"""
文本切分器

使用 LangChain RecursiveCharacterTextSplitter
"""
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> List[str]:
    """
    文本切分

    Args:
        text: 原始文本
        chunk_size: 切片大小（字符数）
        chunk_overlap: 切片重叠大小

    Returns:
        切片列表
    """
    if not text or not text.strip():
        return []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", "。", "！", "？", ".", "!", "?", " ", ""],
    )
    return splitter.split_text(text)
