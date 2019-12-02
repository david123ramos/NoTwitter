import tweepy, time, json, nltk
from cucco import Cucco
from ibge import Municipio
from pyUFbr.baseuf import ufbr

t = Municipio(ufbr.get_cidade('Blumenau').codigo)

print (t)

# f = open("arq.txt", "w")

# consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
# consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
# access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
# access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B'

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)



# query = "MasterChef"
# maxCount = 20
# max_id = -1
# count = 0

# while count < maxCount:
#     if max_id <= 0:
#         searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*5)
#     else:
#         searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*5, max_id=str(max_id - 1))
#     if not searched_tweets:
#         print("tem nada aq mona") 
#         break
#     else:
#         for tweet in searched_tweets:
#             if (tweet.place is not None) and (count < maxCount):
#                 text = json.dumps(tweet._json['full_text'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8').decode()
#                 if not 'https://' in text:
#                     finalText = text.split(" ")
#                     text = ""
#                     for aux in finalText:
#                         if not '@' in aux:
#                             text += aux + " "

#                     count += 1
#                     f.write(json.dumps(tweet._json['user']['screen_name'], sort_keys=True, indent=4))
#                     f.write("\n")
#                     text = Cucco.replace_emojis(text)
#                     f.write(text.replace('"', ''))
#                     f.write("\n")
#                     f.write((json.dumps(tweet._json['place']['full_name'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode())
#                     f.write("\n")
#                     f.write("\n")
#                     print(tweet.id)

#     max_id = searched_tweets[-1].id
