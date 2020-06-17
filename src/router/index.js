import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'
import firebase from 'firebase'

import Home from '../views/Home.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    meta: {auth: true},
    component: Home,

  },
  {
    path: '/search',
    name: 'Search',
    meta: {auth: true},
    component: () => import('../views/Search.vue'),
  },
  {
    path: '/library',
    name: 'Library',
    meta: {auth: true},
    component: () => import('../views/Library.vue'),
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: () => import('../views/SignIn.vue'),
    
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
    meta: {auth: true},
    component: () => import('../views/AddTrack.vue'),

  },
  {
    path: '/create_playlist',
    name: 'CreatePlaylist',
    meta: {auth: true},
    component: () => import('../views/CreatePlaylist.vue'),
  },
  {
    path: '/featured',
    name: 'Featured',
    meta: {auth: true},
    component: () => import('../views/Featured.vue'),
  },
  {
    path: '/uploaded',
    name: 'Uploaded',
    meta: {auth: true},
    component: () => import('../views/Uploaded.vue'),

  },
  {
    path: '/playlist/:id',
    name: 'Playlist',
    meta: {auth: true},
    component: () => import('../views/Playlist.vue'),
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const currentUser = firebase.auth().currentUser
  const requireAuth = to.matched.some(Library => Library.meta.auth)

  if(requireAuth && !currentUser){
    next('/signin')
  }else if (to.path == '/login' && currentUser) {
    next('/')
  }else{
    next()
  }

})

export default router
