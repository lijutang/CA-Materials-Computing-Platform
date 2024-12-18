<!-- LeftMenu.vue -->
<template>
    <aside class="menu">
      <ul>
        <li v-for="(item, index) in menuItems" :key="index" @click="selectMenu(item)">
          {{ item }}
        </li>
      </ul>
    </aside>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const menuItems = ref(['Reaction', 'Equilib', 'Phase Diagram', 'Predom', 'EpH', 'Optimize']);
  const selectMenu = (item) => {
    console.log(`Selected menu: ${item}`);
  };
  </script>
  
  <style scoped>
  .menu {
    width: 200px;
    background-color: #f0f0f0;
    padding: 10px;
    height: 100%;
  }
  
  .menu ul {
    list-style: none;
    padding: 0;
  }
  
  .menu li {
    padding: 10px;
    cursor: pointer;
  }
  
  .menu li:hover {
    background-color: #d0d0d0;
  }
  </style>
  