<template>
  <!-- <div> -->
    <notifications />
    <header class="bg-gray-50">
    <div class="mx-auto max-w-screen-xl px-4 py-8 sm:px-6 sm:py-12 lg:px-8">
      <div class="sm:flex sm:items-center sm:justify-between">
        <div class="text-center sm:text-left">
          <h1 class="text-2xl font-bold text-gray-900 sm:text-3xl">Welcome Back！ </h1>

          <p class="mt-1.5 text-sm text-gray-500">下一代子域名监控平台，监控任意目标 🎉</p>
        </div>

        <div class="mt-4 flex flex-col gap-4 sm:mt-0 sm:flex-row sm:items-center">
          <button
            class="inline-flex items-center justify-center gap-1.5 rounded-lg border border-gray-200 bg-white px-5 py-3 text-gray-500 transition hover:text-gray-700 focus:outline-none focus:ring"
            type="button"
          >
            <span class="text-sm font-medium"> View Website </span>

            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-4 w-4"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              stroke-width="2"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
              />
            </svg>
          </button>

          <button
            class="block rounded-lg bg-indigo-600 px-5 py-3 text-sm font-medium text-white transition hover:bg-indigo-700 focus:outline-none focus:ring"
            type="button" onclick="my_modal_2.showModal()"
          >
            增加监控
          </button>
          <dialog id="my_modal_2" class="modal">
            <div class="modal-box card">
              <div class="card-body items-center text-center">
                <h3 class="font-bold text-lg card-title">Add!</h3>
                <p class="py-4">Press ESC key or input subdomain</p>
                <input type="text" v-model="addMonitor" placeholder="输入域名，例如：www.github.com" class="input input-bordered w-full max-w-xs" />
                <div class="card-body items-center text-center">
                  <div class="card-actions">
                    <button class="btn justify-end " @click="add_monitor">提交</button>
                  </div>
                </div>
              </div>
            </div>
            <form method="dialog" class="modal-backdrop">
              <button>close</button>
            </form>
          </dialog>
        </div>
      </div>
    </div>
  </header>

    <br /> <br />
    
    <div class="text-xl font-medium m-2">
        当前监控：
    </div>
    <subdomainList :my-array="monitorList"></subdomainList>
    <!-- <div id="monitor" class="">
      <h1>监控域名</h1>
      <li v-for="domain in monitorList" :key="domain">
         {{  domain  }}
      </li>
    </div> -->
  <!-- </div> -->
</template>

<script>


import  subdomainList from "../components/subdomainList.vue"
import axios from "axios"




export default {
name: 'homeIndex',
data() {
  return {
    monitorList: '',
    addMonitor: '',
  }
},
components: {
  subdomainList
  },
methods:{
 outfile(){
  axios.get(`${process.env.VUE_APP_API_BASE_URL}/api/outfile/${route.params.filedate}`)
  .then((res) => {
    
  })
 },
 getlist_outfiles(){

 },
 add_monitor(){
    const reg = /^(?=^.{3,255}$)[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+$/;
    if (!reg.test(this.addMonitor)) {
              this.$notify({
                text: "格式错误",
                title: "warning",
              });
      }
    else {
      axios.post(`${process.env.VUE_APP_API_BASE_URL}/api/add_monitor`, {
         domain: this.addMonitor
      },
      {  headers: {
        'Content-Type': 'application/json'
      }})
      .then((res) => {
        this.$notify("添加成功");
      })
    }
 }
},
async created() {
  try {

    axios.get(`${process.env.VUE_APP_API_BASE_URL}/api/get_monitored`)
    .then((res) => {
        this.monitorList = res.data.domains
    })
  } catch (error) {
    console.error("API 请求失败:", error);
  }
},
}

</script>