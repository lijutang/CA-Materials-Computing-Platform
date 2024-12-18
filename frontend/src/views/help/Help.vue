<!-- Help.vue -->
<template>
    <div>
      <h1>帮助页面</h1>
      <iframe :src="iframeSrc" title="Help Content" class="help-iframe"></iframe>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  const iframeSrc = 'http://127.0.0.1:5000/u11485_input'; // 硬编码 iframe 链接作为示例
  </script>
  
  <style scoped>
  .help-iframe {
    width: 100%;
    height: 600px;
    border: none;
  }
  </style>
  