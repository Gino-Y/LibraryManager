import {defineStore} from "pinia";
import {getWriters, getList} from '../api'

export const listStore = defineStore('list',{
    state(){
        return {
            writersList:[]
        }
    },
    actions:{ // function
        async getWritersData(){ // 在pinia中发送请求
            let res = await getWriters();
            let {code, message, data} = res.data
            if(code == 200){
                this.writersList = res.data.data; //请求到的数据保存在state.writersList
                this.$message(message)
            }
        }
    },
    persist:{ // 持久化
        enabled: true, // 开启
    }

})




