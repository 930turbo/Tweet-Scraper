import tweepy
import pandas as pd
from datetime import datetime

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

topic = input("Enter a hashtag or topic to track: ")

# Scraping tweets
tweets = tweepy.Cursor(api.search_tweets,
                       q=topic,
                       lang="en",
                       since_id=2021-01-01).items(100)

# Creating a dataframe with scraped tweets
tweet_list = [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]
tweets_df = pd.DataFrame(data=tweet_list, columns=["Username", "Location", "Text"])

# Saving the dataframe to a CSV file
now = datetime.now()
filename = f"{topic}_{now.year}-{now.month}-{now.day}.csv"
tweets_df.to_csv(filename, index=False)

print(f"Scraped tweets saved to {filename}.")
