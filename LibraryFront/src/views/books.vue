<script setup>
import {NButton, NEllipsis, NTable, NModal} from 'naive-ui'

import {mainStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myMainStore = mainStore() // 实例化状态管理
const {booksArray} = storeToRefs(myMainStore); //

import {onMounted, ref} from "vue";
onMounted(async ()=>{
  myMainStore.getBooksData()
})

let showModal= ref(false)

const form = {
  username: '',
  email: '',
}
</script>

<template>
  <n-button @click="showModal = true">
    来吧
  </n-button>

  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>编号</th>
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

  <n-modal
      v-model:show="showModal"
      :mask-closable="false"
      preset="dialog"
      title="确认"
      content="你确认"
      positive-text="确认"
      negative-text="算了"
      @positive-click="onPositiveClick"
      @negative-click="onNegativeClick"
      style="
          opacity: 0.925;
          width: 80%;
          height: 80%;
            "
  />

</template>

<style scoped>

</style>