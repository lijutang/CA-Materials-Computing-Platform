<template>
    <div class="drawing-page">
      <h1>Drawing Tool</h1>
      <button @click="startDrawing" class="draw-button">Start Drawing</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "Drawing",
    methods: {
      startDrawing() {
        alert("Drawing started!");
      },
    },
  };
  </script>
  
  <style scoped>
  .drawing-page {
    padding: 20px;
    text-align: center;
  }
  
  .draw-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  