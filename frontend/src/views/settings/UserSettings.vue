<template>
  <div class="user-settings">
    <h2>用户设置</h2>
    
    <!-- 类别选择功能 -->
    <div class="category-selection-section">
      <p>当前选择的类别：{{ selectedCategory }}</p>
      <button @click="goToCategorySelection">选择类别</button>
    </div>
    
    <!-- 原有的其他设置部分 -->
    <div class="other-settings">
      <h3>通用设置</h3>
      <label>
        <input type="checkbox" v-model="settings.applyPseudonyms" />
        使用别名
      </label>
      <label>
        <input type="checkbox" v-model="settings.useDefault" />
        使用默认设置
      </label>
    </div>
    
    <div class="format-settings">
      <h3>格式设置</h3>
      <label>
        字体：
        <input type="text" v-model="settings.font" placeholder="输入字体" />
      </label>
      <button @click="changeFont">更改字体</button>
    </div>
    
    <!-- 提交和重置 -->
    <div class="actions">
      <button @click="applySettings">应用设置</button>
      <button @click="resetSettings">重置为默认</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserSettings",
  data() {
    return {
      settings: {
        applyPseudonyms: false,
        useDefault: false,
        font: "",
      },
      selectedCategory: "未选择", // 当前选择的类别
    };
  },
  methods: {
    goToCategorySelection() {
      this.$router.push("/settings/category-selection"); // 跳转到选择类别页面
    },
    changeFont() {
      alert(`字体已更改为：${this.settings.font}`);
    },
    applySettings() {
      console.log("应用设置：", this.settings);
    },
    resetSettings() {
      this.settings = {
        applyPseudonyms: false,
        useDefault: false,
        font: "",
      };
      alert("设置已重置为默认值！");
    },
  },
  created() {
    // 如果从 CategorySelection 页面返回，则更新类别
    if (this.$route.query.selectedCategory) {
      this.selectedCategory = this.$route.query.selectedCategory;
    }
  },
};
</script>

<style scoped>
.user-settings {
  max-width: 600px;
  margin: 20px auto;
  font-family: Arial, sans-serif;
}

.category-selection-section {
  margin-bottom: 20px;
}

.other-settings,
.format-settings {
  margin-top: 20px;
}

label {
  display: block;
  margin-bottom: 10px;
}

button {
  margin-top: 10px;
  padding: 10px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.actions {
  margin-top: 20px;
}
</style>
