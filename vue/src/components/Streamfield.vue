<template>
  <component :is="dynamicComponent" :block="block"></component>
</template>

<script>
import find from "lodash/find"

// @ is an alias to /src
import ContentBlock from "@/components/streamfields/ContentBlock.vue"
import ButtonBlock from "@/components/streamfields/ButtonBlock.vue"
import RichTextBlock from "@/components/streamfields/RichTextBlock.vue"
import ImageBlock from "@/components/streamfields/ImageBlock.vue"
import ImageGalleryBlock from "@/components/streamfields/ImageGalleryBlock.vue"
import CallToActionBlock from "@/components/streamfields/CallToActionBlock.vue"

export default {
  name: "Streamfield",
  props: ["block"],
  components: {
    ContentBlock,
    ButtonBlock,
    RichTextBlock,
    ImageBlock,
    ImageGalleryBlock,
    CallToActionBlock,
  },
  computed: {
    dynamicComponent() {
      // return registered component that's name matches our Wagtail streamfield type
      return find(this.$options.components, obj => obj.name === this.block.type)
    },
  },
}
</script>

<style>
.section + .section {
  margin-top: 4rem;
}
</style>
