import Vue from 'vue';
import axios from 'axios';
import Buefy from 'buefy';

import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';

import '@mdi/font/css/materialdesignicons.css';


// Buefy Framework
Vue.use(Buefy);

// Axios
Vue.prototype.$http = axios;
Vue.http = Vue.prototype.$http;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
