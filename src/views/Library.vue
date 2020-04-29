<template>
  <v-card
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Моя медіатека</h2>
    <v-divider
    ></v-divider>
    <v-simple-table>
      <template v-slot:default>
        <thead>
          <tr>
            <th class="text-left"></th>
            <th class="text-left">Artist</th>
            <th class="text-left">Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="track in tracks" :key="track.id">
            <td width="5%">
              
              <v-btn
                fab
                x-small
                class="my-3"
                @click='getTrackData'
                >
                  <v-icon size="22" 
                  :data-trackArtist="track.artist"
                  :data-trackName="track.trackName"
                  :data-trackUrl="track.trackUrl">mdi-play</v-icon>
                </v-btn>
            </td>
            <td width="20%">{{track.artist}}</td>
            <td>{{track.trackName}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    
            <!-- <audio controls>
              <source :src="track.trackUrl" type="audio/mp3" >
            </audio> -->
    <v-btn to="/add_track" 
    class="mx-2" fab
    style="position: fixed;
    bottom: 10px;
    right: 10px;
    z-index: 1000"
    >
      <v-icon dark>mdi-plus</v-icon>
    </v-btn>
  </v-card>
</template>

<script>



export default {
  async mounted() {
    if (!Object.keys(this.$store.getters.loadedTracks).length) {
        await this.$store.dispatch('loadTracks')
    }
  },

  methods:{
    getTrackData(e){

      let target = event.target

      let playTrack = {
        artist: target.getAttribute('data-trackArtist'),
        name: target.getAttribute('data-trackName'),
        url: target.getAttribute('data-trackUrl')
      }

      this.$store.dispatch('sendTrackToPlayer', playTrack)
    }
  },
  computed: {
    tracks () {
      return this.$store.getters.loadedTracks
    },
    color(){
      function getRandomInt(max) {
        return Math.floor(Math.random() * Math.floor(max));
      }

      let rnd = getRandomInt(10);
      switch(rnd){
        case 0: 
          return 'primary';
          break;
        case 1: 
          return 'pink';
          break;
        case 2: 
          return 'indigo';
          break;
        case 3: 
          return 'teal';
          break;
        case 4: 
          return 'cyan'
          break;
        case 5: 
          return 'purple';
          break;
        case 6: 
          return 'warning';
          break;
        case 7: 
          return 'success';
          break;
        case 8: 
          return 'error';
          break;
        case 9: 
          return 'deep-orange';
          break;
      }
    }
  }
};

</script>

<style scoped>

</style>