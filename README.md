# Cirycle 2022 birthday web

We collect all the tweets with tag "Cirycle生日快樂2022"

And assemble into a big star !

## Tools

* web: nuxt3
* collect, assemble the figure and data server: python3

## Setup

For development:

``` bash
yarn install
# start a developing web server
yarn dev
# start a example data serving server
python3 serve_json_data.py
```

## Data Preparation

Register twitter developer(https://developer.twitter.com/en/portal/dashboard),
and get the token then save in `twitter_secret.py` (You can copy from template `twitter_secret.example.py`)

After all prepared, just run 

``` bash
python3 tweets_to_starts.py
```

This script will

* Retrieve tweets and save into json (`tweets.json`)
* Download image or Generate image if it's text-only tweet
* Assign color and position of each image
* Save the result into json (`tweets_cirycle.json`)
* Upload image and json to KV

## Web architecture

* I deploy on Clouflare Worker, all the data are saved in KV
* `server/api/tweets.ts` is the server script to output tweets json from KV
* `server/api/image.ts` is the server script to output binary image data from KV
* `pages/index.vue` The main page, it contains cover-image, introduction, tweet-images and staff information
* `components/star.vue` This define how to show each of tweet image
* `components/lighthouse.vue`  Popup the tweet when click on it
* `components/tweets_image.vue` The main of tweet-images. It arranage all the tweet image on the canvas

## Some basic KV operator
``` bash
# Create a namespace
wrangler kv:namespace create cirycle_2022_birthday
# upload image
# you can copy from previous stdout
wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 xx.png --path ./xx.png
# upload json
wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 tweets_cirycle.json --path ./tweets_cirycle.json
# publish
wrangler publish
```


## Notes

When I use Cloudflare as image server, I found this bug
https://github.com/nuxt/framework/issues/3982
