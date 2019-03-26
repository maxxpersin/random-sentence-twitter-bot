import tweepy
import requests
import random
import time
import sys

consumer_key = 'UPBKZkknAwoyGbos7bW7dKUiR'
consumer_secret = 'FVtQWSKuOAD6SCYVoQXlrFXWfFN2NhJoG0SFohVB9jIeu9dcFr'
access_token = '1110573743536041985-1ebhe0TJebmquhN93QOEdXlPtIrwUt'
access_token_secret = 'HGqe2mxxlPhVWyAiF0JsDzpAOYxtjNyPq4xSwPgAuzIXc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)


def instant(text):
    r1 = random.randrange(0, len(text))
    r2 = random.randrange(0, len(text))
    r3 = random.randrange(0, len(text))

    x = text[r1]
    y = text[r2]
    z = text[r3]

    tweet = "%s %s %s." % (x,y,z)
    api.update_status(status = tweet)


def ten_min(text, upper_limit):
    t = 600
    counter = 0
    while counter < upper_limit:
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
            print ("Followed everyone that is following " + user.name)
    
        r1 = random.randrange(0, len(text))
        r2 = random.randrange(0, len(text))
        r3 = random.randrange(0, len(text))

        x = text[r1]
        y = text[r2]
        z = text[r3]

        tweet = "%s %s %s." % (x,y,z)
        api.update_status(status = tweet)
        counter = counter + 1
        time.sleep(t)


def one_hour(text, upper_limit):
    t = 3600
    counter = 0
    while counter < upper_limit:
        for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
            #print ("Followed everyone that is following " + user.name)
    
        r1 = random.randrange(0, len(text))
        r2 = random.randrange(0, len(text))
        r3 = random.randrange(0, len(text))

        x = text[r1]
        y = text[r2]
        z = text[r3]

        tweet = "%s %s %s." % (x,y,z)
        api.update_status(status = tweet)
        counter = counter + 1
        time.sleep(t)


f = open("curr_followers.txt", "r")
temp = f.read()
list_of_followers = temp.splitlines()
cur_followers_write = open("curr_followers.txt", "a+")

u = 0

f = open("BIG_TEXT.txt", "r")
contents = f.read()
text = contents.split()
for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
            #print ("Followed everyone that is following " + user.name)
            for x in list_of_followers:
                if x is follower.screen_name:
                    u = u + 1
            
            if u is 0:
                try:
                    api.update_status(status = "Thanks for the follow @%s" % (follower.screen_name))
                    cur_followers_write.write("%s\n" % (follower.screen_name))
                except:
                    print("oops")
            u = 0


if len(sys.argv) == 1:
    instant(text)
elif sys.argv[1] == "hour":
    one_hour(text, int(sys.argv[2]))
elif sys.argv[1] == "ten":
    ten_min(text, int(sys.argv[2]))