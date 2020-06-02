<template>
  <v-alert
    :value="true"
    transition="scale-transition"
    border="right"
    class="grey darken-3"
    dark   
    >
    <div class="player">
      <div class="d-flex align-center">
      <div class="mr-7">
          <v-btn icon small>
          <v-icon size="24" color="blue-grey lighten-4">mdi-skip-previous-circle</v-icon>
          </v-btn>
          <v-btn icon>
          <v-icon size="44" color="blue-grey lighten-4">
              {{ isPlaying ? 'mdi-pause-circle' : 'mdi-play-circle' }}
          </v-icon>
          </v-btn>

          <v-btn icon small>
            <v-icon size="24" color="blue-grey lighten-4">mdi-skip-next-circle</v-icon>
          </v-btn>
      </div>
      
      
      <v-card
      width="400px"
      height="55px"
      outlined
      color="transparent"
      >

      <span 
          class="d-flex justify-center subtitle-1" color="#212121" 
      >{{trackUrl}}</span>

          <v-slider
          color="blue-grey lighten-4"
          track-color="blue-grey lighten-2"
          label="00:00"
          min="0"
          max="100"
          step="1"
          ></v-slider>
      </v-card>
      <v-card
      width="100px"
      height="55px"
      outlined
      color="transparent"
      class="ml-5 pt-1 d-flex align-center"

      >
      
      <v-slider
      prepend-icon="mdi-volume-high"
      min="0"
      max="100"
      step="1"
      color="blue-grey lighten-4"
      track-color="blue-grey lighten-2"
      >
      </v-slider>

      </v-card>
      </div>
  </div>
  </v-alert>
</template>

<script>
export default {
  data: () => ({
    isPlaying: false
  }),
  computed:{

    track(){
      let track = JSON.parse(JSON.stringify(this.$store.getters.playTrack))
      console.log(track)
      return track
    },

    trackUrl(){
      function isEmpty(obj) {
        for (let key in obj) {
          // если тело цикла начнет выполняться - значит в объекте есть свойства
          return false;
        }
        return true;
      }

      let track = this.track
      let playTrack
      let flag = isEmpty(track)

      if(!flag){
        playTrack = new Audio(track.url)
        if(!this.isPlaying){
          this.isPlaying = true
          return playTrack.play()
        }else{
          return playTrack.pause()
        }
        
      }
    }
  }



  // player(){
  //   if(!this.isPlaying){
  //     playtrack = new Audio(this.$store.getters.playTrack.url)
      
  //     this.isPlaying = true
  //     playtrack.play()
  //   }else{
  //     this.isPlaying = false
  //     console.log(1)
  //     playtrack.pause()
  //   }
  // },
}
</script>

<style>

</style>