<template>
  <div class="help">
    <h1>帮助中心</h1>
    <!-- 保留现有功能：主导航 -->
    <nav>
      <ul>
        <li><router-link to="/help/examples">示例目录</router-link></li>
        <li><router-link to="/quickstart">快速入门</router-link></li>
        <li><router-link to="/moduledocs">模块文档</router-link></li>
      </ul>
    </nav>

    <!-- 保留现有的动态内容部分 -->
    <div class="content">
      <div v-if="activeTab === 'examples'">
        <router-view name="examples"></router-view>
      </div>
      <div v-else-if="activeTab === 'quickstart'">
        <router-view name="quickstart"></router-view>
      </div>
      <div v-else-if="activeTab === 'moduledocs'">
        <router-view name="moduledocs"></router-view>
      </div>
      <div v-else>
        <p>请选择一个选项查看详细信息。</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Help",
  data() {
    return {
      activeTab: "examples", // 默认选项
      tabs: [
        { name: "examples", label: "示例目录", path: "/help/examples" },
        { name: "quickstart", label: "快速入门", path: "/quickstart" },
        { name: "moduledocs", label: "模块文档", path: "/moduledocs" },
      ],
    };
  },
  methods: {
    switchTab(tabName) {
      this.activeTab = tabName;
      const selectedTab = this.tabs.find((tab) => tab.name === tabName);
      if (selectedTab) {
        this.$router.push(selectedTab.path);
      }
    },
  },
};
</script>

<style scoped>
.help {
  max-width: 800px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

nav ul {
  display: flex;
  list-style-type: none;
  padding: 0;
  gap: 20px;
}

nav li {
  cursor: pointer;
}

nav a {
  color: #007bff;
  text-decoration: none;
}

nav a:hover {
  text-decoration: underline;
}

.content {
  margin-top: 20px;
}
</style>