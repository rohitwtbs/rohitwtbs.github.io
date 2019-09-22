<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <Profile/>
    <TechnicalSkills/>

  </div>
</template>

<script>
import Profile from './components/Profile.vue'
import TechnicalSkills from './components/TechnicalSkills'

export default {
  name: 'app',
  components: {
    Profile,
    TechnicalSkills
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
img{
  border: 2px solid green;
}
</style>
