import axios from '../utils/request'

export function getList(){
    return axios({
        method:'get',
        url:'home/page/6/10',
    })
}

export function getWriters(){
    return request({
        url: 'writers',
        method: 'get'
    })
}