<template>

  <ul class="mt-6 space-y-1">
    <li v-for="menu in menus" :key="menu[0]">
      <router-link :to="menu[1]"  class="block rounded-lg px-4 py-2 text-sm font-medium text-gray-500 hover:bg-gray-100 hover:text-gray-700"
     
     >
      {{ menu[0] }}
      </router-link>

    </li>
  </ul>


  
  </template>


<script type="text/javascript">




export default {
  name: 'SideMenu',
  data() {
    return {
      menus:[
        ['首页','/'],
        ['今日新增', '/today'],
        ['运行日志','/log'],
        ['计划任务','/task'],
        ['运行统计','/statistics'],
        ['告警提醒','/alert'],
        ['添加域名','/add']
      ]
    }
  }
}


</script>