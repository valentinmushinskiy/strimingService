import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  },
  {
    path: '/search',
    name: 'Search',
    component: () => import('../views/Search.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
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
    path: '/signin',
    name: 'SignIn',
    component: () => import('../views/SignIn.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next()
    }
    
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
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
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  },
  {
    path: '/create_playlist',
    name: 'CreatePlaylist',
    component: () => import('../views/CreatePlaylist.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  },
  {
    path: '/playlist/:id',
    name: 'Playlist',
    component: () => import('../views/Playlist.vue'),
    beforeEnter(to, from, next){
      store.getters.checkUser ? next() : next('/signin')
    }
  }


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
