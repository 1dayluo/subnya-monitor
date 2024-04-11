<template>
    <div id="app">
    
    
    <nav class="home-nav">
        <ul id="menu">
            
            <h1>Dashboard</h1>
            <li v-for="menu in menus" :key="menu">{{ menu }}</li>
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
            "Home", 
            "Today's New", 
            "Logs", 
            "Scheduled Tasks", 
            "Run Statistics", 
            "Alert"]
        }
      }
    }
    
    
    </script>