import Vue from 'vue'
import store from '@/store'
import App from '@/components/App'
import '@/global'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  components: { App },
  template: '<App/>'
})
