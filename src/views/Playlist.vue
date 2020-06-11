<template>
  <v-card
  style="min-height:72vh"
  width="1000"
  class="mx-auto mt-5 px-8 py-5"
  v-if="playlist"
  >
    <h2 class="title mb-1">{{playlist.name}}</h2>

    <v-divider
    ></v-divider>
    <div class="wrap">
        <div class="d-flex pt-4">
            <div class="img">
                <img :src="playlist.imageUrl"
                    width="100%"
                >
            </div>
            <div class="audio pl-5">
                <div v-for="track in playlist.tracksToPlaylist" :key="track.id">
                    <span class="subtitle-2">{{track.artist}}</span>
                    -
                    <span>{{track.trackName}}</span>
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