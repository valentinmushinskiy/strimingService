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
            <v-list rounded>

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
        <v-btn text>SIGN IN</v-btn>
          <v-divider
            class="mx-4"
            inset
            vertical
          ></v-divider>
        <v-btn text :to=register>REGISTER</v-btn>
        </v-app-bar>
        <v-content>
          <router-view></router-view>
        </v-content>
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
        mini: false,
      },
      footer: {
        inset: true,
      },
      item: 1,
      items: [
        { text: 'Main', icon: 'mdi-home', route: '/'},
        { text: 'Search', icon: 'mdi-magnify', route: '/search'},
        { text: 'Library', icon: 'mdi-music-box-multiple', route: '/library'},
        { text: 'Settings', icon: 'mdi-cogs', route: '/settings'},
      ],
    }),
  }


</script>

