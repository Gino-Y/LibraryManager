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
<!--        <n-anchor-link title="作者管理" to="/authors" />-->
<!--        <n-anchor-link title="出版社管理" href="/publishers" />-->
<!--        <n-anchor-link title="书籍管理" href="/books" />-->

      <router-link to="/writers">作者管理</router-link><br>
      <router-link to="/publishers">出版社管理</router-link><br>
      <router-link to="/books">书籍管理</router-link>

    </n-anchor>
</template>

<style scoped>
*{
  text-align: left;
  padding: 5px;
}
</style>