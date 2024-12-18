<template>
    <div class="load-data-page">
      <h1>Load Data</h1>
      <button @click="loadTemplate" class="load-button">Load Template</button>
      <button @click="goBack" class="back-button">Back</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "LoadData",
    methods: {
      loadTemplate() {
        alert("Template loaded successfully!");
      },
      goBack() {
        alert("Going back to the previous page...");
      },
    },
  };
  </script>
  
  <style scoped>
  .load-data-page {
    padding: 20px;
    text-align: center;
  }
  
  .load-button,
  .back-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .back-button {
    background-color: #6c757d;
  }
  
  .load-button:hover {
    background-color: #218838;
  }
  
  .back-button:hover {
    background-color: #5a6268;
  }
  </style>
  