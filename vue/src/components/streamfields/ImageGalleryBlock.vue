<template>
  <div class="image-gallery mw8 center ph4 pv4 flex">
    <!-- list block -->
    <wagtail-image
      class="w-50 pa3 mr2"
      v-for="image in this.block.value.images"
      :key="image.id"
      :id="image.ImageBlock"
      ></wagtail-image>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from '@/components/WagtailImage.vue'

export default {
  name: "ImageGalleryBlock",
  components: {
    WagtailImage,
  },
  props: [
    "block",
  ],
}
</script>
