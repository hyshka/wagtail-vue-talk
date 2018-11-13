<template>
  <div class="carousel mw8 center ph4 pv4">
    {{ this.block }}
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
