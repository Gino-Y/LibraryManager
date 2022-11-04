<script setup>
import {
    NButton,
    NEllipsis,
    NTable,
    NModal,
    NForm,
    NFormItem,
    NInput,
    NRow,
    NCol,
} from 'naive-ui'

import {mainStore} from '../store/index'; // 导入状态管理
import {storeToRefs} from 'pinia'
const myMainStore = mainStore() // 实例化状态管理
const {writersArray} = storeToRefs(myMainStore); //
// 异步请求
function query(){
  myMainStore.getAllWriter()
}

import {onMounted, ref, reactive } from "vue";
import {create_writer} from '../api'

onMounted(async ()=>{
  console.log(writersArray)
  await myMainStore.getAllWriter()
})

let showModal= ref(false)
const formRef = ref(null);
const model = reactive({
  username:'请输入作者姓名',
  email:'请输入作者邮箱'
})
// const rules = {}
const rules = {
  username:[
    {
      required:true,
      message:'请输入用户名',
      trigger: ['input', 'blur']
    }
  ],
  email:[
    {
      required:true,
      message:'请输入邮箱',
      trigger: ['input', 'blur']
    }
  ]
}
function onPositiveClick(){ //弹框中单击确认调用函数
  create_writer(model).then(res=>{   //发送请求，这里的请求不用在pinia中处理，因为每单一次就要请求
    console.log(res)
    //服务端如果返回200，这里调用下
    myMainStore.getAllWriter()
  })
}
//为什么要添加到formdata，因为文件上传是通过文件流的文件，提交的文件需要放在formdata中

// function creatWriter(model).then(res=>{})
</script>

<template>
  <n-modal
      v-model:show="showModal"
      :mask-closable="false"
      preset="dialog"
      title="添加作者信息"
      content="你确认"
      positive-text="确认"
      negative-text="取消"
      @positive-click="onPositiveClick"
      @negative-click="onNegativeClick"
      style="width: 80%;"
  >
    <n-form ref="formRef" :model="model" :rules="rules">
      <n-form-item path="username" label="姓名">
        <n-input v-model:value="model.username" @keydown.enter.prevent></n-input>
      </n-form-item>
      <n-form-item path="email" label="邮箱">
        <n-input v-model:value="model.email" @keydown.enter.prevent></n-input>
      </n-form-item>
    </n-form>

<!--    <n-form ref="formRef" :model="model" :rules="rules">-->
<!--      <n-form-item path="age" label="年龄">-->
<!--        <n-input v-model:value="model.age" @keydown.enter.prevent />-->
<!--      </n-form-item>-->
<!--      <n-form-item path="password" label="密码">-->
<!--        <n-input-->
<!--            v-model:value="model.password"-->
<!--            type="password"-->
<!--            @input="handlePasswordInput"-->
<!--            @keydown.enter.prevent-->
<!--        />-->
<!--      </n-form-item>-->
<!--      <n-form-item-->
<!--          ref="rPasswordFormItemRef"-->
<!--          first-->
<!--          path="reenteredPassword"-->
<!--          label="重复密码"-->
<!--      >-->
<!--        <n-input-->
<!--            v-model:value="model.reenteredPassword"-->
<!--            :disabled="!model.password"-->
<!--            type="password"-->
<!--            @keydown.enter.prevent-->
<!--        />-->
<!--      </n-form-item>-->
<!--      <n-row :gutter="[0, 24]">-->
<!--        <n-col :span="24">-->
<!--          <div style="display: flex; justify-content: flex-end">-->
<!--            <n-button-->
<!--                :disabled="model.age === null"-->
<!--                round-->
<!--                type="primary"-->
<!--                @click="handleValidateButtonClick"-->
<!--            >-->
<!--              验证-->
<!--            </n-button>-->
<!--          </div>-->
<!--        </n-col>-->
<!--      </n-row>-->
<!--    </n-form>-->
  </n-modal>
  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>编号</th>
        <th>姓名</th>
        <th>邮箱</th>
      </tr>
    </thead>
    <tr v-for="(item, index) in writersArray" :key="item.id">
      <td>{{item.id}}</td>
      <td>{{item.username}}</td>
      <td>{{item.email}}</td>
    </tr>
  </n-table>

  <n-button @click="showModal = true">
    添加作者
  </n-button>
</template>

<style scoped>

</style>