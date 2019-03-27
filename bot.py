import tweepy
import random
import time
import sys

# Simple Twitter bot
# This bot tweets a random sentence ever t seconds based on user args
# And tweets as many times as specified by the user

# @author Maxx Persin
# @date 3/26/2019
# Check out my github at https://github.com/maxxpersin

# API set up

consumer_key = 'UPBKZkknAwoyGbos7bW7dKUiR'
consumer_secret = 'FVtQWSKuOAD6SCYVoQXlrFXWfFN2NhJoG0SFohVB9jIeu9dcFr'
access_token = '1110573743536041985-1ebhe0TJebmquhN93QOEdXlPtIrwUt'
access_token_secret = 'HGqe2mxxlPhVWyAiF0JsDzpAOYxtjNyPq4xSwPgAuzIXc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def status_update(n, v, a, t, upper_limit): # Updates the status
    counter = 0
    while counter < upper_limit:
        for follower in tweepy.Cursor(api.followers).items(): # Double checks followers
            follower.follow()
    
        r1 = random.randrange(0, len(n)) # Getting the randomized indexes
        r2 = random.randrange(0, len(n))
        r3 = random.randrange(0, len(v))
        r4 = random.randrange(0, len(a))

        w = n[r1] # Getting the word for that index
        x = n[r2]
        y = v[r3]
        z = a[r4]

        tweet = "%s %s %s %s." % (z, x, y, w) # Concatination
        api.update_status(status = tweet) # Publishes tweet
        counter = counter + 1
        time.sleep(t) # Waits for specified time


# Checking followers
f = open("curr_followers.txt", "r")
temp = f.read()
list_of_followers = temp.splitlines()
cur_followers_write = open("curr_followers.txt", "a+")

# Opening word files and parsing them
noun_file = open("nouns.txt", "r")
contents = noun_file.read()
n = contents.split()

verb_file = open("verbs.txt", "r")
contents = verb_file.read()
v = contents.split()

adj_file = open("adjectives.txt", "r")
contents = adj_file.read()
a = contents.split()

u = 0
for follower in tweepy.Cursor(api.followers).items():
            follower.follow()
            for x in list_of_followers:
                if x == follower.screen_name:
                    u = u + 1
            
            if u is 0:
                try:
                    api.update_status(status = "Thanks for the follow @%s" % (follower.screen_name)) # Saying hello to new followers
                    cur_followers_write.write("%s\n" % (follower.screen_name)) # Saves followers name in file to not duplicate hello messages
                except:
                    print("oops") # Error handling
            u = 0

# Status updates based on args
if len(sys.argv) == 1:
    status_update(n, v, a, 0, 1)
else:
    status_update(n, v, a, int(sys.argv[1]), int(sys.argv[2]))
