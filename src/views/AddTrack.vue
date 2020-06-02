<template>
  <v-card 
  height="88vh"
  width="1000"
  class="mx-auto mt-5 px-8 py-5"
  >

    <h2 class="title mb-1">Додавання нового треку</h2>


    <v-divider
    ></v-divider>

    <div class="d-flex">
        <div class="d-flex image mr-5" style="position: relative; width: 30%;">
        <img :src="imageUrl" alt="preview" width="100%" height="auto">

        <v-btn
            class="btn subtitle-2"
            outlined
            @click="onPickFoto"
            >
            Виберіть картинку
        </v-btn>

        <input type="file"
            accept="image/*"
            style="display: none"
            ref="imageInput"
            @change="onFotoPicked"
        >
        </div>
    
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
    </div>

    <v-form @submit.prevent="onUploadTrack">
    


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
      <button type="submit" ref="fileSubmit">Загрузити</button>
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
      }
    },
    // computed:{
    //   artistName() {
    //     return this.$store.getters.info.name 
    //   }
    // },
    methods: {
      onPickFoto(){
        this.$refs.imageInput.click()
      },

      onFotoPicked(event){
          const files = event.target.files
          let filename = files[0].name
          this.fileName = filename
          const fileReader = new FileReader()

          fileReader.addEventListener('load', () => {
            this.imageUrl = fileReader.result
          })
          fileReader.readAsDataURL(files[0])
          this.file = files[0]
      },

      onUploadTrack(){
        if(this.$v.$invalid){
          this.$v.$touch()
          return
        }else if(!this.file){
          return
        }

        console.log(this.trackName)
        let artist = this.$store.getters.info.name 
        const track = {
          artist,
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
        this.$refs.fileSubmit.click()
      }
    },
}
</script>

<style scoped>
.image .btn {
    position: absolute;
    top: 90%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    background-color: #555;
    color: white;
    font-size: 16px;
    padding: 12px 24px;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}
</style>