import tweepy

consumer_key = 'xxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxx'
access_token = 'xxxxxxxxxx'
access_token_secret = 'xxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

FILE_NAME = 'last.txt'
toReply = 'elonmusk'

mystring_us = f""" Testing these numbers
    Number 1
    Number 2
    Number 3"""

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.user_timeline(read_last_seen(FILE_NAME), screen_name = toReply, count=1)
    for tweet in tweets:
            api.update_status("@" + toReply + mystring_us, in_reply_to_status_id = tweet.id)

    store_last_seen(FILE_NAME, tweet.id)
    api.create_favorite(tweet.id) # Like the tweet with mentions

while True:
    reply()
    time.sleep(30)
