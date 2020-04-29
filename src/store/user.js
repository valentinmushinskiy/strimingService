import firebase from 'firebase/app'
import User from './user_help'

import 'firebase/storage';
// import { url } from 'vuelidate/lib/validators';

export default{
    state: {
        loadedTracks: [],
        user: null,
        createdTrackKey: '',
        tracks: []
    },
    mutations:{
        setLoadedTracks (state, payload) {
            state.loadedTracks = payload
        },
        setUser(state, payload){
            state.user = payload
        },
        createTrack(state, payload) {
            state.tracks.push(payload)
        },
        setCreatedTrackKey (state, payload) {
            state.createdTrackKey = payload
        },
        clearTracks(state) {
            state.loadedTracks = []
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

        loadTracks ({commit}) {
            commit('setLoading', true)
            console.log('here')
            const user = firebase.auth().currentUser
            firebase.database().ref(`users/${user.uid}/tracks`).once('value')
              .then((data) => {
                const tracks = []
                const obj = data.val()
                for (let key in obj) {
                  tracks.push({
                    id: key,
                    trackName: obj[key].trackName,
                    trackUrl: obj[key].trackUrl,
                    artist: obj[key].artist
                  })
                }
                commit('setLoadedTracks', tracks)
                commit('setLoading', false)
              })
              .catch(
                (error) => {
                  console.log(error)
                  commit('setLoading', false)
                }
              )
        },

        uploadTrack({commit}, payload){
            const track = {
                artist: payload.artist,
                trackName: payload.trackName
            }
            console.log(track)
            let trackUrl
            let key
            const user = firebase.auth().currentUser
            
            
            firebase.database().ref(`users/${user.uid}/tracks`).push(track)
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
                    return firebase.database().ref(`users/${user.uid}/tracks`).child(key).update({trackUrl: trackUrl})
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
            commit('clearTracks')
        },
        
    },
    getters:{
        loadedTracks (state) {
            return state.loadedTracks
        },
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