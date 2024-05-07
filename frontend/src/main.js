import { createApp } from 'vue'
import App from './App.vue'
import "../css/tailwind.css"
import router from './components/router'
import Notifications from '@kyvg/vue3-notification'

const app = createApp(App).use(router)
app.use(Notifications)
app.mount('#app')

// new Vue({
//     router,
//     render: h => h(App),
//   }).\$mount('#app')