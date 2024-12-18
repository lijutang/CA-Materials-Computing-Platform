<template>
    <div class="image-processing-examples-page">
      <h1>Image Processing Examples</h1>
      <button @click="viewExample('Example 1')" class="example-button">View Example 1</button>
      <button @click="viewExample('Example 2')" class="example-button">View Example 2</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "ImageProcessingExamples",
    methods: {
      viewExample(example) {
        alert(`Viewing ${example}`);
      },
    },
  };
  </script>
  
  <style scoped>
  .image-processing-examples-page {
    padding: 20px;
    text-align: center;
  }
  
  .example-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #17a2b8;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  