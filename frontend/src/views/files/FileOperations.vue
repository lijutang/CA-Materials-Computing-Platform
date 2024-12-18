<template>
    <div>
      <h2>文件操作</h2>
      <div>
        <h3>打开文件</h3>
        <input type="file" @change="openFile" />
      </div>
      <div>
        <h3>另存为</h3>
        <input type="text" v-model="fileName" placeholder="输入文件名" />
        <button @click="saveFile">保存</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "FileOperations",
    data() {
      return {
        fileName: "",
      };
    },
    methods: {
      openFile(event) {
        const file = event.target.files[0];
        if (file) {
          alert(`文件 ${file.name} 已打开`);
        }
      },
      saveFile() {
        if (this.fileName) {
          alert(`文件已保存为：${this.fileName}`);
        } else {
          alert("请输入文件名！");
        }
      },
    },
  };
  </script>
  
  <style scoped>
  h3 {
    margin-top: 10px;
  }
  input {
    margin-right: 10px;
  }
  </style>
  