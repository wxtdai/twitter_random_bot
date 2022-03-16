# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Manage-Likes/like_a_tweet.py

import json
from config import *
from my_info import My_info as My
from test_data import *
from utility import make_my_oauth, response_success_check


def like(user_id: str, tweet_id: str) -> bool:
    payload = {"tweet_id": tweet_id} # 複数のツイートを同時にいいねするのは無理っぽい
    oauth = make_my_oauth()
    response = oauth.post(
        f"https://api.twitter.com/2/users/{user_id}/likes", json=payload
    )
    response_success_check(response, 200)
    print(f"Response code: {response.status_code}")

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    return json_response["data"]["liked"]


if __name__ == "__main__":
    like(My.id, some_tweets_data["data"][3]["id"])

