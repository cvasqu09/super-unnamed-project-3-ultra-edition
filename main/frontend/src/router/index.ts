import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import journalRoutes from '@/router/journal.routes';
import Home from '../pages/Home.vue';
import UserPage from '../pages/UserPage.vue';
import PostsPage from '../pages/PostsPage.vue';
import BooksPage from '../pages/BooksPage.vue';

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
  ...journalRoutes,
];

const router = new VueRouter({
  mode: 'history',
  routes,
});

export default router;
