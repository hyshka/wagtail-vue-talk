<template>
  <div class="carousel mw8 center ph4 pv4">
    <!-- stream block -->
    <streamfield
      v-for="nestedBlock in this.block.value"
      :key="nestedBlock.id"
      :block="nestedBlock"
      ></streamfield>
  </div>
</template>

<script>
export default {
  name: "carousel",
  props: [
    "block",
  ],
}
</script>
