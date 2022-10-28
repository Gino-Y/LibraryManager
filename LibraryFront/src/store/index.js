import {defineStore} from "pinia";
import {getWriters} from '../api'

export const listStore = defineStore('list',{
    state(){
        return {
            writersList:[
                {id: '0', username: 'testname', email: 'test@test.com'}
            ]
        }
    },
    actions:{ // function
        async getWritersData(){ // 在pinia中发送请求
            let res = await getWriters();
            console.log(res.data)
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




