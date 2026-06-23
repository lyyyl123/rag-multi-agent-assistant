"""
会话相关 Schema
"""
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime


class SessionResponse(BaseModel):
    """会话响应"""
    id: str
    title: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SessionListResponse(BaseModel):
    """会话列表响应"""
    sessions: List[SessionResponse]


class AgentLogResponse(BaseModel):
    """Agent 日志响应"""
    id: str
    session_id: str
    agent_name: str
    action: str
    input_data: Optional[dict] = None
    output_data: Optional[dict] = None
    status: str
    duration_ms: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class AgentTraceResponse(BaseModel):
    """Agent 执行轨迹响应"""
    session_id: str
    logs: List[AgentLogResponse]
