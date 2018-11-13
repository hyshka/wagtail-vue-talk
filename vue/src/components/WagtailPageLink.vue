<template>
  <!-- TODO: don't hardcode wagtail domain -->
  <router-link
    :to="this.path"
    ><slot></slot></router-link>
</template>

<script>
import axios from "axios"

export default {
  name: "wagtail-page-link",
  props: [
    "id",
  ],
  data() {
    return {
      path: "",
    }
  },
  created() {
    // TODO: set hostname + port dynamically
    axios
      .get(`//localhost:8000/api/v2/pages/${this.id}/`)
      .then(response => {
        const pageObj = response.data
        this.path = pageObj.meta.html_url
      })
  },
}
</script>
