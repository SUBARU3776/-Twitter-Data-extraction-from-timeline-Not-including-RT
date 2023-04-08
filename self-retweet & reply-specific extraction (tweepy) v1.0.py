import tweepy
import pandas as pd
from datetime import datetime, timezone, timedelta
import time 

# Set authentication information
consumer_key = 'Your Consumer Key'
consumer_secret = 'Your Secret Consumer Key'
access_token = 'Your Access Token Key'
access_token_secret = 'Your Secret Access Token Key'

# Configuration to handle OAuth authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create an instance to use Twitter API
api = tweepy.API(auth)

# Perform a word search
all_tweets = []
query = '@_SUBARU_3776_'

# Extraction stops at 1,000 cases.
max_tweets = 1000
while len(all_tweets) < max_tweets:
    tweets = api.search_tweets(q=query, 
                        count=200,
                        lang='ja',
                        tweet_mode='extended',
                        max_id=all_tweets[-1].id - 1 if all_tweets else None
                       )
    if not tweets:
        break
    all_tweets.extend(tweets[:min(max_tweets - len(all_tweets), 100)])
    time.sleep(5) # Idle for 5 seconds between
    
# Retrieve information from the tweet and add it to the data frame
data = pd.DataFrame(data=[[tweet.id, tweet.created_at.astimezone(timezone(timedelta(hours=+9))), tweet.user.id, tweet.user.name, tweet.full_text.replace('\n', ' '), tweet.retweeted_status.id_str if hasattr(tweet, 'retweeted_status') else None] for tweet in all_tweets], columns=['tweet_id', 'created_at', 'user_id', 'user_name', 'tweet_text', 'retweeted_id'])


# Save as CSV file (with time stamp)
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
file_name = f"tweepy_{query}_{timestamp}.csv"
data.to_csv(file_name, index=False)

# Show 5 lines of saved files
saved_data = pd.read_csv(file_name)
print(saved_data.head())
print(f"Tweets saved to file: {file_name}")
