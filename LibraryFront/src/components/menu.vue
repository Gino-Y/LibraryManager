<script setup>
import {
    NAnchor,
    NAnchorLink,
} from 'naive-ui'
</script>

<template>
    <n-anchor
        affix
        listen-to=".document-scroll-container"
        :trigger-top="24"
        :top="88"
        style="z-index: 1; height: 93.5vh; width: 100px"
        :bound="24"
    >
      <div></div><div></div>
      <router-link to="/writers">作者&nbsp;&nbsp;&nbsp;管理</router-link><br>
      <router-link to="/publishers">出版社管理</router-link><br>
      <router-link to="/books">书籍&nbsp;&nbsp;&nbsp;管理</router-link>

    </n-anchor>
</template>

<style scoped>
*{
  text-align: left;
  padding: 5px;
}
:focus{
  color: #397e92;
  background-color: #500000;
  font-weight:bold;
}
</style>