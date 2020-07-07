<template>
    <div class="player"
      dark
    >
      <div class="d-flex align-center">
      <div class="mr-7" v-if="!mobile">
          <v-btn icon small>
          <v-icon size="24" @click="prevTrack" color="blue-grey lighten-4">mdi-skip-previous-circle</v-icon>
          </v-btn>
          <v-btn icon 
          @click="play"
          >
            <v-icon size="44" color="blue-grey lighten-4">
              {{ isTimerPlaying ? 'mdi-pause-circle' : 'mdi-play-circle' }}
            </v-icon>
          </v-btn>

          <v-btn icon small>
            <v-icon size="24" @click="nextTrack" color="blue-grey lighten-4">mdi-skip-next-circle</v-icon>
          </v-btn>
      </div>
      
      
      <v-card
      width="400px"
      height="55px"
      outlined
      color="transparent"
      class="mr-4"
      >

      <span class="d-flex justify-space-between">
        <span v-if="mobile">
          <div class="mr-1" >
            <v-btn icon x-small>
            <v-icon size="20" @click="prevTrack" color="blue-grey lighten-4">mdi-skip-previous-circle</v-icon>
            </v-btn>
            <v-btn icon 
            @click="play"
            >
              <v-icon size="24" color="blue-grey lighten-4">
                {{ isTimerPlaying ? 'mdi-pause-circle' : 'mdi-play-circle' }}
              </v-icon>
            </v-btn>

            <v-btn icon x-small>
              <v-icon size="20" @click="nextTrack" color="blue-grey lighten-4">mdi-skip-next-circle</v-icon>
            </v-btn>
          </div>
        </span>
        <span class="d-flex justify-center subtitle-1" style="color: #fff">

        <span class="subtitle-2" >{{currentTrack.trackName}}</span>
        <pre class="caption" style="margin-top: 1px"> - {{currentTrack.artist}}</pre>  
        </span>
        <span class="body-2"
        style="color: #fff">
          {{ currentTime }} / {{ duration }}
        </span>
      </span>
      
        <div class="progress" ref="progress">
          
          <div class="progress__bar" color="blue-grey lighten-4" @click="clickProgress">
            <div class="progress__current" color="blue-grey lighten-2" :style="{ width : barWidth }"></div>
          </div>
          
        </div>

      </v-card>
      
      </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      mobile: false,
      audio: null,
      circleLeft: null,
      barWidth: null,
      duration: null,
      currentTime: null,
      isTimerPlaying: false,
      currentTrack: null,
      currentTrackIndex: 0,
      transitionName: null,
      tracks: []
    };
  },

  methods: {
    tracksToPlay(){
      if(this.$store.getters.hasSong){
        let playlistTracks = this.$store.getters.playPlaylist
        this.tracks = playlistTracks
        console.log(this.tracks)
      }
    },

    trackId(){
      if(this.$store.getters.hasSong){
        let trackId = this.$store.getters.playTrack
        this.currentTrack = this.tracks.find(track => track.id === trackId)
        console.log(this.currentTrack)
      }
    },

    play() {
      if (this.audio.paused){
        this.audio.play();
        this.isTimerPlaying = true;
      } else {
        this.audio.pause();
        this.isTimerPlaying = false;
      }
    },

    generateTime() {
      let width = (100 / this.audio.duration) * this.audio.currentTime;
      this.barWidth = width + "%";
      this.circleLeft = width + "%";
      let durmin = Math.floor(this.audio.duration / 60);
      let dursec = Math.floor(this.audio.duration - durmin * 60);
      let curmin = Math.floor(this.audio.currentTime / 60);
      let cursec = Math.floor(this.audio.currentTime - curmin * 60);
      if (durmin < 10) {
        durmin = "0" + durmin;
      }
      if (dursec < 10) {
        dursec = "0" + dursec;
      }
      if (curmin < 10) {
        curmin = "0" + curmin;
      }
      if (cursec < 10) {
        cursec = "0" + cursec;
      }
      this.duration = durmin + ":" + dursec;
      this.currentTime = curmin + ":" + cursec;
    },

    updateBar(x) {
      let progress = this.$refs.progress;
      let maxduration = this.audio.duration;
      let position = x - progress.getBoundingClientRect().left;
      let percentage = (100 * position) / progress.offsetWidth;
      if (percentage > 100) {
        percentage = 100;
      }
      if (percentage < 0) {
        percentage = 0;
      }
      this.barWidth = percentage + "%";
      this.circleLeft = percentage + "%";
      this.audio.currentTime = (maxduration * percentage) / 100;
      this.audio.play();
    },

    clickProgress(e) {
      
      this.isTimerPlaying = true;
      this.audio.pause();
      this.updateBar(e.pageX);
    },

    prevTrack() {
      this.transitionName = "scale-in";
      this.isShowCover = false;
      if (this.currentTrackIndex > 0) {
        this.currentTrackIndex--;
      } else {
        this.currentTrackIndex = this.tracks.length - 1;
      }
      this.currentTrack = this.tracks[this.currentTrackIndex];
      this.resetPlayer();
    },

    nextTrack() {
      this.transitionName = "scale-out";
      this.isShowCover = false;
      if (this.currentTrackIndex < this.tracks.length - 1) {
        this.currentTrackIndex++;
      } else {
        this.currentTrackIndex = 0;
      }
      this.currentTrack = this.tracks[this.currentTrackIndex];
      this.resetPlayer();
    },

    resetPlayer() {
      this.barWidth = 0;
      this.circleLeft = 0;
      this.audio.currentTime = 0;
      this.audio.src = this.currentTrack.trackUrl;
      setTimeout(() => {
        if(this.isTimerPlaying) {
          this.audio.play();
        } else {
          this.audio.play();
        }
      }, 300);
    }
  },

  mounted(){
    
    this.$store.watch(
      (state, getters) => getters.playPlaylist,
      (newValue, oldValue) => {
        if(newValue != oldValue){
          console.log(newValue)
          this.tracks = newValue
          this.nextTrack()
          this.prevTrack()
        }
      }
    )
    if(window.innerWidth < 600){
      this.mobile = true 
    }
  },

  created() {
    if(this.$store.getters.hasSong){
      let vm = this;
      // if(this.$store.getters.hasResult){
      //   vm.searchedTrack()
      // }else{
        vm.tracksToPlay()
        vm.trackId()
        
      // }
      
      // this.currentTrack = tracks.find(track => track.id === trackId);
      this.audio = new Audio();
      this.audio.src = this.currentTrack.trackUrl;
      this.audio.ontimeupdate = function() {
        vm.generateTime();
      };
      this.audio.onloadedmetadata = function() {
        vm.generateTime();
      };
      this.audio.onended = function() {
        vm.nextTrack();
        this.isTimerPlaying = true;
      };
      vm.play()
    }else{
      vm.paused()
    }
  }
}
</script>

<style>
.progress{
  position: relative;
}
.progress__bar {
  height: 6px;
  width: 100%;
  cursor: pointer;
  background-color: #CFD8DC;
  display: inline-block;
  border-radius: 10px;
}

.progress__current {
  height: inherit;
  width: 0%;
  background-color: #90A4AE;
  border-radius: 10px;
}
</style>