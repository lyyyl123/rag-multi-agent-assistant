# 数据库设计文档

## 概述

本项目使用 PostgreSQL 作为核心持久化数据库，存储文档元数据、聊天记录、Agent 日志和长期记忆。

## 数据表设计

### 1. document (文档表)

存储上传的文档元数据。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| filename | VARCHAR(255) | 文件名 |
| file_type | VARCHAR(50) | 文件类型 (pdf/txt/md) |
| file_size | INTEGER | 文件大小 (字节) |
| file_path | VARCHAR(500) | 文件存储路径 |
| content_hash | VARCHAR(64) | 内容哈希，用于去重 |
| metadata | JSONB | 文档元数据 |
| status | VARCHAR(50) | 状态 (pending/processing/completed/failed) |
| chunk_count | INTEGER | 切片数量 |
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

### 2. document_chunk (文档切片表)

存储文档切片内容和向量引用。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| document_id | VARCHAR(36) | 外键，关联 document.id |
| chunk_index | INTEGER | 切片序号 |
| content | TEXT | 切片内容 |
| metadata | JSONB | 切片元数据 |
| embedding_id | VARCHAR(255) | Chroma 中的向量 ID |
| created_at | TIMESTAMP | 创建时间 |

### 3. chat_session (聊天会话表)

存储聊天会话信息。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| title | VARCHAR(255) | 会话标题 |
| metadata | JSONB | 会话元数据 |
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

### 4. chat_message (聊天消息表)

存储聊天消息记录。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| session_id | VARCHAR(36) | 外键，关联 chat_session.id |
| role | VARCHAR(20) | 角色 (user/assistant/system) |
| content | TEXT | 消息内容 |
| metadata | JSONB | 消息元数据 |
| token_count | INTEGER | Token 数量 |
| created_at | TIMESTAMP | 创建时间 |

### 5. agent_log (Agent 执行日志表)

存储 Agent 执行过程日志。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| session_id | VARCHAR(36) | 外键，关联 chat_session.id |
| message_id | VARCHAR(36) | 外键，关联 chat_message.id |
| agent_name | VARCHAR(100) | Agent 名称 |
| action | VARCHAR(100) | 执行动作 |
| input_data | JSONB | 输入数据 |
| output_data | JSONB | 输出数据 |
| status | VARCHAR(50) | 状态 (running/completed/failed) |
| duration_ms | VARCHAR(50) | 执行耗时 (毫秒) |
| created_at | TIMESTAMP | 创建时间 |

### 6. long_term_memory (长期记忆表)

存储长期记忆信息。

| 字段 | 类型 | 说明 |
|------|------|------|
| id | VARCHAR(36) | 主键，UUID |
| namespace | VARCHAR(255) | 命名空间 |
| memory_key | VARCHAR(255) | 记忆键 |
| memory_type | VARCHAR(50) | 记忆类型 (fact/preference/context) |
| content | TEXT | 记忆内容 |
| metadata | JSONB | 元数据 |
| importance | FLOAT | 重要性权重 (0-1) |
| source_session_id | VARCHAR(36) | 来源会话 ID |
| created_at | TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 更新时间 |

## 索引设计

### document 表
- `idx_document_status`: status
- `idx_document_created_at`: created_at

### document_chunk 表
- `idx_chunk_document_id`: document_id

### chat_session 表
- `idx_session_created_at`: created_at

### chat_message 表
- `idx_message_session_id`: session_id
- `idx_message_created_at`: created_at

### agent_log 表
- `idx_log_session_id`: session_id
- `idx_log_created_at`: created_at

### long_term_memory 表
- `idx_memory_namespace`: namespace
- `idx_memory_type`: memory_type
- `idx_memory_created_at`: created_at

## 关系设计

```
document (1) ---> (N) document_chunk
chat_session (1) ---> (N) chat_message
chat_session (1) ---> (N) agent_log
chat_message (1) ---> (N) agent_log
```

## 数据库初始化

使用 SQLAlchemy 创建表:

```python
from app.core.database import engine, Base
from app.models import document, document_chunk, chat_session, chat_message, agent_log, long_term_memory

# 创建所有表
Base.metadata.create_all(bind=engine)
```

## 注意事项

1. 所有 ID 使用 UUID 格式
2. 时间字段使用带时区的 TIMESTAMP
3. JSONB 字段用于存储灵活的元数据
4. 外键关系通过应用层维护，不使用数据库外键约束
5. 长期记忆表的 importance 字段用于记忆检索排序
