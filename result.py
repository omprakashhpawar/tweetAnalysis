from __future__ import division
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

global  data
data= pd.read_csv('J_tsar_tweets.csv')

print data

def get_tweet_sentiment():
	'''
	Utility function to classify sentiment of passed tweet
	using textblob's sentiment method
	'''

	analysis = TextBlob(self.clean_tweet(data))

	if analysis.sentiment.polarity > 0:
	    return 'positive'
	elif analysis.sentiment.polarity == 0:
	    return 'neutral'
	else:
	    return 'negative'

def main():
    #api = TwitterClient()
   
    for x in data:
    	x = api.get_tweets( data,count = 1000)

	
   
 
    ptweets = [data for data in x if tweet['sentiment'] == 'positive']
   
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(data)))

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(data)))

    print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(data)))
 
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])
 
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])
    if (ntweets>ptweets):
	print ("company is lagging")
    else:
        print("company is riasing")
	
   

 
if __name__ == "__main__":
    main()

