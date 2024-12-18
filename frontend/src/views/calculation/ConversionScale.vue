<template>
    <div class="conversion-scale-page">
      <!-- 页面标题 -->
      <h1>Conversion Scale</h1>
  
      <!-- X轴和Y轴比例选择 -->
      <div class="axis-section">
        <label for="x-axis">X-axis:</label>
        <select v-model="xAxis" id="x-axis">
          <option value="scale1">Scale 1</option>
          <option value="scale2">Scale 2</option>
        </select>
  
        <label for="y-axis">Y-axis:</label>
        <select v-model="yAxis" id="y-axis">
          <option value="scale1">Scale 1</option>
          <option value="scale2">Scale 2</option>
        </select>
      </div>
  
      <!-- 转换比例输入框 -->
      <div class="scale-input-section">
        <label for="scale-type">Scale Type:</label>
        <input v-model="scaleType" id="scale-type" type="text" placeholder="Enter scale type" />
  
        <label for="multiplication-factor">Multiplication Factor:</label>
        <input v-model="multiplicationFactor" id="multiplication-factor" type="number" placeholder="Enter factor" />
  
        <label for="translation">Translation:</label>
        <input v-model="translation" id="translation" type="number" placeholder="Enter translation value" />
      </div>
  
      <!-- 按钮部分 -->
      <div class="button-section">
        <button @click="applyConversion" class="apply-button">Apply</button>
        <button @click="resetFields" class="reset-button">Reset</button>
      </div>
  
      <!-- 结果展示 -->
      <div v-if="result" class="result-section">
        <h2>Results</h2>
        <p>{{ result }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ConversionScale",
    data() {
      return {
        xAxis: "scale1",
        yAxis: "scale1",
        scaleType: "",
        multiplicationFactor: null,
        translation: null,
        result: null,
      };
    },
    methods: {
      applyConversion() {
        if (!this.scaleType || !this.multiplicationFactor || !this.translation) {
          alert("Please fill in all fields");
          return;
        }
        this.result = `Applying conversion: ${this.scaleType} with factor ${this.multiplicationFactor} and translation ${this.translation}.`;
      },
      resetFields() {
        this.scaleType = "";
        this.multiplicationFactor = null;
        this.translation = null;
        this.result = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .conversion-scale-page {
    padding: 20px;
  }
  
  .axis-section,
  .scale-input-section {
    margin-bottom: 20px;
  }
  
  input,
  select {
    display: block;
    margin-bottom: 10px;
  }
  
  .apply-button {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
  }
  
  .reset-button {
    background-color: #dc3545;
    color: white;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
  }
  
  .result-section {
    margin-top: 20px;
    background-color: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
  }
  </style>