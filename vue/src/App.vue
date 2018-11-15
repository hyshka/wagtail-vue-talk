<template>
  <div id="app">
    <site-header></site-header>
    <transition name="fade" appear>
      <router-view/>
    </transition>
  </div>
</template>

<script>
// @ is an alias to /src
import SiteHeader from '@/components/SiteHeader.vue'

export default {
  components: {
    SiteHeader,
  },
}
</script>

<style>
@import "~tachyons";

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
