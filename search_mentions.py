# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/User-Mention-Timeline/user_mentions.py 
import requests
import json
from config import *
from my_info import My_info as My
from utility import response_success_check


bearer_token = BEARER_TOKEN

def create_url(user_id):
    return "https://api.twitter.com/2/users/{}/mentions?max_results=100".format(user_id)

def get_params():
    return {"tweet.fields": "created_at,public_metrics"}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    response_success_check(response,200)
    return response.json()


def search_mentions(user_id):
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    if "errors" in json_response:
        raise Exception(
            "Request returned an error: {}".format(
                json_response["errors"][0]["detail"]
            )
        )
    return json_response["data"]


def search_my_mentions():
    return search_mentions(My.id)


if __name__ == "__main__":
    print(search_my_mentions())

