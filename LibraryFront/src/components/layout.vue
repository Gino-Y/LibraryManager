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
  darkTheme
} from 'naive-ui'
import Anchor from "./menu.vue";


</script>

<template>
    <n-config-provider :theme="flag?null:darkTheme" abstract>
<!--      <n-space vertical class="d">-->
        <n-layout >
          <n-layout-header >
            图书馆里系统
          </n-layout-header>
          <n-layout has-sider>
            <n-layout-sider content-style="padding: 24px;" >
              <Anchor/>
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

.n-layout-header{
  background: rgba(128, 128, 128, 0.2);
  /*background: red;*/
  padding: 10px;
  text-align: center;
}

.n-layout-sider {
  background: rgba(128, 128, 128, 0.3);
  /*background: red;*/
}

.n-layout-content {
  background: rgba(128, 128, 128, 0.4);
  /*background: red;*/

}
</style>