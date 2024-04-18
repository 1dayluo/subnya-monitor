<template>
  <div>
    <nav class="flex flex-col space-y-2 p-4">
      <ul>
        <li v-for="menu in menus" :key="menu[0]" class="hover:bg-gray-700 rounded-md transition duration-200">
          <router-link :to="menu[1]" class="block py-2 px-4 text-gray-100 hover:text-gray-400">
            {{ menu[0] }}
          </router-link>
        </li>
      </ul>
    </nav>
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