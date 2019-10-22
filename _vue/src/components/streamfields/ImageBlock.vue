<template>
  <div class="mv4">
    <wagtail-image class="db" :id="this.block.value.image"></wagtail-image>
  </div>
</template>

<script>
// @ is an alias to /src
import WagtailImage from "@/components/WagtailImage.vue"

export default {
  name: "ImageBlock",
  components: {
    WagtailImage,
  },
  props: ["block"],
}
</script>
