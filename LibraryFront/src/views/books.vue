<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {listStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myListStore = listStore() // 实例化状态管理
const {booksArray} = storeToRefs(myListStore); //

import {onMounted} from "vue";
onMounted(async ()=>{
  myListStore.getBooksData()
})

</script>

<template>
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>书名</th>
        <th>价格</th>
        <th>出版日期</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in booksArray" :key="item.id">
        <td>
          <!--        <n-ellipsis style="max-width: 60px; font-size: small;">-->
          {{item.title}}
          <!--        </n-ellipsis>-->
        </td>
          <td>{{item.price}}</td>
          <td>{{item.publisher_data}}</td>
      </tr>
    </tbody>
  </n-table>

</template>

<style scoped>

</style>