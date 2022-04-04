<template lang="pug">
.main(@mouseover="playMusic" @touchemove="playMusic")
  Title ★Cirycle生日快樂！★
  Meta(charset='utf-8')
  Meta(name='viewport'            content='width=device-width, initial-scale=1')
  Meta(name='twitter:card'        content='summary_large_image')
  Meta(name='twitter:site'        content='https://cirycle-2022-birthday.linnil1.me')
  Meta(name='twitter:title'       content='★Cirycle生日快樂！★')
  Meta(name='twitter:description' content='2022/4/4 大宇宙彩星市電波星人Cirycle慶生企劃，來自彩虹獨角獸的虹彩祝福！')
  Meta(name='twitter:image'       content='https://cirycle-2022-birthday.linnil1.me/_nuxt/assets/CI_foreground_low.webp')
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
      p BGM：虹の彼方に！－Cirycle remix by 螺絲釘 (@<a href="https://twitter.com/peter60507000">peter60507000</a>)
      p 游標：yun (@<a href="https://twitter.com/mp678922">mp678922</a>)
      p 感謝所有祝賀Cirycle的彩虹獨角獸
  // data in public
  audio#audio(src="/cirycle_cover.mp3" type="audio/mp3" autoplay)
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
  cursor: url("~/assets/cursor_default.png"), auto
  background-position-x: center
  background-size: cover

  .full_screen
    @media only screen and (max-width: 1024px)
      height: 100vh
    @media only screen and (min-width: 1024px)
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
