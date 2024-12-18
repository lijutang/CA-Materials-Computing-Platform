<template>
    <div class="save-data-page">
      <h1>Save Data</h1>
      <button @click="saveData" class="save-button">Save</button>
      <button @click="closePage" class="close-button">Close</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "SaveData",
    methods: {
      saveData() {
        alert("Data saved successfully!");
      },
      closePage() {
        alert("Closing the page...");
      },
    },
  };
  </script>
  
  <style scoped>
  .save-data-page {
    padding: 20px;
    text-align: center;
  }
  
  .save-button,
  .close-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .close-button {
    background-color: #dc3545;
  }
  
  .save-button:hover {
    background-color: #0056b3;
  }
  
  .close-button:hover {
    background-color: #c82333;
  }
  </style>
  