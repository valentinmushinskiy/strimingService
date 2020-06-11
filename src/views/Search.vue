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
      label="Введіть назву трека або імя користувача"
      solo
    ></v-text-field>
  </v-card>
</template>

<script>

export default {
  data(){
    return{
      search: ''
    }
  },

  methods:{
    log(){
      console.log(this.search)
    }
  }
};

</script>

<style scoped>

</style>