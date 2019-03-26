You must install tweepy,
in your console write :
```
pip install tweepy
```
You will then need to go to your apps.twitter.com page and navegate to your keys & tokens.
You will need to copy your consumer api keys and access tokens to the corresponding keys in the bot.py file

```
consumer_key = 'consumer-key'
consumer_secret = 'consumer-secret'
access_token = 'access-token'
access_token_secret = 'access-token-secret'
```

To run your bot navegate to your cloned directory. argv[1] is how many seconds you desire between tweets, and agrv[2] is how many times you would like the bot to tweet on this particular execution. For example:
```
...\random-sentence-twitter-bot> python bot.py 3600 24
```
Will have the bot tweet once every hour (3600 seconds) for a total of 24 times. This will occur over the following 24 hours.
To run the bot only once, simply ommit argv[1] and argv[2]:
```
...\random-sentence-twitter-bot> python bot.py
```
Every execution of this code will also check for new followers and add them to the curr_followers.txt file. It will also tweet a thank you to any new users.
