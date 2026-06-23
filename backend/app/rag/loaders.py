"""
文档加载器

第一阶段预留，后续实现
"""
from typing import List
from pathlib import Path


def load_document(file_path: str) -> str:
    """
    加载文档内容

    TODO: 第二阶段实现，支持 PDF/TXT/Markdown
    """
    raise NotImplementedError


def load_documents(directory: str) -> List[str]:
    """
    批量加载文档

    TODO: 第二阶段实现
    """
    raise NotImplementedError
