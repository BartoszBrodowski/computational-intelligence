import pandas as pd
import snscrape.modules.twitter as sntwitter

scraper = sntwitter.TwitterSearchScraper("andrewtate")

tweets = []
for i, tweet in enumerate(scraper.get_items()):
    tweet_data = {
        tweet.id,
        tweet.rawContent,
        tweet.user.username,
        tweet.likeCount,
        tweet.retweetCount,
    }
    tweets.append(tweet_data)
    if i > 1000:
        break
