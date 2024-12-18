<template>
    <div class="forgot-password-page">
      <!-- 背景 -->
      <div class="background"></div>
  
      <!-- 忘记密码面板 -->
      <div class="forgot-password-panel">
        <!-- 标题 -->
        <h1>Forgot Password</h1>
  
        <!-- 用户名输入框 -->
        <div class="input-group">
          <input
            v-model="username"
            type="text"
            placeholder="Enter your username"
            maxlength="20"
            class="input"
          />
        </div>
  
        <!-- 提交按钮 -->
        <button @click="handleForgotPassword" class="submit-button">Submit</button>
  
        <!-- 链接 -->
        <div class="links">
          <router-link to="/login">Back to login</router-link>
        </div>
  
        <!-- 错误提示 -->
        <div v-if="errorMessage" class="error-message">
          {{ errorMessage }}
        </div>
  
        <!-- 成功提示 -->
        <div v-if="successMessage" class="success-message">
          {{ successMessage }}
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ForgotPassword",
    data() {
      return {
        username: "",
        errorMessage: "",
        successMessage: "",
      };
    },
    methods: {
      handleForgotPassword() {
        if (!this.username) {
          this.errorMessage = "Username is required!";
          this.successMessage = "";
          return;
        }
  
        // 模拟忘记密码逻辑
        console.log("Requesting password reset for", this.username);
        this.errorMessage = "";
        this.successMessage = "Password reset link sent to your email!";
      },
    },
  };
  </script>
  
  <style scoped>
  .forgot-password-page {
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
  
  .forgot-password-panel {
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
  
  .submit-button {
    width: 100%;
    padding: 10px;
    background: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .submit-button:hover {
    background: #0056b3;
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