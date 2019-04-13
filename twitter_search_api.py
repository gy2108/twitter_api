import twitter, requests

twitter_api = twitter.Api(consumer_key="VCLpKHiZffcrMMQJYIQ5BLH6E",
    consumer_secret="MrPpMZU687qOAoAnjYrQfiTOOinAnWO7G4yWBgEpnTmBuGg77f",
    access_token_key="1016050483125895168-94Wv1TAPEjYkqMq6OqKkPnRHRlbJOI",
    access_token_secret="aty7SzQxjsRR6SAR8bRnwfysbOhR7xV1HqLGY1Ugvv8S3")

# print(twitter_api.VerifyCredentials())
my_tweets = twitter_api.GetUserTimeline(screen_name='gy2108',count=5)

tweets = [tweet.AsDict() for tweet in my_tweets]

for tweet in tweets:
    print(tweet['text'])

help(twitter_api.GetUserTimeline)