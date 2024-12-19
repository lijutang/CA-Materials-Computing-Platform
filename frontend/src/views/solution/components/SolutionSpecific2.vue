<template>
    <div class="solution-specific">
      <h2>{{ config }} - 解决方案 2</h2>
      <iframe :src="iframeSrc" class="solution-iframe"></iframe>
      <div class="options">
        <h3>功能选项</h3>
        <select v-model="selectedOption" @change="handleOptionChange">
          <option v-for="option in options" :key="option.value" :value="option.value">
            {{ option.label }}
          </option>
        </select>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "SolutionSpecific2",
    props: {
      config: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        iframeSrc: "http://127.0.0.1:5000/u10373_input", // iframe动态加载URL
        options: [
          { label: "查看数据", value: "viewData" },
          { label: "单位设置", value: "units" },
          { label: "工具设置", value: "tools" },
        ],
        selectedOption: "viewData",
      };
    },
    methods: {
      handleOptionChange() {
        console.log("选择的选项：", this.selectedOption);
      },
    },
  };
  </script>
  