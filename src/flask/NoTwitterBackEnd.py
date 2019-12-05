from flask import Flask, render_template, request
from index import searchTweets
from NoTwitter import classify_demo
import json

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/pesquisa', methods=['POST' ,])
def pesquisa():
    data = searchTweets(request.form['query'])
    data[0] = json.dumps(data[0])
    data[1] = json.dumps(data[1])
    data[0] = json.loads(data[0])
    data[1] = json.loads(data[1])
    return render_template('index.html', data=data, q=request.form['query'])

@app.route('/iademo')
def demo():
    return render_template('nlpIndividual.html')

@app.route('/classificador', methods=['POST' ,])
def classificador():
    em = classify_demo(request.form['frase'])
    aux = []
    for i in em:
        aux.append(round(i * 100, 2))

    return render_template('nlpIndividual.html', data=aux, q=request.form['frase'])



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)