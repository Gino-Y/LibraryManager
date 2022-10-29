<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {mainStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myMainStore = mainStore() // 实例化状态管理
const {writersArray} = storeToRefs(myMainStore); //
// 异步请求
function query(){
  myMainStore.getWritersData()
}
import {onMounted} from "vue";
onMounted(async ()=>{
  myMainStore.getWritersData()
})
</script>

<template>
<!--  <n-button @click="query">Query Data</n-button>-->
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>编号</th>
        <th>姓名</th>
        <th>邮箱</th>
      </tr>
    </thead>
    <tr v-for="(item, index) in writersArray" :key="item.id">
      <td>{{item.id}}</td>
      <td>{{item.username}}</td>
      <td>{{item.email}}</td>
    </tr>
  </n-table>

</template>

<style scoped>

</style>