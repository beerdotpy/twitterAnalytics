"""
Script to filter tweets with word "analytics" and dump them in "data.txt" file
"""
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
access_token = "3269893483-QsIpgW3NOXQnpeuQ6WHoresl7Zs2DcyILqiqF43"
access_token_secret = "z4nfj7ydNInekkMapUueVBRfFXTqBzJfBhK3x35C0ZHCy"
consumer_key = "ZOknVDmUZRXkyjrN7xQ6jallv"
consumer_secret = "VV2cM6giaHjpsx5XOnHvO1aPxA601weedpBJOjsZmCOXo6BOfU"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    stream.filter(track=['analytics'])