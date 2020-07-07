import firebase from 'firebase/app'
import 'firebase/storage';


export default {
    state: {
        loadedTracks: [],
        tracks: [],
        createdTrackKey: '',
        loadFeatured: []
    },
    mutations: {
        setFeaturedTracks(state, payload){
            state.loadFeatured = payload
        },
        setLoadedTracks (state, payload) {
            state.loadedTracks = payload
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
    actions: {
        async addToFeatures({commit, state}, payload){
            commit('clearError')
            commit('setLoading', true)
            try {
                const user = firebase.auth().currentUser
                
                await firebase.database().ref(`/users/${user.uid}/featured`).push(payload)
                
                commit('setLoading', false)
                }catch (error) {
                commit('setLoading', false)
                commit('setError', error.message)
                throw error
            }
        },

        loadFeaturedTracks ({commit}) {
            commit('setLoading', true)
            const user = firebase.auth().currentUser
            
            firebase.database().ref(`/users/${user.uid}/featured`).once('value')
              .then((data) => {
                const featuredTracks = []
                const obj = data.val()
                for (let key in obj) {
                featuredTracks.push({
                    id: key,
                    trackName: obj[key].trackName,
                    trackUrl: obj[key].trackUrl,
                    artist: obj[key].artist,
                    userId: obj[key].userId
                  })
                }
                
                commit('setFeaturedTracks', featuredTracks)
                commit('setLoading', false)
              })
              .catch(
                (error) => {
                  console.log(error)
                  commit('setLoading', false)
                }
              )
        },

        loadTracks ({commit}) {
            commit('setLoading', true)
            firebase.database().ref(`tracks`).once('value')
              .then((data) => {
                const tracks = []
                const obj = data.val()
                for (let key in obj) {
                    if(obj[key].trackUrl){
                        tracks.push({
                            id: key,
                            trackName: obj[key].trackName,
                            trackUrl: obj[key].trackUrl,
                            artist: obj[key].artist,
                            userId: obj[key].userId
                          })
                    }
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
            commit('clearError')
            commit('setLoading', true)
            try {
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
                
                commit('setLoading', false)
                }catch (error) {
                commit('setLoading', false)
                commit('setError', error.message)
                throw error
            }
        },

        async deleteTrackFromUploaded({commit}, payload){
            commit('clearError')
            commit('setLoading', true)
            try {
              await firebase.database().ref('tracks').child(payload).remove()
              commit('setLoading', false)
            } catch (error) {
              commit('setLoading', false)
              commit('setError', error.message)
              throw error
            }
        },

        async deleteTrackFromFeatured({commit}, payload){
            commit('clearError')
            commit('setLoading', true)
            try {
              const user = firebase.auth().currentUser
              await firebase.database().ref(`/users/${user.uid}/featured`).child(payload).remove()
              commit('setLoading', false)
            } catch (error) {
              commit('setLoading', false)
              commit('setError', error.message)
              throw error
            }
        },

    },
    getters: {
        loadedAllTracks (state) {
            return state.loadedTracks
        },

        featuredTracks(state){
            return state.loadFeatured
        },

        loadedTracks (state) {
            const user = firebase.auth().currentUser

            return state.loadedTracks.filter(loadedTrack => {
                return loadedTrack.userId === user.uid
            })
        },

        createdTrackKey (state) {
            return state.createdTrackKey
        }
    }
}