<!--suppress ALL -->
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
    NBreadcrumb,
    NBreadcrumbItem,
  darkTheme
} from 'naive-ui'
import Menu from "./menu.vue";


</script>

<template>
    <n-config-provider :theme="flag?null:darkTheme" abstract>
<!--      <n-space vertical >-->
        <n-layout >
          <n-layout-header >
            <div style="display: flex;
                  justify-content: center;
                  align-items: center;">
              <div style="width: 24px">
              <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512">
                <path d="M64 480H48a32 32 0 0 1-32-32V112a32 32 0 0 1 32-32h16a32 32 0 0 1 32 32v336a32 32 0 0 1-32 32z" fill="currentColor"></path>
                <path d="M240 176a32 32 0 0 0-32-32h-64a32 32 0 0 0-32 32v28a4 4 0 0 0 4 4h120a4 4 0 0 0 4-4z" fill="currentColor"></path>
                <path d="M112 448a32 32 0 0 0 32 32h64a32 32 0 0 0 32-32v-30a2 2 0 0 0-2-2H114a2 2 0 0 0-2 2z" fill="currentColor"></path>
                <rect x="112" y="240" width="128" height="144" rx="2" ry="2" fill="currentColor"></rect>
                <path d="M320 480h-32a32 32 0 0 1-32-32V64a32 32 0 0 1 32-32h32a32 32 0 0 1 32 32v384a32 32 0 0 1-32 32z" fill="currentColor"></path>
                <path d="M495.89 445.45l-32.23-340c-1.48-15.65-16.94-27-34.53-25.31l-31.85 3c-17.59 1.67-30.65 15.71-29.17 31.36l32.23 340c1.48 15.65 16.94 27 34.53 25.31l31.85-3c17.59-1.67 30.65-15.71 29.17-31.36z" fill="currentColor"></path>
              </svg>
              </div>
              <div>&nbsp;&nbsp;&nbsp;图书管理系统</div>
              <n-breadcrumb>
                <n-breadcrumb-item>&nbsp;&nbsp;&nbsp;图书管理系统</n-breadcrumb-item>
                <n-breadcrumb-item>天津分行</n-breadcrumb-item>
                <n-breadcrumb-item>天津分行</n-breadcrumb-item>
                <n-breadcrumb-item>天津分行</n-breadcrumb-item>
                <n-breadcrumb-item>天津分行</n-breadcrumb-item>
              </n-breadcrumb>
            </div>

          </n-layout-header>
          <n-layout has-sider>
            <n-layout-sider content-style="padding: 24px;" >

              <Menu/>
            </n-layout-sider>
            <n-layout-content content-style="padding: 24px;" >
              <router-view />
            </n-layout-content>
          </n-layout>
        </n-layout>
<!--      </n-space>-->
    </n-config-provider>
</template>

<style scoped>

.n-layout-header {
  background: rgba(128, 128, 128, 0.2);
  padding: 10px;
  text-align: center;
  font-weight:bold;
  color: #397e92;
}

.n-layout-sider {
  background: rgba(128, 128, 128, 0.3);
  /*background: red;*/
}

.n-layout-content {
  background: rgba(128, 128, 128, 0.4);
  background: rgba(0, 183, 255, 0.13);

}
</style>