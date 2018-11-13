<template>
  <component :is="dynamicComponent" :page="responseData"></component>
</template>

<script>
import axios from "axios"
import find from "lodash/find"

// @ is an alias to /src
import NotFound from "@/views/NotFound.vue"
import HomePage from "@/views/HomePage.vue"
import FlexPage from "@/views/FlexPage.vue"

export default {
  name: "WagtailPageHandler",
  components: {
    HomePage,
    FlexPage,
  },
  data() {
    return {
      dynamicComponent: null,
      responseData: null,
    }
  },
  beforeRouteEnter (to, from, next) {
    // called before the route that renders this component is confirmed.
    // does NOT have access to `this` component instance,
    // because it has not been created yet when this guard is called!

    console.log("WagtailPageHandler.beforeRouteEnter", to, from)

    // TODO: set hostname + port dynamically
    axios
      .get(`//localhost:8000/api/v2/pages/find/?html_path=${to.fullPath}`)
      .then(response => {
        console.log("WagtailPageHandler.beforeRouteEnter response", response)

        // catch 302/200 response, render matching Vue component
        // pass page data from response to component
        next(vm => {
          // access to component instance via `vm`
          vm.dynamicComponent = vm.getWagtailPage(response.data.meta.type)
          vm.responseData = response.data
        })
      })
      .catch(error => {
        console.log("WagtailPageHandler.beforeRouteEnter error", error)

        // catch 404 response, page doesn't exist
        // retain request path but render NotFound component instead
        // TODO: find a way to actually return a 404 response

        next(vm => {
          // access to component instance via `vm`
          vm.dynamicComponent = NotFound
          vm.responseData = null
        })
      })
  },
  methods: {
    getWagtailPage(pageType) {
      // return registered component that's name matches our Wagtail page type
      // strip `pages.` from the Wagtail page type
      return find(this.$options.components, obj => obj.name === pageType.replace("pages.", ""))
    },
  },
  created() {
  },
}
</script>
