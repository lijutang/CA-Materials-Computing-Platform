<template>
    <div>
      <!-- Test 页面内容 -->
      <section>
        <h2>Test 页面 - Section 1</h2>
        <div>
          <!-- test.html 内容 -->
          <p>这里是 test.html 的内容。</p>
        </div>
      </section>
      <section>
        <h2>Test 页面 - Section 2</h2>
        <div>
          <!-- test1.html 内容 -->
          <p>这里是 test1.html 的内容。</p>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Test'
  };
  </script>
  
  <style scoped>
  h2 {
    font-size: 20px;
    color: #555;
  }
  
  section {
    margin-bottom: 20px;
  }
  </style>
  