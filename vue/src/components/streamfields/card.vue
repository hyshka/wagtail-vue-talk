<template>
  <div class="card">
    <wagtail-image
      :id="this.block.image"
      ></wagtail-image>
    <h2>{{ this.block.title }}</h2>
    <div v-html="this.block.content"></div>
    <wagtail-page-link
      :id="this.block.page"
      >Read more</wagtail-page-link>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from '@/components/WagtailImage.vue'
import WagtailPageLink from '@/components/WagtailPageLink.vue'

export default {
  name: "card",
  components: {
    WagtailImage,
    WagtailPageLink,
  },
  props: [
    "block",
  ],
}
</script>
