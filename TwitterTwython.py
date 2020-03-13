# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 00:03:57 2019

@author: s6040865
"""


import twitter as tw
import tweepy as tp
import json


consumer_key="1U4HldV4FsKbXIaphybo8sEJq"
consumer_secret="nJw8f8RCkys02KQ9R5oYP2jg0udFOvki2w5YwVAGnWAnvPruuW"
access_token="1099354391423913985-iRB1gtKVrBqnUu16u6Ua1AghxhraiZ"
access_token_secret="XvNvFf9REbFYECMwOtlHGryJoBXM6aSytPqJPFLUcr29c"
# Load credentials from json file
#with open("twitter_credentials.json", "r") as file:  
 #   creds = json.load(file)

auth = tw.oauth.OAuth(access_token,access_token_secret,
                           consumer_key,consumer_secret)


twitter_api = tw.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

CANADA_WOE_ID = 23424775

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

us_trends = twitter_api.trends.place(_id=US_WOE_ID)
canada_trends =  twitter_api.trends.place(_id=CANADA_WOE_ID)

#print (us_trends)

print

#print (json.dumps(us_trends, indent=1))
    
    

# using set of python to find common trends
world_trends_set = set([trend['name'] 
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] 
                     for trend in us_trends[0]['trends']]) 

common_trends = world_trends_set.intersection(us_trends_set)

print()
print()
#print (json.dumps(common_trends,indent=1))
print ("Common trends between World and US",common_trends)




query = {'q': '#CrewDragon',  
        'count': 100,
        'until': '2018-01-20',
        }




search_results = twitter_api.search.tweets(q="#ArtificialIntelligence")

statuses = search_results['statuses']
#print(json.dumps(statuses, indent=1))


trends_related_articles = json.dumps(statuses, indent=1)

print(trends_related_articles)