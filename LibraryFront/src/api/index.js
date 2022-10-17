import axios from '../utils/request'

export function getList(){
    return axios({
        method:'get',
        url:'home/page/6/10',
    })
}

