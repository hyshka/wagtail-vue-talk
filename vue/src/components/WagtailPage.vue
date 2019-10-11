<template>
  <router-link :to="this.path"><slot></slot></router-link>
</template>

<script>
import { getWagtailPage } from "@/api"

export default {
  name: "wagtail-page",
  props: ["id"],
  data() {
    return {
      path: "",
    }
  },
  created() {
    getWagtailPage(this.id).then(response => {
      this.page = response.data
      this.slug = page.meta.slug
      this.path = page.meta.html_url.replace("http://localhost:8000", "")
      // console.log(this.page)
    })
  },
}
</script>
