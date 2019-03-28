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

def check_followers():
    followers = []
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)

    print ("Found %s followers, finding friends.." % len(followers))
    friends = []
    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)

    # creating dictionaries based on id's is handy too

    friend_dict = {}
    for friend in friends:
        friend_dict[friend.id] = friend

    follower_dict = {}
    for follower in followers:
        follower_dict[follower.id] = follower

    # now we find all your "non_friends" - people who don't follow you
    # even though you follow them.

    non_followers = [friend for friend in friends if friend.id not in follower_dict] # people who are not following me but i am following them
    not_yet_following = [follower for follower in followers if follower.id not in friend_dict] # people who are following me but i am not following them
    

    for nf in non_followers:
        nf.unfollow() # unfollow non followers

    for nyf in not_yet_following:
        nyf.follow()
        api.update_status(status="Thanks for the follow @%s" % (nyf.screen_name))  # Saying hello to new followers
        


def status_update(textgen, timer, upper_limit): # Updates the status
    counter = 0
    while counter < upper_limit:
        check_followers()

        api.update_status(status=''.join(textgen.generate(return_as_list=True, max_gen_length=280))) # Publishes tweet
        counter += 1
        time.sleep(timer) # Waits for specified time


# Checking followers
f = open("curr_followers.txt", "r")
temp = f.read()
list_of_followers = temp.splitlines()
cur_followers = open("curr_followers.txt", "r+")

# Status updates based on args
t = textgenrnn()

if len(sys.argv) == 1:
    status_update(t, 0, 1)
else:
    status_update(t, int(sys.argv[1]), int(sys.argv[2]))
