<template>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <!-- {{ monitor_config  }} -->
    <!-- {{ Object.keys(monitor_config).length }} -->
    <!-- {{ Object.keys(monitor_config).length === 0 }} -->
    <div v-if="Object.keys(monitor_config).length != 0" class=" mx-auto  min-h-screen">
      <div class="flex h-full  min-h-screen">
        <!-- 左侧导航栏 -->
        <!-- <div class="w-1/6 "> -->
        <div class="fixed h-full w-1/6">
            <div class=" flex  h-screen flex-col justify-between border-e bg-white">
            <div class="px-4 py-6">
                <span class="grid h-10 w-32 place-content-center rounded-lg bg-gray-100 text-xs text-gray-600">
                    Subnya-Monitor 
                </span>

                <ul class="mt-6 space-y-1">
                    <SideMenu></SideMenu>
                </ul>
            </div>

            <div class="sticky inset-x-0 bottom-0 border-t border-gray-100">
                <a href="#" class="flex items-center gap-2 bg-white p-4 hover:bg-gray-50">
                <img
                    alt=""
                    src="https://img2.woyaogexing.com/2017/06/26/0d722bd19ef69c88!400x400_big.jpg"
                    class="size-10 rounded-full object-cover"
                />

                <div>
                    <p class="text-xs">
                    <strong class="block font-medium">1Dayluo</strong>
                    5ms2hu11@duck.com
                    <span>  </span>
                    </p>
                </div>
                </a>
            </div>
            </div>

        </div>
        <!-- 右侧内容区 -->
        <div class=" w-5/6 p-10">
          <div class="mx-auto container ">
          <!-- <router-tree :routes="routes" /> -->
          <router-view />
          </div>
        </div>
      </div>
    </div>
  
    <div v-else>
      <div class="flex items-center justify-center h-screen bg-gray-100">
        
      <form class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" @submit.prevent="submitConfigPath">
        <div class="mb-4">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="configPath">
            Config 路径
          </label>
          <input
            class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
            id="configPath"
            type="text"
            placeholder="/path/to/config"
            v-model="configPath"
          />
        </div>
        <p v-if="message" :class="{'text-red-500': isError}">{{ message }} </p>
        <div class="flex items-center justify-between">
          <button
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            type="submit"
          >
            设置路径
          </button>
        </div>
       
      </form>
      </div>
    </div>
  
  </template>
  
  <script> 
  import axios from 'axios';
  import SideMenu from './components/side.vue'
  
  export default {
    name: 'App',
    components: {
      SideMenu
    },
    data(){
      return {
        monitor_config:{},
        configPath:'',
        message:''
      }
    },
    async created() {
      try {
        // console.log(process.env.VUE_APP_API_BASE_URL)
        const apiUrl=`${process.env.VUE_APP_API_BASE_URL}/api/read_config`
        axios.get(apiUrl)
        .then((res) => {
          this.monitor_config = res.data
          console.log(this.monitor_config)
        })
      } catch(error) {
        console.log("API 请求失败:", error)
      }
      
    },
    methods: {
      submitConfigPath() {
        console.log(this.configPath)
        this.message = 'Path does not exist'
        const apiUrl=`${process.env.VUE_APP_API_BASE_URL}/api/set-config-path`
        axios.post(apiUrl, { path: this.configPath }).then((res) => {
          if(res.status===200){
            console.log(res);
            this.monitor_config=res.data.path
  
          } 
        }).catch((error) => 
        {
          this.message = 'Please check your path!'
        })
  
      }
  
    }
  
    }
  </script>
  
  <!-- <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style> -->