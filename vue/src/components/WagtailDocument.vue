<template>
  <a :href="this.download_url" :title="this.title"><slot></slot></a>
</template>

<script>
import { getWagtailDocument } from "@/api"

export default {
  name: "wagtail-document",
  props: ["id"],
  data() {
    return {
      download_url: "",
      title: "",
    }
  },
  created() {
    getWagtailDocument(this.id).then(response => {
      const document = response.data
      this.download_url = document.meta.download_url
      this.title = document.title
    })
  },
}
</script>
