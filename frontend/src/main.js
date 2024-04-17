import { createApp } from 'vue'
import App from './App.vue'
import "../css/tailwind.css"
import router from './components/router'

const app = createApp(App).use(router)
app.mount('#app')

// new Vue({
//     router,
//     render: h => h(App),
//   }).\$mount('#app');