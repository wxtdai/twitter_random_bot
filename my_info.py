from requests_oauthlib import OAuth1Session
import json
from config import *

def get_users_me_user_context():
    print("start:get_users_me_user_context()")
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


class My_info:
    id         = None # "1501949516575961101"
    title_name = None # "ランダムBot"
    at_name    = None # "RandomValueBot" @を付けると英数字名前になる


if My_info.id is None:
    print("descript My_info")
    json_response_data = (get_users_me_user_context())["data"]
    My_info.id         = json_response_data["id"]
    My_info.title_name = json_response_data["name"]
    My_info.at_name    = json_response_data["username"]  
else:
    print("already descripted My_info")


if __name__ == "__main__":
    print(My_info.at_name)