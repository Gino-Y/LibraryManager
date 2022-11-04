import {defineStore} from "pinia";
import {
    get_all_publisher,
    get_all_writer,
    get_all_book,
    delete_book,
    delete_publisher,
    delete_writer,
} from '../api'

export const mainStore = defineStore('main',{
    state(){
        return {
            writersArray:[],
            publishersArray:[],
            booksArray:[],
        }
    },
    actions:{ // function
        async getAllWriter(){ // 在pinia中发送请求
            let res = await get_all_writer();
            // console.log(res)
            let {code, message, data} = res.data
            if(code == 200){
                this.writersArray = res.data.data; //请求到的数据保存在state.writersList
                this.publishersArray.message
            }
        },
        async getAllPublisher(){ // 在pinia中发送请求
            let res = await get_all_publisher();
            let {code, message, data} = res.data
            if(code == 200){
                this.publishersArray = res.data.data; //请求到的数据保存在state.writersList
                this.publishersArray.message
            }
        },
        async getAllBook(){ // 在pinia中发送请求
            let res = await get_all_book();
            let {code, message, data} = res.data
            if(code == 200){
                this.booksArray = res.data.data; //请求到的数据保存在state.writersList
                this.publishersArray.message
            }
        },
        async deleteBook(id){
            let res = await delete_book({id: id});
            let {code, message, data} = res.data
            if(code == 200){
                this.booksArray = res.data.data;
                this.publishersArray.message
            }
        },
        async deletePublisher(id){
            let res = await delete_publisher({id: id});
            let {code, message, data} = res.data
            if(code == 200){
                this.booksArray = res.data.data;
                this.publishersArray.message
            }
        },
        async deleteWriter(id){
            let res = await delete_writer({id: id});
            console.log(res)
            let {code, message, data} = res.data
            if(code == 200){
                this.booksArray = res.data.data;
                this.publishersArray.message
            }
        },
    },
    persist:{ // 持久化
        enabled: true, // 开启
    }

})




