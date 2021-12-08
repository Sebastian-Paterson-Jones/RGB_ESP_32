<template>
  <Sketch v-model="color" />
</template>

<script>
// import { Sketch } from '@ckpack/vue-color';

export default {
  name: "colourComponent",
  data() {
    return {
      color: '#FFFFFF',
    }
  },
  components: {
    // Sketch,
  }
}
</script>

<style scoped>
</style>
