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

            <v-list-item-group v-model="item" color="blue-grey">
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


        </v-navigation-drawer>
        <v-app-bar
        :clipped-left="primaryDrawer.clipped"
        app
        color="blue-grey"
        >
        <v-app-bar-nav-icon
            v-if="primaryDrawer.type !== 'permanent'"
            @click.stop="primaryDrawer.model = !primaryDrawer.model"
        />
        <v-toolbar-title>YOUX</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn text to="signin" v-show="!checkUser" color="#212121">Вхід</v-btn>
          <v-divider
            class="mx-5"
            inset
            vertical
            v-show="!checkUser"
          ></v-divider>
        <v-btn text to="register" v-show="!checkUser" color="#212121">Реєстрація</v-btn>
        

        <v-btn v-show="checkUser" class="mr-5"
        text>

          <v-icon size="32" class="mr-1">mdi-account-circle</v-icon>
          
          {{name}}
        
        </v-btn>
        
        <v-btn outlined @click="logout" v-show="checkUser" color="#212121" class="mr-5">Вийти</v-btn>
        </v-app-bar>
        <v-content>
          <router-view></router-view>
        </v-content>

        <v-footer
          :inset="footer.inset"
          app
          color="blue-grey"
        >
            <audio controls>
              <source type="audio/mp3" >
            </audio>
        </v-footer>
    </v-app>
</template>


<script>
  export default {
    data: () => ({
      drawers: ['Default (no property)', 'Permanent', 'Temporary'],
      primaryDrawer: {
        model: null,
        type: 'default (no property)',
        clipped: true,
        floating: false,
        mini: true,
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
      },
      
    },
    
    
    computed: {
      name() {
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
          return[
             { text: 'Головна', icon: 'mdi-home', route: '/'},
             { text: 'Пошук', icon: 'mdi-magnify', route: '/search'},
            ]
        }
        else{
          return [
            { text: 'Головна', icon: 'mdi-home', route: '/'},
            { text: 'Пошук', icon: 'mdi-magnify', route: '/search'},
            { text: 'Моя медіатека', icon: 'mdi-music-box-multiple', route: '/library'},
            { text: 'Налаштування', icon: 'mdi-cogs', route: '/settings'},
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

