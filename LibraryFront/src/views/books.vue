<script setup>
import {NButton, NEllipsis, NTable} from 'naive-ui'

import {mainStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myMainStore = mainStore() // 实例化状态管理
const {booksArray} = storeToRefs(myMainStore); //

import {onMounted} from "vue";
onMounted(async ()=>{
  myMainStore.getBooksData()
})

</script>

<template>
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>书籍编号</th>
        <th>书名</th>
        <th>作者信息</th>
        <th>出版社</th>
        <th>价格</th>
        <th>出版日期</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, index) in booksArray" :key="item.id">
        <td>{{item.id}}</td>
        <td>{{item.title}}</td>
        <td>
          <div>{{item.writers.username}}</div>
          <div style="color: rgba(249,249,249,0.5)">{{item.writers.email}}</div>
        </td>
        <td class="start">
          <div v-for="(itemp, index) in item.publishers" :key="itemp.id">
            {{itemp.name}}
          </div>
        </td>
        <td>{{item.price}}</td>
        <td>{{item.publisher_data}}</td>
      </tr>
    </tbody>
  </n-table>

</template>

<style scoped>

</style>