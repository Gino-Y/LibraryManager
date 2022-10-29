<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {mainStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myMainStore = mainStore() // 实例化状态管理
const {publishersArray} = storeToRefs(myMainStore); //

import {onMounted} from "vue";
onMounted(async ()=>{
  myMainStore.getPublishersData()
})

</script>

<template>
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>编号</th>
        <th>出版社</th>
      </tr>
    </thead>
      <tr v-for="(item, index) in publishersArray" :key="item.id">
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
      </tr>
  </n-table>

</template>

<style scoped>

</style>