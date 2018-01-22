<template lang="pug">
md-content
  .output
    .pre(
      v-for="(item, index) in output"
      :key="index"
      :class="{ s : index % 2 > 0}"
    )
      .num {{ item.time }}
      .message {{ item.message }}
</template>

<script>
import { MQTT } from '@/lib/MQTT'

export default {
  name: 'Log',
  data: () => ({
    output: []
  }),
  methods: {
    pushOutput (message) {
      let d = new Date()

      this.output.unshift({
        time: `${d.getHours()}:${d.getMinutes()}`,
        message
      })
    }
  },
  created () {
    this.bus.$on('mqtt:connect', () => {
      this.pushOutput('MQTT client connected.')
    })
    this.bus.$on('mqtt:close', () => {
      this.pushOutput('Connection closed.')
    })
    this.bus.$on('mqtt:error', (e) => {
      this.pushOutput(`Error: ${e}`)
    })
    this.bus.$on('mqtt:subscribe', (topic) => {
      this.output = []
      this.pushOutput(`Subscribing to topic: ${topic}`)
    })
    this.bus.$on('mqtt:message', (topic, message) => {
      this.pushOutput(message)
    })
  },
  beforeDestroy () {
    this.bus.$off('mqtt:connect')
    this.bus.$off('mqtt:close')
    this.bus.$off('mqtt:error')
  }
}
</script>

<style lang="scss">
.md-content {
  margin: 20px 0 0;
  padding: 20px;
  flex: 2;
  background-color: rgba(0, 0, 0, .03) !important;
  overflow-y: scroll;

  .output {
    .pre {
      margin: 0;
      padding-bottom: 3px;
      font-size: 10px;
      font-family: monospace;

      &.s {
        background: rgba(0, 0, 0, .025);
      }

      .num {
        max-width: 25px;
        font-weight: bold;
        position: relative;
        float: left;
      }

      .message {
        padding-left: 37px;
        overflow-wrap: break-word;
        word-wrap: break-word;
        word-break: normal;
        line-break: strict;
        hyphens: none;
        -webkit-hyphens: none;
        -moz-hyphens: none;
      }
    }
  }
}
</style>
