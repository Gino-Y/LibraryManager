<script setup>
import {listStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myListStore = listStore() // 实例化状态管理
const {items} = storeToRefs(myListStore); //
// 异步请求
function query(){
  myListStore.getWritersData()
}
</script>

<template>
  <div>authors</div>
</template>

<style scoped>

</style>