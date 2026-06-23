<template>
  <div class="upload-container">
    <el-card class="upload-card">
      <template #header>
        <div class="card-header">
          <span>文档上传</span>
        </div>
      </template>
      <div class="upload-content">
        <el-empty description="文档上传页面开发中" />
      </div>
    </el-card>
  </div>
</template>

<script setup>
// TODO: 第二阶段实现文档上传功能
</script>

<style scoped>
.upload-container {
  max-width: 800px;
  margin: 0 auto;
}

.upload-card {
  min-height: 500px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.upload-content {
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
