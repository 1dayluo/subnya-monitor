<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="container mx-auto">
    <div class="box p-6">
      <div class="flex  pl-1 ">
        <div class="w-1/3 outline-cyan-500  text-slate-700 bg-gray-300 rounded-lg ">
          <div class="grid place-content-center m-10  ">
            <h1 class="capitalize">dash board</h1>
            <div class="pt-6 ">
              <SideMenu class="hover:transition-all"/>
            </div>
          </div>  

          
        </div>
        <div class="w-2/3">    
          <div class="grid place-content-center m-10">
            <p>content</p>
          </div>
        </div>

      </div>

    </div>
  </div>

</template>

<script>
import SideMenu from './components/side.vue'

export default {
  name: 'App',
  components: {
    SideMenu
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