<template>
  <v-card 
  height="88vh"
  width="600"
  class="mx-auto mt-5 px-8 py-5"
  >

    <h2 class="title mb-1">Додавання нового треку</h2>


    <v-divider
    ></v-divider>

    <div class="d-flex">
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
    

        <div class="d-flex">
          <v-btn color="blue-grey"
            outlined
            @click="onPickFile"
            >
              Виберіть файл
          </v-btn>
        
        </div>
        
        <div class="mb-4 d-flex align-center">
          <v-checkbox
          v-model="checkbox"
          id="check"
        ></v-checkbox>
        <label for="check">Сервіс не несе відповідальності за контент який ви завантажуєте.</label>
        </div>
        <v-btn v-if="checkbox" class="ml-2" ref="submitTrack" color="#555" outlined type="submit">Додати</v-btn>
        
        <input type="file"
              accept="audio/mp3"
              style="display: none"
              ref="fileInput"
              @change="onFilePicked"
        >
        <span class="mt-2 subtitle-2">{{fileName}}</span>
    </v-form>
  </v-card>
</template>

<script>

import {required} from 'vuelidate/lib/validators'

export default {
    data: () => ({
      checkbox: false,
      dialog: false,
      agree: false,
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

    computed: {
      watch(){
        if(this.agree){
          this.$refs.submitTrack.click()
        }
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
        let artist = this.$store.getters.info.name 
        const track = {
          artist,
          trackName: this.trackName,
          file: this.file,
          fileUrl: this.fileUrl
        }

        this.$store.dispatch('uploadTrack', track)
        // .then(() => {
        //     this.$store.dispatch('loadTracks')
        // })
        this.$router.push('/library')
      },
      
      onPickFile(){
        this.$refs.fileInput.click()
      },

      onSubmit(){
        this.agree = true
        if(this.agree){

          this.$refs.submitTrack.click()
        }
        
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