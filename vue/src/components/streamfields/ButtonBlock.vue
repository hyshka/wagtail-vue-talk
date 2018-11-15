<template>
  <div class="button mv3">
    <router-link
      class="f6 link dim ba ph3 pv2 dib black"
      :to="this.block.value.external_link"
      >{{ this.block.value.text }}</router-link>
  </div>
</template>

<script>
export default {
  name: "ButtonBlock",
  props: [
    "block",
  ],
}
</script>
