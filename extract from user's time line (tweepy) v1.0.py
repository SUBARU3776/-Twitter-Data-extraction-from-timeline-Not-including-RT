import tweepy
from pandas import DataFrame
from datetime import datetime, timezone, timedelta
import time


# Set your Twitter API key
CK="Your Consumer Key"
CS="Your Secret Consumer Key"
AT="Your Access Token Key"
AS="Your Secret Access Token Key"

# Generating Twitter API Objects
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Specify screen name
user_screen_name = "_SUBARU_3776_"

# Use the API to retrieve the latest 200 tweets
all_tweets = []
new_tweets = api.user_timeline(screen_name=user_screen_name,
                               count=200,
                               include_rts=False,
                               tweet_mode='extended')
all_tweets.extend(new_tweets)
oldest_id = all_tweets[-1].id

while len(new_tweets) > 0:
    new_tweets = api.user_timeline(screen_name=user_screen_name,
                                   count=200,
                                   max_id=oldest_id - 1,
                                   include_rts=False,
                                   tweet_mode='extended')
    all_tweets.extend(new_tweets)
    oldest_id = all_tweets[-1].id - 1
    print(f"{len(all_tweets)} tweets downloaded so far")

# Save acquired tweets to a csv file
now = datetime.now()
timestamp = now.strftime("%Y%m%d%H%M%S")
outtweets = [[tweet.id_str,
              tweet.created_at,
              tweet.favorite_count,
              tweet.retweet_count,
              tweet.full_text.replace('\n', ' ').encode('utf-8').decode('utf-8')]
             for tweet in all_tweets]

df = DataFrame(outtweets, columns=['id', 'created_at', 'favorite_count', 'retweet_count', 'text'])
df.to_csv(f"{user_screen_name}_tweets_{timestamp}.csv", index=False)
df.head(3)
