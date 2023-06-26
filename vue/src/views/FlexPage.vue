<template>
  <div>
    <!-- banner -->
    <div class="mw7 center pt5">
      <h1 class="fw7 f1 lh-title mv0">{{ this.page.title }}</h1>
    </div>

    <!-- streamfields -->
    <div class="pt5">
      <streamfield
        v-for="block in this.page.content"
        :key="block.id"
        :block="block"
      ></streamfield>
    </div>
  </div>
</template>

<script>
export default {
  name: "FlexPage",
  props: ["page"],
}
</script>
