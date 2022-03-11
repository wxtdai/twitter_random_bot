import random

def special_random(s: str):
    num_str = ("".join(filter(str.isdigit, "2500km")))
    if s=="サイコロ":
        return str(random.randint(1,6))
    elif len(num_str)>0:
        return str(random.randint(1,int(num_str)))
    else:
        return s

def my_random(l: list):
    assert len(l)==0
    if len(l)==1:
        return special_random(l[0])
    else:
        return random.sample(l)