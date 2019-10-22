import Vue from "vue"
import VueMeta from "vue-meta"
import VueLazyload from 'vue-lazyload'

import App from "./App.vue"
import router from "./router"
import Streamfield from "@/components/Streamfield.vue"

Vue.config.productionTip = false

// Vue addons
Vue.use(VueMeta)
Vue.use(VueLazyload, {
  loading: '/loading.gif',
})

// Register streamfield as global component
Vue.component("streamfield", Streamfield)

new Vue({
  router,
  render: h => h(App),
}).$mount("#app")
