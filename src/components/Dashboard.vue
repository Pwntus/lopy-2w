<template lang="pug">
#dashboard
  md-card
    md-card-header
      md-card-header-text
        .md-title Actions
        .md-subhead Turn the LED on/off or adjust the color of the light.
    md-card-content
      md-switch.md-primary(v-model="led") LED
      color-picker(v-model="colors")
  log
</template>

<script>
import _ from 'lodash'
import Log from '@/components/Log'
import { Chrome as ColorPicker } from 'vue-color'
import { MQTT } from '@/lib/MQTT'

export default {
  name: 'Dashboard',
  components: {
    Log,
    ColorPicker
  },
  data: () => ({
    led: true,
    colors: {
      hex: '#00FF00'
    }
  }),
  watch: {
    led: function (val) {
      let hex = (val == true) ? this.colors.hex : '#000000'
      this.$store.dispatch('App/send', hex)
    },
    colors: _.debounce(function (val) {
      this.led = true
      this.$store.dispatch('App/send', val.hex)
    }, 100)
  }
}
</script>

<style lang="scss" scoped>
#dashboard {
  height: 100%;
  display: flex;
  flex-direction: column;

  .vc-chrome {
    width: 100%;
    box-shadow: none;
    font-family: Roboto, Noto Sans, -apple-system, BlinkMacSystemFont, sans-serif;
  }
}
</style>
