import request from "../utils/request";

export function create_writer(data){  //提交作者信息
    return request({
        url: 'create_writer',
        method: 'post',
        data
    })
}

export function get_all_writer(){
    return request({
        url: 'get_all_writer',
        method: 'get'
    })
}

export function create_publisher(data){
    return request({
        url: 'create_publisher',
        method: 'post',
        data
    })
}

export function get_all_publisher(){
    return request({
        url: 'get_all_publisher',
        method: 'get'
    })
}

export function get_all_book(){
    return request({
        url: 'get_all_book',
        method: 'get'
    })
}

export function delete_book(data){
    return request({
        url: 'delete_book',
        method: 'get',
        params: data
    })
}

export function delete_publisher(data){
    return request({
        url: 'delete_publisher',
        method: 'get',
        params: data
    })
}

