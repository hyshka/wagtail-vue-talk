<template>
  <div class="page">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>{{ this.page.title }}</h1>

    <!-- streamfields -->
    <streamfield :content="this.page.content"></streamfield>
  </div>
</template>

<script>
// @ is an alias to /src
// import Streamfield from '@/components/Streamfield.vue'

export default {
  name: "FlexPage",
  // components: {
  //   Streamfield,
  // },
  props: [
    "page",
  ],
}
</script>
