<template>
  <section class="main" id="main" :style="`background-color: ${color}`">
    <colour-component></colour-component>
  </section>
</template>

<script>
import colourComponent from "./components/colours.vue";

export default {
  data() {
    return {
      color: '#FFFFFF',
    }
  },
  methods: {
    setBackgroundColour(color) {
      this.color = color;
    }
  },
  components: {
    colourComponent,
  }
}
</script>
<style scoped>
.main {
  width: 100vw;
  height: 100vh;
}
</style>
