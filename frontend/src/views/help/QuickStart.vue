<!-- QuickStart.vue -->
<template>
    <div>
      <h1>快速入门</h1>
      <section v-for="(item, index) in tutorials" :key="index" class="quickstart-section">
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
      </section>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const tutorials = ref([
    { title: '教程1', description: '教程1的简介' },
    { title: '教程2', description: '教程2的简介' },
    { title: '模块介绍', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' },
  ]);
  </script>
  
  <style scoped>
  .quickstart-section {
    margin-bottom: 20px;
  }
  </style>
  