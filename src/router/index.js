import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue')
  },
  {
    path: '/library',
    name: 'Library',
    component: () => import('../views/Library.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  },
  {
    path: '/settings',
    name: 'Settings',
    component: () => import('../views/Settings.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: () => import('../views/SignIn.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue')
  },
  {
    path: '/termsOfUse',
    name: 'TermsOfUse',
    component: () => import('../views/TermsOfUse.vue')
  },
  {
    path: '/add_track',
    name: 'AddTrack',
    component: () => import('../views/AddTrack.vue'),
    // beforeEnter(to, from, next){
    //   store.getters.checkUser ? next() : next('/signin')
    // }
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
