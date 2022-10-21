import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router/index"; // 导入路由
import {createPinia} from "pinia";
import piniaPluginPersist from 'pinia-plugin-persist' // keep data
const pinia = createPinia()
pinia.use(piniaPluginPersist) // use keep data

// import ElementPlus from 'element-plus'
// import 'element-plus/dist/index.css'

createApp(App).mount('#app')
const app = createApp(App)
app.use(router)
app.use(pinia)
// app.use(ElementPlus)
app.mount('#app')
