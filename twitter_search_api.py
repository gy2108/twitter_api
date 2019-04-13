import twitter, requests

twitter_api = twitter.Api(consumer_key="***",
    consumer_secret="***",
    access_token_key="***",
    access_token_secret="***")

# print(twitter_api.VerifyCredentials())
my_tweets = twitter_api.GetUserTimeline(screen_name='gy2108',count=5)

tweets = [tweet.AsDict() for tweet in my_tweets]

for tweet in tweets:
    print(tweet['text'])

help(twitter_api.GetUserTimeline)