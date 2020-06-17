import firebase from 'firebase/app'
import User from './user_help'

export default{
    state: {
        user: null,
    },

    mutations:{
        setUser(state, payload){
            state.user = payload
        }
    },

    actions:{
        async registerUser ({commit}, {name, email, password}) {
            commit('clearError')
            commit('setLoading', true)
            try {
              const user = await firebase.auth().createUserWithEmailAndPassword(email, password)
              commit('setUser', new User(user.user.uid))
              await firebase.database().ref(`/users/${user.user.uid}/info`).set({
                    name,
                    role: 'user'
                })
              commit('setLoading', false)
            } catch (error) {
              commit('setLoading', false)
              commit('setError', error.message)
              throw error
            }
        },

        async loginUser ({commit}, {email, password}) {
            commit('clearError')
            commit('setLoading', true)
            try {
              const user = await firebase.auth().signInWithEmailAndPassword(email, password)
              commit('setUser', new User(user.user.uid))
      
              commit('setLoading', false)
            } catch (error) {
              commit('setLoading', false)
              commit('setError', error.message)
              throw error
            }
        },

        loggedUser({commit}, payload){
            commit('setUser', new User(payload.uid))
        },

        logoutUser({commit}){
            firebase.auth().signOut()
            commit('setUser', null)
            commit('clearInfo')
            commit('clearTracks')
            commit('setClaearPlayer')
        },
        
    },

    getters:{
        user(state){
            return state.user
        },

        checkUser(state){
            return state.user !== null
        },
    }
}