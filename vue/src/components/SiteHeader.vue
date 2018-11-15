<template>
  <div class="mw7 center pv2">
    <router-link
      class="f6 link dim ph3 pv2 dib black"
      v-for="page in this.pages"
      :to="page.meta.html_url">
      {{ page.title }}
    </router-link>
  </div>
</template>

<script>
import axios from "axios"

export default {
  name: "SiteHeader",
  data() {
    return {
      pages: null,
    }
  },
  created() {
    // TODO: set hostname + port dynamically
    // TODO: document this request url
    axios
      .get("//localhost:8000/api/v2/pages/?show_in_menus=true&fields=_,html_url,title")
      .then(response => {
        this.pages = response.data.items
      })
  },
}
</script>

<style>
</style>

