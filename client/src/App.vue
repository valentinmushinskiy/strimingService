<template>
  <div id="app">
    <router-view/>
    <div id="nav">
      <router-link to="/">Home</router-link>
      <router-link to="/search">Search</router-link>
      <router-link to="/library">My Library</router-link>
    </div>
  </div>
</template>

<style>
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app{
  background: #3aafa9;
  height: 100vh;
  
}

a{
  padding-bottom: 10px;
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
  /* font-weight: bold; */
  color: #def2f1;
  transition: .05s color linear;
}

a:hover{
  color: #def2f1a8;
  
}

#nav{
  position: fixed;
  top: 70px;
  display: flex;
  flex-direction: column;
  width: 20%;
  height: 100vh;
  padding: 30px 20px;
  margin: 0;
  background: #2b7a78;
  border-right: 1px solid #145e797e;
}
/* 
#nav a{
  padding-left: 1px;
} */
</style>
