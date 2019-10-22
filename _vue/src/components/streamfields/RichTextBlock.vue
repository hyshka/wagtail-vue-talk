<template>
  <div class="richtext" v-html="this.block.value"></div>
</template>

<script>
export default {
  name: "RichTextBlock",
  props: ["block"],
}
</script>

<style>
.richtext p:first-child {
  margin-top: 0;
}

.richtext p:last-child {
  margin-bottom: 0;
}
</style>
