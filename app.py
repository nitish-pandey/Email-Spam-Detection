# Imports 

import nltk 

import pandas as pd
import numpy as np
import re
import joblib
from flask import Flask ,render_template,request
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer,PorterStemmer

# Load the model and vectorizer
encoder=joblib.load('Resources/vectorizer.pkl')
model=joblib.load('Resources/mymodel.pkl')

# load the lemmatizer and stopwords
lematizer=WordNetLemmatizer()
stops=set(stopwords.words('english'))

# Basic functions for data cleaning and preprocessing

def process(data):
    data=re.sub('[^a-zA-Z]'," ",data)
    data=data.lower()
    data=data.split()
    data=[lematizer.lemmatize(word) for word in data if word not in set(stops)]
    data=" ".join(data)
    return data


app = Flask(__name__)
@app.route('/')

def hello():
    return render_template('index.html')


@app.route('/',methods=['GET','POST'])
def predict():
    data=request.form['message']
    data=[process(data)]
    vector=encoder.transform(data).toarray()
    pred=model.predict(vector)
    
    if pred:
        return render_template('spam.html')

    else:
        return render_template('safe.html')

  

if __name__=='__main__':
  app.run(debug=True)