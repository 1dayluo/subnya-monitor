<template>
  <div id="app">
    <nav class="home-nav">
      <ul id="menu">
        <li v-for="menu in menus" :key="menu[0]">
          <!-- 我不会告诉你 我注视掉没有删掉只是觉得很好玩x （⬇️谁点到算谁狠） -->
          <!-- <button type="button" class="animate-spin transition duration-300 cursor-pointer"> -->
           
              <button type="button" class=" transition duration-300 cursor-pointer pt-4 ">
              <!-- <a :href="menu[1]" class="text-gray-100 hover:text-gray-400 ">{{ menu[0] }}</a> -->
              <router-link :to="menu[1]" class="text-gray-100 hover:text-gray-400 ">{{ menu[0] }}</router-link>

              </button>
           
        </li>
      </ul>
    </nav>
    <!-- File List Section -->
  </div>
</template>

<script type="text/javascript">




export default {
  name: 'SideMenu',
  data() {
    return {
      menus:[
        ['Home','/'],
        ['Today\'s New', '/today'],
        ['Logs','/log'],
        ['Scheduled Tasks','/task'],
        ['Run Statistics','/statistics'],
        ['Alert','/alert']
      ]
    }
  }
}


</script>