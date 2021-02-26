import tweepy
import time
consumer_key = 'wgbB6FU5pYO92IVeOno1uSfp4'
consumer_secret = 'sEgp9duE3rd4sJ0wAOlWVnNWsukvISwZxwy0r35QSz6bg9KK8O'
key = '1354811883442737152-MyI2BGQLkpkfIRCZOp1doL3yRzHxdw'
secret = 'SbzrhhciSIEZSZhHJBzQLbVAATTtqR8QhSSw8H5r3w3VF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

tweets = api.mentions_timeline()

FILE_NAME = "last_seen.txt"

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME,"r")
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME,last_seen_id):
    file_write = open(FILE_NAME,"w")
    file_write.write(str(last_seen_id))
    file_write.close()
    return
def reply():
    tweets = api.mentions_timeline(read_last_seen(FILE_NAME),tweet_mode='extended')
    for tweet in reversed(tweets):
            if "#tweetbot" in tweet.full_text.lower():
                print("Replied to -",tweet.id)
                api.update_status("@"+tweet.user.screen_name+" good luck for #100DaysOFCode!",tweet.id)
                api.create_favorite(tweet.id)
                api.retweet(tweet.id)
                store_last_seen(FILE_NAME,tweet.id)
while True:
    reply()
    time.sleep(20)
