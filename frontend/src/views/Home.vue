<template>
    <!-- <div> -->
      <div id="history-files" class="">
        <h1>History</h1>

        
      </div>
      <div id="monitor" class="">
        <h1>Monitor domains</h1>
        <li v-for="domain in monitorList" :key="domain">
           {{  domain  }}
        </li>
      </div>
    <!-- </div> -->
</template>

<script>
import axios from "axios";

export default {
  name: 'homeIndex',
  data() {
    return {
      monitorList: ''
    }
  },

  methods:{
   outfile(){
    axios.get(`${process.env.VUE_APP_API_BASE_URL}/api/outfile/${route.params.filedate}`)
    .then((res) => {
      
    })
   },
   getlist_outfiles(){

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