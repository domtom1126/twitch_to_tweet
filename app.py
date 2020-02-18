# 1.) Return True if user is live on Twitch via Twitch api
"""
Or use selenium to get "live" element and if that is True 
send the tweet
"""
# 2.) If True send tweet via Twitter api
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from twitter import *

twitch_user = str(input('What is your user name'))
driver = webdriver.Safari()
driver.get('https://www.twitch.tv/{:s}'.format(twitch_user))
#check to see if live element
"""
xpath for live element for summit1g:
//*[@id="root"]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div[1]/p

access_token = 848635117836873728-nKVTlzuOGOaYNxJlcXe4TgVMEe7mrTc

secret = cEulcY4AmEqz8Ao9kQG9oWMgjBAe66MvX7F3iGzOY1niD
"""
# Twitter Creds
t = Twitter(auth=OAuth(
'848635117836873728-nKVTlzuOGOaYNxJlcXe4TgVMEe7mrTc', 'cEulcY4AmEqz8Ao9kQG9oWMgjBAe66MvX7F3iGzOY1niD','t10bqenGY0gWTcTcjzq48ZMWA','EODw9yoAiUYxBxnbRAQg7LZrz6kqSQgOEDQnIiAIhCaNgOAQtu'))

live = True
try:
    if live: 
        is_live = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div[1]/p')
        test = t.statuses.update(status = "is live python test")
        print('is live')
except Exception:
    live = False
    print('not live')
# if live:
#     is_live = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/main/div[1]/div/div[2]/div/div[1]/div[1]/div/div/div[3]/div/div[1]/p')
#     print('is live')
# else:
#     print('not live')
driver.close()


