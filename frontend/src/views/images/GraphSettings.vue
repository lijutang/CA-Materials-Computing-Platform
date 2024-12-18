<template>
    <div class="graph-settings-page">
      <h1>Graph Settings</h1>
      <button @click="cancelSettings" class="cancel-button">Cancel</button>
      <button @click="copySettings" class="copy-button">Copy</button>
      <button @click="plotGraph" class="plot-button">Plot</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "GraphSettings",
    methods: {
      cancelSettings() {
        alert("Settings canceled!");
      },
      copySettings() {
        alert("Settings copied!");
      },
      plotGraph() {
        alert("Graph plotted!");
      },
    },
  };
  </script>
  
  <style scoped>
  .graph-settings-page {
    padding: 20px;
  }
  
  .cancel-button,
  .copy-button,
  .plot-button {
    margin: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .cancel-button {
    background-color: #dc3545;
    color: white;
  }
  
  .copy-button {
    background-color: #ffc107;
    color: black;
  }
  
  .plot-button {
    background-color: #28a745;
    color: white;
  }
  </style>
  