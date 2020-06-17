<template>
    <v-app>
        <v-navigation-drawer
        v-model="primaryDrawer.model"
        :clipped="primaryDrawer.clipped"
        :floating="primaryDrawer.floating"
        :mini-variant="primaryDrawer.mini"
        :permanent="primaryDrawer.type === 'permanent'"
        :temporary="primaryDrawer.type === 'temporary'"
        app
        overflow
        
        >
            <v-list>

            <v-list-item-group v-model="item" color="grey darken-3">
            <v-list-item
                v-for="(item, i) in items"
                :key="i"
                :to="item.route"
            >
                <v-list-item-icon>
                <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title v-text="item.text"></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
            </v-list>
            
            <v-divider
            class="mx-4"
            ></v-divider>

            

            <v-btn 
            text @click="logout" 
            v-if="checkUser" 
            class="mt-2 d-flex justify-start" color="red" width="100%">
              <v-icon class="mr-8">mdi-logout</v-icon>Вихід</v-btn>

        </v-navigation-drawer>
        <v-app-bar
        :clipped-left="primaryDrawer.clipped"
        app
        class="grey darken-3"
        dark
        >
        <v-app-bar-nav-icon
            v-if="primaryDrawer.type !== 'default'"
            @click.stop="primaryDrawer.model = !primaryDrawer.model"
        />
        <v-toolbar-title class="mr-8" color="">YOUX</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text to="signin" v-show="!checkUser" color="blue-grey lighten-4">Вхід</v-btn>
          <v-divider
            class="mx-5"
            inset
            vertical
            v-show="!checkUser"
            color="blue-grey lighten-4"
          ></v-divider>
        <v-btn text to="register" v-show="!checkUser" color="blue-grey lighten-4">Реєстрація</v-btn>
        

        <v-btn v-show="checkUser"
        to="/library"
        text>

          <v-icon size="32" class="mr-1" dark>mdi-account-circle</v-icon>
          
          {{name}}
        
        </v-btn>
        
        </v-app-bar>
        <v-content>
          <router-view></router-view>
        </v-content>
        <v-footer
          color="grey darken-3"
          height="80px"
          class="d-flex justify-center pt-3"
          app
          v-if="hasSong"
        >
          <Player/>
        </v-footer>
    </v-app>
</template>


<script>
  import Player from '@/components/player'

  export default {

    components: {
      Player
    },

    data: () => ({
      drawers: ['Default (no property)', 'Permanent', 'Temporary'],
      primaryDrawer: {
        model: true,
        type: 'Default (no property)',
        clipped: true,
        floating: false,
        mini: false,
        
      },
      footer: {
        inset: true,
      },
      item: 1,
    }),
    
    
    async mounted() {
    if (!Object.keys(this.$store.getters.info).length) {
        await this.$store.dispatch('fetchInfo')
    }

    this.loading = false
    },

    methods:{
      logout(){
        this.$store.dispatch('logoutUser')
        this.$router.push('/signin')
      },
    },
    
    
    computed: {
      hasSong() {
        return this.$store.getters.hasSong;
      },
      name(){
        return this.$store.getters.info.name
      },
      error(){
        return this.$store.getters.error
      },
      checkUser(){
        return this.$store.getters.checkUser
      },  
  
      items(){
        if(!this.checkUser){
          return[]
        }
        else{
          return [
            { text: 'Головна', icon: 'mdi-home', route: '/'},
            { text: 'Пошук', icon: 'mdi-magnify', route: '/search'},
            { text: 'Моя медіатека', icon: 'mdi-music-box-multiple', route: '/library'}
          ]
        }
      }
      
    },
    watch: {
      error(fbError){
        console.log(fbError)
      }
    }
  }


</script>

<style scoped>
  .v-input__slot{
    margin-bottom: 0px !important;
  }
</style>
