import pdb
import os
from bs4 import BeautifulSoup as bs

def extractTexts(entities):
    return [i.get_text().strip() for i in entities]

class pooter:
    def get():
        return ""
    def get_text():
        return ""




home = os.path.expanduser("~")
os.chdir(home+"/Google Drive/storify")
ht = open("input_twitter.html", 'r')
soup = bs(ht, 'html.parser')

tweets = soup.find_all("div", {"class":"content"})
tweetData = []

for tweet in tweets:
    tweetDat = {}
    try:
        tweetDat['name'] = soup.find("span", {"class": "FullNameGroup"}).get_text()
    except AttributeError:
        tweetDat['name'] = ""
    try:
        tweetDat['handle'] = soup.find("span", {"class":"username"}).get_text()
    except AttributeError:
        tweetDat['handle'] = ""
    try:
        tweetDat['link'] = soup.find("a", {"class":"tweet_timestamp"}).get("href")
    except AttributeError:
        tweetDat['link'] = ""
    try:
        tweetDat['time'] = soup.find("span", {"class":"_timestamp"}).get("data-time")
    except AttributeError:
        tweetDat['link'] = ""


    for tweet_time in tweet_times:
        tweet_timestamps.append(tweet_time.get("data-time"))
        tweet_timestamps.append()


pdb.set_trace()
