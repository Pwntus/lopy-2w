<template lang="pug">
.md-layout.md-alignment-center
  .md-layout-item.md-medium-size-33.md-small-size-50.md-xsmall-size-100
    md-card
      md-card-header
        md-card-header-text
          .md-title Login
          .md-subhead Please provide your Managed IoT Cloud credentials to start using this tool
      md-card-content
        md-field
          label Username
          md-input(
            v-model="username"
            v-bind:disabled="loading"
            @keyup.enter.native="login"
          )
        md-field
          label Password
          md-input(
            type="password"
            v-model="password"
            v-bind:disabled="loading"
            @keyup.enter.native="login"
          )
      md-card-actions
        md-button.md-raised.md-primary(
          v-bind:disabled="loading"
          @click.native="login"
        )
          span Login
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      loading: false
    }
  },
  computed: {
    payload () {
      return { username: this.username, password: this.password, ctx: this }
    }
  },
  methods: {
    login () {
      if (this.username == '' || this.password == '') return
        
      this.loading = true
      this.$store.dispatch('App/auth', this.payload)
        .catch(error => {
          this.showSnackbar(error)
          this.loading = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
.md-layout {

}
</style>
