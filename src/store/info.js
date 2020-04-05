import firebase from 'firebase/app'


export default {
  state: {
    info: {}
  },
  mutations: {
    setInfo(state, info) {
      state.info = info
    },
    clearInfo(state) {
      state.info = {}
    }
  },
  actions: {
    async fetchInfo({commit}) {
      try {
        const user = firebase.auth().currentUser
        const info = (await firebase.database().ref(`/users/${user.uid}/info`).once('value')).val()

        commit('setInfo', info)
      } catch (e) {}
    }
  },
  getters: {
    info: s => s.info
  }
}
