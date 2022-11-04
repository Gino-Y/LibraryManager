import axios from 'axios'

const request = axios.create({
    baseURL: "http://47.241.35.150:8030/", //基本路径
    timeout: 5000
});
//请求拦截器
request.interceptors.request.use(config => config);

//响应拦截器
request.interceptors.response.use(res => {
    return res
}, err => {
    return Promise.reject(err)
})

export default request;