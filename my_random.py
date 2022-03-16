import random
from typing import List
import re


def dice_str(max = 6) -> str:
    return str(random.randint(1,max))


def special_random(s: str) -> str:
    regex = re.compile('d+')
    match = regex.findall(s)
    
    if s=="サイコロ":
        return dice_str()
    elif len(match)>0:
        return random.choice(match)
    else:
        return s


def my_random(l: List[str]) -> str:
    if len(l)==0:
        ret = dice_str
    elif len(l)==1:
        ret = special_random(l[0])
    else:
        ret = random.choice(l)
    assert(type(ret)==str)
    return ret

