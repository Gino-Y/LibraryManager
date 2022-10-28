<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {listStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myListStore = listStore() // 实例化状态管理
const {writersList} = storeToRefs(myListStore); //
// // 异步请求
// function query(){
//   myListStore.getWritersData()
// }
// import {ref, onMounted} from "vue";
// const store = productStore() // 实例化状态
// let items = ref([]) // 初始化数据
//
// onMounted(async ()=>{
//   let res = await store.getWritersData
//   items.value = res.data.data
// })
</script>

<template>
  <n-table :bordered="false" :single-line="false" size="small">
    <tr>
      <th>姓名</th>
      <th>邮箱</th>
    </tr>
    <tr v-for="(item, index) in writersList" :key="item.id">
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