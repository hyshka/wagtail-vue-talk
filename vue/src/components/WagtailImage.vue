<template>
  <!-- TODO: don't hardcode wagtail domain -->
  <img :src="'//localhost:8000' + this.download_url" :alt="this.title">
</template>

<script>
import axios from "axios"

export default {
  name: "wagtail-image",
  props: [
    "id",
  ],
  data() {
    return {
      download_url: "",
      title: "",
    }
  },
  created() {
    // TODO: set hostname + port dynamically
    axios
      .get(`//localhost:8000/api/v2/images/${this.id}/`)
      .then(response => {
        const imageObj = response.data
        this.download_url = imageObj.meta.download_url
        this.title = imageObj.title
      })
  },
}
</script>
