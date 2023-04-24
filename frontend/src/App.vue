<template>
  <nav class = "navbar navbar-expand-lg navbar-light">
    <div class = "navbar-brand">
      <router-link class="elements" to="/">Bloglite</router-link>
    </div>
    <!-- <router-link class="elements" to="/about">About</router-link> -->
    
    <router-link id = "login" class="elements" to="/login" v-if="!isLogged">Login</router-link>
    <router-link id = "signup" class="elements" to="/signup" v-if="!isLogged">Signup</router-link>
    <router-link id = "feed" class="elements" to="/feed" v-if="isLogged">Feed</router-link>
    <router-link id = "upload-blog" class="elements" to="/upload" v-if="isLogged">Upload</router-link>
    <router-link id = "logout" class="elements" to="/logout" v-if="isLogged">Logout</router-link>
  </nav>
  <router-view/>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  computed: {
    isLogged() {
      return this.$store.state.isLogged;
    }
  },
  created() {
    if (localStorage.getItem('isLogged')) {
      this.$store.dispatch('refresh');
    }
  }
}
</script>

<style scoped>
#app {
  font-family: "Montserrat", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: #2c3e50;
}

h1, h2, h3 {
  font-weight: normal;
  font-family: "Montserrat";
}

nav {
  padding: 0.5% 2%;
  background-color: #87CEEB;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #FF7F50;
}

.elements {
  margin: 0 10px;
  text-decoration: none;
}
</style>
