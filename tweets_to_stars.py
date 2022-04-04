import os
import json
import asyncio
from pprint import pprint
from PIL import Image
import aiohttp

from text_to_image import word2Img
from crawl_twitter import updateDB

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

star_style = [  # total 55
    # (number of column in this row, row color)
    (1, 0),
    (1, 0),
    (1, 0),
    (1, 0),
    (1, 1),
    (1, 1),
    (3, 1),
    (3, 1),
    (3, 2),
    (5, 2),
    (7, 2),
    (11, 3),
    (7, 4),
    (5, 4),
    (3, 4),
    (3, 5),
    (3, 5),
    (1, 5),
    (1, 5),
    (1, 6),
    (1, 6),
    (1, 6),
    (1, 6),
    (1, 6),
]


async def downloadImage(url, path):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open(path, "wb") as f:
                    f.write(await resp.read())


def assignImageToTweet(tweets):
    # download or create image
    os.makedirs(image_folder, exist_ok=True)
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


def updateKV(name, path):
    run("wrangler kv:key put "
        "--namespace-id=b90dbe1acf46420f908611387f0bcd08 "
        f"{name} --path {path}")


def uploadImgs(tweets):
    for tweet in tweets:
        if tweet['is_new']:
            name = tweet['my_img_file'].split("/")[-1]
            updateKV(name, f"{image_folder}/{name}")


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


def assignPosColorToTweet(tweets):
    # transfer to new format
    i = 0
    tweets_simple_format = []
    for tweet in tweets:
        if i >= sum(i[0] for i in star_style):
            continue
        # Exclude promotion tweets
        # Total tweets: 55. It's enough to fit the star
        if tweet['id'] in [1505113563400060929, 1507465729796620289]:
            continue
        # main
        tweets_simple_format.append({
            'twitter_id': str(tweet['id']),
            'user_name': tweet['user_name'],
            'image': tweet['my_img_file'].replace(image_folder, url),
            **index_to_pos_color(i)
        })
        i += 1
    return tweets_simple_format


if __name__ == "__main__":
    updateDB()
    tweets = json.load(open(file_db))
    tweets = assignImageToTweet(tweets)
    tweets_star = assignPosColorToTweet(tweets)
    pprint(tweets_star)
    json.dump(tweets_star, open(file_cirycle_db, "w"))
    uploadImgs(tweets)
    updateKV("tweets_cirycle.json", "./tweets_cirycle.json")
