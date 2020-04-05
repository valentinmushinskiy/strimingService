import firebase from 'firebase/app'

export default {
    state: {
        tracks: [],
    },

    mutation:{
        createTrack(state, payload) {
            state.tracks.push(payload)
        }
    },

    action: {
        uploadTrack({commit}, payload){
            const track = {
                trackName: payload.trackName,
                file: payload.file,
                // date: payload.date.toISOString(),
                // creatorId: user.id
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
                    return firebase.storage().ref(`tracks/${key}.${filename}`).put()
                })
                .then(fileData => {
                    trackUrl = fileData.metadata.downloadURLs[0]
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
        }
    }
}