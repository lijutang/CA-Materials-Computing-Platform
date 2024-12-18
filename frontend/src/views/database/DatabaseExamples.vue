<template>
    <div class="database-examples-page">
      <h1>Database Examples</h1>
      <p class="description">
        This section provides examples and instructions for using the database.
      </p>
      <div class="examples">
        <button @click="viewExample(1)" class="example-button">Example 1</button>
        <button @click="viewExample(2)" class="example-button">Example 2</button>
      </div>
      <button @click="goBack" class="back-button">Back to Examples</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "DatabaseExamples",
    methods: {
      viewExample(exampleNumber) {
        alert(`Viewing Example ${exampleNumber}`);
      },
      goBack() {
        alert("Returning to examples...");
      },
    },
  };
  </script>
  
  <style scoped>
  .database-examples-page {
    padding: 20px;
    text-align: center;
  }
  
  .description {
    margin: 20px 0;
  }
  
  .example-button,
  .back-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #17a2b8;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .back-button {
    background-color: #6c757d;
  }
  
  .example-button:hover {
    background-color: #138496;
  }
  
  .back-button:hover {
    background-color: #5a6268;
  }
  </style>
  