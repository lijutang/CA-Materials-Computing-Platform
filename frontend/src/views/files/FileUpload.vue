<template>
    <div>
      <h2>文件上传</h2>
      <div class="upload-section">
        <input type="file" @change="handleFileUpload" multiple />
        <button @click="submitFiles">上传文件</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "FileUpload",
    data() {
      return {
        selectedFiles: [],
      };
    },
    methods: {
      handleFileUpload(event) {
        this.selectedFiles = Array.from(event.target.files);
      },
      submitFiles() {
        // 上传文件逻辑：模拟文件提交
        if (this.selectedFiles.length) {
          console.log("Uploading files:", this.selectedFiles);
          alert("文件已上传成功！");
        } else {
          alert("请选择文件！");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .upload-section {
    margin-top: 20px;
  }
  button {
    margin-left: 10px;
  }
  </style>
  