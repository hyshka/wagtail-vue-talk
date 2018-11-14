<template>
  <div class="image">
    <wagtail-image
      :id="this.block.value.image"
      ></wagtail-image>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from '@/components/WagtailImage.vue'

export default {
  name: "ImageBlock",
  components: {
    WagtailImage,
  },
  props: [
    "block",
  ],
}
</script>
