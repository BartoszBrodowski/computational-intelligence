import snscrape.modules.twitter as sntwitter

# Use snscrape to get 100 recent tweets with the #Ukraine hashtag
max_results = 100
tweets = []
for i, tweet in enumerate(sntwitter.TwitterSearchScraper("#Ukraine").get_items()):
    if i >= max_results:
        break
    tweets.append(tweet)

# Print out each tweet
for tweet in tweets:
    print(tweet.content)
