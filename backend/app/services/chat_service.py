"""
聊天服务

处理 RAG 问答流程
"""
import uuid
from typing import Optional
from sqlalchemy.orm import Session

from ..core.llm import get_llm
from ..models.chat_session import ChatSession
from ..models.chat_message import ChatMessage
from ..rag.vector_store import search
from ..schemas.chat import ChatResponse


class ChatService:
    """聊天服务"""

    async def chat(self, message: str, session_id: Optional[str], db: Session) -> ChatResponse:
        """
        处理聊天请求

        流程：创建/获取会话 → 保存用户消息 → 向量检索相关文档 → 构建 Prompt → 调用 LLM → 保存回复 → 返回结果

        Args:
            message: 用户消息
            session_id: 会话 ID（可选）
            db: 数据库会话

        Returns:
            聊天响应
        """
        # 1. 创建或获取会话
        if session_id:
            session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
            if not session:
                session = self._create_session(db)
        else:
            session = self._create_session(db)

        # 2. 保存用户消息
        user_message = ChatMessage(
            id=str(uuid.uuid4()),
            session_id=session.id,
            role="user",
            content=message,
        )
        db.add(user_message)
        db.commit()

        # 3. 向量检索相关文档
        relevant_docs = search(message, k=4)
        context = "\n\n".join([doc["content"] for doc in relevant_docs]) if relevant_docs else ""

        # 4. 构建 Prompt
        prompt = self._build_prompt(message, context)

        # 5. 调用 LLM
        llm = get_llm()
        response = await llm.ainvoke(prompt)
        assistant_content = response.content

        # 6. 保存助手回复
        assistant_message = ChatMessage(
            id=str(uuid.uuid4()),
            session_id=session.id,
            role="assistant",
            content=assistant_content,
        )
        db.add(assistant_message)
        db.commit()

        # 7. 构建 agent_trace
        agent_trace = []
        if relevant_docs:
            agent_trace.append({
                "agent": "KnowledgeAgent",
                "action": "文档检索",
                "detail": f"检索到 {len(relevant_docs)} 个相关文档切片",
            })
        agent_trace.append({
            "agent": "FinalizeAgent",
            "action": "生成回答",
            "detail": "基于检索结果生成回答",
        })

        return ChatResponse(
            session_id=session.id,
            message=assistant_content,
            agent_trace=agent_trace,
        )

    def _create_session(self, db: Session) -> ChatSession:
        """创建新会话"""
        session = ChatSession(id=str(uuid.uuid4()))
        db.add(session)
        db.commit()
        return session

    def _build_prompt(self, question: str, context: str) -> str:
        """构建 RAG Prompt"""
        if context:
            return f"""基于以下参考文档回答用户问题。如果文档中没有相关信息，请说明无法从知识库中找到答案。

参考文档：
{context}

用户问题：{question}

回答："""
        else:
            return f"""请回答以下用户问题。注意：当前知识库中没有找到相关文档。

用户问题：{question}

回答："""


chat_service = ChatService()
