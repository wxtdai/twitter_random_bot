
from typing import List

from my_info import My_info as My

def is_liked(my_id: int, tweet: dict):
    return False

def exclude_liked(tweets: List[dict]):
    # Todo: exclude process
    non_replyed_tweets = []
    for tweet in tweets:
        if is_liked(My.id, tweet):
            non_replyed_tweets.append(tweet)
    return non_replyed_tweets

def exclude_replyed(tweets: List[dict]):
    return exclude_liked(tweets) # いいねしたもの = リプライ済 としている
