import { defineNuxtConfig } from 'nuxt3'

export default defineNuxtConfig({
  meta: {
    script: [
      { src: "https://platform.twitter.com/widgets.js" }
    ],
  },
  css: [
    '@/assets/default.css',
  ],
})
