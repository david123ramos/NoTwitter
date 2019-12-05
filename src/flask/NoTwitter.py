import pandas as pd
import demoji
import nltk
from cucco import Cucco

downloaded = False

if not downloaded:
    nltk.download('stopwords')
    nltk.download('rslp')
    downloaded = True




stopwordsnltk = nltk.corpus.stopwords.words('portuguese')


data = pd.read_csv('EmotionsDataset.csv')


def returnBase(arr1, arr2):
    base = []
    tup = []
    index = 0

    for texto in arr1:
        tup.append(texto)
        tup.append(arr2[index])
        index += 1
        base.append(tuple(tup))
        tup = []
    return base


texto = data['Texto'].values
emocoes = data['Emoção'].values

base = returnBase(texto, emocoes)


def fazstemmer(texto):
    """
    Deixa apenas os radicais das palavras
    """
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming


frasescomstemming = fazstemmer(base)


def buscapalavras(frases):
    """
    Busca as palavras nas frases e separa das emoções
    """
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras


palavras = buscapalavras(frasescomstemming)


def buscafrequencia(palavras):
    """
    Define a frequência que as palavras aparecem no banco de dados
    """
    palavras = nltk.FreqDist(palavras)
    return palavras


frequenciatreinamento = buscafrequencia(palavras)


def busca_palavrasunicas(frequencia):
    """
    Cria um dicionário de palavras únicas
    """
    freq = frequencia.keys()
    return freq


palavrasunicas = busca_palavrasunicas(frequenciatreinamento)


def extraipalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas


basecompleta = nltk.classify.apply_features(extraipalavras, frasescomstemming)
classificador = nltk.NaiveBayesClassifier.train(basecompleta)


def classify(tweet):

    tweetstem = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrastreinamento) in tweet.split():
        comstem = [p for p in palavrastreinamento.split()]
        tweetstem.append(str(stemmer.stem(comstem[0])))


    nova_frase = extraipalavras(tweetstem)

    emotionsDict = {0:"tristeza", 1:"alegria", 2:"amor", 3:"raiva"}

    distribuicao = classificador.prob_classify(nova_frase)  
    emotions = []

    for classe in distribuicao.samples():    
        emotions.append(distribuicao.prob(classe))

    return emotionsDict[emotions.index(max(emotions))]

def classify_demo(tweet):

    tweetstem = []
    stemmer = nltk.stem.RSLPStemmer()
    for (palavrastreinamento) in tweet.split():
        comstem = [p for p in palavrastreinamento.split()]
        tweetstem.append(str(stemmer.stem(comstem[0])))


    nova_frase = extraipalavras(tweetstem)

    #emotionsDict = {0:"tristeza", 1:"alegria", 2:"amor", 3:"raiva"}

    distribuicao = classificador.prob_classify(nova_frase)  
    emotions = []

    for classe in distribuicao.samples():    
        emotions.append(distribuicao.prob(classe))

    return emotions

