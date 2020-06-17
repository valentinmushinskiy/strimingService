export default{
    state:{
        playlist: [],
        trackId: null,
    },

    mutations:{
        setTrack(state, payload){
            state.trackId = payload
        },
        setPlaylist(state, payload){
            state.playlist = payload
        },
        setClaearPlayer(state){
            console.log('empty')
            state.trackId = null
            state.playlist = []
        }
    },

    actions:{
        sendPlaylistToPlayer({commit}, playTrack){
            commit('setPlaylist', playTrack.playlist)
            commit('setTrack', playTrack.track)

            console.log(playTrack.track)
        },
    },

    getters:{
        hasSong (state){
            return state.playlist && state.playlist.length > 0
        },
        playPlaylist(state){
            return state.playlist
        },
        playTrack(state){
            return state.trackId
        },
        playPlaylistObject(state){
            let play = {
                playlist: state.playlist,
                trackId: state.trackId
            }
            console.log(play)
            return play
        },
    }
}