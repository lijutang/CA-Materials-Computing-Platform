<!-- ResultsDisplay.vue -->
<template>
    <div class="results-display">
      <h2>Results</h2>
      <textarea v-model="results" placeholder="Result content will appear here"></textarea>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const results = ref(`Mg + 3 Cu2O + 2 Fe3C + Ar =\n\n...Generated results appear here...`);
  </script>
  
  <style scoped>
  .results-display {
    margin-bottom: 20px;
  }
  
  textarea {
    width: 100%;
    height: 200px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-family: monospace;
  }
  </style>
  