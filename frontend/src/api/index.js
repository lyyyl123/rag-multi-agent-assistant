import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
})

// 健康检查
export const healthCheck = () => api.get('/api/health')

// 聊天
export const chat = (data) => api.post('/api/chat', data)

// 文档上传
export const uploadDocument = (formData) =>
  api.post('/api/documents/upload', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  })

// 获取文档列表
export const getDocuments = () => api.get('/api/documents')

// 获取会话列表
export const getSessions = () => api.get('/api/sessions')

// 获取会话消息
export const getSessionMessages = (sessionId) =>
  api.get(`/api/sessions/${sessionId}/messages`)

// 获取 Agent 执行日志
export const getAgentLogs = (sessionId) =>
  api.get(`/api/sessions/${sessionId}/agent-logs`)

export default api
