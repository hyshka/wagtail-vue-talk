import Vue from 'vue'
import VueMeta from 'vue-meta'

import App from './App.vue'
import router from './router'
import store from './store'

import Streamfield from '@/components/Streamfield.vue'

Vue.config.productionTip = false

Vue.use(VueMeta)

Vue.component("streamfield", Streamfield)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
