import request from "../utils/request";

export function getWriters(){
    return request({
        url: 'writers',
        method: 'get'
    })
}