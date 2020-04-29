export default{
    state:{
        track: {}
    },
    mutations:{
        setTrack(state, payload){
            state.track = payload
        }
    },
    actions:{
        sendTrackToPlayer({commit}, playTrack){
            commit('setTrack', playTrack)
        }
    },
    getters:{
        playTrack(state){
            return state.track
        }
    }
}