# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Manage-Tweets/create_tweet.py
# ツイートを行う

from requests_oauthlib import OAuth1Session
import json
from config import *
import datetime


def post(payload: dict):
    print("start:post")

    oauth = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    text = "[twitter bot 練習中]ここに書いた文章がTwitter上に投稿されます。" + str(datetime.datetime.now())
    payload = {
        "text": text,
        "reply": {
            "in_reply_to_tweet_id": "1502167033152040969"
        }
    }
    post(text)