import axios from 'axios'
const request = axios.create({
    baseURL:"/", //基本路径
    timeout:1000
});
//请求拦截器
request.interceptors.request.use(config=>config);

//响应拦截器
request.interceptors.response.use(res=>{
    return res
},err=>{
    return Promise.reject(err)
})

export default request;