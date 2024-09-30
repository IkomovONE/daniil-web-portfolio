<template>
  <aside>
    <p class="sidebar-font"></p>
    <ul class="menu-list">
      
      <li class="menu-item">
          <div class="card-header" @click="logout_handler">Sign out</div>
        </li>
    </ul>
  </aside>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      isAdmin: false,
      apiKey: import.meta.env.VITE_API_KEY,
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    

    
    logout_handler(){
        window.open('https://www.google.com', '_self'); //parameterise here too
      }
  },
};
</script>

  
















  <style lang="scss" scoped>
    aside {
      position: fixed;
      left: 0;
      top: var(--topbar-height);
      bottom: 0;
      display: flex;
      flex-direction: column;
      width: var(--sidebar-width);
      overflow: auto;
      z-index: 101;
      background-color: var(--md-sys-color-surface-container-low);
      color: var(--md-sys-color-on-surface-variant);
      // border-top-right-radius: 28px;
      // border-bottom-right-radius: 28px;
      @media (max-width: 768px) {
        width: 80%;
      }
    }
  
    .sidebar-font {
      text-align: left;
      font-size: 1.5rem;
      margin: 1.5rem 2rem;
      color: var(--md-sys-color-on-surface-high);
    }
  
    .menu-list {
      list-style-type: none;
      padding: 0;
      margin: 0, 0, 0, 0;
    }
  
    .menu-item {
      display: flex;
      justify-content: flex-start;
      align-items: center;
      padding-left: 20px;
      padding-right: 20px;
      margin-bottom: 1rem;
    }

    .card-header {
      position: relative;
      height: 30px;
      width: 80%;
      box-shadow: rgba(0, 0, 0, 0.2) 0px 2px 1px -1px, rgba(0, 0, 0, 0.14) 0px 1px 1px 0px, rgba(0, 0, 0, 0.12) 0px 1px 3px 0px;
      border: 1px solid; 
      border-radius: 12px; 
      padding: 20px; 
      background-color: var(--md-sys-color-surface-container-highest); 
      cursor: pointer; 
      text-align: center;
    }

    .settings-button {
      position: absolute;
      top: 18px;
      right: 0px;
      background: none;
      border: none;
      padding: 0;
    }

    .settings-button img {
      width: 40%; 
      height: auto;
    }

    .save-button-text {
      background: linear-gradient(to right, #1452b0, #3AB151); 
      color: white;
    }

    .version-text {
      color: black;
    }



  </style>
  