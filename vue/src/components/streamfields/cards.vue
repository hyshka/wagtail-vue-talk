<template>
  <div class="cards mw8 center ph4 pv4 flex">
    <!-- list block -->
    <card
      class="w-50 pa3 mr2"
      v-for="card in this.block.value.card"
      :key="card.id"
      :block="card"
      ></card>
  </div>
</template>

<script>
// @ is an alias to /src
import Card from '@/components/streamfields/card.vue'

export default {
  name: "nested_streams",
  components: {
    Card,
  },
  props: [
    "block",
  ],
}
</script>
