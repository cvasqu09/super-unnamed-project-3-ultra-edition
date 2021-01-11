import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import Home from '../pages/Home.vue';
import UserPage from '../pages/UserPage.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/users',
    name: 'users',
    component: UserPage,
  },
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
