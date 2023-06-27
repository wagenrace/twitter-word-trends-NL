import re
from typing import List

regex = re.compile(r"#?\w[\w-]*")
regex_links = re.compile(r"https://[\w\.\d/]+")


def tokenize_tweet(tweet: str) -> List[str]:
    tweet = tweet.lower()
    tweet = regex_links.sub("", tweet)
    tokens = regex.findall(tweet)
    return tokens
