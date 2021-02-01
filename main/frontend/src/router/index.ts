import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import journalRoutes from '@/router/journal.routes';
import Home from '../pages/Home.vue';
import UserPage from '../pages/UserPage.vue';
import PostsPage from '../pages/PostsPage.vue';
import BooksPage from '../pages/BooksPage.vue';
import LoginPage from '../pages/LoginPage.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/users',
    name: 'users',
    component: UserPage,
  },
  {
    path: '/posts',
    name: 'posts',
    component: PostsPage,
  },
  {
    path: '/books',
    name: 'books',
    component: BooksPage,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  ...journalRoutes,
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
