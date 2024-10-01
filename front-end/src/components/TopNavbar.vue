<template>
  <div class="header">
    <div class="left-section"> 
      <span class="menu-icon" v-if="isHamburgerVisible" @click="toggleDrawer">
        <span class="material-symbols-outlined">{{ menuIcon }}</span>
      </span>
    </div>
    <div class="middle-section">
      <div class="middle-p">
      </div>
    </div>
    <div class="right-section">
      
      <span style="position: relative">

      <md-button id="language-anchor" @click="openLanguagemenu">
        <img class="language" src="../assets/img/icons/language.png" alt="language"/>
      </md-button>

        <md-menu id="language-menu" positioning="popover" ref="languagemenu" anchor="language-anchor">
          <md-menu-item @click="selectedLanguage('fi')">
            <div class= "texts" slot="headline">FI</div>
          </md-menu-item>
          <md-menu-item @click="selectedLanguage('en')">
            <div class= "texts" slot="headline">EN</div>
          </md-menu-item>
          
          

        </md-menu>

      <md-icon-button id="user-anchor" @click="openmenu">
        <img class="profile" src="../assets/img/icons/profile.png" alt="profile"/>
      </md-icon-button>

        <md-menu id="user-menu" positioning="popover" ref="usermenu" anchor="user-anchor">
          
          <md-menu-item @click="logout_handler">
            <div class= "texts" slot="headline">{{ logoutUI }}</div>
          </md-menu-item>
          

        </md-menu>
      </span>
    </div>
  </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'TopNavbar',
  props: {
    premium: Boolean,
    isDrawerOpen: {
      type: Boolean,
      required: true
    },
    isHamburgerVisible: Boolean,
    customerOrganization: String,
    userName: String,
    showUserName: Boolean,
    customisedAppName: String

  },
 
  computed: {
    menuIcon() {
      return this.isDrawerOpen ? 'menu_open' : 'menu';
    },
    iconColor() {
      return this.premium ? 'var(--md-sys-color-primary)' : 'var(--md-sys-color-on-primary)';
    }
  },
  data() {
    return {
      apiKey: import.meta.env.VITE_API_KEY,

      logoutUI: "Sign out",
    }
  },
  methods: {
    toggleDrawer() {
      this.$emit('toggle-drawer');
    }, 

    openmenu() {
      this.$refs.usermenu.show()
    },

    openLanguagemenu() {
      this.$refs.languagemenu.show()
    },

    logout_handler(){
      window.open('https://www.google.com', '_self'); //parameterise URL here
    },
    selectedLanguage(lang) {
      console.log('Setting language:', lang);
      axios.get(`http://https://daniil-web-portfolio.onrender.com/language/${lang}`)
        .then(response => {
          this.logoutUI = response.data.logoutUI;
        })
        .catch(error => {
          console.error('Error setting language:', error);
        });

      this.$emit('language-set', lang);
    }
  },
};
</script>
















<style scoped>




.menu-icon {
  color: var(--md-sys-color-on-background);
  padding: 12px 12px;
  font-size: 16px;
  cursor: pointer;
  display: flex;
  align-items: center;
  margin-left: 10px;
  transition: color 0.3s;
}

.menu-icon:hover {
  background-color: var(--md-sys-color-surface-variant);
  border-radius: 100%;
}

.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}

.header {
  height: var(--topbar-height);
  display: flex;
  flex-direction: row; 
  justify-content: space-between;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background: var(--md-sys-color-surface-container-low);
  z-index: 102;
}

.left-section {
  display: flex;
  align-items: center;    
}

.middle-p {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.middle-section {
  flex: 1;
}

.right-section {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-right: 10px;
  flex-shrink: 0;
}

.logo {
  height: 40px;
  padding: 10px;
  will-change: filter;
  transition: filter 300ms;
}

.header-font {
  font-size: 18px;
  color: var(--md-sys-color-on-surface);
}

.user-font {
  font-size: 16px;
  color: var(--md-sys-color-on-surface);
}

.profile {
  height: 40px;
  padding: 10px;
  will-change: filter;
  transition: filter 300ms;
  border-radius: 50%;
  cursor: pointer;
}

.language {
  height: 40px;
  padding: 10px;
  will-change: filter;
  transition: filter 300ms;
  border-radius: 50%;
  cursor: pointer;
}

.texts {

  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;

}

.profile:hover {
  transform: scale(1.1);
}

.language-option {
  cursor: pointer;

}
</style>
