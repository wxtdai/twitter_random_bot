# https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/User-Mention-Timeline/user_mentions.py 
import requests
import json
from config import *
from get_users_me_user_context import *


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = BEARER_TOKEN


def create_url(user_id):
    # Replace with user ID below
    return "https://api.twitter.com/2/users/{}/mentions".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at,public_metrics"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

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


def search_mentions(user_id = 2244994945):
    url = create_url(user_id)
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))

def search_my_mentions():
    search_mentions(get_user_id())

if __name__ == "__main__":
    search_my_mentions()
    