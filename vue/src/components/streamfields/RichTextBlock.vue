<template>
  <div class="text" v-html="this.block.value"></div>
</template>

<script>
export default {
  name: "RichTextBlock",
  props: [
    "block",
  ],
}
</script>
