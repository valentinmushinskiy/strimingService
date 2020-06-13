<template>
  <v-card 
  height="auto"
  width="600"
  class="mx-auto mt-5 px-8 pt-5"
  >
  <v-container
  fluid>
  <v-form
    ref="form"
    lazy-validation
    @submit.prevent="onSubmit"
  >
  <h2 class="display-1">Вхід</h2>
  <v-divider
  class="mt-2"
  ></v-divider>

    <v-text-field
      v-model.trim="email"
      label="E-mail"
    ></v-text-field>
    <small
      class="error"
      v-if="$v.email.$dirty && !$v.email.required"
    >
    Поле обовязкове
    </small>
    <small
      class="error"
      v-else-if="$v.email.$dirty && !$v.email.email"
    >
    E-mail не коректний
    </small>
    
    <v-text-field
      v-model="password"
      label="Пароль"
      type="password"
    ></v-text-field>

    <small
      class="error"
      v-if="$v.password.$dirty && !$v.password.required"
    >
    Поле обовязкове
    </small>
    <small
      class="error"
      v-else-if="$v.password.$dirty && !$v.password.minLength"
    >
    Пароль повинен мати більше 6 символів
    </small>

    <v-btn
    outlined
      class="mr-4 mb-4"
      type="submit"
    >
      Ввійти
    </v-btn>
    <p class="error">{{submitStatus}}</p>
    <p class="text-center pb-5" outlined>Немає акауну? <router-link to="/register">Зареєструватись</router-link> </p>
  </v-form>
  </v-container>
    
  </v-card>
  
</template>

<script>
import {required, email, sameAs, minLength} from 'vuelidate/lib/validators'

export default {
    data: () => ({
      email: '',
      password: '',
      submitStatus: null
    }),

    validations: {

      email: {
        email,
        required
      },

      password: {
        required,
        minLength: minLength(6)
      }
    },

    methods: {
      onSubmit(){
        if(this.$v.$invalid){
          this.$v.$touch()
          return
        } else {

          const user = {
            email: this.email,
            password: this.password
          }
          
          this.$store.dispatch('loginUser', user)
          .then(() => {
            this.$store.dispatch('loginUser', user)
            // Message
            // let message = {
            //   context: 'success',
            //   title: 'You are logged!'
            // }
            // this.$store.dispatch('getMessage', message)
            // this.submitStatus = 'OK'
            this.$router.push('/')
          })
          .catch(err => {
            this.submitStatus = err.message
          })
      }
    },
  }
}
</script>

<style scoped>

</style>