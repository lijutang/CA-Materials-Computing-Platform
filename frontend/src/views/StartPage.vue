<template>
    <div class="start-page">
      <!-- 顶部导航工具栏 -->
      <div id="topPanel">
        <div id="interfaceControlFrame">
          <div id="interfaceControlFrameLeft">
            <div id="interfaceControlFrameMinimizeContainer">
              <button title="Collapse" id="interfaceControlFrameMinimizeButton">
                Minimize
              </button>
            </div>
            <div id="interfaceControlFrameCloseContainer">
              <button title="Close" id="interfaceControlFrameCloseButton">
                Close
              </button>
            </div>
          </div>
          <div id="interfaceControlFrameRight">
            <div id="publishContainer">
              <button id="publishButton">Share Prototype</button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- 主内容框架 -->
      <div id="outerContainer">
        <div id="mainPanel">
          <iframe
            id="mainFrame"
            :src="mainFrameSrc"
            frameborder="0"
            allowfullscreen
            style="width: 100%; height: 100%;"
          ></iframe>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "StartPage",
    props: {
      config: {
        type: String,
        default: null, // 配置参数，默认为空
      },
    },
    computed: {
      mainFrameSrc() {
        // 动态加载 iframe 内容，根据配置参数选择
        return this.config === "1"
          ? "/path/to/alternative/config"
          : "/path/to/default/content";
      },
    },
  };
  </script>
  
  <style scoped>
  .start-page {
    height: 100vh;
    display: flex;
    flex-direction: column;
  }
  #topPanel {
    height: 50px;
    background-color: #f5f5f5;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
  }
  #outerContainer {
    flex: 1;
    display: flex;
    background-color: #ffffff;
  }
  #mainPanel {
    flex: 1;
    overflow: hidden;
  }
  </style>
  