# -*- coding: utf-8 -*-
"""
python-twitter Graphs
"""

import twitter
import json

consumer_key="1U4HldV4FsKbXIaphybo8sEJq"
consumer_secret="nJw8f8RCkys02KQ9R5oYP2jg0udFOvki2w5YwVAGnWAnvPruuW"
access_token="1099354391423913985-iRB1gtKVrBqnUu16u6Ua1AghxhraiZ"
access_token_secret="XvNvFf9REbFYECMwOtlHGryJoBXM6aSytPqJPFLUcr29c"

auth = twitter.oauth.OAuth(access_token,access_token_secret,
                           consumer_key,consumer_secret)


twitter_api = twitter.Twitter(auth=auth)

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

CANADA_WOE_ID = 23424775

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)

us_trends = twitter_api.trends.place(_id=US_WOE_ID)

#print (us_trends)

print

#print (json.dumps(us_trends, indent=1))



# using set of python to find common trends
world_trends_set = set([trend['name'] 
                        for trend in world_trends[0]['trends']])

us_trends_set = set([trend['name'] 
                     for trend in us_trends[0]['trends']]) 

common_trends = world_trends_set.intersection(us_trends_set)

#print (json.dumps(common_trends,indent=1))
print (common_trends)


count = 10


# See https://dev.twitter.com/rest/reference/get/search/tweets

for trends_details in common_trends:
    
        search_results = twitter_api.search.tweets(q=trends_details, count=count, lang='en')
        statuses = search_results['statuses']
       # print ((json.dumps(statuses, indent=4)))
        print(statuses)

from urllib.parse import unquote


# Iterate through 5 more batches of results by following the cursor
for _ in range(5):
    print('Length of statuses', len(statuses))
    try:
        next_results = search_results['search_metadata']['next_results']
    except KeyError as e: # No more results when next_results doesn't exist
        break

    # Create a dictionary from next_results, which has the following form:
    # ?max_id=847960489447628799&q=%23RIPSelena&count=100&include_entities=1
    kwargs = dict([ kv.split('=') for kv in unquote(next_results[1:]).split("&") ])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
print(json.dumps(statuses[0], indent=1))



status_texts = [ status['text']
                 for status in statuses ]

screen_names = [ user_mention['screen_name']
                 for status in statuses
                     for user_mention in status['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
             for status in statuses
                 for hashtag in status['entities']['hashtags'] ]

# Compute a collection of all words from all tweets
words = [ w
          for t in status_texts
              for w in t.split() ]

# Explore the first 5 items for each...

print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(words[0:5], indent=1))

