# Cirycle 2022 birthday web

We collect all the tweets with tag "Cirycle生日快樂2022"

And assemble into a big star !

## Tools

* web: Nuxt3 (Using Vue composition API)
* collect, assemble the star and data server: python3

## Setup

For development:

``` bash
# install packages
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

* Retrieve tweets and save into database (`tweets.json`)
* Download image or Generate image if it's text-only tweet
* Assign color and position of each image
* Save the result into json (`tweets_cirycle.json`)
* Upload image and json to KV


## Web architecture

* I deploy on Clouflare Worker, all the data are served in KV
* `server/api/tweets.ts` is the server script to output tweets json from KV
* `server/api/image.ts` is the server script to output binary image data from KV
* `pages/index.vue` The main page
* `components/tweet.vue` This define how to show each of tweet image
* `components/star.vue` It arranage all the tweet image on the canvas
* `components/lighthouse.vue`  Popup the tweet when click on it


## Some basic wrangler (Cloudflare worker) operator
``` bash
# Create a namespace
wrangler kv:namespace create cirycle_2022_birthday
# upload image
wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 xx.png --path ./xx.png
# upload json
wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 tweets_cirycle.json --path ./tweets_cirycle.json
# publish the web
wrangler publish
```


## Notes

When I use Cloudflare as image server, I found this bug
https://github.com/nuxt/framework/issues/3982


## LICENSE
MIT

BUT the media in `assets/*` and `public/*` have copyright.
Don't use it for any other usage.
