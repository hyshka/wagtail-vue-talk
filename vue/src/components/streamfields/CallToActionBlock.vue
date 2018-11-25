<template>
  <div class="section bg-dark-gray white pv5">
    <div class="mw7 center">
      <h2 class="fw7 f2 lh-title mv0">{{ this.block.value.title }}</h2>
      <div class="f4" v-html="this.block.value.text"></div>
      <div class="mv3">
        <button-block
          class="di mr3"
          v-for="(button, index) in this.block.value.buttons"
          color="white"
          :key="index"
          :block="button"
        ></button-block>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import ButtonBlock from "@/components/streamfields/ButtonBlock.vue"

export default {
  name: "CallToActionBlock",
  components: {
    ButtonBlock,
  },
  props: ["block"],
}
</script>
