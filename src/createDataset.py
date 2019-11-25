import tweepy, time, json, nltk, pandas as pd



consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

emotions = {1:"tristeza", 2:"raiva", 3:"frustração", 4:"alegria", 5:"humor", 6:"amor", 7:"esperança", 8:"entusiasmo", 9:"neutro"}
data = []

query = "c"
maxCount = 10
max_id = -1
count = 0
print(emotions)
print("\n\n")
while count < maxCount:
    if max_id <= 0:
        searched_tweets = api.search(q=query+" -filter:retweets",lang="pt-br" ,tweet_mode='extended', count=maxCount)
    else:
        searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br" ,tweet_mode='extended', count=maxCount, max_id=str(max_id - 1))
    if not searched_tweets:
        print("tem nada aq mona") 
        break
    else:
        
        for tweet in searched_tweets:
            if (tweet.place is not None) and (count < maxCount):
                count += 1
                text = (json.dumps(tweet._json['full_text'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode()
                print(text)
                index = int(input("classifique: "))
                aux = [text, emotions[index]]
                data.append(aux)
                print(tweet.id)

    max_id = searched_tweets[-1].id
df = pd.DataFrame(data, columns=['Texto', 'Emoção'])
print(df)
with open('EmotionsDataset.csv', 'a') as dataset:
    df.to_csv(dataset, header=False)