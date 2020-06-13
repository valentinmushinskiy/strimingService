<template>
  <v-card
  style="min-height:72vh"
  width="1000"
  class="mx-auto mt-5 px-8 py-5"
  v-if="playlist"
  >
    <h2 class="title mb-1">{{playlist.name}}</h2>
    <h4>{{playlist.description}}</h4>
    <v-divider></v-divider>
    <div class="wrap">
        <div class="d-flex pt-4">
            
            <div class="img col-4">
                <img :src="playlist.imageUrl"
                    width="100%"
                >
            </div>
            <div class="audio pl-5 col-8">
                <div v-for="track in playlist.tracksToPlaylist" :key="track.id">
                    <span>
                        <v-btn
                            fab
                            x-small
                            class="my-3 mr-5"
                            @click="play(playlist.tracksToPlaylist, track.id)"
                            
                        >
                            <v-icon size="22"
                            >mdi-play</v-icon>
                        </v-btn>
                        <span class="subtitle-2">{{track.artist}}</span>
                        -
                        <span>{{track.trackName}}</span>
                    </span>
                    
                    <v-divider></v-divider>
                </div>
            </div>
        </div>
    </div>
    
  </v-card>
</template>

<script>
export default {
    computed:{
        playlist(){
            return this.$store.getters.playlist(this.$route.params.id)
        }
    },
    methods:{
        play(tracks, trackId){

            let playTrack = {
                playlist: tracks,
                track: trackId
            }

            console.log(playTrack.playlist)

            this.$store.dispatch('sendTrackToPlayer', playTrack)
        }
    }
}
</script>

<style>
    .wrap{
        width: 100%;
    }
    .img{
        width: 25%
    }
</style>