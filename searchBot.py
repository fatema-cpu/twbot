import tweepy
import time

consumer_key = 'wgbB6FU5pYO92IVeOno1uSfp4'
consumer_secret = 'sEgp9duE3rd4sJ0wAOlWVnNWsukvISwZxwy0r35QSz6bg9KK8O'
key = '1354811883442737152-MyI2BGQLkpkfIRCZOp1doL3yRzHxdw'
secret = 'SbzrhhciSIEZSZhHJBzQLbVAATTtqR8QhSSw8H5r3w3VF'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

hashtag = "kanganaranaut"
tweetNumber = 10
tweets = tweepy.Cursor(api.search,hashtag).items(tweetNumber)
def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("retweet done")
            time.sleep(5)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(5)
searchbot()
