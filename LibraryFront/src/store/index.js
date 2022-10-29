import {defineStore} from "pinia";
import {getPublishers, getWriters, getBooks} from '../api'

export const mainStore = defineStore('main',{
    state(){
        return {
            writersArray:[],
            publishersArray:[],
            booksArray:[],
        }
    },
    actions:{ // function
        async getWritersData(){ // 在pinia中发送请求
            let res = await getWriters();
            // console.log(res)
            let {code, message, data} = res.data
            if(code == 200){
                this.writersArray = res.data.data; //请求到的数据保存在state.writersList
                this.$message(message)
            }
        },
        async getPublishersData(){ // 在pinia中发送请求
            let res = await getPublishers();
            let {code, message, data} = res.data
            if(code == 200){
                this.publishersArray = res.data.data; //请求到的数据保存在state.writersList
                this.$message(message)
            }
        },
        async getBooksData(){ // 在pinia中发送请求
            let res = await getBooks();
            let {code, message, data} = res.data
            if(code == 200){
                this.booksArray = res.data.data; //请求到的数据保存在state.writersList
                this.$message(message)
            }
        },
    },
    persist:{ // 持久化
        enabled: true, // 开启
    }

})




