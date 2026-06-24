<template>
  <div class="chat-container">
    <el-card class="chat-card">
      <template #header>
        <div class="card-header">
          <span>智能问答</span>
          <el-button type="primary" size="small" @click="createNewSession">
            <el-icon><Plus /></el-icon>
            新对话
          </el-button>
        </div>
      </template>

      <!-- 消息列表 -->
      <div class="message-list" ref="messageListRef">
        <div v-if="messages.length === 0" class="empty-state">
          <el-empty description="开始你的第一个问题吧" />
        </div>
        <div v-else>
          <div v-for="(msg, index) in messages" :key="index" :class="['message-item', msg.role]">
            <div class="message-avatar">
              <el-icon v-if="msg.role === 'user'"><User /></el-icon>
              <el-icon v-else><Monitor /></el-icon>
            </div>
            <div class="message-content">
              <div class="message-text">{{ msg.content }}</div>
              <div v-if="msg.agent_trace && msg.agent_trace.length > 0" class="agent-trace">
                <el-collapse>
                  <el-collapse-item title="执行过程">
                    <div v-for="(trace, i) in msg.agent_trace" :key="i" class="trace-item">
                      <el-tag size="small">{{ trace.agent }}</el-tag>
                      <span class="trace-action">{{ trace.action }}</span>
                      <span class="trace-detail">{{ trace.detail }}</span>
                    </div>
                  </el-collapse-item>
                </el-collapse>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 输入区域 -->
      <div class="input-area">
        <el-input
          v-model="inputMessage"
          type="textarea"
          :rows="3"
          placeholder="输入你的问题..."
          @keydown.enter.ctrl="sendMessage"
        />
        <div class="input-actions">
          <span class="input-tip">Ctrl + Enter 发送</span>
          <el-button type="primary" @click="sendMessage" :loading="sending" :disabled="!inputMessage.trim()">
            发送
          </el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { ElMessage } from 'element-plus'
import { chat } from '../api'

const inputMessage = ref('')
const sending = ref(false)
const messages = ref([])
const currentSessionId = ref(null)
const messageListRef = ref(null)

const createNewSession = () => {
  messages.value = []
  currentSessionId.value = null
}

const scrollToBottom = async () => {
  await nextTick()
  if (messageListRef.value) {
    messageListRef.value.scrollTop = messageListRef.value.scrollHeight
  }
}

const sendMessage = async () => {
  const message = inputMessage.value.trim()
  if (!message) return

  // 添加用户消息
  messages.value.push({
    role: 'user',
    content: message,
  })

  inputMessage.value = ''
  sending.value = true

  await scrollToBottom()

  try {
    const response = await chat({
      message,
      session_id: currentSessionId.value,
    })

    const data = response.data

    // 更新会话 ID
    currentSessionId.value = data.session_id

    // 添加助手回复
    messages.value.push({
      role: 'assistant',
      content: data.message,
      agent_trace: data.agent_trace,
    })

    await scrollToBottom()
  } catch (error) {
    ElMessage.error('发送失败：' + (error.response?.data?.detail || error.message))
  } finally {
    sending.value = false
  }
}
</script>

<style scoped>
.chat-container {
  max-width: 1200px;
  margin: 0 auto;
}

.chat-card {
  height: calc(100vh - 160px);
  display: flex;
  flex-direction: column;
}

.chat-card :deep(.el-card__body) {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.message-list {
  flex: 1;
  overflow-y: auto;
  padding: 20px 0;
}

.empty-state {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.message-item {
  display: flex;
  margin-bottom: 20px;
  gap: 12px;
}

.message-item.user {
  flex-direction: row-reverse;
}

.message-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: #e4e7ed;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-shrink: 0;
}

.message-item.user .message-avatar {
  background: #409eff;
  color: white;
}

.message-content {
  max-width: 70%;
}

.message-text {
  background: #f4f4f5;
  padding: 12px 16px;
  border-radius: 8px;
  line-height: 1.6;
  word-break: break-word;
}

.message-item.user .message-text {
  background: #ecf5ff;
}

.agent-trace {
  margin-top: 8px;
}

.trace-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
  font-size: 12px;
  color: #909399;
}

.trace-action {
  font-weight: 500;
}

.input-area {
  margin-top: 16px;
  border-top: 1px solid #ebeef5;
  padding-top: 16px;
}

.input-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 8px;
}

.input-tip {
  font-size: 12px;
  color: #909399;
}
</style>
