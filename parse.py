
from get_users_me_user_context import My_info as My

def parse(text: str):
    text2 = text.replace("@" + My.at_name, '')
    text_list = text2.split('\n')
    text_list2 = [t.strip() for t in text_list]
    return text_list2

if __name__ == "__main__":
    print(parse(" @RandomValueBot abc \n def "))