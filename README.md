To check out a live version of this project, please visit https://twitter.com/hour_random

You must install TensorFlow. Navigate to your cloned directory through your console and type 
```
pip install tensorflow
```
After this, you will need to install Keras using git clone (Additional installation procedures can be found at https://github.com/keras-team/keras). In the same directory type
```
git clone https://github.com/keras-team/keras.git
```
then move into the keras directory and run setup.py
```
cd keras
python setup.py install
```
After this, you will need to install the textgenrnn. cd out of the keras folder and follow these steps
```
cd ..
git clone https://github.com/minimaxir/textgenrnn.git
cd textgenrnn
python setup.py install
cd ..
```
Now you are back in the main directory
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
To train your bot, place your text file into your cloned directory and run with argv[1] as the file to train the bot on, and argv[2] as the number of epochs
```
...\random-sentence-twitter-bot> python bot.py train your_file_name.txt 150
```

To run your bot navigate to your cloned directory. argv[1] is how many seconds you desire between tweets, and agrv[2] is how many times you would like the bot to tweet on this particular execution. For example:
```
...\random-sentence-twitter-bot> python bot.py 3600 24
```
Will have the bot tweet once every hour (3600 seconds) for a total of 24 times. This will occur over the following 24 hours.
To run the bot only once, simply ommit argv[1] and argv[2]:
```
...\random-sentence-twitter-bot> python bot.py
```
Every execution of this code will also check for new followers and unfollow any non followers.
