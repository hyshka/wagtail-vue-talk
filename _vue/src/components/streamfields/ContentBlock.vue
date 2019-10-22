<template>
  <div class="section mw7 center">
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
  props: ["block"],
}
</script>
