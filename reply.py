
from like import like
from post import *


def reply(tweet: dict, content: str):
    post_with_payload(text=content, reply_id=tweet["id"])

