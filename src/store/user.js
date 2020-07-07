import firebase from 'firebase/app'
import User from './user_help'

import 'firebase/storage';
// import { url } from 'vuelidate/lib/validators';

export default{
    state: {
        user: null,
        results: []
    },
    mutations:{
        setUser(state, payload){
            state.user = payload
        },
        clearTracks(state) {
            state.loadedTracks = []
        },
        setSearch(state, payload){
            state.results = payload
        },
 
    },
    actions:{
        search({commit}, payload){
            commit('clearError')
            commit('setLoading', true)
            try {
                firebase.database().ref(`tracks`).orderByChild(`trackName`)
                .startAt(payload)
                .limitToFirst(1)
                .once('value')

                .then((data) => {
                    const search = []
                    const obj = data.val()
                    for (let key in obj) {
                        search.push({
                            id: key,
                            trackName: obj[key].trackName,
                            trackUrl: obj[key].trackUrl,
                            artist: obj[key].artist,
                            userId: obj[key].userId
                        })
                    }
                    commit('setSearch', search)
                    console.log(search)
                })
                
                commit('setLoading', false)
                }catch (error) {
                commit('setLoading', false)
                commit('setError', error.message)
                throw error
            }
        },


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
        loadedResults(state){
            return state.results
        },

        user(state){
            return state.user
        },

        checkUser(state){
            return state.user !== null
        },
    }
}