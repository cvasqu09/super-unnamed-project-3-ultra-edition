import Vue from 'vue';
import Vuex, { createLogger } from 'vuex';
import auth from '@/store/auth/auth.store';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createLogger()],
  state: {},
  mutations: {},
  actions: {},
  modules: {
    auth,
  },
});
