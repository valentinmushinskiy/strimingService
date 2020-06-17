import firebase from 'firebase/app'

export default {
    state:{
        playlist: [],
        loadedPlaylists: [],
    },
    mutations:{
        setLoadedPlaylists (state, payload) {
            state.loadedPlaylists = payload
        },
        createPlaylist(state, payload){
            state.playlist.push(payload)
        },
    },
    actions:{
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
    }
}