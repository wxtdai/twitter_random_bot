from requests_oauthlib import OAuth1Session
import json
from config import *


def get_users_me_user_context():
    # User fields are adjustable, options include:
    # created_at, description, entities, id, location, name,
    # pinned_tweet_id, profile_image_url, protected,
    # public_metrics, url, username, verified, and withheld
    fields = "created_at,description"
    params = {"user.fields": fields}

    # Get request token
    request_token_url = "https://api.twitter.com/oauth/request_token"
    oauth = OAuth1Session(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET
    )

    response = oauth.get("https://api.twitter.com/2/users/me", params=params)

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    json_response = response.json()

    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False))
    return(json_response)

def get_user_id():
    s = get_users_me_user_context()["data"]["id"]
    print(s)
    print(type(s))
    return s

if __name__ == "__main__":
    get_user_id()