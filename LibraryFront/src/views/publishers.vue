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
const {publishersArray} = storeToRefs(myMainStore); //
import {create_publisher} from '../api'

function query(){
  myMainStore.getAllPublisher()
}
import {onMounted, reactive, ref} from "vue";

onMounted(async ()=>{
  await myMainStore.getAllPublisher()
})

let showModal= ref(false)
const formRef = ref(null);
const model = reactive({
  name:'请输入出版社'
})

function onPositiveClick(){ //弹框中单击确认调用函数
  create_publisher(model).then(res=>{   //发送请求，这里的请求不用在pinia中处理，因为每单一次就要请求
    console.log(res)
    //服务端如果返回200，这里调用下
    myMainStore.getAllPublisher()
  })
}

const rules = {
  name:[
    {
      required:true,
      message:'请输入出版社',
      trigger: ['input', 'blur']
    }
  ],
}

let id = ref()
function deletePublisher(id) {
  myMainStore.deletePublisher(id)
  myMainStore.getAllPublisher()
}
</script>

<template>
  <n-modal
      v-model:show="showModal"
      :mask-closable="false"
      preset="dialog"
      title="添加出版社"
      content="你确认"
      positive-text="确认"
      negative-text="取消"
      @positive-click="onPositiveClick"
      @negative-click="onNegativeClick"
      style="width: 80%;"
  >
    <n-form ref="formRef" :model="model" :rules="rules">
      <n-form-item path="name" label="出版社">
        <n-input v-model:value="model.name" @keydown.enter.prevent></n-input>
      </n-form-item>
    </n-form>
  </n-modal>

  <n-table :bordered="false" :single-line="false" size="small" striped>
    <thead>
      <tr>
        <th>删除</th>
        <th>编号</th>
        <th>出版社</th>
      </tr>
    </thead>
      <tr v-for="(item, index) in publishersArray" :key="item.id">
        <n-button
            @click="deletePublisher(item.id)"
            size="small"
            strong
            secondary
            circle
            type="error"
        >X</n-button>
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
      </tr>
  </n-table>

  <n-button @click="showModal = true">
    添加出版社
  </n-button>
</template>

<style scoped>

</style>