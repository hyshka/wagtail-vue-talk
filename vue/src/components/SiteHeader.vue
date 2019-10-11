<template>
  <header class="bg-dark-gray">
    <div class="mw7 center pv2 flex justify-between items-center">
      <div>
        <router-link class="f6 link dim dib white flex items-center" exact to="/">
          <img class="logo db" src="../assets/logo.png" alt="Wagtail + Vue.js">
        </router-link>
      </div>
      <div>
        <router-link
          class="f6 link dim ph3 pv2 dib white"
          active-class="bg-black"
          exact
          v-for="page in this.pages"
          :key="page.id"
          :to="page.meta.slug"
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

<style>
.logo {
  max-height: 25px;
}
</style>
