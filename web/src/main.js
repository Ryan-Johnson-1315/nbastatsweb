import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'

Vue.config.productionTip = false
Vue.prototype.$enpoints = {
  "career": "http://localhost:5000/career"
}

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
