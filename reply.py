
from like import like
from my_info import My_info
from post import *

def reply(tweet: dict, content: str):
    post(make_post_payload(text=content, reply_id=tweet["id"]))
    like(My_info.id, tweet["id"])

