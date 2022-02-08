import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'

App.vue.prototype.axios = axios
createApp(App).mount('#app')
