import firebase from 'firebase/app'

export default{
    state: {
        results: []
    },
    mutations: {
        setSearch(state, payload){
            state.results = payload
        }
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
    },
    mutations:{
        loadedResults(state){
            return state.results
        },
    }

}