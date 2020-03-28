import Vue from 'vue'
import Vuex from 'vuex'

import info from './info'
import common from './common'
import user from './user'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    common,
    user,
    info
  }
})
