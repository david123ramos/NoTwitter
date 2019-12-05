from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/pesquisa', methods=['POST' ,])
def pesquisa():
    return request.form['query']


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)