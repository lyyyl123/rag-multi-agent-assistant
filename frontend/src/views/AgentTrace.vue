<template>
  <div class="trace-container">
    <el-card class="trace-card">
      <template #header>
        <div class="card-header">
          <span>Agent 执行过程</span>
        </div>
      </template>
      <div class="trace-content">
        <el-empty description="Agent 执行过程页面开发中" />
      </div>
    </el-card>
  </div>
</template>

<script setup>
// TODO: 第二阶段实现 Agent 执行过程展示
</script>

<style scoped>
.trace-container {
  max-width: 1200px;
  margin: 0 auto;
}

.trace-card {
  min-height: 500px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.trace-content {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
