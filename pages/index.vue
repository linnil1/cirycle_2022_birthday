<template lang="pug">
.main
  img.bgimg(src="~/assets/CI.jpg")
  .main-img-box
    .intro
      p 時值  2022年  4月  4日  ！
      p 今天  的  天氣  是 ⋯⋯
      p 慶賀著  ！  滿滿的  祝福  ！
      p 今天  的  十字星  是  ——
      p 集結  彩虹  獨角獸們  的  十字星  ！
      p 無論  在  什麼地方  ，  都能看見  虹彩  十字星  。
    .tweetsimage
      TweetsImage
    .staff
      p 企劃：金架海拉 (@<a href="https://twitter.com/HelaGoldfish">HelaGoldfish</a>)
      p 文案：呼嘯而過(@<a href="https://twitter.com/WhizzingWind">WhizzingWind</a>)
      p 網站：linnil1(@<a href="https://twitter.com/1linnil1">linnil1</a>)
      p 所有祝賀 CI 醬的繪師
</template>

<style lang="stylus">
.main
  position: relative
  height: 100%

  .bgimg
    width: 100%
    top: 0
    left: 0
    z-index: -100

  .main-img-box
    position: absolute
    top: 0
    left: 0
    width: 100%
    height: 100%

    display: flex
    display: flex
    align-items: center
    flex-direction: column
    
    .intro
      position: absolute
      top: 42%
      width: 60%
      min-width: 460px
      text-align: center
      color: white
      font-size: 24px
      p
        margin-top: 12px
        margin-bottom: 12px

    .tweetsimage
      position: absolute
      top: 60%
      width: 800px
      height: 500px
      border: solid 1px white

    .staff
      position: absolute
      bottom: 20px
      width: 60%
      text-align: center
      color: white
      p
        margin: 2px
</style>
