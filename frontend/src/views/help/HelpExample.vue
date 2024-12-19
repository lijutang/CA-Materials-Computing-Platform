<template>
    <div class="help-examples">
      <h2>示例目录</h2>
      <!-- 示例列表 -->
      <ul>
        <li v-for="example in examples" :key="example.id">
          <a :href="example.link" target="_blank">{{ example.title }}</a> - {{ example.description }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: "HelpExamples",
    data() {
      return {
        examples: [
          { id: 1, title: "示例 1", description: "这是第一个示例", link: "/example1" },
          { id: 2, title: "示例 2", description: "这是第二个示例", link: "/example2" },
          { id: 3, title: "示例 3", description: "这是第三个示例", link: "/example3" },
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .help-examples {
    max-width: 600px;
    margin: 20px auto;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
  }
  
  li {
    margin-bottom: 10px;
  }
  
  a {
    color: #007bff;
    text-decoration: none;
  }
  
  a:hover {
    text-decoration: underline;
  }
  </style>