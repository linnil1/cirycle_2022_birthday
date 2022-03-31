<template lang="pug">
.image-container(:style='{top: star.x + "px", left: star.y + "px", "background-color": star.color}')
  img(:src="star.image" @click="clickTwitter($event, star)")
  .tip-container
    .tip(@click="clickTwitter($event, star)") {{ star.user_name }}
</template>

<script setup>
const props = defineProps({
  'star': {
    type: Object,
    required: true,
  },
  'clickTwitter': {
    type: Function,
    required: true,
  },
})
</script>

<style lang="stylus">
.image-container
  box-sizing: border-box
  position: absolute
  width: 50px 
  height: 50px 
  overflow: hidden
  display: flex
  justify-content: center

  .tip-container
    position: absolute
    width: 100%
    height: 100%
    display: flex
    justify-content: center
    align-items: center

    .tip
      visibility: hidden
      top: 40%
      text-align: center
      text-weight: 600
      color: white
      text-shadow: black 0 0 5px
      font-size: 10px

  img
    max-height: 100%
    width: auto
    opacity: 30%

  &:hover
    border: 0px solid
    .tip 
      visibility: visible
</style>

