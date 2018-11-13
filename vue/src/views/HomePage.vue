<template>
  <div class="page">
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>{{ this.page.title }}</h1>

    <!-- banner -->
    {{ this.page.banner_subtitle }}
    {{ this.page.banner_image }}
    {{ this.page.banner_image_thumbnail }}

    <!-- streamfields -->
    <streamfield :content="this.page.content"></streamfield>
  </div>
</template>

<script>
// @ is an alias to /src
import Streamfield from '@/components/Streamfield.vue'

export default {
  name: "HomePage",
  components: {
    Streamfield,
  },
  props: [
    "page",
  ],
}
</script>
