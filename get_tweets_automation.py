import requests
from bs4 import BeautifulSoup as bs
import tweepy as tw
import pandas as pd

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


def all_user_twets(api, user_name):
    for status in tw.Cursor(api.user_timeline, id=user_name).items(10):
        # process status here
        print(status.text)

    # api.user_timeline(id=user_name)
    # user = api.get_user(user_name)
    # print(user.screen_name)
    # print(user.followers_count)
    # for friend in user:
    #     print(friend.screen_name)

def friends_list(api):
    csv_file_name = "followers_list_exported.csv"
    columns = ['description', 'friends_count', 'id', 'location', 'name', 'screen_name', 'statuses_count', 'verified']

    friends_dict = {col_name: [] for col_name in columns}


    # raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
    #             'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
    #             'age': [42, 52, 36, 24, 73],
    #             'preTestScore': [4, 24, 31, 2, 3],
    #             'postTestScore': [25, 94, 57, 62, 70]}





    for user in tw.Cursor(api.friends).items():
        for col_name in columns:
            friends_dict[col_name].append(getattr(user, col_name, "nothing shanto"))

        # process status here
        print(user)

    df = pd.DataFrame(friends_dict, columns=columns)
    df.to_csv(csv_file_name, index=False)


api = tw_auth()
# test_tweet(api)
# all_user_twets(api, "eugenegu")
friends_list(api)
print("DONE")