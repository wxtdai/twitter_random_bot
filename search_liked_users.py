# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Likes-Lookup/liking_users.py

import requests
import json
from config import *
from utility import response_success_check

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = BEARER_TOKEN


def create_url(tweet_id: str):
    user_fields = "user.fields=created_at,description"
    url = f"https://api.twitter.com/2/tweets/{tweet_id}/liking_users?max_results=100&expansions=pinned_tweet_id"
    return url, user_fields


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2LikingUsersPython"
    return r


def connect_to_endpoint(url, user_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=user_fields)
    print(response.status_code)
    response_success_check(response,200)
    return response.json()


def search_liked_users(tweet_id: str):
    url, tweet_fields = create_url(tweet_id)
    json_response = connect_to_endpoint(url, tweet_fields)
    print("search_liked_users's result:")
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    if "data" not in json_response:
        return []
    return [user["id"] for user in json_response["data"]]


if __name__ == "__main__":
    print(search_liked_users("1466062033967738880")) # 「俺だけしかいないアドカレ。」