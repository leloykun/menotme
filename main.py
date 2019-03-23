from flask import Flask, request, jsonify, render_template

import _pickle as cPickle
import tensorflow.keras as tfk

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DontTellAnyone'

vectorizer = None
model = None

print("HAS STARTED SAFELY")

def load_model():
  global vectorizer, model
  with open('misc/vectorizer.pkl', 'rb') as f:
    vectorizer = cPickle.load(f)
  model = tfk.models.load_model('misc/menotme_neuralnetwork.h5')

def predict(sentence):
    print(sentence)
    sentence_t = vectorizer.transform([sentence])
    pred = model.predict(sentence_t)
    print(pred)
    return pred[0][0]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['GET', 'POST'])
def query():
    sentence = request.args.get("sentence", None)
    if sentence is None:
        sentence = request.json["sentence"]
    pred = predict(sentence)
    return jsonify(sentence=sentence,
                   decision="true" if pred >= 0.5 else "false")

if __name__ == '__main__':
  load_model()
  print(predict("HAHAHA"))
  app.run(debug=True)
