<template>
  <v-app>
        <h1>Виберіть трек на вашому пристрої</h1>
        <v-file-input 
            accept="audio/mp3, audio/wav"
            show-size 
            counter 
            multiple 
            label="File input"></v-file-input>
  </v-app>
</template>

<script>
export default {
    data: () => ({
      rules: [
        value => !value || value.size < 2000000 || 'Avatar size should be less than 2 MB!',
      ],
    }),
}
</script>

<style>

</style>