<template>
  <div class="app" >
    <TopNavbar :isDrawerOpen="is_drawer_open" :isHamburgerVisible="isHamburgerVisible" @toggle-drawer="toggleDrawer" :customerOrganization="customerOrganization" :userName="userName" :showUserName="showUserName" :customisedAppName="customisedAppName" @language-set="setLanguage"/>
    <!-- overlay class is used so that when clicking outside the side menu, the side menu would be closed -->
    <div v-if="is_drawer_open" class="overlay" @click="closeDrawer"></div>
    <main>
      <Drawer v-if="is_drawer_open"  @click.stop />
      <LaunchPad :isDrawOpen="is_drawer_open"
           @userinfoUpdated="fetchUserInfo"
           :showUserName="showUserName"
           :customisedAppName="customisedAppName"
           @update-show-user-name="showUserName = $event"
           @update-customisedAppName="customisedAppName = $event" 
           :selectedLanguage="selectedLanguage"/>

    </main>
  </div>
</template>

<script>
import LaunchPad from './components/LaunchPad.vue';
import TopNavbar from './components/TopNavbar.vue';
import Drawer from './components/Drawer.vue';

import axios from 'axios';
export default {
  components: {
    LaunchPad,
    TopNavbar,
    Drawer
  },
  data() {
    return {
      is_drawer_open: false,
      isHamburgerVisible: true, // change this to "false" to disable the menu or true to enable it
      showUserName: true,
      customerOrganization: '',
      userName: '',
      customisedAppName: '',
      selectedLanguage: 'en', // default language

    };
  },
  mounted() {
    this.fetchUserInfo();
  },
  methods: {
    toggleDrawer() {
      this.is_drawer_open = !this.is_drawer_open;
    },
    closeDrawer() {
      if (window.innerWidth <= 768 && this.is_drawer_open) {
      this.is_drawer_open = false;
      }
    },
    fetchUserInfo() {
      axios.get('https://daniil-web-portfolio.onrender.com/userinfo/')
        .then(response => {
          this.customerOrganization = response.data.user_organization;
          this.userName = response.data.user_name;
          this.showUserName = response.data.show_user_name;
          this.customisedAppName = response.data.customised_app_name
    })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    },
    setLanguage(lang) {
      this.selectedLanguage = lang;
      console.log('Setting language app:', this.selectedLanguage);
    },
  }
};
</script>

<style lang = "scss">

* {
  font-family: var(--md-ref-typeface-brand);
}

.app {
  padding-top: var(--topbar-height);

  main {
    padding: 0rem 2rem;
    margin: 0 auto;


  }
  .overlay {
    position: fixed; /* Cover the whole screen */
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 101; /*  below the drawer z-index */
  }
}
</style>
