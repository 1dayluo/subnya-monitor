<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <div class="container mx-auto">

    <div class="flex  pl-1 ">
      <div class="w-1/6 outline-cyan-500  text-slate-700 rounded-lg bg-gradient-to-b from-sky-800 to-indigo-800 ">
        <div class="grid place-content-center m-10 h-screen">

          <div class="pt-6 ">
            <SideMenu class="hover:transition-all"/>
            <!-- <route-view></route-view> -->
          </div>
        </div>  

        
      </div>
      <div class="w-5/6">    
        <!-- <div class="grid place-content-center m-10"> -->
          <router-view></router-view>
        <!-- </div> -->
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
  },


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