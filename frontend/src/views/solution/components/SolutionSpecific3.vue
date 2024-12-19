<template>
    <div class="solution-specific">
      <h2>{{ config }} - 解决方案 3</h2>
      <iframe :src="iframeSrc" class="solution-iframe"></iframe>
  
      <div class="controls">
        <h3>选择功能</h3>
        <div>
          <input type="checkbox" id="enableFeature" v-model="isFeatureEnabled" />
          <label for="enableFeature">启用高级功能</label>
        </div>
  
        <label>
          配置名称：
          <input type="text" v-model="configName" />
        </label>
        <button @click="saveConfig">保存配置</button>
      </div>
  
      <div class="selection">
        <h3>多选列表</h3>
        <select multiple v-model="selectedItems">
          <option v-for="item in selectionOptions" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
        <button @click="submitSelection">提交选择</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SolutionSpecific3",
    props: {
      config: {
        type: String,
        required: true, // 父组件需要传递该值
      },
    },
    data() {
      return {
        iframeSrc: `http://127.0.0.1:5000/${this.config}_input`, // 动态加载 iframe 内容
        isFeatureEnabled: false, // 是否启用高级功能
        configName: "", // 用户输入的配置名称
        selectedItems: [], // 用户选择的多选项
        selectionOptions: ["选项1", "选项2", "选项3", "选项4"], // 可选项
      };
    },
    methods: {
      saveConfig() {
        console.log("解决方案 3 保存的配置：", this.configName);
      },
      submitSelection() {
        console.log("解决方案 3 提交的选择项：", this.selectedItems);
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
  
  .selection {
    margin-top: 20px;
  }
  
  label {
    display: block;
    margin-bottom: 10px;
  }
  
  select {
    margin-bottom: 10px;
    padding: 5px;
    width: 300px;
  }
  </style>
  