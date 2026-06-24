<template>
  <div class="upload-container">
    <el-card class="upload-card">
      <template #header>
        <div class="card-header">
          <span>文档上传</span>
        </div>
      </template>

      <!-- 上传区域 -->
      <el-upload
        class="upload-dragger"
        drag
        :auto-upload="false"
        :on-change="handleFileChange"
        :file-list="fileList"
        accept=".pdf,.txt,.md,.markdown"
      >
        <el-icon class="el-icon--upload"><Upload /></el-icon>
        <div class="el-upload__text">
          将文件拖到此处，或<em>点击上传</em>
        </div>
        <template #tip>
          <div class="el-upload__tip">
            支持 PDF、TXT、Markdown 格式文件
          </div>
        </template>
      </el-upload>

      <!-- 上传按钮 -->
      <div class="upload-actions">
        <el-button type="primary" @click="handleUpload" :loading="uploading" :disabled="!selectedFile">
          {{ uploading ? '上传中...' : '开始上传' }}
        </el-button>
      </div>

      <!-- 上传结果 -->
      <div v-if="uploadResult" class="upload-result">
        <el-alert
          :title="uploadResult.success ? '上传成功' : '上传失败'"
          :type="uploadResult.success ? 'success' : 'error'"
          :description="uploadResult.message"
          show-icon
        />
      </div>

      <!-- 已上传文档列表 -->
      <div class="document-list">
        <h3>已上传文档</h3>
        <el-table :data="documents" style="width: 100%">
          <el-table-column prop="filename" label="文件名" />
          <el-table-column prop="file_type" label="类型" width="80" />
          <el-table-column prop="status" label="状态" width="100">
            <template #default="{ row }">
              <el-tag :type="row.status === 'completed' ? 'success' : row.status === 'failed' ? 'danger' : 'warning'">
                {{ row.status === 'completed' ? '已完成' : row.status === 'failed' ? '失败' : '处理中' }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column prop="chunk_count" label="切片数" width="80" />
          <el-table-column prop="created_at" label="上传时间" width="180">
            <template #default="{ row }">
              {{ new Date(row.created_at).toLocaleString() }}
            </template>
          </el-table-column>
        </el-table>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { ElMessage } from 'element-plus'
import { uploadDocument } from '../api'

const fileList = ref([])
const selectedFile = ref(null)
const uploading = ref(false)
const uploadResult = ref(null)
const documents = ref([])

const handleFileChange = (file) => {
  selectedFile.value = file.raw
}

const handleUpload = async () => {
  if (!selectedFile.value) {
    ElMessage.warning('请先选择文件')
    return
  }

  uploading.value = true
  uploadResult.value = null

  try {
    const formData = new FormData()
    formData.append('file', selectedFile.value)

    const response = await uploadDocument(formData)
    uploadResult.value = {
      success: true,
      message: response.data.message,
    }
    ElMessage.success('文档上传成功')

    // 刷新文档列表
    await loadDocuments()

    // 清空选择
    selectedFile.value = null
    fileList.value = []
  } catch (error) {
    uploadResult.value = {
      success: false,
      message: error.response?.data?.detail || '上传失败',
    }
    ElMessage.error('文档上传失败')
  } finally {
    uploading.value = false
  }
}

const loadDocuments = async () => {
  // TODO: 实现获取文档列表 API
  documents.value = []
}

onMounted(() => {
  loadDocuments()
})
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

.upload-dragger {
  width: 100%;
}

.upload-actions {
  margin-top: 20px;
  text-align: center;
}

.upload-result {
  margin-top: 20px;
}

.document-list {
  margin-top: 30px;
}

.document-list h3 {
  margin-bottom: 15px;
  color: #303133;
}
</style>
