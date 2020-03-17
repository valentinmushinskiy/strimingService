<template>
  <v-app id="sandbox">
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

        <!-- <v-subheader>REPORTS</v-subheader> -->
        <v-list-item-group v-model="item" color="blue-grey">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
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
    </v-app-bar>

    <v-content>
      <v-container>
        <v-row>
          <v-col>
            <v-card class="mx-auto" max-width="400">
              <v-card-text>
                <p class="display-1 text--primary">
                  Register
                </p>
                <v-form ref="form" v-model="valid" lazy-validation>
                  <v-text-field
                    v-model="name"
                    :rules="nameRules"
                    label="Name"
                    required
                    outlined
                    rounded
                    dense
                    color="blue-grey">
                  ></v-text-field>

                  <v-text-field
                    v-model="email"
                    :rules="emailRules"
                    label="E-mail"
                    required
                    outlined
                    rounded
                    dense
                    color="blue-grey">
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    :rules="passwordRules"
                    label="Password"
                    required
                    outlined
                    rounded
                    type="password"
                    dense
                    :counter="8"
                    color="blue-grey">
                  ></v-text-field>

                  <v-checkbox
                    v-model="checkbox"
                    :rules="[v => !!v || 'You must agree to continue!']"
                    label="Do you agree?"
                    required
                    class="ml-2"
                    color="blue-grey">
                  ></v-checkbox>
                </v-form>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
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
        { text: 'Main', icon: 'mdi-home' },
        { text: 'Search', icon: 'mdi-magnify' },
        { text: 'Library', icon: 'mdi-music-box-multiple' },
        { text: 'Settings', icon: 'mdi-wrench'},
      ],
    }),
  }


</script>