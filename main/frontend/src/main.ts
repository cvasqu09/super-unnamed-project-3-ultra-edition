import Vue from 'vue';
import Buefy from 'buefy';
import axios from 'axios';
import App from './App.vue';
import router from './router';
import store from './store';
import 'buefy/dist/buefy.css';

Vue.config.productionTip = false;

axios.defaults.baseURL = 'http://localhost:8000/api/';

const app = new Vue({
  router,
  store,
  render: (h) => h(App),
});

Vue.use(Buefy, {
  defaultIconPack: 'fas',
  defaultContainerElement: '#content',
});
app.$mount('#app');
