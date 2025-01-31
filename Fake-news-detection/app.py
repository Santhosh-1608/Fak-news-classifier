from flask import Flask, jsonify, request, render_template
from predictionModel import PredictionModel
import pandas as pd
from random import randrange

import nltk


nltk.download('averaged_perceptron_tagger')



app = Flask(__name__, static_folder="./public/static", template_folder="./public")

@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    model = PredictionModel(request.json)
    return jsonify(model.predict())


@app.route('/random', methods=['GET'])
def random():
    data = pd.read_csv("data/fake_or_real_news_test.csv")
    index = randrange(0, len(data)-1, 1)
    return jsonify({'title': data.loc[index].title, 'text': data.loc[index].text})



# Only for local running
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

