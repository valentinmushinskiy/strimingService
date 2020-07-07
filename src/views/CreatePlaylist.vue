<template>
  <v-card
  style="min-height:82vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Створення нового плейлиста</h2>
    <v-divider></v-divider>
   <v-text-field
   v-model="name"
   placeholder="Назва плейлиста"
   ></v-text-field>
   
    <div class="d-flex">
        <div class="d-flex image mr-5" style="position: relative; width: 30%; height: 30%">
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

        <div style="width:70%">

            <v-textarea
                v-model="description"
                solo
                label="Опис"
                width="100%"
            ></v-textarea>

        <v-dialog scrollable width="500px">

        <template v-slot:activator="{ on }">
            <v-btn color="#555" outlined dark v-on="on">Оберіть треки</v-btn>
        </template>
        

        <v-card>
            <v-card-title>Оберіть треки</v-card-title>
            <v-divider class="pb-4"></v-divider>
            <v-card-text style="height: 500px;">
                <v-simple-table>
                    <tr v-for="track in tracks" :key="track.id" >
                        <td>
                            <span class="subtitle-2 pr-2">{{track.artist}}</span>
                            -
                            <span class="pl-2">{{track.trackName}}</span>
                        </td>
                        <td class="d-flex justify-end">
                            <v-btn text icon @click="addTrack(track)"><v-icon dark>mdi-{{tracksToPlaylist.includes(track) ? 'check' : 'plus'}}</v-icon></v-btn>
                        </td>
                    </tr>
                </v-simple-table>
            </v-card-text>
        </v-card>
        
        </v-dialog>
        <v-btn class="ml-2" color="#555" outlined type="submit" @click="onUploadPlaylist">Створити</v-btn>
            <v-simple-table>
                <tr v-for="track in tracksToPlaylist" :key="track.id">
                    <td>
                        <span class="subtitle-2 pr-2">{{track.artist}}</span>
                        -
                        <span class="pl-2">{{track.trackName}}</span>
                    </td>
                    
                </tr>
            </v-simple-table>
        </div>

        
        
    </div>
    
  </v-card>
</template>

<script>
export default {
    data: () => ({
        tracksToPlaylist: [],
        name: '',
        imageUrl: 'https://www.tibs.org.tw/images/default.jpg',
        description: ''
    }),

    async mounted() {
        if (!Object.keys(this.$store.getters.loadedTracks).length) {
            await this.$store.dispatch('loadTracks')
        }
    },

    methods:{
        addTrack(track){
            this.tracksToPlaylist.push(track)
            console.log(this.tracksToPlaylist)
        },

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

        onUploadPlaylist(){
            const playlist = {
                name: this.name,
                imageUrl: this.imageUrl,
                description: this.description,
                tracksToPlaylist: this.tracksToPlaylist
            }

            console.log(playlist)

            this.$store.dispatch('uploadPlaylist', playlist)
            .then(() => {
                this.$store.dispatch('loadPlaylists')
            })

            .catch(err => {
                this.submitStatus = err.message
            })

            this.$router.push('/')
        }
    },
    computed: {
        tracks () {
            return this.$store.getters.loadedAllTracks
        },
    }

}
</script>

<style>
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