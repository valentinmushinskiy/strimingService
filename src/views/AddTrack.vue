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
        <v-dialog
          v-model="dialog"
          width="500"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#555"
              outlined
              class="ml-2"
              v-bind="attrs"
              v-on="on"
            >
              Додати
            </v-btn>
          </template>

          <v-card>
            <v-card-title
              class="headline grey lighten-2"
              primary-title
            >
              Політика конфіденціальності
            </v-card-title>

            <v-card-text>
              Сервіс не несе відповідальності за завантажуючий на нього контент
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                color="primary"
                text
                type="submit"
                 @click="dialog = false"
              >
                Погоджуюсь
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- <v-btn class="ml-2" color="#555" outlined type="submit">Додати</v-btn> -->
        </div>
        
      
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
      dialog: false,
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