<template>
    <div class="login-page">
      <!-- 背景 -->
      <div class="background"></div>
  
      <!-- 登录面板 -->
      <div class="login-panel">
        <!-- 标题 -->
        <h1>Log in</h1>
  
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
  
        <!-- 登录按钮 -->
        <button @click="handleLogin" class="login-button">Log in</button>
  
        <!-- 链接 -->
        <div class="links">
          <router-link to="/forgot-password">Forget password?</router-link>
          <router-link to="/register">Sign up</router-link>
        </div>
  
        <!-- 错误提示 -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "Login",
    data() {
      return {
        username: "",
        password: "",
        errorMessage: "",
      };
    },
    methods: {
      handleLogin() {
        if (!this.username || !this.password) {
          this.errorMessage = "Username and password are required!";
          return;
        }
  
        // 模拟登录逻辑
        console.log("Logging in with", this.username, this.password);
        // 此处可添加API请求逻辑
      },
    },
  };
  </script>
  
  <style scoped>
  .login-page {
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
  
  .login-panel {
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
  
  .login-button {
    width: 100%;
    padding: 10px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .login-button:hover {
    background: #0056b3;
  }
  
  .links {
    margin-top: 10px;
    text-align: center;
  }
  
  .links a {
    margin: 0 5px;
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
  </style>
  