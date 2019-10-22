<template>
  <!-- TODO: don't hardcode wagtail domain -->
  <img v-lazy="'//localhost:8000' + this.download_url" :alt="this.title" />
</template>

<script>
import { getWagtailImage } from "@/api"

export default {
  name: "wagtail-image",
  props: ["id"],
  data() {
    return {
      download_url: "",
      title: "",
    }
  },
  created() {
    getWagtailImage(this.id).then(response => {
      const image = response.data
      this.download_url = image.meta.download_url
      this.title = image.title
    })
  },
}
</script>
