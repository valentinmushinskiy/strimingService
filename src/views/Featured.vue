<template>
  <v-card
    style="min-height:72vh"
    width="1000"
    class="mx-auto mt-5 px-8 py-5"
  >
    <h2 class="title mb-1">Вподобані</h2>
    <v-divider></v-divider>
    <div v-for="track in tracks" :key="track.id">
        <span class="d-flex justify-space-between">
            <span>
                <v-btn
                    fab
                    x-small
                    class="my-3 mr-3"
                    @click="play(tracks, track.id)"
                >
                    <v-icon size="22"
                    >mdi-play</v-icon>
                </v-btn>
                
                <span class="subtitle-2">{{track.artist}}</span>
                -
                <span>{{track.trackName}}</span>
            </span>
            
            <v-spacer></v-spacer>
            <span>
                <v-btn
                    icon
                    x-small
                    class="my-5 mr-3"
                    @click="deleteTrack(track.id)"
                >
                    <v-icon size="22"
                    >mdi-delete</v-icon>
                </v-btn>
            </span>

        </span>
        <v-divider></v-divider>
    </div>
  </v-card>
</template>

<script>
export default {
  async mounted() {
    if (!Object.keys(this.$store.getters.featuredTracks).length) {
        await this.$store.dispatch('loadFeaturedTracks')
    }
  },

  methods:{
    play(tracks, trackId){
        let playTrack = {
            playlist: tracks,
            track: trackId
        }

        console.log(playTrack.playlist)
        this.$store.dispatch('sendPlaylistToPlayer', playTrack)
    },
    deleteTrack(trackId){
      this.$store.dispatch('deleteTrackFromFeatured', trackId)
          .then(() => {
              this.$store.dispatch('loadFeaturedTracks')
          })
    }
  },
  computed: {
    tracks () {
        return this.$store.getters.featuredTracks
    },
  }
}
</script>

<style>

</style>