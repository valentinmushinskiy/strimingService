import Vue from 'vue'
import Vuelidate from 'vuelidate'

import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'

import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/database'
import store from './store'

Vue.use(Vuelidate)

Vue.config.productionTip = false


firebase.initializeApp({
  apiKey: "AIzaSyCFdUvAscyQdOCdLRyCFx10aD8cZDx3fkY",
  authDomain: "youx-diplom.firebaseapp.com",
  databaseURL: "https://youx-diplom.firebaseio.com",
  projectId: "youx-diplom",
  storageBucket: "youx-diplom.appspot.com",
  messagingSenderId: "24127108163",
  appId: "1:24127108163:web:2cd8bfd7b330e67fed50f6",
  measurementId: "G-BL084GFS2X"
})

let app

firebase.auth().onAuthStateChanged(user => {
  if (!app){
    new Vue({
      router,
      vuetify,
      store,
      render: function (h) { return h(App) },
      created(){
        if (user) {
          this.$store.dispatch('loggedUser', user)
        }
      }
    }).$mount('#app')
  }
})