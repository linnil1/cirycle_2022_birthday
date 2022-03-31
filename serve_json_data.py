import os
import sys
import csv
import json
import asyncio
import datetime
from pprint import pprint
from aiohttp import web


cors_header = {
    'Access-Control-Allow-Origin': "http://localhost:3000",
}


async def getTweetsJsonExample(request):
    data = [
        {'create_at': datetime.datetime(2021, 11, 30, 3, 2, 12, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFaPX47acAA66ix.png'],
         'text': '【廢】\n不知道啦 如果九壹是蘿莉之類的 https://t.co/6X6RGhHPWI',
         'url': 'https://t.co/6X6RGhHPWI',
         'user_id': 'adsl6658',
         'user_image': 'https://pbs.twimg.com/profile_images/1453399851886993415/p-dXd5rQ_normal.jpg',
         'twitter_id': "1465516485590204417",
         'color': 'rgba(242, 72, 53, 0.5)',
         'x': 160,
         'y': 30,
         'user_name': 'LOS'},
        {'create_at': datetime.datetime(2021, 11, 30, 4, 2, 5, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFadHRhaQAA2OJy.png'],
         'text': '91不要討厭我 https://t.co/KE5ssopoEO https://t.co/aNJLjKkGDW',
         'url': 'https://t.co/KE5ssopoEO',
         'user_id': 'zzz_2605',
         'twitter_id': "1465531552616484872",
         'color': 'rgba(242, 226, 53, 0.5)',
         'x': 50,
         'y': 30,
         'user_image': 'https://pbs.twimg.com/profile_images/1457965328458469376/ilqVrjsT_normal.jpg',
         'user_name': '歷曆歷🪐現在要多畫畫'},
        {'create_at': datetime.datetime(2021, 11, 30, 16, 35, 44, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFdJrIaaQAAby4r.jpg'],
         'text': '大家有畫過的都是共犯我們裡面見QwQ\n'
                 '#玖要在依起 https://t.co/aWLSmym41r https://t.co/SpMIQZC2Y7',
         'url': 'https://t.co/aWLSmym41r',
         'twitter_id': "1465521877607063552",
         'color': 'rgba(75, 226, 53, 0.5)',
         'x': 150,
         'y': 150,
         'user_id': 'miziquan_naiali',
         'user_image': 'https://pbs.twimg.com/profile_images/1413456490518614019/cYZGVUrX_normal.jpg',
         'user_name': '米自犬'},
    ]
    return web.json_response(data, headers=cors_header)


async def getTweetsJson(request):
    data = json.load(open("tweets_cirycle.json"))
    return web.json_response(data, headers=cors_header)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.post('/api/tweets', getTweetsJsonExample)])
    # app.add_routes([web.post('/api/tweets', getTweetsJson)])
    web.run_app(app, port=8081)
