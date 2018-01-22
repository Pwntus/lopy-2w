<template lang="pug">
#app
  login(v-if="page == 0")
  keep-alive
    dashboard(v-if="page == 1")
</template>

<script>
import Login from '@/components/Login.vue'
import Dashboard from '@/components/Dashboard.vue'

export default {
  name: 'App',
  components: {
    Login,
    Dashboard
  },
  computed: {
    page () {
      return this.$store.getters['App/page']
    }
  }
}
</script>

<style lang="scss">
#app {
  height: 100%;
  padding: 20px;
}
</style>
