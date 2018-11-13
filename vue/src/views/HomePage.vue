<template>
  <div class="page">
    <!-- banner -->
    <div class="mw8 center tc ph4 pv5">
      <h1 class="fw7 f1 lh-title mt0 mb3">
        {{ this.page.title }}
      </h1>
      <h2 class="fw4 f2 lh-copy mt0 mb3">
        {{ this.page.banner_subtitle }}
      </h2>

      <!-- {{ this.page.banner_image }} -->
      <!-- TODO: don't hardcode wagtail domain -->
      <img :src="'//localhost:8000' + this.page.banner_image_thumbnail.url" :alt="this.page.banner_image.title">
    </div>

    <!-- streamfields -->
    <streamfield
      v-for="block in this.page.content"
      :key="block.id"
      :block="block"
      ></streamfield>
  </div>
</template>

<script>
// @ is an alias to /src
// import Streamfield from '@/components/Streamfield.vue'

export default {
  name: "HomePage",
  // components: {
  //   Streamfield,
  // },
  props: [
    "page",
  ],
}
</script>
