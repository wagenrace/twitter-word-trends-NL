import os
from time import time

import pandas as pd
import snscrape.modules.twitter as sntwitter

result_dir = "results"
os.makedirs(result_dir, exist_ok=True)
# Creating list to append tweet data to
tweets_list1 = []

query = 'lang:nl' #ur is code for urdu

# Using TwitterSearchScraper to scrape data and append tweets to list
start = time()
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if tweet.inReplyToTweetId:
        continue
    tweets_list1.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.url])
    print(f"A total of {len(tweets_list1)} have been colleted in {time() - start}s", end='\r')
    if len(tweets_list1)>=10000:
        break
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username', "Url"])
tweets_df1.to_csv(os.path.join(result_dir, "10k_tweets_nl.csv"))