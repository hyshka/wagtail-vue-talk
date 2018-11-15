<template>
  <div class="button mv3">
    <router-link
      class="f6 link dim ba ph3 pv2 dib"
      :class="this.color ? this.color : 'black'"
      :to="this.external_link"
      >{{ this.text }}</router-link>
  </div>
</template>

<script>
export default {
  name: "ButtonBlock",
  props: [
    "block",
    "color",
  ],
  data() {
    return {
      text: "",
      external_link: "",
      page: null,
      document: null,
    }
  },
  created() {
    console.log('XXX', this.block)

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

    //.TODO handle page and document ids
  },
}
</script>
