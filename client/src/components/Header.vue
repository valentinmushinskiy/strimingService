<template>
  <header class="header">
    <router-link class="logo" to="/">YOUX</router-link>

    <div class="sign">
      <router-link to="/signin">Sign In</router-link>
      <router-link to="/register">Register</router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.header{
  background: #2b7a78;
  height: 70px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom: 1px solid #145e797e;
}

.logo{
  font-family: 'Open Sans', sans-serif;
  color: #feffff;
  font-size: 26px;
  letter-spacing: 2px;
}

.sign{
  color: #feffff;
}

.sign a:first-child{
  padding-right: 10px;
}

.sign a:last-child{
  padding-left: 10px;
  border-left: 2px solid #feffff;
}
</style>
