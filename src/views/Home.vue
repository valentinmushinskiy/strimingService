<template>
  <v-card
  style="min-height:82vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Головна</h2>
    <v-divider
    ></v-divider>
    <v-btn v-show="isAdmin" 
    class="mt-3"
    to="/create_playlist" 
    >Створити плейлист</v-btn>
   <div class="d-flex justify-start flex-wrap">
     <v-card
      v-bind:class="{noPhone: !mobile, phone: mobile}"
      class="mx-1 my-4"
      v-for="playlist in playlists" :key="playlist.id"
      :to="`/playlist/${playlist.id}`"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="headline d-flex justify-space-between">
            <span>{{playlist.name}}</span>
            <v-btn 
              v-show="isAdmin" 
              @click="deletePlaylist(playlist.id)"
              icon
              >
                <v-icon>mdi-delete</v-icon>
            </v-btn>
        </v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-img
        :src="playlist.imageUrl"
        v-bind:class="{img: !mobile, '.mobile-img': mobile}"
      ></v-img>

      <v-card-text>
        {{playlist.description}}
      </v-card-text>
    </v-card>
   </div>
   
  </v-card>
</template>

<script>

export default {
  data(){
      return{
        mobile: false
      }
    },  
    async mounted() {
    if (!Object.keys(this.$store.getters.loadedPlaylists).length) {
        await this.$store.dispatch('loadPlaylists')
    }
  },
  
  computed:{
    isAdmin() {
      return this.$store.getters.info.role == 'admin' ? true : false 
    },
    playlists() {
      return this.$store.getters.loadedPlaylists
    }
  },

  methods:{
    deletePlaylist(id){
      console.log(id)
      this.$store.dispatch('deletePlaylist', id)
        .then(() => {
          this.$store.dispatch('loadPlaylists')
        })

    }
  },

  created(){
    if(window.innerWidth < 600){
      this.mobile = true 
    }
  }

}
</script>
<style scoped>
.noPhone{
  max-width: 226px
}

.phone{
  width: 100%
}

.img{
  height:200px
}

.mobile-img{
  height: auto;
}


</style>