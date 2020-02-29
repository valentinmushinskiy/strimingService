<template>
<div class="app">
  <SiteHeader></SiteHeader>
  <div class="wrapper">
    <div class="form-register">
      <h1>Register</h1>
      <div class="inputs">
        <input type="email" name="email" v-model="email" placeholder="E-Mail">
        <input type="password" name="password" v-model="password" placeholder="Password">
      </div>
      <button @click="register">Register</button>
    </div>
    
  </div>
  
</div>
  
  
</template>

<script>
import SiteHeader from '@/components/Header.vue'
import AuthenticationService from '@/services/AuthanticationService'

export default {
  name: 'siteheader',
  components: {
    SiteHeader
  },
  data () {
    return{
      email: '',
      password: ''
    }
  },
  methods: {
    async register() {
      const response = await AuthenticationService.register({
        email: this.email,
        password: this.password
      });
      /*eslint-disable-next-line*/
      console.log(response.data);
    }
  }
}
</script>

<style>
.wrapper{
  position: absolute;
  left: 20%;
  width: 80%;
  background: #fff;

  display: flex;
  justify-content: center;
}

.form-register{
  min-width: 200px;
  max-width: 300px;

  background: #f3f3f3;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

input{
  width: 100%;
}

</style>