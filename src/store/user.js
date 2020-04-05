import firebase from 'firebase/app'
import User from './user_help'

import 'firebase/storage';
import { url } from 'vuelidate/lib/validators';

export default{
    state: {
        user: null,
        tracks: [],
        createdTrackKey: ''
    },
    mutations:{
        setUser(state, payload){
            state.user = payload
        },
        createTrack(state, payload) {
            state.tracks.push(payload)
        },
        setCreatedMeetupKey (state, payload) {
            state.createdTrackKey = payload
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

        uploadTrack({commit}, payload){
            // const user = firebase.auth().currentUser
            const track = {
                trackName: payload.trackName
                //date: payload.date.toISOString(),
                // creatorId: user.user.uid
            }
            console.log(track)
            let trackUrl
            let key
            firebase.database().ref('tracks').push(track)
                .then((data) => {
                    key = data.key
                    return key
                })
                .then(key => {
                    const filename = payload.trackName
                    return firebase.storage().ref(`tracks/${key}/${filename}.mp3`).put(payload.file)
                })
                .then(fileData => {
                    let fullPath = fileData.metadata.fullPath
                    return firebase.storage().ref(fullPath).getDownloadURL()
                  })
                .then(URL => {
                    trackUrl = URL
                    console.log(trackUrl)
                    return firebase.database().ref('tracks').child(key).update({trackUrl: trackUrl})
                })
                .then(() => {
                    commit('createTrack', {
                        ...track,
                        trackUrl: trackUrl,
                        id: key
                    })
                })
                .catch(error => {
                    console.log(error);
                })
        },

        loggedUser({commit}, payload){
            console.log(payload.uid)
            commit('setUser', new User(payload.uid))
        },
        logoutUser({commit}){
            firebase.auth().signOut()
            commit('setUser', null)
            commit('clearInfo')
        },
        
    },
    getters:{
        user(state){
            return state.user
        },
        checkUser(state){
            return state.user !== null
        },
        createdTrackKey (state) {
            return state.createdTrackKey
      }
    }
}