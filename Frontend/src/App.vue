<template>
  <section class="main" id="main" :style="`background-color: ${colors[selectedIndex].color}`" @click="closeOverlay" @touchdown="closeOverlay">
    <h1 class="header-bg">Culer majik</h1>
    <div class="main-container">
      <div :class="`button-container ${(index===selectedIndex)? 'selected': ''}`" v-for="(item, index) in colors" :key="index" @click.stop="">
        <button
            aria-haspopup="false"
            class="color-button"
            @mouseup="buttonUp(index)"
            @touchend="buttonUp(index)"
            @mousedown="buttonDown($event, index)"
            @touchstart="buttonDown($event, index)"
            :style="`background: ${item.color};
                    -webkit-box-shadow: 0 0 5px ${item.color};
                     -moz-box-shadow: 0 0 5px ${item.color};
                     box-shadow: 0 0 5px ${item.color}`"
        />
      </div>
      <p class="hint">Hold to edit color</p>
    </div>
    <transition name="slide-fade">
      <div ref="overlay" v-show="showOverlay" class="overlay" :style="`left: ${overlayX}px; top: ${overlayY}px`" @click.stop="">
        <h1 class="header">Edit button</h1>
        <chrome-picker v-model="editColor"></chrome-picker>
        <button class="button" @click="updateColor()">save</button>
      </div>
    </transition>
  </section>
</template>

<script>
import { Chrome } from 'vue-color';

export default {
  data() {
    return {
      selectedIndex: 0,
      buttonDownTime: null,
      buttonDebounce: null,
      colors: [
        {color: '#ff0000', mood: ''}, {color: '#ff5900', mood: ''}, {color: '#f8ff00', mood: ''},
        {color: '#10ff00', mood: ''}, {color: '#00ffd0', mood: ''}, {color: '#6c47ff', mood: ''},
        {color: '#c600ff', mood: ''}, {color: '#ff00ae', mood: ''}, {color: '#ff0000', mood: ''},
      ],
      showOverlay: false,
      editColor: '#FFF',
      editIndex: 0,
      overlayX: 100,
      overlayY: 100
    }
  },
  mounted() {
    window.oncontextmenu = function(event) {
      event.preventDefault();
      event.stopPropagation();
      return false;
    };
  },
  methods: {
    buttonDown(event, index) {
      this.buttonDownTime = Date.now();
      this.buttonDebounce = setTimeout(() => this.triggerOverlay(event, index), 500);
    },
    buttonUp(index) {
      const currentTime = Date.now();
      if((currentTime - this.buttonDownTime) >= 500) return
      clearTimeout(this.buttonDebounce);
      this.buttonDownTime = null;
      this.selectedIndex=index;
    },
    triggerOverlay(event, index) {
      const windowHeight = window.innerHeight;
      const windowWidth = window.innerWidth;
      const positionY =
          (this.$refs.overlay.getBoundingClientRect().y + this.$refs.overlay.getBoundingClientRect().height + 25 - windowHeight) > 0?
              (windowHeight - this.$refs.overlay.getBoundingClientRect().height - 10) : event.target.getBoundingClientRect().y + 25;
      const positionX =
          (windowWidth - event.target.getBoundingClientRect().x - this.$refs.overlay.getBoundingClientRect().width/2) < 0?
              (windowWidth - this.$refs.overlay.getBoundingClientRect().width) :
              (event.target.getBoundingClientRect().x - this.$refs.overlay.getBoundingClientRect().width/2) < 0? 0 : event.target.getBoundingClientRect().x - 125;
      this.overlayY = positionY;
      this.overlayX = positionX;
      this.editIndex = index;
      this.showOverlay = true;
    },
    updateColor() {
      this.colors[this.editIndex].color = this.editColor.hex;
      this.closeOverlay();
    },
    closeOverlay() {
      this.showOverlay = false;
    }
  },
  components: {
    'chrome-picker' : Chrome,
  },
}
</script>

<style>
#main .vc-chrome {
  box-shadow: none;
}
#main .vc-chrome-saturation-wrap {
  border-radius: 0.5rem;
}
#main .vc-chrome-fields-wrap {
  display: none;
}
#main .vc-chrome-hue-wrap .vc-hue{
  border-radius: 100vw;
}
</style>

<style scoped>

.slide-fade-enter, .slide-fade-leave-to {
  transform: translateY(10px);
  opacity: 0;
}

.main {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  transition: background-color 0.5s ease-in-out;
  overflow: hidden;
}

.main-container {
  position: relative;
  width: 33%;
  height: 66%;
  max-width: 410px;
  min-width: 310px;
  max-height: 600px;
  background-color: white;
  border-radius: 0.5rem;
  border: 5px solid rgba(231, 231, 231, 0.25);
  display: flex;
  align-content: flex-start;
  flex-wrap: wrap;
}

.button-container {
  height: 40px;
  width: 40px;
  margin: 5px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.color-button {
  width: 100%;
  height: 100%;
  border-radius: 100vw;
  border: none;
  outline: none;
  cursor: pointer;
  transition: width 0.25s ease-in-out, height 0.25s ease-in-out, background-color 0.25s ease-in-out;
}

.button-container:active .color-button {
  width: 1.5rem;
  height: 1.5rem;
}

.button-container.selected .color-button {
  width: 1.5rem;
  height: 1.5rem;
}

.overlay {
  position: absolute;
  padding: 1rem;
  border-radius: 0.5rem;
  background: #FFF;
  box-shadow: 0 0 10px #CCC;
  transition: top 0.25s ease-in-out, left 0.25s ease-in-out, transform 0.25s ease-in-out, opacity 0.25s ease-in-out;
}

.overlay .header {
  font-weight: bold;
  font-size: 20px;
  text-align: center;
  margin-bottom: 1rem;
  color: #AAA;
}
</style>
