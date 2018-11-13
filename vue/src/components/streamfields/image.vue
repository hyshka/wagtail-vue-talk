<template>
  <div class="image mw8 center ph4 pv4">
    <wagtail-image
      :id="this.block.value"
      ></wagtail-image>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from '@/components/WagtailImage.vue'

export default {
  name: "image",
  components: {
    WagtailImage,
  },
  props: [
    "block",
  ],
}
</script>
