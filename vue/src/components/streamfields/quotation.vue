<template>
  <div class="quotation mw8 center ph4 pv4">
    <blockquote class="f1 ma0">"{{ this.block.value.text }}"</blockquote>
    <div>By <cite>{{ this.block.value.author }}</cite></div>
  </div>
</template>

<script>
export default {
  name: "quotation",
  props: [
    "block",
  ],
}
</script>
