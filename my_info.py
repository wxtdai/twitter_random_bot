
from config import *
from utility import make_my_oauth, response_success_check


def get_users_me_user_context():
    fields = "created_at,description"
    params = {"user.fields": fields}
    oauth = make_my_oauth()
    response = oauth.get("https://api.twitter.com/2/users/me", params=params)
    response_success_check(response,200)

    json_response = response.json()
    return(json_response)


class My_info:
    id         = None # "1501949516575961101"
    title_name = None # "ランダムBot"
    at_name    = None # "RandomValueBot" @を付けると英数字名前になる


if My_info.id is None:
    json_response_data = (get_users_me_user_context())["data"]
    My_info.id         = json_response_data["id"]
    My_info.title_name = json_response_data["name"]
    My_info.at_name    = json_response_data["username"]  


if __name__ == "__main__":
    print(My_info.at_name)

