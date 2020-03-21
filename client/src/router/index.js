import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Search from '../components/Search.vue'
import Library from '../components/Library.vue'
import Settings from '../components/Settings.vue'
import SignIn from '../components/SignIn.vue'
import Register from '../components/Register.vue'

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
    component: Search
  },
  {
    path: '/library',
    name: 'Library',
    component: Library
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
