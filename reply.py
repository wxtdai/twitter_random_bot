
from like import like
from my_info import My_info


def reply(tweet: dict, content: str):
    like(My_info.id, tweet["id"])
    pass

