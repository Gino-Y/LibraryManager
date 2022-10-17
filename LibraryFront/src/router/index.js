import { createRouter, createWebHashHistory} from "vue-router";
import Layout from '../layout/index.vue'

const routes = [
    {
        path: '/',
        name:'Layout',
        component: Layout,
    },
]

// 创建路由
const router = createRouter({
    history: createWebHashHistory(), // 路由的模式 哈希模式#
    linkActiveClass:'active', // 路由样式
    routes // 路由配置
})

// 使用router.beforeEach 注册一个全局前置首位
router.beforeEach((to, from, next)=>{
    console.log(to) //to.path
    next() // 下一步操作
    // if(to.path !='/home'){
    //     next({path:'/home'})
    // }else {
    //     next()
    // }
})

// 导出
export default router
