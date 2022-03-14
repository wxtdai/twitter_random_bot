# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Manage-Tweets/create_tweet.py
# ツイートを行う

from requests_oauthlib import OAuth1Session
import json
from config import *
import datetime


def post(payload: dict):
    print("start:post")
    oauth = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
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


def make_post_payload(text: str = "", reply_id: str = ""):
    default_text = "[twitter bot 練習中]ここに書いた文章がTwitter上に投稿されます。" + str(datetime.datetime.now()) # Twitterは同じ文章を連投できない仕様なので時刻を入れている
    if text == "":
        text = default_text

    payload = {
        "text": text
    }
    if reply_id != "":
        payload["reply"] = {
            "in_reply_to_tweet_id": reply_id
        }
    return payload


def post_with_payload(text: str = "", reply_id: str = ""):
    post(post_with_payload(text=text,reply_id=reply_id))


if __name__ == "__main__":
    reply_id = "1502167033152040969"
    post_with_payload(reply_id = reply_id)