import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Chat',
    component: () => import('../views/Chat.vue'),
  },
  {
    path: '/upload',
    name: 'Upload',
    component: () => import('../views/Upload.vue'),
  },
  {
    path: '/history',
    name: 'History',
    component: () => import('../views/History.vue'),
  },
  {
    path: '/agent-trace',
    name: 'AgentTrace',
    component: () => import('../views/AgentTrace.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
