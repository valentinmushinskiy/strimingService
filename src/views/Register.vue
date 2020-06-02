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
    @submit.prevent="onSubmit"
  >
  <h2 class="display-1">Реєстрація</h2>
  <v-divider
  class="mt-2"
  ></v-divider>
    <v-text-field
      v-model.trim="name"
      label="Нікнейм"
    ></v-text-field>
    <small
      class="error"
      v-if="$v.name.$dirty && !$v.name.required"
    >
    Поле обовязкове
    </small>
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


    <v-text-field
      v-model="repeatPassword"
      label="Повторіть пароль"
      type="password"
    ></v-text-field>

    <small
      class="error"
      v-if="$v.repeatPassword.$dirty && !$v.repeatPassword.required"
    >
    Поле обовязкове
    </small>
    <small
      class="error"
      v-else-if="$v.repeatPassword.$dirty && !$v.repeatPassword.sameAsPassword"
    >
    Паролі не співпадають
    </small>


    <div class="mb-4 d-flex align-center">
      <v-checkbox
      v-model="checkbox"
      id="check"
      
    ></v-checkbox>
    <label for="check">Я приймаю <router-link to="/termsOfUse">Умови використання YOUX</router-link> </label>
    </div>
    

    <v-btn
      color="success"
      class="mr-4 mb-5"
      type="submit"
    >
      Зареєструватись
    </v-btn>
    <p class="error">{{submitStatus}}</p>
    <p class="text-center">Вже є акаунт? <router-link to="/signin">Ввійти</router-link> </p>
  </v-form>
  </v-container>
    
  </v-card>
  
</template>

<script>

import {required, email, sameAs, minLength} from 'vuelidate/lib/validators'


export default {

    data: () => ({
      name: '',
      email: '',
      password: '',
      repeatPassword: '',
      checkbox: false,
      submitStatus: null
    }),


    validations: {
      name: {
        required
      },

      email: {
        email,
        required
      },

      password: {
        required,
        minLength: minLength(6)
      },

      repeatPassword:{
        required,
        sameAsPassword: sameAs('password')
      },

      checkbox:{
        checked: v => v
      }
    },
 
    methods: {
      onSubmit(){
        if(this.$v.$invalid){
          this.$v.$touch()
          return
        }else{

          const user = {
            name: this.name,
            email: this.email,
            password: this.password
          }
          



          this.$store.dispatch('registerUser', user)
          .then(() => {
            // let message = {
            //   context: 'success',
            //   title: 'You are register!'
            // }
            // this.$store.dispatch('getMessage', message)
            // this.submitStatus = 'OK'
            this.$router.push('/')
          })
          .catch(err => {
            this.submitStatus = err.message
          })


          // try{
          //   this.$store.dispatch('registerUser', user)
          //   this.submitStatus = 'OK'
          //   this.$router.push('/')
          // }catch(e){

          // } 
          
        }  
      }
    },
    computed: {
      loading() {
        return this.$store.getters.loading
      }
    }
  }

</script>

<style scoped>
small {
    top: -20px;
    position: relative;
}
.error{
  color: red !important;
  background: #fff !important;
}
</style>