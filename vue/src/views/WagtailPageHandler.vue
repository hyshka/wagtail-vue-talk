<template>
  <component :is="dynamicComponent" :page="responseData"></component>
</template>

<script>
// @ is an alias to /src
import WagtailPage from "@/views/WagtailPage.vue"
import NotFound from "@/views/NotFound.vue"
import axios from "axios"

export default {
  name: "WagtailPageHandler",
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

    axios
      .get(`//localhost:8000/api/v2/pages/find/?html_path=${to.fullPath}`)
      .then(response => {
        console.log("WagtailPageHandler.beforeRouteEnter response", response)

        // catch 302/200 response, render matching Vue component
        // pass page data from response to component
        next(vm => {
          // access to component instance via `vm`
          vm.dynamicComponent = WagtailPage
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
}
</script>
