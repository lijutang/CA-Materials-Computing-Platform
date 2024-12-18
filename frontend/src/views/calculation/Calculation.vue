<template>
    <div class="calculation-page">
      <!-- 页面标题 -->
      <h1>Calculation</h1>
  
      <!-- 数据库选择 -->
      <div class="database-section">
        <label for="database">Database:</label>
        <select v-model="selectedDatabase" id="database">
          <option value="Melts">Melts</option>
          <option value="Glasses">Glasses</option>
        </select>
      </div>
  
      <!-- 输入框部分 -->
      <div class="input-section">
        <label for="species">Species:</label>
        <input v-model="species" id="species" type="text" placeholder="Enter species" />
  
        <label for="amount">Amount (mol):</label>
        <input v-model="amount" id="amount" type="number" placeholder="Enter amount" />
  
        <label for="temperature">Temperature (°C):</label>
        <input v-model="temperature" id="temperature" type="number" placeholder="Enter temperature" />
      </div>
  
      <!-- 计算按钮 -->
      <button @click="calculate" class="calculate-button">Calculate</button>
  
      <!-- 结果显示 -->
      <div v-if="result" class="result-section">
        <h2>Results</h2>
        <p>{{ result }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Calculation",
    data() {
      return {
        selectedDatabase: "Melts",
        species: "",
        amount: null,
        temperature: null,
        result: null,
      };
    },
    methods: {
      calculate() {
        // 模拟计算逻辑
        if (!this.species || !this.amount || !this.temperature) {
          alert("Please fill in all fields");
          return;
        }
        this.result = `Calculating ${this.species} with ${this.amount} mol at ${this.temperature}°C using ${this.selectedDatabase} database.`;
      },
    },
  };
  </script>
  
  <style scoped>
  .calculation-page {
    padding: 20px;
  }
  
  .database-section,
  .input-section {
    margin-bottom: 20px;
  }
  
  input {
    display: block;
    margin-bottom: 10px;
  }
  
  .calculate-button {
    background-color: #007bff;
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
  