<template>
  <v-card 
  height="auto"
  width="600"
  class="mx-auto mt-5 px-8 py-5"
  >

    <h2 class="title mb-1">Додавання нового треку</h2>


    <v-divider
    ></v-divider>


    <v-form @submit.prevent="onUploadTrack">
    <v-text-field
        v-model="trackName"
        label="Імя Треку"
        required
        class="my-4"
        style="width: 50%"
    ></v-text-field>

    <small
      class="error"
      v-if="$v.trackName.$dirty && !$v.trackName.required"
    >
    Поле обовязкове
    </small>

    <v-text-field
        v-model="artist"
        label="Виконавець"
        required
        style="width: 50%"
    ></v-text-field>
    <small
      class="error"
      v-if="$v.artist.$dirty && !$v.artist.required"
    >
    Поле обовязкове
    </small>

    <v-row class="align-center">
      <v-col cols="4" md="4">
        <v-btn color="blue-grey"
          outlined
          @click="onPickFile"
          >
            Виберіть файл
        </v-btn>
      
        <input type="file"
              accept="audio/mp3"
              style="display: none"
              ref="fileInput"
              @change="onFilePicked"
        >

      </v-col>

      <v-col cols="8" md="8">
        <span class="mt-2 subtitle-2">{{fileName}}</span>
      </v-col>
      <button type="submit">Загрузити</button>
      </v-row>
    </v-form>
  </v-card>
</template>

<script>

import {required} from 'vuelidate/lib/validators'

export default {
    data: () => ({
      artist: '',
      trackName: '',
      fileName: '',
      fileUrl: '',
      file: null,
      rules: [
        value => !value || value.size < 20000000 || 'файл повинен мати розмір менше 20 мб',
      ],
    }),

    validations: {
      trackName: {
        required
      },
      artist: {
        required
      }
    },

    methods: {
      onUploadTrack(){
        if(this.$v.$invalid){
          this.$v.$touch()
          return
        }else if(!this.file){
          return
        }

        console.log(this.trackName)

        const track = {
          artist: this.artist,
          trackName: this.trackName,
          file: this.file,
          fileUrl: this.fileUrl
        }

        this.$store.dispatch('uploadTrack', track)
        this.$router.push('/library')
      },
      
      onPickFile(){
        this.$refs.fileInput.click()
      },
      onFilePicked(event){
        const files = event.target.files
        let filename = files[0].name
        this.fileName = filename
        const fileReader = new FileReader()
        fileReader.addEventListener('load', () => {
          this.fileUrl = fileReader.result
        })
        fileReader.readAsDataURL(files[0])
        this.file = files[0]
      }
    },
}
</script>

<style scoped>
</style>