<template>
    <div class="axes-and-frames-page">
      <h1>Axes and Frames</h1>
      <button @click="updateAxes" class="axes-button">Update Axes</button>
      <button @click="applyFrame" class="frame-button">Apply Frame</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "AxesAndFrames",
    methods: {
      updateAxes() {
        alert("Axes updated!");
      },
      applyFrame() {
        alert("Frame applied!");
      },
    },
  };
  </script>
  
  <style scoped>
  .axes-and-frames-page {
    padding: 20px;
    text-align: center;
  }
  
  .axes-button,
  .frame-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  