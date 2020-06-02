<template>
  <v-card
  height="88vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Головна</h2>
    <v-divider
    ></v-divider>
   <v-btn v-show="isAdmin" 
   to="/create_playlist" 
   >Створити плейлист</v-btn>
   <div class="d-flex justify-start py-5">
     <v-card
      max-width="250"
      v-for="playlist in playlists" :key="playlist.id"
    >
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="headline">{{playlist.name}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <v-img
        :src="playlist.imageUrl"
        height="194"
      ></v-img>

      <v-card-text>
        {{playlist.description}}
      </v-card-text>

      <v-card-actions>
        <v-btn
          text
          color="deep-purple accent-4"
        >
          Listen
        </v-btn>
        
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
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
    playlists () {
      return this.$store.getters.loadedPlaylists
    }
  }

}
</script>
