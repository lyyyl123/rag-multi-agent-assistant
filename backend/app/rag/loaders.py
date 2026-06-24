"""
文档加载器

支持 PDF、TXT、Markdown 格式
"""
from pathlib import Path
from pypdf import PdfReader


def load_document(file_path: str) -> str:
    """
    加载文档内容

    Args:
        file_path: 文件路径

    Returns:
        文档文本内容
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"文件不存在: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".pdf":
        return _load_pdf(file_path)
    elif suffix in (".txt", ".md", ".markdown"):
        return _load_text(file_path)
    else:
        raise ValueError(f"不支持的文件格式: {suffix}")


def _load_pdf(file_path: str) -> str:
    """加载 PDF 文件"""
    reader = PdfReader(file_path)
    text_parts = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text_parts.append(page_text)
    return "\n\n".join(text_parts)


def _load_text(file_path: str) -> str:
    """加载文本文件（TXT/Markdown）"""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
