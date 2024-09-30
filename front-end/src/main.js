import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import '@material/web/button/filled-button.js';
import '@material/web/button/outlined-button.js';
import '@material/web/button/text-button.js';
import '@material/web/checkbox/checkbox.js';
import '@material/web/menu/menu.js';
import '@material/web/menu/menu-item.js';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: App },
        
    ],
})


createApp(App).use(router).mount('#app')
