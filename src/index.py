import tweepy, time, json

f = open("arq.txt", "w")

consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B '

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweepy.StreamListener



query = "Biroliro"
maxCount = 1000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(maxCount)]
# print(json.dumps(searched_tweets, sort_keys=True, indent=4))


for i in searched_tweets:
    print(i)
    f.write(json.dumps(i._json['text'], sort_keys=True, indent=4))
    f.write("\n")


