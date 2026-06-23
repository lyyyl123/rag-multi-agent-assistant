"""
LangGraph 状态定义

第一阶段预留，后续实现
"""
from typing import TypedDict, Annotated, List, Optional
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """Agent 状态定义"""
    messages: Annotated[list, add_messages]
    current_agent: Optional[str]
    context: Optional[str]
    session_id: Optional[str]
