import  { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue'
import Today from '../views/Today.vue'
import Log from '../views/Log.vue'
import Task from '../views/Task.vue'
import Statistics from '../views/Statistics.vue'
import Alert from '../views/Alert.vue'
// VueRouter.use(VueRouter)


const routes = [
    { path: '/', component: ()=>Home },
    { path: '/today', component: () => Today },
    { path: '/log', component: () => Log },
    { path: '/task', component: () => Task },
    { path: '/statistics', component: () => Statistics },
    { path: '/alert', component: () => Alert }

  ];
  
const router = createRouter({
  // 4. 内部提供了 history 模式的实现。为了简单起见，我们在这里使用 hash 模式。
  history: createWebHistory(),
  routes, // `routes: routes` 的缩写
})

export default router;