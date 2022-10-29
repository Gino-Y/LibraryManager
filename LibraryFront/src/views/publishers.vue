<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {listStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myListStore = listStore() // 实例化状态管理
const {publishersArray} = storeToRefs(myListStore); //

import {onMounted} from "vue";
onMounted(async ()=>{
  myListStore.getPublishersData()
})

</script>

<template>
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>出版社</th>
      </tr>
    </thead>
      <tr v-for="(item, index) in publishersArray" :key="item.id">
        <td>
            {{item.name}}
        </td>
      </tr>
  </n-table>

</template>

<style scoped>

</style>