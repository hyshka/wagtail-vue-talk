<template>
  <div class="mv3">
    <wagtail-page
      v-if="this.page"
      class="f6 link dim ba ph3 pv2 dib"
      :class="this.color ? this.color : 'black'"
      :id="this.page"
      >{{ this.text }}</wagtail-page>
    <wagtail-document
      v-else-if="this.document"
      class="f6 link dim ba ph3 pv2 dib"
      :class="this.color ? this.color : 'black'"
      :id="this.document"
      >{{ this.text }}</wagtail-document>
    <a
      v-else
      class="f6 link dim ba ph3 pv2 dib"
      :class="this.color ? this.color : 'black'"
      :href="this.external_link"
      >{{ this.text }}</a>
  </div>
</template>

<script>
import WagtailPage from "@/components/WagtailPage.vue"
import WagtailDocument from "@/components/WagtailDocument.vue"

export default {
  name: "ButtonBlock",
  props: ["block", "color"],
  components: {
    WagtailPage,
    WagtailDocument,
  },
  data() {
    return {
      text: "",
      external_link: "",
      page: null,
      document: null,
    }
  },
  created() {
    if (this.block.value) {
      this.text = this.block.value.text
      this.external_link = this.block.value.external_link
      this.page = this.block.value.page
      this.document = this.block.value.document
    } else {
      this.text = this.block.text
      this.external_link = this.block.external_link
      this.page = this.block.page
      this.document = this.block.document
    }
  },
}
</script>
