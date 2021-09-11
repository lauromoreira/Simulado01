from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def anime():
    dados = requests.get('https://nekos.best/api/v1/nekos').json()
    print(dados)
    return render_template('index.html', fotos = dados['url'], nome = dados['artist_name'])


if __name__ == '__main__':
    app.run()
