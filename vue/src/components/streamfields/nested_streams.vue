<template>
  <div class="nested_streams">
    {{ this.block }}
    <!-- nested streamfields -->
    <streamfield
      v-for="nestedBlock in this.block.value"
      :key="nestedBlock.id"
      :block="nestedBlock"
      ></streamfield>
  </div>
</template>

<script>
// @ is an alias to /src
import Streamfield from '@/components/Streamfield.vue'

export default {
  name: "nested_streams",
  components: {
    Streamfield,
  },
  props: [
    "block",
  ],
}
</script>
