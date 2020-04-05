<template>
  <v-card
  height="88vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Моя медіатека</h2>
    <v-divider
    ></v-divider>

    <v-btn to="/add_track" 
    class="mx-2" fab dark 
    color="indigo" 
    style="position: fixed;
    bottom: 10px;
    right: 10px">
      <v-icon dark>mdi-plus</v-icon>
    </v-btn>
  </v-card>
</template>

<script>

export default {

};

</script>

<style scoped>

</style>