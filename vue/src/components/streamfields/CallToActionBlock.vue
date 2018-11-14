<template>
  <div class="cta mw8 center ph4 pv4">
    <h2>{{ this.block.value.title }}</h2>
    <div v-html="this.block.value.text"></div>
    <!-- WIP -->
    <button-block
      v-for="button in this.block.value.buttons"
      :block="button"
      ></button-block>
  </div>
</template>

<script>
// @ is an alias to /src
import ButtonBlock from '@/components/streamfields/ButtonBlock.vue'

export default {
  name: "CallToActionBlock",
  components: {
    ButtonBlock,
  },
  props: [
    "block",
  ],
}
</script>

