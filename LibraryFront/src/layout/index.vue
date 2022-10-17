<script setup>
import {
  NConfigProvider,
  NCard,
  NSpace,
  NLayout,
  NLayoutHeader,
  NLayoutContent,
  NLayoutFooter,
  NAnchor,
  NAnchorLink,
  NPagination,
  NGrid,
  NGridItem,
  NScrollbar,
  NSwitch,
  darkTheme
} from 'naive-ui'
import Header from './Header/index.vue'
import Main from './Main/index.vue'
import SidBar from './SidBar/index.vue'
// import {
//     ElHeader,
//     ElContainer,
//     ElAside,
// } from 'element-plus'
</script>

<template>
<!--  <el-header>图书管理系统</el-header>-->
<!--  <Header/>-->
<!--  <Main/>-->
<!--  <SidBar/>-->
<!--  <div>qwe</div>-->
<!--  <el-row class="mb-4">-->
<!--    <el-button>Default</el-button>-->
<!--    <el-button type="primary">Primary</el-button>-->
<!--    <el-button type="success">Success</el-button>-->
<!--    <el-button type="info">Info</el-button>-->
<!--    <el-button type="warning">Warning</el-button>-->
<!--    <el-button type="danger">Danger</el-button>-->
<!--  </el-row>-->
<!--  <div class="common-layout">-->
<!--    <el-container>-->
<!--      <el-header>Header</el-header>-->
<!--      <el-container>-->
<!--        <el-aside width="200px">Aside</el-aside>-->
<!--        <el-main>Main</el-main>-->
<!--      </el-container>-->
<!--    </el-container>-->
<!--  </div>-->
  <n-config-provider :theme="flag?null:darkTheme" abstract>
  <n-space vertical size="large">
    <n-layout>
      <n-layout-header >颐和园路</n-layout-header>
      <n-layout has-sider>
        <n-layout-sider content-style="padding: 24px;" >
          海淀桥
        </n-layout-sider>
        <n-layout-content content-style="padding: 24px;" >
          平山道
        </n-layout-content>
      </n-layout>
<!--      <n-layout-footer>成府路</n-layout-footer>-->
    </n-layout>
  </n-space>
  </n-config-provider>
</template>

<style scoped>
/*.n-config-provider{*/
/*  width: 1000px;*/
/*}*/
.n-layout-header,
.n-layout-footer {
  background: rgba(128, 128, 128, 0.2);
  padding: 10px;
}

.n-layout-sider {
  background: rgba(128, 128, 128, 0.3);
}

.n-layout-content {
  background: rgba(128, 128, 128, 0.4);
}
</style>