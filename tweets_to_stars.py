from text_to_image import word2Img
from crawl_twitter import updateDB
from pprint import pprint
import os
from PIL import Image 
import aiohttp
import asyncio
import json


image_folder = "data1"
file_db = "tweets.json"
file_cirycle_db = "tweets_cirycle.json"
url = "https://cirycle-2022-birthday.linnil1.me/api/image"

# temp position and color setting
colors = [
    "rgb(236, 34,   10)",
    "rgb(236, 123,  11)",
    "rgb(236, 218,  10)",
    "rgb(13,  215,   9)",
    "rgb(11,  149, 237)",
    "rgb(30,   12, 238)",
    "rgb(232,  11, 238)",
]
W, H = 50, 50
W_full, H_full = 1000, 1000
N = 1000 // 50


async def downloadImage(url, path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
           if resp.status == 200:
               with open(path, "wb") as f:
                   f.write(await resp.read())


def saveImgs():
    # download or create image
    os.makedirs(image_folder, exist_ok=True)
    tweets = json.load(open(file_db))
    for tweet in tweets:
        # no image -> word as imge
        if not tweet['image']:
            file_img = f"{image_folder}/{tweet['id']}.jpg"
            if not os.path.exists(file_img):
                img = word2Img(tweet['text'])
                img.save(file_img)
            else:
                img = Image.open(file_img)
        # with image -> download and resize
        else:
            file_img = image_folder + "/" + tweet['image'][0].split("/")[-1]
            if not os.path.exists(file_img):
                asyncio.run(downloadImage(tweet['image'][0], file_img))
            img = Image.open(file_img).convert('RGB')
            file_img = f"{image_folder}/{tweet['id']}.jpg"
            img.save(file_img, quality=90)

        tweet['my_img_file'] = file_img
        tweet['my_img'] = img
    return tweets


def run(cmd):
    print(cmd)
    os.system(cmd)


def uploadImgs(tweets):
    for tweet in tweets:
        name = tweet['my_img_file'].split("/")[-1]
        run(f"wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 {name} --path {image_folder}/{name}")


def saveCirycleDB(tweets):
    # transfer to new format
    i = 0
    tweets_simple_format = []
    for tweet in tweets:
        tweets_simple_format.append({
            'twitter_id': str(tweet['id']),
            # 'url': tweet['url'],
            'user_name': tweet['user_name'],
            # 'user_image': tweet['user_image'],
            # 'text': tweet['text'],
            'image': tweet['my_img_file'].replace(image_folder, url),
            'color': colors[i % 7].replace("rgb", "rgba").replace(")", ", 0.5)"),
            'x': (i // N) * W,  # height
            'y': (i  % N) * H,  # width
        })
        i += 1
    pprint(tweets_simple_format)
    json.dump(tweets_simple_format, open(file_cirycle_db, "w"))


if __name__ == "__main__":
    # updateDB()
    tweets = saveImgs()
    saveCirycleDB(tweets)
    uploadImgs(tweets)
    run(f"wrangler kv:key put --namespace-id=b90dbe1acf46420f908611387f0bcd08 tweets_cirycle.json --path tweets_cirycle.json")
