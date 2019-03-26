import tweepy
import tkinter
import requests
import random
import time

consumer_key = 'UPBKZkknAwoyGbos7bW7dKUiR'
consumer_secret = 'FVtQWSKuOAD6SCYVoQXlrFXWfFN2NhJoG0SFohVB9jIeu9dcFr'
access_token = '1110573743536041985-1ebhe0TJebmquhN93QOEdXlPtIrwUt'
access_token_secret = 'HGqe2mxxlPhVWyAiF0JsDzpAOYxtjNyPq4xSwPgAuzIXc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)

f = open("BIG_TEXT.txt", "r")
contents = f.read()
text = contents.split()

t = 600
counter = 0
while counter < 5:
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

