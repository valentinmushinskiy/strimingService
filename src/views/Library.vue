<template>
  <v-card
  style="min-height:72vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Моя медіатека</h2>
    <v-divider
    ></v-divider>
    <div class="d-flex justify-space-between flex-wrap mt-3" 
      v-bind:class="{'flex-column': mobile}"
    >

          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
          >
            <v-card
            :elevation="hover ? 16 : 2"
            to="/featured"
            v-bind:class="{noPhone: !mobile, phone: mobile}"

            >
              <v-img
                class="white--text align-end"
                height="200px"
                src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              >
                <v-card-title>
                  <v-icon color="red" class="mr-2">mdi-heart</v-icon>
                  Вподобані
                  </v-card-title>
              </v-img>
            </v-card>
          </v-hover>
          <v-hover
            v-slot:default="{ hover }"
            open-delay="50"
            >
            <v-card 
            :elevation="hover ? 16 : 2"
              to="/uploaded"
              v-bind:class="{noPhone: !mobile, phone: mobile, 'mt-3': mobile}"
              >
              <v-img
                class="white--text align-end"
                height="200px"
                src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              >
                <v-card-title>
                  <v-icon color="white" class="mr-2">mdi-upload</v-icon>
                  Завантажені
                  </v-card-title>
              </v-img>
            </v-card>
          </v-hover>

    </div>
    <!-- <v-simple-table>
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
                  <v-icon size="22">mdi-play</v-icon>
                </v-btn>
            </td>
            <td width="20%">{{track.artist}}</td>
            <td>{{track.trackName}}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table> -->
    
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
  data(){
    return{
      mobile: false
    }
  },
  mounted(){
    if(window.innerWidth < 600){
      this.mobile = true 
    }
  }
};

</script>

<style scoped>
  .noPhone{
    width: 49%
  }
  .phone{
    width: 100%
  }
</style>