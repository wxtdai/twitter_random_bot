
from my_info import My_info as My

def parse(text: str):
    text2 = text.replace("@" + My.at_name, '')
    text_list = text2.split('\n')
    text_list2 = [t.strip() for t in text_list]
    text_list3 = [t for t in text_list2 if t != ""]
    return text_list3

if __name__ == "__main__":
    print(parse(" @RandomValueBot abc \n def "))