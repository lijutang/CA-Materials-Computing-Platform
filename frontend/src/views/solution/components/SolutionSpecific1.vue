<template>
    <div class="solution-specific">
      <h2>{{ config }} - 解决方案 1</h2>
      <iframe :src="iframeSrc" class="solution-iframe"></iframe>
  
      <div class="controls">
        <label>
          输入值：
          <input type="text" v-model="inputValue" />
        </label>
        <button @click="submitSolution">提交</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SolutionSpecific1",
    props: {
      config: {
        type: String,
        required: true, // 父组件需要传递该值
      },
    },
    data() {
      return {
        iframeSrc: `http://127.0.0.1:5000/${this.config}_input`, // 动态加载 iframe 内容
        inputValue: "", // 输入框的值
      };
    },
    methods: {
      submitSolution() {
        console.log("解决方案 1 提交值：", this.inputValue);
      },
    },
  };
  </script>
  
  <style scoped>
  .solution-specific {
    display: flex;
    flex-direction: column;
  }
  
  .solution-iframe {
    width: 100%;
    height: 600px;
    border: none;
  }
  
  .controls {
    margin-top: 20px;
  }
  
  label {
    margin-bottom: 10px;
    display: block;
  }
  </style>
  