
from libcst import For
from requests_oauthlib import OAuth1Session
import json

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