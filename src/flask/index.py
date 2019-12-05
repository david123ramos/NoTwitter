import tweepy, time, json, nltk
from cucco import Cucco
from ibge import Municipio
from pyUFbr.baseuf import ufbr
from NoTwitter import classify
import regioes
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials


f = open("arq.txt", "w")

consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B'

#FIRE BASE
cred = credentials.Certificate("NoTwitterKeys.json")
firebase_admin.initialize_app(cred)


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



def searchTweets(query):
    db = firestore.client()
    maxCount = 100
    max_id = -1
    count = 0

    obj = {
    query : {
        "regioes": {
        "Norte": {
            "tristeza": 0,
            "alegria": 0,
            "amor": 0,
            "raiva": 0
        },
        "Nordeste": {
            "tristeza": 0,
            "alegria": 0,
            "amor": 0,
            "raiva": 0
        },
        "Centro-Oeste": {
            "tristeza": 0,
            "alegria": 0,
            "amor": 0,
            "raiva": 0
        },
        "Sul": {
            "tristeza": 0,
            "alegria": 0,
            "amor": 0,
            "raiva": 0
        },
        "Sudeste": {
            "tristeza": 0,
            "alegria": 0,
            "amor": 0,
            "raiva": 0
        }
        }
    }
    }

    other_obj = {
    "regioes": {
        "Norte": {
        "tristeza": 0,
        "alegria": 0,
        "amor": 0,
        "raiva": 0,
        "count": 0
        },
        "Nordeste": {
        "tristeza": 0,
        "alegria": 0,
        "amor": 0,
        "raiva": 0,
        "count": 0
        },
        "Centro-Oeste": {
        "tristeza": 0,
        "alegria": 0,
        "amor": 0,
        "raiva": 0,
        "count": 0
        },
        "Sul": {
        "tristeza": 0,
        "alegria": 0,
        "amor": 0,
        "raiva": 0,
        "count": 0
        },
        "Sudeste": {
        "tristeza": 0,
        "alegria": 0,
        "amor": 0,
        "raiva": 0,
        "count": 0
        }
    }
    }

    users_ref = db.collection(query)
    docs = users_ref.stream()

    jsonT = ""
    for doc in docs:
        jsonT = doc.to_dict()["porcentagem"]
    if jsonT == "":
        while count < maxCount:
            if max_id <= 0:
                searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*5)
            else:
                searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*5, max_id=str(max_id - 1))
            if not searched_tweets:
                print("tem nada aq mona") 
                break
            else:
                for tweet in searched_tweets:
                    if (tweet.place is not None) and (count < maxCount):
                        text = json.dumps(tweet._json['full_text'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8').decode()
                        finalText = text.split(" ")
                        text = ""
                        for aux in finalText:
                            if not '@' in aux and not 'https://' in aux:
                                text += aux + " "

                        count += 1
                        text = Cucco.replace_emojis(text)
                        text = text.replace('"', '')
                        municipio = (json.dumps(tweet._json['place']['full_name'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode().split(",")[0].replace('"',"")
                        
                        try:
                            if municipio == 'Sao Paulo':
                                municipio = 'São Paulo'
                            regiao = regioes.getRegion(ufbr.get_cidade(municipio).codigo)
                            em = classify(text)
                            other_obj["regioes"][regiao][em] +=1
                            other_obj["regioes"][regiao]["count"] +=1
                            pass
                        except Exception as identifier:
                            count -= 1
                            pass

            max_id = searched_tweets[-1].id

        arr_reg = ["Norte", "Nordeste", "Centro-Oeste", "Sul", "Sudeste"]
        arr_emo = ["tristeza", "alegria", "amor", "raiva"]
        for i in arr_reg:
            for j in arr_emo:
                total = other_obj["regioes"][i]["count"]
                if total == 0:
                    obj[query]["regioes"][i][j] = 0
                else :
                    obj[query]["regioes"][i][j] = round((other_obj["regioes"][i][j] / total) * 100, 2)

        db.collection(query).add({ "tweets_classificados": json.dumps(other_obj), "porcentagem" : json.dumps(obj) })
        objs = [obj, other_obj]
        return objs

    else:
        users_ref = db.collection(query)
        docs = users_ref.stream()

        jsonP = ""
        for doc in docs:
            jsonP = doc.to_dict()["porcentagem"]
            jsonT = doc.to_dict()["tweets_classificados"]

            arr = [json.loads(jsonP), json.loads(jsonT)]

        return arr