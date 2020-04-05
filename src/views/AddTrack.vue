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
        label="Імя"
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
      <button type="submit">Загрузить</button>
      </v-row>
    </v-form>
  </v-card>
</template>

<script>

import {required} from 'vuelidate/lib/validators'

export default {
    data: () => ({
      trackName: '',
      fileName: '',
      fileUrl: '',
      date: new Date(),
      time: new Date(),
      file: null,
      rules: [
        value => !value || value.size < 20000000 || 'файл повинен мати розмір менше 20 мб',
      ],
    }),
    validations: {
      trackName: {
        required
      }
    },
    computed: {
      submittableDateTime(){
        const date = new Date(this.date)

        if(typeof this.time === 'string'){
          let hours = this.time.match(/^(\d+)/)[1]
          let minutes = this.time.match(/:(\d+)/)[1]
          date.setHours(hours)
          date.setMinutes(minutes)
        }else{
          date.setHours(this.time.getHours())
          date.setMinutes(this.time.getMinutes())
        }

        return date
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
          trackName: this.trackName,
          file: this.file,
          fileUrl: this.fileUrl
          // date: this.submittableDateTime
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