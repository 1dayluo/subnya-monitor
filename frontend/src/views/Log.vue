<template>
    <div class="mockup-window border border-base-300">
    <div class="flex justify-center px-4 py-16 border-t border-base-300">
      <pre>日志内容:
{{ logfContent }}</pre>
    </div>
  </div>
</template>
<script>
import axios from "axios"

export default {
  name: 'LogRouter',
  data(){
    return {
      logfContent: '',
    }
  },
  mounted: function(){
    this.getLog()
  },
  methods: {
    getLog(){
      try {
        axios.get(`${process.env.VUE_APP_API_BASE_URL}/api/log`)
        .then((res) => {
            this.logfContent = res.data.data
        })
        } catch (error) {
        console.error("API 请求失败:", error);
        }
      }
  }
}
</script>
