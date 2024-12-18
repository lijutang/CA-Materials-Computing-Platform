<template>
    <div class="user-settings">
      <h2>用户设置与选项</h2>
      <!-- General Settings Section -->
      <div class="section">
        <h3>General</h3>
        <label>
          <input type="checkbox" v-model="settings.applyPseudonyms" />
          Apply Pseudonyms
        </label>
        <label>
          <input type="checkbox" v-model="settings.useDefault" />
          Use Default
        </label>
      </div>
  
      <!-- Highlight and Colors Section -->
      <div class="section">
        <h3>Highlight</h3>
        <p>Choose Highlight Color:</p>
        <input type="color" v-model="settings.highlightColor" />
        <h3>Background</h3>
        <p>Choose Background Color:</p>
        <input type="color" v-model="settings.backgroundColor" />
      </div>
  
      <!-- Format Settings -->
      <div class="section">
        <h3>Format</h3>
        <label>Font:
          <input type="text" v-model="settings.font" placeholder="Enter Font" />
        </label>
        <button @click="changeFont">Change Font</button>
      </div>
  
      <!-- Data Settings -->
      <div class="section">
        <h3>Data Settings</h3>
        <label>
          <input type="checkbox" v-model="settings.onlyShowStable" />
          Only Show Stable
        </label>
        <label>
          <input type="checkbox" v-model="settings.showDatabaseSource" />
          Show Database Source
        </label>
      </div>
  
      <!-- Actions -->
      <div class="actions">
        <button @click="applySettings">Apply</button>
        <button @click="resetSettings">Reset to Default</button>
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
          highlightColor: "#FFD700",
          backgroundColor: "#FFFFFF",
          font: "",
          onlyShowStable: false,
          showDatabaseSource: false,
        },
      };
    },
    methods: {
      changeFont() {
        alert(`Font changed to: ${this.settings.font}`);
      },
      applySettings() {
        console.log("Settings applied:", this.settings);
      },
      resetSettings() {
        this.settings = {
          applyPseudonyms: false,
          useDefault: false,
          highlightColor: "#FFD700",
          backgroundColor: "#FFFFFF",
          font: "",
          onlyShowStable: false,
          showDatabaseSource: false,
        };
        alert("Settings reset to default.");
      },
    },
  };
  </script>
  
  <style scoped>
  .user-settings {
    font-family: Arial, sans-serif;
    padding: 20px;
  }
  
  .section {
    margin-bottom: 20px;
  }
  
  .section h3 {
    margin-bottom: 10px;
  }
  
  label {
    display: block;
    margin-bottom: 10px;
  }
  
  button {
    margin-right: 10px;
    padding: 5px 10px;
    cursor: pointer;
  }
  
  .actions {
    margin-top: 20px;
  }
  </style>
  