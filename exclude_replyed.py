
from typing import List
from utility import get_newest_replyed_tweet_id,set_newest_replyed_tweet_id
from test_data import *


def select_tweet_after_newest_id(tweets: List[dict]):
    # ツイートの選択
    newest_id_int = get_newest_replyed_tweet_id()
    newer_tweets = []
    for tweet in tweets:
        if int(tweet["id"]) > newest_id_int:
            newer_tweets.append(tweet)

    # newest_idの更新
    ids_int: List[int] = [newest_id_int]
    for tweet in tweets:
        ids_int.append(int(tweet["id"]))
    next_newest_id_int = max(ids_int)
    set_newest_replyed_tweet_id(next_newest_id_int)

    return newer_tweets


def exclude_replyed(tweets: List[dict]):
    return select_tweet_after_newest_id(tweets)

