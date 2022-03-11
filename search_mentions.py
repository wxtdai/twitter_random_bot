# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/User-Mention-Timeline/user_mentions.py 
import requests
import json
from config import *
from get_users_me_user_context import My_info as My

bearer_token = BEARER_TOKEN

def create_url(user_id):
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)

def get_params():
    return {"tweet.fields": "created_at,public_metrics"}

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def search_mentions(user_id):
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print("search_mentions")
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    return json_response["data"]

def search_my_mentions():
    print("search_my_mentions")
    return search_mentions(My.id)

if __name__ == "__main__":
    search_my_mentions()
    