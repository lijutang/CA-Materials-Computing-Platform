<template>
    <div class="image-display-page">
      <h1>Image Display</h1>
      <img :src="imageSrc" alt="Example Image" />
      <button @click="addImage" class="add-button">Add Image</button>
      <button @click="editImage" class="edit-button">Edit Image</button>
    </div>
  </template>
  
  <script>
  export default {
    name: "ImageDisplay",
    data() {
      return {
        imageSrc: "path/to/example/image.png",
      };
    },
    methods: {
      addImage() {
        alert("Adding a new image!");
      },
      editImage() {
        alert("Editing the current image!");
      },
    },
  };
  </script>
  
  <style scoped>
  .image-display-page {
    padding: 20px;
    text-align: center;
  }
  
  img {
    max-width: 100%;
    height: auto;
    margin: 20px 0;
  }
  
  .add-button,
  .edit-button {
    margin: 10px;
    padding: 10px 20px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  