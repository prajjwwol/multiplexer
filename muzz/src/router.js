import { createRouter, createWebHistory } from 'vue-router'
import MultiplexerSelection from './components/MultiplexerSelection.vue'

const routes = [
  {
    path: '/multiplexer-selection',
    name: 'MultiplexerSelection',
    component: MultiplexerSelection
  }
  // other routes
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
