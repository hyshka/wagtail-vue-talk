<template>
  <header class="bg-dark-gray">
    <div class="mw7 center pv2 flex justify-between">
      <div>
        <router-link class="f6 link dim ph3 pv2 dib white" exact to="/">
          Wagtail + Vue.js
        </router-link>
      </div>
      <div>
        <!-- TODO: don't hardcode wagtail domain -->
        <router-link
          class="f6 link dim ph3 pv2 dib white"
          active-class="bg-black"
          exact
          v-for="page in this.pages"
          :key="page.id"
          :to="page.meta.html_url.replace('http://localhost:8000', '')"
        >
          {{ page.title }}
        </router-link>
      </div>
    </div>
  </header>
</template>

<script>
import { getWagtailPagesInMenu } from "@/api"

export default {
  name: "SiteHeader",
  data() {
    return {
      pages: null,
    }
  },
  created() {
    getWagtailPagesInMenu().then(response => {
      this.pages = response.data.items
    })
  },
}
</script>
