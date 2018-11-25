<template>
  <div class="section image-gallery ph3 flex">
    <!-- list block -->
    <div class="w-50 pa3" v-for="image in this.block.value.images">
      <wagtail-image
        class="w-100 h-100 image-gallery-image"
        :key="image.id"
        :id="image.ImageBlock"
      ></wagtail-image>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from "@/components/WagtailImage.vue"

export default {
  name: "ImageGalleryBlock",
  components: {
    WagtailImage,
  },
  props: ["block"],
}
</script>

<style>
.image-gallery {
  margin-top: -1rem;
  margin-bottom: -1rem;
}

.image-gallery-image {
  object-fit: cover;
}
</style>
