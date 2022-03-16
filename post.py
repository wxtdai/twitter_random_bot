# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Manage-Tweets/create_tweet.py
# ツイートを行う

from requests_oauthlib import OAuth1Session
import json
from config import *
import datetime
from utility import make_my_oauth, response_success_check


def post(payload: dict):
    oauth = make_my_oauth()
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )
    response_success_check(response,201)
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    print()


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
    post(make_post_payload(text=text,reply_id=reply_id))


if __name__ == "__main__":
    reply_id = "1502167033152040969"
    post_with_payload(reply_id = reply_id)

