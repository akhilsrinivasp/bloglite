import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/edit/user/:what',
    name: 'edit_user',
    component: ()  => import(/* webpackChunkName: "login" */ '../components/EditUser.vue'),
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/LoginView.vue')
  },
  {
    path: '/signup',
    name: 'signup',
    component: () => import(/* webpackChunkName: "signup" */ '../views/SignupView.vue')
  },
  { 
    path: '/logout',
    name: 'logout',
    component: () => import(/* webpackChunkName: "logout" */ '../components/LogoutComp.vue')
  }, 
  {
    path: '/user/:username',
    name: 'user',
    component: () => import(/* webpackChunkName: "user" */ '../views/UserView.vue'),
  },
  {
    path: '/feed',
    name: 'feed',
    component: () => import(/* webpackChunkName: "feed" */ '../views/FeedView.vue'),
  },
  {
    path: '/upload',
    name: 'upload',
    component: () => import(/* webpackChunkName: "upload" */ '../views/UploadBlog.vue'),
  },
  {
    path: '/blog/:id',
    name: 'blog',
    component: () => import(/* webpackChunkName: "upload" */ '../views/BlogView.vue'),
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
