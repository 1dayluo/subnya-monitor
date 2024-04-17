<template>
    <!-- <div> -->
      <div id="history-files" class="flex">
        <h1>History</h1>
      </div>
      <div id="monitor" class="flex">
        <h1>Monitor domains</h1>
      </div>
    <!-- </div> -->
</template>

<script>
import axios from "axios";

export default {
  name: 'homeIndex',
  methods:{
   outfile(){
    axios.get('/api/outfile/${{ route.params.filedate}}')
    .then((res) => {
      
    })
   },
   getlist_outfiles(){
    axios.get('/api/get_outfile')
    .then((res) => {

    })
   } 
  }
}
</script>