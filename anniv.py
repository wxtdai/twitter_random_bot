# https://exactsolutions.co.jp/column/rpa/python-twitterapi-tweet/

import random
import datetime
import sys
import requests
from time import sleep
from requests_oauthlib import OAuth1Session
from config import *
from bs4 import BeautifulSoup
from config import *

#リクエストエラーが発生した場合のリトライ回数
RETRY_TIME = 5
#記念日取得用URL
ANNIV_URL = r'https://zatsuneta.com/category/anniversary.html'

def main():
    
    anniv_lists = fetch_anniv()

    #リストが空の場合は取得失敗として処理を中断
    if len(anniv_lists) == 0:        
        print(f"{'#'*10}\nFail to fetch anniversary\nCancel all processing\nPlease try again\n{'#'*10}")
        sys.exit()
    else:        
        rand_num = random.randrange(0,(len(anniv_lists)-1))
        anniv_name = anniv_lists[rand_num][0]
        anniv_link = anniv_lists[rand_num][1]

        #選択した記念日出力
        print(f"{'#'*10}\nselected_anniversary --> {anniv_name}\nlink --> {anniv_link}\n{'#'*10}")        
        
        results = post_tweet(anniv_name,anniv_link)

        #結果出力
        if results['code'] != 201:
            print(f"Tweet is failed\nstatus_code --> {results['code']}\ndetail --> {results['response']['detail']}\n{'#'*10}")
        else:
            print(f"Tweet is Succeed\n{'-'*3}tweet_text{'-'*3}\n{results['response']['data']['text']}\n{'#'*10}")      
    
#記念日一覧の取得関数（取得に失敗した場合、空のリストを返す）
def fetch_anniv():

    res = None

    try:
        res = requests.get(ANNIV_URL)
    #エラーが発生した場合、リクエストリトライ実行（回数はRETRY_TIME定数で設定）
    except Exception as err:

        print(f"{'#'*10}\nREQUETS_ERROR --> {err}\nstart_retry_requests\n{'#'*10}")
        sleep(1.5)

        cnt_loop = 1
        while cnt_loop <= RETRY_TIME:
            try:
                print(f'RETRY_COUNTER --> {cnt_loop}')     
                res = requests.get(ANNIV_URL)
            except Exception as err:
                print(f'REQUETS_ERROR --> {err}')
                sleep(1.5)
                pass
            else:
                print(f"SUCCESS_TO_CONNECTING_NETWORK\n{'#'*10}")
                break            
            
            cnt_loop += 1
        
    if res == None:
        return_val = []
    else:
        
        sp = BeautifulSoup(res.text,'html.parser')
        elms = sp.select('#contents > div.article:nth-child(2) > p > ul > li:nth-child(n) > a')
        
        anniv_names = [elm.text for elm in elms]
        anniv_links = [elm.get('href') for elm in elms]
        return_val = list(zip(anniv_names,anniv_links))

    return return_val

#api接続の関数
def define_client():
    AK = CONSUMER_KEY
    AKS = CONSUMER_SECRET
    AT = ACCESS_TOKEN
    ATS = ACCESS_TOKEN_SECRET

    return OAuth1Session(AK,AKS,AT,ATS)

def make_context(param_text:str, param_url:str):
    #テキスト編集
    today = datetime.date.today()
    edited_text = f'本日は{today.year}年{today.month}月{today.day}日、「{param_text}」です。\n\n今日も頑張っていきましょー!!\n\n紹介した記念日については「{param_url}」を参考にしています。気になったらぜひご覧ください。'
    return edited_text

#ツイート処理の関数
def post_tweet(param_text:str,param_url:str):

    edited_text:str = make_context(param_text, param_url)
    
    api = define_client()
    resource_url = r'https://api.twitter.com/2/tweets' #エンドポイントURL

    params = {
        "text":edited_text
    }

    res = api.post(resource_url,json=params)
    dict_results = {'code':res.status_code,
                    'response':res.json()}

    return dict_results

if __name__ =='__main__':
    main()