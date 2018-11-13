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
import Cards from "@/components/streamfields/cards.vue"
import Carousel from "@/components/streamfields/carousel.vue"
import Quotation from "@/components/streamfields/quotation.vue"

export default {
  name: "Streamfield",
  props: [
    "block",
  ],
  components: {
    Richtext,
    ImageBlock,
    Cards,
    Carousel,
    Quotation,
  },
  computed: {
    dynamicComponent() {
      // return registered component that's name matches our Wagtail streamfield type
      return find(this.$options.components, obj => obj.name === this.block.type)
    },
  },
}
</script>
