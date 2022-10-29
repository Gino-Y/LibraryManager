import request from "../utils/request";

export function getWriters(){
    return request({
        url: 'writers',
        method: 'get'
    })
}

export function getPublishers(){
    return request({
        url: 'publishers',
        method: 'get'
    })
}

export function getBooks(){
    return request({
        url: 'books',
        method: 'get'
    })
}

