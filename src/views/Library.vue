<template>
  <v-card
  height="88vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Моя медіатека</h2>
    <v-divider
    ></v-divider>
    <v-container>
      <v-row>
        <v-col
          v-for="track in tracks"
          :key="track.id"
          cols="12"
        >
          <v-card
            :color="color"
            dark
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div class="d-flex px-5">

                <v-btn
                fab
                small
                class="my-3"
                >
                  <v-icon size="32">mdi-play</v-icon>
                </v-btn>
                
                <v-card-title
                  class="headline"
                  v-text="track.trackName"
                ></v-card-title>
              </div>
            </div>
            <!-- <audio controls>
              <source :src="track.trackUrl" type="audio/mp3" >
            </audio> -->
          </v-card>
        </v-col>
      </v-row>
    </v-container>

    <v-btn to="/add_track" 
    class="mx-2" fab dark 
    color="blue-grey" 
    style="position: fixed;
    bottom: 80px;
    right: 10px">
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

    // this.loading = false
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