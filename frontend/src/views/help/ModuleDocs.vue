<!-- ModuleDocs.vue -->
<template>
    <div>
      <h1>文档与模块</h1>
      <div v-for="(doc, index) in docs" :key="index" class="doc-section">
        <h2>{{ doc.title }}</h2>
        <p>{{ doc.content }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const docs = ref([
    { title: '概括文档', content: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' },
    { title: '桌面基础知识', content: 'Proin gravida dolor sit amet lacus accumsan et viverra justo commodo.' },
  ]);
  </script>
  
  <style scoped>
  .doc-section {
    margin-bottom: 20px;
  }
  </style>
  