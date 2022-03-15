import random
from typing import List


def dice_str(max = 6) -> str:
    return str(random.randint(1,max))


def special_random(s: str) -> str:
    digit_only_str = ("".join(filter(str.isdigit, str)))
    if s=="サイコロ":
        return dice_str
    elif len(digit_only_str)>0:
        return str(random.randint(1,int(digit_only_str)))
    else:
        return s


def my_random(l: List[str]) -> str:
    if len(l)==0:
        return dice_str
    elif len(l)==1:
        return special_random(l[0])
    else:
        return random.sample(l)

