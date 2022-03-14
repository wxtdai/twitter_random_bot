
from typing import List
from my_info import My_info as My
from search_liked_users import search_liked_users
from test_data import *

def is_liked(my_id: str, tweet: dict) -> bool:
    liked_users: List[str] = search_liked_users(tweet["id"])
    MAX_COUNTS = 100
    return len(liked_users) >= MAX_COUNTS or (my_id in liked_users)
    # 100いいね以上の場合は、本来は複数回クエリを送ってuser_idを収集しなければならないのだがレアケースだしバグが起こりそうなので100いいね以上なら無条件でいいねしているものとみなします


def exclude_liked(tweets: List[dict]):
    non_replyed_tweets = []
    for tweet in tweets:
        if is_liked(My.id, tweet):
            non_replyed_tweets.append(tweet)
    return non_replyed_tweets


def exclude_replyed(tweets: List[dict]):
    return exclude_liked(tweets) # いいねしたもの = リプライ済 としている


if __name__ == "__main__":
    print(is_liked(My.id, { "id": some_tweets_data["data"][3]["id"]}))

