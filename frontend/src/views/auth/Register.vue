<template>
    <div class="register-page">
      <!-- 背景 -->
      <div class="background"></div>
  
      <!-- 注册面板 -->
      <div class="register-panel">
        <!-- 标题 -->
        <h1>Sign Up</h1>
  
        <!-- 用户名输入框 -->
        <div class="input-group">
          <input
            v-model="username"
            type="text"
            placeholder="Username"
            maxlength="20"
            class="input"
          />
        </div>
  
        <!-- 密码输入框 -->
        <div class="input-group">
          <input
            v-model="password"
            type="password"
            placeholder="Password"
            maxlength="20"
            class="input"
          />
        </div>
  
        <!-- 确认密码输入框 -->
        <div class="input-group">
          <input
            v-model="confirmPassword"
            type="password"
            placeholder="Confirm Password"
            maxlength="20"
            class="input"
          />
        </div>
  
        <!-- 注册按钮 -->
        <button @click="handleRegister" class="register-button">Sign Up</button>
  
        <!-- 链接 -->
        <div class="links">
          <router-link to="/login">Back to login</router-link>
        </div>
  
        <!-- 错误提示 -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
  
        <!-- 注册成功提示 -->
        <div v-if="successMessage" class="success-message">
          {{ successMessage }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Register",
    data() {
      return {
        username: "",
        password: "",
        confirmPassword: "",
        errorMessage: "",
        successMessage: "",
      };
    },
    methods: {
      handleRegister() {
        if (!this.username || !this.password || !this.confirmPassword) {
          this.errorMessage = "All fields are required!";
          this.successMessage = "";
          return;
        }
  
        if (this.password !== this.confirmPassword) {
          this.errorMessage = "Passwords do not match!";
          this.successMessage = "";
          return;
        }
  
        // 模拟注册逻辑
        console.log("Registering with", this.username, this.password);
        this.errorMessage = "";
        this.successMessage = "Registration successful!";
      },
    },
  };
  </script>
  
  <style scoped>
  .register-page {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f5f5f5;
  }
  
  .background {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #eef1f5;
    z-index: -1;
  }
  
  .register-panel {
    width: 300px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  h1 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .input-group {
    margin-bottom: 15px;
  }
  
  .input {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 14px;
  }
  
  .register-button {
    width: 100%;
    padding: 10px;
    background: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .register-button:hover {
    background: #218838;
  }
  
  .links {
    margin-top: 10px;
    text-align: center;
  }
  
  .links a {
    text-decoration: none;
    color: #007bff;
  }
  
  .links a:hover {
    text-decoration: underline;
  }
  
  .error-message {
    color: red;
    font-size: 14px;
    text-align: center;
    margin-top: 10px;
  }
  
  .success-message {
    color: green;
    font-size: 14px;
    text-align: center;
    margin-top: 10px;
  }
  </style>