import tweepy, time, json, nltk

f = open("arq.txt", "w")

consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



query = "egirl"
maxCount = 10
max_id = -1
count = 0

while count < maxCount:
    if max_id <= 0:
        searched_tweets = api.search(q=query+" -filter:retweets", tweet_mode='extended', count=10)
    else:
        searched_tweets = api.search(q=query+" -filter:retweets", tweet_mode='extended', count=10, max_id=str(max_id - 1))
    if not searched_tweets:
        print("tem nada aq mona") 
        break
    else:
        for tweet in searched_tweets:
            if (tweet.place is not None) and (count < maxCount):
                count += 1
                f.write(json.dumps(tweet._json['user']['screen_name'], sort_keys=True, indent=4))
                f.write("\n")
                text = json.dumps(tweet._json['full_text'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')
                f.write(text.decode())
                f.write("\n")
                f.write((json.dumps(tweet._json['place']['full_name'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode())
                f.write("\n")
                f.write("\n")
                print(tweet.id)

    max_id = searched_tweets[-1].id
