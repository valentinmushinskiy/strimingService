<template>
  <v-card
  style="min-height:72vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Пошук</h2>
    <v-divider
    ></v-divider>
    <v-text-field
      class="mt-4"
      v-model="search"
      @input="log"
      label="Введіть назву композиції"
      solo
    ></v-text-field>
        <span v-for="result in results" :key="result.id">
            <v-btn
                fab
                x-small
                class="my-3 mr-5"
                @click="play(results, result.id)"
                
            >
                <v-icon size="22"
                >mdi-play</v-icon>
            </v-btn>
            <span class="subtitle-2">{{result.artist}}</span>
            -
            <span>{{result.trackName}}</span>
        </span>
        
        <v-divider></v-divider>
  </v-card>
</template>

<script>

export default {
  data(){
    return{
      search: '',
      results: []
    }
  },
  // computed:{
  //   results(){
  //       return this.$store.getters.loadedResults
  //   }
  // },
  methods:{
    log(){
      this.$store.dispatch('search', this.search)
      this.results = this.$store.getters.loadedResults
    },

    play(tracks, trackId){
        let playTrack = {
            playlist: tracks,
            track: trackId
        }

        console.log(playTrack.playlist)

        this.$store.dispatch('sendPlaylistToPlayer', playTrack)
    },
  }
};

</script>

<style scoped>

</style>