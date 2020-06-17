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
      max-width="226"
      class="mx-1 my-4"
      v-for="playlist in playlists" :key="playlist.id"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="headline">{{playlist.name}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-img
        :src="playlist.imageUrl"
        height="200"
      ></v-img>

      <v-card-text>
        {{playlist.description}}
      </v-card-text>
      <div class="d-flex">
        <v-btn v-show="isAdmin" 
        @click="deletePlaylist(playlist.id)"
        class="subtitle-2 ml-3"
        >
          <v-icon>mdi-delete</v-icon>
        </v-btn>
        <v-btn v-show="isAdmin" 
        @click="editPlaylist(playlist.id)"
        class="subtitle-2 ml-2"
        >
          <v-icon>mdi-pencil-outline</v-icon>
          
        </v-btn>
      </div>
      <v-card-actions>
        <v-btn
          text
          color="deep-purple accent-4"
          :to="`/playlist/${playlist.id}`"
        >
          <span>Детальніше</span>
        </v-btn>
      </v-card-actions>
    </v-card>
   </div>
   
  </v-card>
</template>

<script>

export default {
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
  }

}
</script>
