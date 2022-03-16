
import os
from requests_oauthlib import OAuth1Session
from config import *


def toCSV(l: list):
    ret = ""
    for e in l:
        ret += str(e)
        ret += ","
    if len(ret)>0:
        ret = ret[:-1]
    return ret


def response_success_check(response, success_code: int):
    if response.status_code != success_code:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )


def make_my_oauth():
    return OAuth1Session(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
    )


base = os.path.dirname(os.path.abspath(__file__))
newest_id_file = os.path.normpath(os.path.join(base, 'newest_replyed_tweet_id.txt'))

def get_newest_replyed_tweet_id() -> int:
    with open(newest_id_file, 'r') as file:
        for line in file:
            id_int:int = int(line)
    return id_int


def set_newest_replyed_tweet_id(id_int: int):
    with open(newest_id_file, 'w') as file:
        file.write(str(id_int))


