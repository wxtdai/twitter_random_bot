
#tweet_form_python.py

import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理

url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント

print("内容を入力してください。")
tweet = input('>> ') #キーボード入力の取得
print('*******************************************')

'''

req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = {})

timeline = json.loads(req.text)

for tweet in timeline:
    print(tweet)



'''
params = {"status" : tweet}

res = twitter.post(url, params = params) #post送信

if res.status_code == 200: #正常投稿出来た場合
    print("Success.")
else: #正常投稿出来なかった場合
    print("Failed. : %d"% res.status_code)
    print(res)





'''
import twitter

auth = twitter.OAuth(consumer_key="",
consumer_secret="",
token="",
token_secret="")

t = twitter.Twitter(auth=auth)

#ツイートのみ
status="Hello,World" #投稿するツイート
t.statuses.update(status=status) #Twitterに投稿

#画像付きツイート
pic="" #画像を投稿するなら画像のパス
with open(pic,"rb") as image_file:
    image_data=image_file.read()
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img1 = pic_upload.media.upload(media=image_data)["media_id_string"]
t.statuses.update(status=status,media_ids=",".join([id=img1]))

'''
