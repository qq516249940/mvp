import axios from 'axios';
import Buefy from 'buefy';
import Vue from 'vue';
import VueI18n from 'vue-i18n';

import App from './App.vue';
import './registerServiceWorker';
import router from './router';
import store from './store';

import '@mdi/font/css/materialdesignicons.css';

import dateTimeFormats from './i18n/dateTime';


// Axios
Vue.prototype.$http = axios;
Vue.http = Vue.prototype.$http;

// Buefy Framework
Vue.use(Buefy);

// i18n
Vue.use(VueI18n);

const i18n = new VueI18n({
  dateTimeFormats,
  locale: 'en',
});


Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: h => h(App),
}).$mount('#app');
