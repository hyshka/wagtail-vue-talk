<template>
  <div class="section cta bg-black-80 white pv5">
    <div class="mw7 center">
      <h2 class="fw7 f2 lh-title mv0">{{ this.block.value.title }}</h2>
      <div
        class="f4"
        v-html="this.block.value.text"></div>
      <!-- WIP -->
      <button-block
        v-for="button in this.block.value.buttons"
        :block="button"
        ></button-block>
    </div>
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

