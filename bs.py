import csv
import pdb
import os
from bs4 import BeautifulSoup as bs
from types import NoneType


#home = os.path.expanduser("~")
#os.chdir(home+"/Google Drive/storify")
ht = open("input_twitter.html", 'r')
soup = bs(ht, 'html.parser')

tweets = soup.find_all("div", {"class":"content"})
tweetData = []

def isNonTweet(content):
    test = content.find("a", {"class":"js-recommend-link"})
    return test is not None

for tweet in tweets:
    tweetDat = {}
    if isNonTweet(tweet):
        continue
    try:
        tweetDat['name'] = tweet.find("span", {"class": "FullNameGroup"}).get_text()
    except AttributeError:
        tweetDat['name'] = ""
    try:
        tweetDat['handle'] = tweet.find("span", {"class":"username"}).get_text()
    except AttributeError:
        tweetDat['handle'] = ""
    try:
        tweetDat['link'] = tweet.find("a", {"class":"tweet_timestamp"}).get("href")
    except AttributeError:
        tweetDat['link'] = ""
    try:
        tweetDat['time'] = tweet.find("span", {"class":"_timestamp"}).get("data-time")
    except AttributeError:
        tweetDat['time'] = ""
    print(tweetDat)
    pdb.set_trace()
