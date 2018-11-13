<template>
  <div class="image mw8 center ph4 pv4">
    {{ this.block }}
    <!-- <img :src="" :alt=""> -->
  </div>
</template>

<script>
export default {
  name: "image",
  props: [
    "block",
  ],
}
</script>
