<template lang="pug">
.canvas
  .image-container(v-for="i in data" :style='{top: i.x + "px", left: i.y + "px", "background-color": i.color}')
    img(:src="i.image[0]" @click="clickTwitter($event,i)")
    .tip {{ i.user_name }}

  // v-if in child component will cause error
  template(v-if="twitter_display")
    Lighthouse(:tweetid="twitter_id", :hideFunc="() => (twitter_display = false)")
</template>

<script setup>
import { ref, onMounted } from 'vue'

/*
let data = ref([
{
  user_name: "nyadoi",
  image: 'https://yt3.ggpht.com/ytc/AKedOLRbqG9InKSaB4NTjZ2OlKLFEooJC7sCJnsti6Sk=s176-c-k-c0x00ffffff-no-rj',
  color: 'rgba(242, 72, 53, 0.5)',
  x: 50,
  y: 20,
  twitter_id: "1504768347438981120"
},
{
  user_name: "hela",
  image: 'https://yt3.ggpht.com/BCj6J0qMsy84We512B-MWfzizJdAdln9ihvGCTokaLYswAGBhbQ0jiwYxtLOgNemoHilfzuNMA=s176-c-k-c0x00ffffff-no-rj',
  color: 'rgba(242, 226, 53, 0.6)',
  x: 150,
  y: 30,
  twitter_id: "1504516744739962880"
},
])
onMounted(() => {
  console.log(data)
})
*/

let twitter_id = ref(""),
    twitter_display = ref(false);

function clickTwitter(evt, i) {
  console.log("Click", i, twitter_ref)
  twitter_display.value = true
  twitter_id.value = i.twitter
}

let { data } = await useFetch("/api/tweets")

</script>

<style lang="stylus">
.canvas
  position: relative

.image-container
  box-sizing: border-box
  position: absolute
  width: 50px 
  height: 50px 
  overflow: hidden
  display: flex
  justify-content: center

  .tip
    visibility: hidden
    position: absolute
    width: 100%
    top: 40%
    text-align: center
    text-weight: 600
    color: white
    text-shadow: black 0 0 5px

  img
    max-height: 100%
    width: auto
    opacity: 30%

  &:hover
    border: 0px solid
    .tip 
      visibility: visible

.twitter
  display: none
</style>

