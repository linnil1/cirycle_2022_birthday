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
    data = [{
        'twitter_id': '1505113558618546176',
        'user_name': '金架海拉(◉▽◉)🔸超異界通信+海鮮部',
        'image': 'https://cirycle-2022-birthday.linnil1.me/api/image/1505113558618546176.jpg',
        'color': 'rgb(236, 123,  11)',
        'x': 300,
        'y': 425,
        'width': 50,
        'height': 50
    }, {
        'twitter_id': '1508553566939942912',
        'user_name': '華鳥風月🎗#一生推觀空部的夕飯@大家都愛欺負的傲嬌王$油到滑倒 ',
        'image': 'https://cirycle-2022-birthday.linnil1.me/api/image/1508553566939942912.jpg',
        'color': 'rgb(236, 123,  11)',
        'x': 300,
        'y': 475,
        'width': 50,
        'height': 50
    }, {
        'twitter_id': '1508462096857518080',
        'user_name': '阿緹密斯',
        'image': 'https://cirycle-2022-birthday.linnil1.me/api/image/1508462096857518080.jpg',
        'color': 'rgb(236, 123,  11)',
        'x': 300,
        'y': 525,
        'width': 50,
        'height': 50
    }]
    return web.json_response(data, headers=cors_header)


async def getTweetsJson(request):
    data = json.load(open("tweets_cirycle.json"))
    return web.json_response(data, headers=cors_header)


if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.post('/api/tweets', getTweetsJsonExample)])
    # app.add_routes([web.post('/api/tweets', getTweetsJson)])
    web.run_app(app, port=8081)
