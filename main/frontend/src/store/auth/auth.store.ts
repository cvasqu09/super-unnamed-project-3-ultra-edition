import axios from 'axios';
import router from '../../router/index';

const auth = {
  state: () => ({
    token: '',
    error: null,
  }),
  mutations: {
    loginSuccessful(state, token) {
      state.token = token;
      state.error = null;
      router.push({ name: 'home' });
    },
    loginFailed(state, err) {
      state.error = err.message;
    },
  },
  actions: {
    async login({ commit }, loginInfo) {
      try {
        const res = await axios.post('auth/', {
          username: loginInfo.username,
          password: loginInfo.password,
        });

        commit('loginSuccessful', res.data);
      } catch (e) {
        commit('loginFailed', e);
      }
    },
  },
  getters: {},
};

export default auth;
