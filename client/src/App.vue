<template>
  <div id="app">
    <Header :currentUser=token></Header>
    <router-view @updateLocalStorage="updateLocalStorage"/>
    <!-- $emit('updateLocalStorage', localStorage.getItem('token')) -->
  </div>
</template>

<script>
import Header from './components/Header.vue'


export default {
  name: 'App',
  components: {
    Header
  },
  methods: {
      updateLocalStorage(token) {
        this.token = token;
      }
    },
  computed: {
    // a computed getter
    getToken() {
      return this.token
    }
  },
  data()
    {
        return {
          token: undefined
        }
    },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
