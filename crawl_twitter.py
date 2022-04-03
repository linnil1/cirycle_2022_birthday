import os
import json
import tweepy
from twitter_secret import secret
api = tweepy.Client(**secret)


def getAllTweets(start_time=None):
    # Start time show be less than 1 week
    # otherwise you will get
    # Invalid 'start_time':'2022-03-21T09:14Z'.
    #     'start_time' must be on or after 2022-03-22T04:35Z
    tag = "#Cirycle生日快樂2022"
    next_token = None
    new_tweets = []
    while True:
        # TODO: shrink some fields that always return None
        # e.g. preview_image_url
        # search hashtag
        tweets = api.search_recent_tweets(
            query=tag,
            max_results=100,
            expansions=["attachments.media_keys", "author_id", "referenced_tweets.id"],
            user_fields=["id", "name", "profile_image_url", "username"],
            tweet_fields=["created_at", "entities"],
            media_fields=["media_key", "url", "preview_image_url"],
            next_token=next_token,
            start_time=start_time,
        )
        # remove retweeted
        new_tweets.extend([i for i in tweets[0] if not i.referenced_tweets or i.referenced_tweets[0].type != "retweeted"])
        # next page
        next_token = tweets.meta.get('next_token')
        if not next_token:
            break

    return new_tweets


def query(id):
    # query tweet's information
    data = api.get_tweet(
        id,
        expansions=["author_id", "attachments.media_keys"],
        user_fields=["profile_image_url"],
        tweet_fields=["created_at", "entities"],
        media_fields=["url", "preview_image_url"]
    )

    return {
        'id': id,
        'user_name': data.includes['users'][0].data['name'],
        'user_id': data.includes['users'][0].data['username'],
        'user_image': data.includes['users'][0].data['profile_image_url'],
        'text': data.data.text,
        'image': [img.data['url'] if img.data.get('url') else img.data['preview_image_url'] for img in data.includes.get('media', [])],
        'url': data.data.entities['urls'][0]['url'] if data.data.entities.get('url') else None,
        'create_at': data.data.created_at.isoformat(),
    }


def updateDB():
    """ I use json as db to keep it simple """
    file_db = "tweets.json"
    tweets = []

    # load
    start_time = None
    tweets_id = set()
    if os.path.exists(file_db):
        tweets = json.load(open(file_db))
        start_time = max(map(lambda i: i['create_at'], tweets))
        tweets_id = set(map(lambda i: i['id'], tweets))

    # query
    tweets_search_result = getAllTweets(start_time)
    new_tweets = [query(i.id) for i in tweets_search_result if i.id not in tweets_id]

    # save
    tweets.extend(new_tweets)
    # tweets = sorted(tweets, key=lambda i: i['created_at'])
    json.dump(tweets, open(file_db, 'w'))


if __name__ == "__main__":
    updateDB()
