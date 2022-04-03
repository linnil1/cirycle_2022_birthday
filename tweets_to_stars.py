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
        tweet['is_new'] = False
        # with image -> download and resize
        if tweet['image']:
            file_img = image_folder + "/" + tweet['image'][0].split("/")[-1]
            # donwload
            if not os.path.exists(file_img):
                tweet['is_new'] = True
                asyncio.run(downloadImage(tweet['image'][0], file_img))

                # set to lower quality
                img = Image.open(file_img).convert('RGB')
                file_img = f"{image_folder}/{tweet['id']}.jpg"
                img.save(file_img, quality=90)

        file_img = f"{image_folder}/{tweet['id']}.jpg"
        # no image -> word as imge
        if not os.path.exists(file_img):
            img = word2Img(tweet['text'])
            img.save(file_img)
            tweet['is_new'] = True
        else:
            img = Image.open(file_img)

        tweet['my_img_file'] = file_img
        tweet['my_img'] = img
    return tweets


def run(cmd):
    print(cmd)
    os.system(cmd)


def uploadImgs(tweets):
    for tweet in tweets:
        if tweet['is_new']:
            name = tweet['my_img_file'].split("/")[-1]
            run("wrangler kv:key put "
                "--namespace-id=b90dbe1acf46420f908611387f0bcd08 "
                f"{name} --path {image_folder}/{name}")


star_style = [
    # (number of column in this row, row color)
    (1, 0),
    (1, 0),
    (1, 1),
    (3, 1),
    (3, 1),
    (5, 2),
    (7, 2),
    (13, 3),
    (7, 4),
    (5, 4),
    (3, 5),
    (3, 5),
    (1, 5),
    (1, 6),
    (1, 6),
]


def index_to_pos_color(i):
    center_pos = W_full // 2 - W // 2
    acc = 0
    for h, s in enumerate(star_style):
        if i < acc + s[0]:
            return {
                'color': colors[s[1]],
                'x': h * H,  # height
                'y': (i - acc - s[0] // 2) * W + center_pos,  # width
                'width': W,
                'height': H,
            }
        else:
            acc += s[0]

    # list style
    return {
        'color': colors[i % 7].replace("rgb", "rgba").replace(")", ", 0.5)"),
        'x': (i // N) * W,  # height
        'y': (i % N) * H,  # width
        'width': W,
        'height': H,
    }


def saveCirycleDB(tweets):
    # transfer to new format
    i = 0
    tweets_simple_format = []
    for tweet in tweets:
        # promotion tweets
        if tweet['id'] in [1505113558618546176, 1505113563400060929,
                           1510065128787812352, 1507465729796620289]:
            continue
        # main
        tweets_simple_format.append({
            'twitter_id': str(tweet['id']),
            # 'url': tweet['url'],
            'user_name': tweet['user_name'],
            # 'user_image': tweet['user_image'],
            # 'text': tweet['text'],
            'image': tweet['my_img_file'].replace(image_folder, url),
            **index_to_pos_color(i)
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
