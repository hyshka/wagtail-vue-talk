<template>
  <div class="page">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>{{ this.page.title }}</h1>
    <div>
      {{ this.page }}
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: "WagtailPage",
  components: {
    // HelloWorld
  },
  props: [
    "page",
  ],
}
</script>
