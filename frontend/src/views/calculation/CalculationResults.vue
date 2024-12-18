<!-- CalculationResults.vue -->
<template>
    <div class="calculation-results-page">
      <!-- 页面标题 -->
      <h1>Calculation Results</h1>
  
      <!-- 结果表格 -->
      <table class="results-table">
        <thead>
          <tr>
            <th>Parameter</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(value, parameter) in results" :key="parameter">
            <td>{{ parameter }}</td>
            <td>{{ value }}</td>
          </tr>
        </tbody>
      </table>
  
      <!-- 操作按钮 -->
      <div class="button-section">
        <button @click="exportResults" class="export-button">Export</button>
        <button @click="resetResults" class="reset-button">Reset</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "CalculationResults",
    data() {
      return {
        results: {
          Temperature: "300 K",
          Pressure: "1 atm",
          "Molar Fraction": "0.5",
          "Phase Stability": "Stable",
        },
      };
    },
    methods: {
      exportResults() {
        alert("Results exported successfully!");
        console.log("Exporting results:", this.results);
      },
      resetResults() {
        this.results = {};
      },
    },
  };
  </script>
  
  <style scoped>
  .calculation-results-page {
    padding: 20px;
  }
  
  .results-table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  .results-table th,
  .results-table td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
  }
  
  .results-table th {
    background-color: #f8f9fa;
  }
  
  .export-button {
    background-color: #007bff;
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
  </style>
  