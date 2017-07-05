"""
Script to read the "data.txt" file and save it mongo
"""
import json
import pymongo

conn = pymongo.MongoClient()
tweets = conn.valianceAnalytics.analytics_tweets

with open('data1.txt', 'r') as fp:
    array = fp.read().strip().split("\n")

for item in array:
    if len(item) != 0:
        tweets.save(json.loads(item))
