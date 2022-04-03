<template lang="pug">
.canvas(:style='{height: total_height + "px"}')
  Star(:star="star" :clickTwitter="clickTwitter" v-for="star in data" :scale="scale")
  // v-if in child component will cause error
  .lighthouse-container(v-if="twitter_display")
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
*/

let twitter_id = ref(""),
    twitter_display = ref(false);

function clickTwitter(evt, star) {
  twitter_id.value = star.twitter_id.toString()
  twitter_display.value = true
  console.log(twitter_id)
}

let { data } = await useFetch("/api/tweets")
let scale = ref(1)
let total_height = ref(0)

onMounted( () => {
  // get the width and height of the star
  let total_width_min = 1000,
      total_width_max = 0
  data.value.forEach( (i) => {
    if (i.height + i.x > total_height.value)
      total_height.value = i.height + i.x
    if (i.y < total_width_min)
      total_width_min = i.y
    if (i.y + i.width > total_width_max)
      total_width_max = i.y + i.width
  })

  // scale it if it can (maybe scale down)
  const width_scale = (window.innerWidth - 100) / (total_width_max - total_width_min)
  const height_scale = (window.innerHeight - 100) / total_height.value
  scale.value = Math.min(width_scale, height_scale)
  console.log("Set scale", scale.value)
  total_height.value = total_height.value * scale.value
})

</script>

<style lang="stylus">
.canvas
  position: relative
  width: 1000px

.lighthouse-container
  position: fixed
  top: 0px
  left: 0px
</style>

