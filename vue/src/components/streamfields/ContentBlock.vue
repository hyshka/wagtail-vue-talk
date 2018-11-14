<template>
  <div class="content mw8 center ph4 pv4">
    <!-- stream block -->
    <streamfield
      v-for="nestedBlock in this.block.value.content"
      :key="nestedBlock.id"
      :block="nestedBlock"
      ></streamfield>
  </div>
</template>

<script>
export default {
  name: "ContentBlock",
  props: [
    "block",
  ],
}
</script>
