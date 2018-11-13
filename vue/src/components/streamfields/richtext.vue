<template>
  <div class="richtext mw8 center ph4 pv4" v-html="block.value"></div>
</template>

<script>
export default {
  name: "richtext",
  props: [
    "block",
  ],
}
</script>
