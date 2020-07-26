import requests
from bs4 import BeautifulSoup as bs
import tweepy as tw

API_KEY="udjdOw1ZGdTbu2YcolgRtkYjJ"
API_SECRET_KEY="2g1Beh94iUB7iECbcBNzmDmP2RHFxqsZwaolCoZ0HlRGohEx4e"
ACCESS_TOKEN = "66484327-tJuAYcOw2ISPswSfwK3xyoObdghtn3xhJRgNmSeqg"
ACCESS_TOKEN_SECRET="QmEc58vTdWOt2o9KfKgxv0e4XMRXW8Sf1NjkmGgV5KNZZ"


def tw_auth():
    auth = tw.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tw.API(auth, wait_on_rate_limit=True)

    return api


def test_tweet(api):
    api.update_status("Look, I'm tweeting from #Python in my #earthanalytics class! @EarthLabCU")


api = tw_auth()
test_tweet(api)
print("DONE")