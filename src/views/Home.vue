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
  </v-card>
</template>

<script>

export default {
  data () {
      return {

    }
  },
  
  computed:{
    isAdmin() {
      return this.$store.getters.info.role == 'admin' ? true : false 
    }
  }

}
</script>
