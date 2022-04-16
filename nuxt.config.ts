import { defineNuxtConfig } from 'nuxt3'

export default defineNuxtConfig({
  meta: {
    script: [
      { src: "https://platform.twitter.com/widgets.js",
        defer: true,
      }, {
        src: 'https://static.cloudflareinsights.com/beacon.min.js',
        defer: true,
        'data-cf-beacon': '{"token": "1edcfa5d82db48b7a8a23c8f81177ee5"}'
      },
    ],
  },
  css: [
    '@/assets/default.css',
  ],
})
