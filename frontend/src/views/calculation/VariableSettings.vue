<!-- VariableSettings.vue -->
<template>
    <div class="variable-settings-page">
      <!-- 页面标题 -->
      <h1>Variable Settings</h1>
  
      <!-- 变量输入部分 -->
      <div class="variable-input-section">
        <label for="variable-name">Variable Name:</label>
        <input v-model="variableName" id="variable-name" type="text" placeholder="Enter variable name" />
  
        <label for="min-value">Min Value:</label>
        <input v-model="minValue" id="min-value" type="number" placeholder="Enter min value" />
  
        <label for="max-value">Max Value:</label>
        <input v-model="maxValue" id="max-value" type="number" placeholder="Enter max value" />
  
        <label for="precision">Precision:</label>
        <input v-model="precision" id="precision" type="number" placeholder="Enter precision" />
  
        <label for="initial-value">Initial Value:</label>
        <input v-model="initialValue" id="initial-value" type="number" placeholder="Enter initial value" />
      </div>
  
      <!-- 复选框 -->
      <div class="checkbox-section">
        <label>
          <input type="checkbox" v-model="isTemperature"> Temperature
        </label>
        <label>
          <input type="checkbox" v-model="isPressure"> Pressure
        </label>
      </div>
  
      <!-- 按钮部分 -->
      <div class="button-section">
        <button @click="applyVariableSettings" class="apply-button">Apply</button>
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
    name: "VariableSettings",
    data() {
      return {
        variableName: "",
        minValue: null,
        maxValue: null,
        precision: null,
        initialValue: null,
        isTemperature: false,
        isPressure: false,
        result: null,
      };
    },
    methods: {
      applyVariableSettings() {
        if (!this.variableName || !this.minValue || !this.maxValue || !this.precision || !this.initialValue) {
          alert("Please fill in all fields");
          return;
        }
        this.result = `Variable ${this.variableName} applied with range (${this.minValue}, ${this.maxValue}), precision ${this.precision}, and initial value ${this.initialValue}. Temperature: ${this.isTemperature}, Pressure: ${this.isPressure}`;
      },
      resetFields() {
        this.variableName = "";
        this.minValue = null;
        this.maxValue = null;
        this.precision = null;
        this.initialValue = null;
        this.isTemperature = false;
        this.isPressure = false;
        this.result = null;
      },
    },
  };
  </script>
  
  <style scoped>
  .variable-settings-page {
    padding: 20px;
  }
  
  .variable-input-section {
    margin-bottom: 20px;
  }
  
  input {
    display: block;
    margin-bottom: 10px;
  }
  
  .checkbox-section {
    margin-bottom: 20px;
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