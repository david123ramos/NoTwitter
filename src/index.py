import tweepy, time, json, nltk
from cucco import Cucco
from ibge import Municipio
from pyUFbr.baseuf import ufbr
from NoTwitter import classify




try:
    t = Municipio(ufbr.get_cidade('Sao Paulo').codigo)
    print(t.getRegiao())
    pass
except Exception as identifier:
    print(", teste")
    pass


f = open("arq.txt", "w")

consumer_key = 'YJYTGBso0CH1T7Kf1VJAM9Rsy'
consumer_secret = '8Xl4OxLCuOCejmQc4qsNmMwFFkpW56TTMQf1xTMlsjRv0eMga5'
access_token = '940715176348803072-4roZWCSwwuf09pE8Zc60SWEL9qmmOXy'
access_token_secret = 'HLA9NVIimAVtsQKSV5HOWVfSFfz7mj0MXIbJyVaIXFI5B'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



query = " "
maxCount = 500
max_id = -1
count = 0

obj = {
    query: {
        "regioes" : [
            {"Norte": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}]},
            {"Nordeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}]},
            {"Centro-Oeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}]},
            {"Sudeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}]},
            {"Sul": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}]}
        ]
    }
}

other_obj = {
    "regioes" : [
        {"Norte": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}, {"count": ""}]},
        {"Nordeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}, {"count": ""}]},
        {"Centro-Oeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}, {"count": ""}]},
        {"Sudeste": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}, {"count": ""}]},
        {"Sul": [{"tristeza ": ""},{"alegria ": ""},{"amor ": ""},{"raiva ":""}, {"count": ""}]}
    ]
}





while count < maxCount:
    if max_id <= 0:
        searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*3)
    else:
        searched_tweets = api.search(q=query+" -filter:retweets", lang="pt-br", tweet_mode='extended', count=maxCount*3, max_id=str(max_id - 1))
    if not searched_tweets:
        print("tem nada aq mona") 
        break
    else:
        for tweet in searched_tweets:
            if (tweet.place is not None) and (count < maxCount):
                text = json.dumps(tweet._json['full_text'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8').decode()
                if not 'https://' in text:
                    finalText = text.split(" ")
                    text = ""
                    for aux in finalText:
                        if not '@' in aux:
                            text += aux + " "

                    count += 1
                    text = Cucco.replace_emojis(text)
                    text = text.replace('"', '')
                    municipio = (json.dumps(tweet._json['place']['full_name'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode().split(",")[0].replace('"',"")
                    
                    try:
                        if municipio == 'Sao Paulo':
                            municipio = 'São Paulo'
                        regiao = Municipio(ufbr.get_cidade(municipio).codigo).getRegiao()
                        print(municipio)
                        print(regiao)
                        pass
                    except Exception as identifier:
                        count -= 1
                        pass

    max_id = searched_tweets[-1].id










    # f.write(json.dumps(tweet._json['user']['screen_name'], sort_keys=True, indent=4))
    # f.write("\n")
    # f.write(text.replace('"', ''))
    # f.write("\n")
    # f.write((json.dumps(tweet._json['place']['full_name'], sort_keys=True, indent=4, ensure_ascii=False).encode('utf8')).decode())
    # f.write("\n")
    # f.write("\n")