import os
from time import time
import datetime
import pandas as pd
import snscrape.modules.twitter as sntwitter

result_dir = "results"
os.makedirs(result_dir, exist_ok=True)

for i in range(365):
    tweets_list1 = []
    start_day = 1641034800 + 86400 * i
    end_day = start_day + 86400
    date = datetime.datetime.fromtimestamp(start_day)
    week_number = date.strftime("%W")
    week_day = date.weekday()
    month = str(date.month).zfill(2)
    query = f"since_time:{start_day} until_time:{end_day} lang:nl"

    start = time()
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if tweet.inReplyToTweetId:
            continue
        tweets_list1.append(
            [tweet.date, tweet.id, tweet.rawContent, tweet.user.username, tweet.url]
        )
        print(
            f"A total of {len(tweets_list1)} have been colleted in {time() - start}s",
            end="\r",
        )
        if tweet.retweetedTweet:
            break
        if len(tweets_list1) >= 1000:
            break
    # Creating a dataframe from the tweets list above
    tweets_df1 = pd.DataFrame(
        tweets_list1, columns=["Datetime", "Tweet Id", "Text", "Username", "Url"]
    )
    tweets_df1.to_csv(
        os.path.join(result_dir, f"2022_{week_number}_{week_day}_{month}_tweets.csv")
    )
    print(f"Finished {week_number}_{week_day}_{month}")
