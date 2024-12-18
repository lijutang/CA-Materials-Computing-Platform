<!-- Results.vue -->
<template>
    <div class="results-page">
      <header>
        <h1>Results Page</h1>
      </header>
      <div class="content">
        <!-- 左侧菜单栏 -->
        <LeftMenu />
  
        <!-- 结果显示区域 -->
        <div class="results-section">
          <ResultsDisplay />
          <SaveResult />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import LeftMenu from './components/LeftMenu.vue';
  import ResultsDisplay from './components/ResultsDisplay.vue';
  import SaveResult from './components/SaveResult.vue';
  </script>
  
  <style scoped>
  .results-page {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }
  
  header {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    font-size: 20px;
  }
  
  .content {
    display: flex;
    flex: 1;
  }
  
  .results-section {
    flex: 1;
    padding: 20px;
    background: #ffffff;
    overflow: auto;
  }
  </style>
  