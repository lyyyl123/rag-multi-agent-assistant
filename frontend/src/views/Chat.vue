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
      <div class="chat-content">
        <el-empty description="智能问答页面开发中" />
      </div>
    </el-card>
  </div>
</template>

<script setup>
const createNewSession = () => {
  // TODO: 第二阶段实现
}
</script>

<style scoped>
.chat-container {
  max-width: 1200px;
  margin: 0 auto;
}

.chat-card {
  height: calc(100vh - 160px);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-content {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
