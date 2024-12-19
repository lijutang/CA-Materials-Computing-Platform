<template>
    <div class="solution-page">
      <header>
        <h1>解决方案管理</h1>
      </header>
      <div class="content">
        <!-- 左侧菜单栏 -->
        <LeftMenu :items="menuItems" @select="selectSolution" />
  
        <!-- 右侧解决方案显示区域 -->
        <div class="solution-content">
          <!-- 动态加载子组件 -->
          <component
            :is="currentSolution.component"
            v-bind="currentSolution.props"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import LeftMenu from "@/components/LeftMenu.vue";
  
  export default {
    name: "Solution",
    components: { LeftMenu },
    data() {
      return {
        menuItems: [
          { name: "解决方案 1", component: "SolutionSpecific1", props: { config: "配置1" } },
          { name: "解决方案 2", component: "SolutionSpecific2", props: { config: "配置2" } },
          { name: "解决方案 3", component: "SolutionSpecific3", props: { config: "配置3" } },
        ],
        currentSolution: { component: "SolutionSpecific1", props: { config: "配置1" } },
      };
    },
    methods: {
      selectSolution(item) {
        this.currentSolution = item;
      },
    },
  };
  </script>
  
  <style scoped>
  .solution-page {
    display: flex;
    flex-direction: column;
    height: 100vh;
  }
  
  header {
    background-color: #f5f5f5;
    padding: 10px;
    text-align: center;
    font-size: 20px;
  }
  
  .content {
    display: flex;
    flex: 1;
  }
  
  .solution-content {
    flex: 1;
    padding: 20px;
    background: #ffffff;
  }
  </style>
  