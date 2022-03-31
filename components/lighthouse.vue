<template lang="pug">
.lighthouse-background(@click="hideFunc")
  .lighthouse
    .embed-twitter
      #twitter
</template>

<script setup>
import { ref, onMounted } from 'vue'

const props = defineProps({
  'tweetid': {
    type: String,
    required: true,
  },
  'hideFunc': {
    type: Function,
    required: true,
  },
})

onMounted( () => {
  console.log("Create twitter object " + props.tweetid)
  window.twttr.widgets.createTweet(
    props.tweetid,
    document.querySelector("#twitter"),
    {
       theme: "dark",
       width: 500,
       lang: "zh-tw",
    },
  ).then( el => {
    console.log("Added ", el);
  }).catch( err => {
    console.log("Fail", err);
  })
})

</script>

<style lang="stylus">
.lighthouse
  padding-left: 10px
  padding-right: 10px
  border-radius: 12px
  background-color: #ffffff
  z-index: 90

.lighthouse-background
  width: 100vw
  height: 100vh
  background-color: rgba(0, 0, 0, 0.5)
  position: relative
  display: flex
  justify-content: center
  align-items: center
  z-index: 100

.embed-twitter
  width: 400px

</style>
