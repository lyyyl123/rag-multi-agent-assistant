<template>
  <el-container class="app-container">
    <el-header>
      <div class="header-content">
        <h1>RAG Multi-Agent Assistant</h1>
        <el-menu
          :default-active="route.path"
          mode="horizontal"
          :router="true"
          class="header-menu"
        >
          <el-menu-item index="/">
            <el-icon><ChatDotRound /></el-icon>
            <span>智能问答</span>
          </el-menu-item>
          <el-menu-item index="/upload">
            <el-icon><Upload /></el-icon>
            <span>文档上传</span>
          </el-menu-item>
          <el-menu-item index="/history">
            <el-icon><Clock /></el-icon>
            <span>历史记录</span>
          </el-menu-item>
          <el-menu-item index="/agent-trace">
            <el-icon><View /></el-icon>
            <span>Agent 执行过程</span>
          </el-menu-item>
        </el-menu>
      </div>
    </el-header>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Helvetica Neue', Helvetica, 'PingFang SC', 'Hiragino Sans GB',
    'Microsoft YaHei', '微软雅黑', Arial, sans-serif;
}

.app-container {
  min-height: 100vh;
}

.el-header {
  background-color: #fff;
  border-bottom: 1px solid #e4e7ed;
  padding: 0 20px;
}

.header-content {
  display: flex;
  align-items: center;
  height: 60px;
}

.header-content h1 {
  font-size: 18px;
  color: #303133;
  margin-right: 50px;
  white-space: nowrap;
}

.header-menu {
  flex: 1;
  border-bottom: none !important;
}

.el-main {
  background-color: #f5f7fa;
  padding: 20px;
}
</style>
