<template>
  <div class="history-container">
    <el-card class="history-card">
      <template #header>
        <div class="card-header">
          <span>历史记录</span>
        </div>
      </template>
      <div class="history-content">
        <el-empty description="历史记录页面开发中" />
      </div>
    </el-card>
  </div>
</template>

<script setup>
// TODO: 第二阶段实现历史记录功能
</script>

<style scoped>
.history-container {
  max-width: 1200px;
  margin: 0 auto;
}

.history-card {
  min-height: 500px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.history-content {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
