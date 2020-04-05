<template>
  <v-card
  height="88vh"
  width="1000"
  class="mx-auto mt-5 px-8 pt-1">
    <h2 class="title mb-1">Головна</h2>
    <v-divider
    ></v-divider>
    <v-tabs
      v-model="tab"
      color="blue-grey"
    >
      <v-tab
        v-for="item in items"
        :key="item.tab"
      >
        {{ item.tab }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item.tab"
      >
        <v-card flat>
          <v-card-text>
            {{ item.content }}
            
          </v-card-text>
        </v-card>
      </v-tab-item>
    </v-tabs-items>
    
    <audio controls>
      <source type="audio/mp3" >
    </audio>
  </v-card>
</template>

<script>

export default {
  data () {
      return {
        tab: null,
        items: [
          { tab: 'Популярні плейлисти', content: 'popular' },
          { tab: 'Новинки сайту', content: 'new' },
          { tab: 'Топ місяця', content: '' },
        ],
      }
    },
}
</script>
