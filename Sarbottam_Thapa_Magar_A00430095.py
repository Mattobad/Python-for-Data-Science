# -*- coding: utf-8 -*-
"""
twitter mining trends
"""

import twitter
import json


# api keys
consumer_key="1U4HldV4FsKbXIaphybo8sEJq"
consumer_secret="nJw8f8RCkys02KQ9R5oYP2jg0udFOvki2w5YwVAGnWAnvPruuW"
access_token="1099354391423913985-iRB1gtKVrBqnUu16u6Ua1AghxhraiZ"
access_token_secret="XvNvFf9REbFYECMwOtlHGryJoBXM6aSytPqJPFLUcr29c"

# authenticating through keys
auth = twitter.oauth.OAuth(access_token,access_token_secret,
                           consumer_key,consumer_secret)


twitter_api = twitter.Twitter(auth=auth)

#WOE(Where On Earth Id) value
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

#CANADA_WOE_ID = 23424775

#fetching the trends
world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

us_trends = twitter_api.trends.place(_id=US_WOE_ID)

# using set of python to find common trends
world_trends_set = set([trend['name'] 
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] 
                     for trend in us_trends[0]['trends']]) 

common_trends = world_trends_set.intersection(us_trends_set)

#printing the common trends 
print("-----------------------------------------------------------------------")
print()
print ("Common Trends of  USA and World =>> ",common_trends)
print()
print("------------------------------------------------------------------------")
print()

#variables
count = 10
i=0

# iterating for the common trends
for trends_details in common_trends:
        i+=1
        search_results = twitter_api.search.tweets(q=trends_details, count=count, lang='en')
        statuses = search_results['statuses']
        
        status_texts = [ status['text']
                 for status in statuses ]
        hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]
        screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]
        
        words = [ w
          for t in status_texts
              for w in t.split() ]

        print(f"Articles {i}",json.dumps(status_texts[0:5], indent=1))
        print("---------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")
        
