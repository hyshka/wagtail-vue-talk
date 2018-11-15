<template>
  <div id="app">
    <div id="nav" class="mw7 center pv2">
      <router-link to="/">Home</router-link> |
      <router-link to="/sample-flex-page">About</router-link>
    </div>
    <transition name="fade" appear>
      <router-view/>
    </transition>
  </div>
</template>

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
