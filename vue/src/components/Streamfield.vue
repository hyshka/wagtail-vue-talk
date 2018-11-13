<template>
  <component
    :is="dynamicComponent"
    :block="block"
    ></component>
</template>

<script>
import find from "lodash/find"

// @ is an alias to /src
import Richtext from "@/components/streamfields/richtext.vue"
import ImageBlock from "@/components/streamfields/image.vue"
import NestedStreams from "@/components/streamfields/nested_streams.vue"
import Carousel from "@/components/streamfields/carousel.vue"

export default {
  name: "Streamfield",
  props: [
    "block",
  ],
  components: {
    Richtext,
    ImageBlock,
    NestedStreams,
    Carousel,
  },
  computed: {
    dynamicComponent() {
      // return registered component that's name matches our Wagtail streamfield type
      return find(this.$options.components, obj => obj.name === this.block.type)
    },
  },
  created() {
  },
}
</script>

