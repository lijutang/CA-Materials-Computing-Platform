<!-- SaveResult.vue -->
<template>
    <div class="save-result">
      <h2>Save Results</h2>
      <button @click="saveResults">Save as File</button>
    </div>
  </template>
  
  <script setup>
  const saveResults = () => {
    const blob = new Blob(['Generated Results'], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'results.txt';
    link.click();
    URL.revokeObjectURL(link.href);
  };
  </script>
  
  <style scoped>
  .save-result {
    margin-top: 20px;
  }
  
  button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  </style>
  