<template lang="pug">
.main(@mouseover="playMusic" @touchemove="playMusic")
  img.full_screen(src="~/assets/CI_foreground_low.webp")
  .main-img-box
    .intro
      p 時值  2022年  4月  4日  ！
      p 今天  的  天氣  是 ⋯⋯
      p 慶賀著  ！  滿滿的  祝福  ！
      p 今天  的  十字星  是  ——
      p 集結  彩虹  獨角獸們  的  十字星  ！
      p 無論  在  什麼地方  ，  都能看見  虹彩  十字星  。
    TweetsImage.tweetsimage
    .staff
      p 企劃：金架海拉 (@<a href="https://twitter.com/HelaGoldfish">HelaGoldfish</a>)
      p 文案：呼嘯而過 (@<a href="https://twitter.com/WhizzingWind">WhizzingWind</a>)
      p 網站：linnil1(@<a href="https://twitter.com/1linnil1">linnil1</a>)
      p BGM：虹の彼方に！－Cirycle cover by (@<a href="https://twitter.com/peter6050700">螺絲釘</a>)
      p 所有祝賀 CI 醬的彩虹獨角獸
  // cannot read .mp3 when put in assets (bug)
  audio#audio(src="https://cirycle-2022-birthday.linnil1.me/api/image/cirycle_cover.mp3" type="audio/mp3" autoplay)
</template>

<script setup>
function playMusic() {
  let audio = document.querySelector("#audio")
  if (audio.paused) {
      console.log("set volume and play")
      audio.volume = 0.1
      document.querySelector("#audio").play()
  }
}
</script>

<style lang="stylus">
.main
  background-image: url("~/assets/CI_background_low.webp")
  height: 100%
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  overflow: hidden

  .full_screen
    @media only screen and (max-width: 1500px)
      height: 100vh
    @media only screen and (min-width: 1500px)
      width: 100vw

  .main-img-box
    width: 100%
    height: 100%

    display: flex
    display: flex
    align-items: center
    flex-direction: column
    
    .intro
      min-width: 460px
      text-align: center
      color: white
      font-size: 32px
      p
        margin-top: 12px
        margin-bottom: 12px

      @media only screen and (max-width: 700px)
        font-size: 18px

    .tweetsimage
      margin-top: 100px
      margin-bottom: 100px
      // width and height written in tweetsimage
      // width: 1000px
      // height: 800px
      // border: solid 1px white

    .staff
      bottom: 20px
      text-align: center
      color: white
      p
        margin: 2px
      @media only screen and (max-width: 700px)
        font-size: 12px
</style>
