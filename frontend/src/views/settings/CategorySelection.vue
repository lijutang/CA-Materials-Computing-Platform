<template>
  <div class="category-selection">
    <h2>选择种类</h2>
    <label for="category-select">选择一个类别：</label>
    <select id="category-select" v-model="selectedCategory">
      <option v-for="category in categories" :key="category" :value="category">
        {{ category }}
      </option>
    </select>
    <button @click="confirmSelection">确认选择</button>
  </div>
</template>

<script>
export default {
  name: "CategorySelection",
  data() {
    return {
      categories: ["类别1", "类别2", "类别3", "类别4"], // 示例类别
      selectedCategory: "",
    };
  },
  methods: {
    // 确认选择并返回 UserSettings 页面
    confirmSelection() {
      if (this.selectedCategory) {
        // 将选择的类别传递回 UserSettings.vue
        this.$router.push({
          path: "/settings",
          query: { selectedCategory: this.selectedCategory },
        });
      } else {
        alert("请选择一个类别！");
      }
    },
  },
};
</script>

<style scoped>
.category-selection {
  display: flex;
  flex-direction: column;
  max-width: 300px;
  margin: 20px auto;
}

label {
  margin-bottom: 10px;
}

select {
  margin-bottom: 20px;
  padding: 5px;
  width: 100%;
}

button {
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
