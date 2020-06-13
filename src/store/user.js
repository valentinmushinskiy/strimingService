import firebase from 'firebase/app'
import User from './user_help'

import 'firebase/storage';
// import { url } from 'vuelidate/lib/validators';

export default{
    state: {
        loadedTracks: [],
        loadedPlaylists: [],
        user: null,
        createdTrackKey: '',
        tracks: [],
        playlist: []
    },
    mutations:{
        setLoadedTracks (state, payload) {
            state.loadedTracks = payload
        },
        setLoadedPlaylists (state, payload) {
            state.loadedPlaylists = payload
        },
        setUser(state, payload){
            state.user = payload
        },
        createTrack(state, payload) {
            state.tracks.push(payload)
        },
        createPlaylist(state, payload){
            state.playlist.push(payload)
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
            const user = firebase.auth().currentUser
            firebase.database().ref(`tracks`).once('value')
              .then((data) => {
                const tracks = []
                const obj = data.val()
                for (let key in obj) {
                  tracks.push({
                    id: key,
                    trackName: obj[key].trackName,
                    trackUrl: obj[key].trackUrl,
                    artist: obj[key].artist,
                    userId: obj[key].userId
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


        loadPlaylists({commit}){
            commit('setLoading', true)

            firebase.database().ref(`playlists`).once('value')
            .then((data) => {
                const playlists = []
                const obj = data.val()
                for(let key in obj){
                    playlists.push({
                        id: key,
                        name: obj[key].name,
                        description: obj[key].description,
                        imageUrl: obj[key].imageUrl,
                        tracksToPlaylist: obj[key].tracksToPlaylist
                    })
                }
                commit('setLoadedPlaylists', playlists)
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
            const user = firebase.auth().currentUser

            const track = {
                artist: payload.artist,
                trackName: payload.trackName,
                userId: user.uid
            }

            let trackUrl
            let key
            

            firebase.database().ref(`tracks`).push(track)
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
                    return firebase.database().ref(`tracks`).child(key).update({trackUrl: trackUrl})
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

        uploadPlaylist({commit}, {name, imageUrl, description, tracksToPlaylist}){
            
            const sendPlaylist = {
                name: name,
                description: description,
                imageUrl: imageUrl,
                tracksToPlaylist: tracksToPlaylist
            }
            commit('createPlaylist', sendPlaylist)

            firebase.database().ref(`playlists`).push(sendPlaylist)
        },

        async deletePlaylist({commit}, payload){
            commit('clearError')
            commit('setLoading', true)
            try {
              await firebase.database().ref('playlists').child(payload).remove()
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
        },
        
    },
    getters:{
        loadedPlaylists(state){
            return state.loadedPlaylists
        },
        playlist(state){
            return (id) => {
                return state.loadedPlaylists.find((playlist) => {
                    return playlist.id === id
                })
            }
        },
        loadedAllTracks (state) {
            return state.loadedTracks
        },

        loadedTracks (state) {
            const user = firebase.auth().currentUser

            return state.loadedTracks.filter(loadedTrack => {
                return loadedTrack.userId === user.uid
            })
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