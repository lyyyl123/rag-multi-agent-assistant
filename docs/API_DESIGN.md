# API 设计文档

## 基础信息

- Base URL: `http://localhost:8000`
- Content-Type: `application/json`
- 认证方式: 无 (第一阶段)

## API 列表

### 1. 健康检查

**GET /api/health**

检查服务是否正常运行。

**响应示例:**
```json
{
  "status": "ok",
  "service": "rag-multi-agent-assistant"
}
```

### 2. 文档上传

**POST /api/documents/upload**

上传文档到知识库。

**请求:**
- Content-Type: multipart/form-data
- 参数:
  - `file`: 文件 (PDF/TXT/Markdown)

**响应示例:**
```json
{
  "id": "doc_123",
  "filename": "example.pdf",
  "file_type": "pdf",
  "file_size": 1024000,
  "status": "processing",
  "message": "文档上传成功，正在处理中"
}
```

### 3. 聊天

**POST /api/chat**

发送聊天消息。

**请求体:**
```json
{
  "message": "什么是机器学习？",
  "session_id": "session_123"
}
```

**响应示例:**
```json
{
  "session_id": "session_123",
  "message": "机器学习是人工智能的一个分支...",
  "agent_trace": [
    {
      "agent": "router",
      "action": "route_to_knowledge",
      "duration_ms": 100
    },
    {
      "agent": "knowledge",
      "action": "search_documents",
      "duration_ms": 500
    }
  ]
}
```

### 4. 获取会话列表

**GET /api/sessions**

获取所有聊天会话。

**响应示例:**
```json
{
  "sessions": [
    {
      "id": "session_123",
      "title": "关于机器学习的讨论",
      "created_at": "2026-06-23T10:00:00Z",
      "updated_at": "2026-06-23T10:30:00Z"
    }
  ]
}
```

### 5. 获取会话消息

**GET /api/sessions/{session_id}/messages**

获取指定会话的所有消息。

**路径参数:**
- `session_id`: 会话 ID

**响应示例:**
```json
{
  "session_id": "session_123",
  "messages": [
    {
      "id": "msg_1",
      "role": "user",
      "content": "什么是机器学习？",
      "created_at": "2026-06-23T10:00:00Z"
    },
    {
      "id": "msg_2",
      "role": "assistant",
      "content": "机器学习是人工智能的一个分支...",
      "created_at": "2026-06-23T10:00:05Z"
    }
  ]
}
```

### 6. 获取 Agent 执行日志

**GET /api/sessions/{session_id}/agent-logs**

获取指定会话的 Agent 执行日志。

**路径参数:**
- `session_id`: 会话 ID

**响应示例:**
```json
{
  "session_id": "session_123",
  "logs": [
    {
      "id": "log_1",
      "agent_name": "router",
      "action": "route_to_knowledge",
      "input_data": {"query": "什么是机器学习？"},
      "output_data": {"route": "knowledge"},
      "status": "completed",
      "duration_ms": "100",
      "created_at": "2026-06-23T10:00:01Z"
    }
  ]
}
```

## 错误响应

所有接口在出错时返回统一格式:

```json
{
  "detail": "错误信息"
}
```

常见 HTTP 状态码:
- `200`: 成功
- `400`: 请求参数错误
- `404`: 资源不存在
- `500`: 服务器内部错误
