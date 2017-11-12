from __future__ import division
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import numpy as np
import matplotlib.pyplot as plt

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
       
        consumer_key = '1jD5DYXp8OtNi30iRMLvEg1Qk'
	consumer_secret = 'oU1phe1DbpRETgrUODdyWa8wESARFgSy09KhgLqh5pJMjrIlbY'
	access_token = '3213716487-1MfLG6KDQpdqAG3dG4MyVjw9yAniE8cYtjPOpBu'
	access_token_secret = 'djkHKpjasoaKyjskgLlBP2Ip86UYrQRYjf32xQfMeuYmx'
       
        try:
         
            self.auth = OAuthHandler(consumer_key, consumer_secret)
         
            self.auth.set_access_token(access_token, access_token_secret)
        
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        
        analysis = TextBlob(self.clean_tweet(tweet))
       
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'
 
    def get_tweets(self, query, count = 1000):
        '''
        Main function to fetch tweets and parse them.
        '''
       
        tweets = []
	query=[]
 
        try:
          
            fetched_tweets = self.api.search(q = query, count = count)
 
           
            for tweet in fetched_tweets:
               
                parsed_tweet = {}
 
               
                parsed_tweet['text'] = tweet.text
               
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
 
                if tweet.retweet_count > 0:
                 
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)
 
        
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))
 
def main():
    api = TwitterClient()
    query=['trumph','namo','demonitization','cryptocurrency', 'bitcoin', 'bitcoins', 'ethereum', 'litecoin', 'bitcoinprice', 'blockchain', 'investment', 'investor', 				   			'stockmarket','stocks', 'getrich','makemoney', 'makemoneyonline', 'mentorship', 'mentoring', 'xrp', 'bitfinex','altcoins', 'moneytalks']
    for x in query:
    	x = api.get_tweets( query,count = 1000)
   
	
   
 
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
   
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/50))

    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    print("Negative tweets percentage: {} %".format(100*len(ntweets)/50))

    print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/70))
 
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

