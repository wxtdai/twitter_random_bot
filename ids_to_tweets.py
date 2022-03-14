# プログラム元: https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Tweet-Lookup/get_tweets_with_bearer_token.py

# リファレンス: https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/api-reference/get-tweets

import requests
import json
import config
from utility import toCSV

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = config.BEARER_TOKEN

def create_url():
    tweet_fields = "tweet.fields=lang,author_id,public_metrics&media.fields=url" # 帰ってくるjsonに含む要素
    ids = [1278747501642657792,1255542774432063488,1497515066232815621,1499633893104025600]
    ids_str = f"ids={toCSV(ids)}"
    
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids_str, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def ids_to_tweets():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True, ensure_ascii=False)) 
    # ensure_ascii=False で日本語表示


if __name__ == "__main__":
    ids_to_tweets()