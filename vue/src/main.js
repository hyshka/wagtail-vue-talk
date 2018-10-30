import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// TODO
// import VueMeta from 'vue-meta'
// Vue.use(VueMeta)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
