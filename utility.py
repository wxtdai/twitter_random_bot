
from libcst import For


def toCSV(l: list):
    ret = ""
    for e in l:
        ret += str(e)
        ret += ","
    if len(ret)>0:
        ret = ret[:-1]
    return ret


if __name__ == "__main__":
    assert(toCSV([111,543,232]) == "111,543,232")
    assert(toCSV([]) == "")
    assert(toCSV(["abc","ppp"]) == "abc,ppp")