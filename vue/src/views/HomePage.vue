<template>
  <div class="page">
    <!-- banner -->
    <div class="relative">
      <div class="absolute absolute--fill flex items-center">
        <div class="mw7 center tc ph4 pv5 white">
          <h1 class="fw7 f1 lh-title mv0">
            {{ this.page.title }}
          </h1>
          <p class="fw4 f3 lh-copy mt3 mb0">
            {{ this.page.banner_subtitle }}
          </p>
        </div>
      </div>
      <wagtail-image
        class="db"
        :id="this.page.banner_image.id"
        ></wagtail-image>
    </div>

    <!-- streamfields -->
    <div class="page-content pt5">
      <streamfield
        v-for="block in this.page.content"
        :key="block.id"
        :block="block"
        ></streamfield>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from '@/components/WagtailImage.vue'

export default {
  name: "HomePage",
  components: {
    WagtailImage,
  },
  props: [
    "page",
  ],
}
</script>

<style>
.section + .section {
  margin-top: 4rem;
}
</style>
