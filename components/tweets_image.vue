<template lang="pug">
.canvas
  Star(:star="star" :clickTwitter="clickTwitter" v-for="star in data")
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
onMounted(() => {
  console.log(data)
})
*/

let twitter_id = ref(""),
    twitter_display = ref(false);

function clickTwitter(evt, star) {
  twitter_id.value = star.twitter_id.toString()
  twitter_display.value = true
  console.log(twitter_id)
}

let { data } = await useFetch("/api/tweets")

</script>

<style lang="stylus">
.canvas
  position: relative

.lighthouse-container
  position: fixed
  top: 0px
  left: 0px
</style>

