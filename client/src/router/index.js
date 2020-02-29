import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Search from '../views/Search.vue'
import Library from '../views/Library.vue'
import SignIn from '../views/SignIn.vue'
import Register from '../views/Register.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/library',
    name: 'lbrary',
    component: Library
  },
  {
    path: '/signin',
    name:'signin',
    component: SignIn
  },
  {
    path: '/register',
    name:'register',
    component: Register
  }
]

const router = new VueRouter({
  routes
})

export default router
