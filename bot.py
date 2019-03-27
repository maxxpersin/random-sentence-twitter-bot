import tweepy
import random
import time
import sys
from textgenrnn import textgenrnn



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


def status_update(textgen, timer, upper_limit): # Updates the status
    counter = 0
    u = 0
    while counter < upper_limit:
        for follower in tweepy.Cursor(api.followers).items(): # Double checks followers
            follower.follow()
            for x in list_of_followers:
                if x == follower.screen_name:
                    u = u + 1

            if u is 0:
                try:
                    api.update_status(
                        status="Thanks for the follow @%s" % (follower.screen_name))  # Saying hello to new followers
                    cur_followers_write.write("%s\n" % (follower.screen_name))  # Saves followers name in file to not duplicate hello messages
                except:
                    print("oops")  # Error handling
            u = 0

        api.update_status(status=''.join(textgen.generate(return_as_list=True, max_gen_length=280))) # Publishes tweet
        counter = counter + 1
        time.sleep(timer) # Waits for specified time


# Checking followers
f = open("curr_followers.txt", "r")
temp = f.read()
list_of_followers = temp.splitlines()
cur_followers_write = open("curr_followers.txt", "a+")
"""
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
"""
# Status updates based on args
t = textgenrnn()

if len(sys.argv) == 1:
    status_update(t, 0, 1)
else:
    status_update(t, int(sys.argv[1]), int(sys.argv[2]))
