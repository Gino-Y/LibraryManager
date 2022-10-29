<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {listStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myListStore = listStore() // 实例化状态管理
const {writersArray} = storeToRefs(myListStore); //
// 异步请求
function query(){
  myListStore.getWritersData()
}
import {onMounted} from "vue";
onMounted(async ()=>{
  myListStore.getWritersData()
})
</script>

<template>
<!--  <n-button @click="query">Query Data</n-button>-->
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>姓名</th>
        <th>邮箱</th>
      </tr>
    </thead>
    <tr v-for="(item, index) in writersArray" :key="item.id">
      <td>
        <n-ellipsis style="max-width: 60px; font-size: small;">
          {{item.username}}
        </n-ellipsis>
      </td>
      <td>{{item.email}}</td>
    </tr>
  </n-table>

</template>

<style scoped>

</style>