<template>
  <div id="app">
    <site-header></site-header>
    <main class="page"><router-view></router-view></main>
  </div>
</template>

<script>
// @ is an alias to /src
import SiteHeader from "@/components/SiteHeader.vue"

export default {
  components: {
    SiteHeader,
  },
}
</script>

<style>
@import "~tachyons";

#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
</style>
