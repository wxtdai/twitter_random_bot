
from typing import List
from my_info import My_info as My


def parse(text: str):
    text_exclude_at_name :      str  = text.replace("@" + My.at_name, '')
    text_list            : List[str] = text_exclude_at_name.split('\n')
    striped_text_list    : List[str] = [t.strip() for t in text_list]
    non_void_text_of_list: List[str] = [t for t in striped_text_list if t != ""]
    return non_void_text_of_list


if __name__ == "__main__":
    print(parse(" @RandomValueBot abc \n def "))