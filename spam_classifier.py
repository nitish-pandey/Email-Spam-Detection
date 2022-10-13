# -*- coding: utf-8 -*-
"""Spam Classifier.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GoYrMTUGnj7eb4WeXIQ1pyV24nEpEHHZ

## Table of contents

1. Basic Imports

2. Data Loading and Visualization

3. Data Cleaning

4. Feature Extraction

5. Machine-Learning Implementation

6. Save and Reuse [ For Deployment ]

# 1. Basic Imports
"""

import os
from os import remove
import pandas as pd
import numpy 
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import re

import wordcloud

from wordcloud import WordCloud ,STOPWORDS, ImageColorGenerator

"""NLTK"""

import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.stem import WordNetLemmatizer,PorterStemmer

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

from sklearn.naive_bayes import GaussianNB,MultinomialNB

"""# 2. Data Loading and Visualization"""

# loading the data

dataset=pd.read_csv(r'/content/spam.csv',encoding='latin-1')
dataset.iloc[:10,:2]

# showing value counts of ham and spam
dataset['v1'].value_counts()

"""Pie-Chart"""

# Visualizing the count of spam and ham messages in pie-chart

plt.figure(figsize=(15,15))
plt.title('Spam or Ham Counts in PIE-Chart')
plt.pie(dataset['v1'].value_counts(),labels=dataset['v1'].unique(),explode=[0,0.3],autopct='%1.2f%%',colors=['green','red'])
plt.savefig('pie1.png',dpi=400,bbox_inches='tight')
plt.plot()

"""Balancing the Imbalanced data"""

spams=dataset[dataset['v1']=='spam'].copy()
hams=dataset[dataset['v1']=='ham'].copy()

data=pd.concat([spams,hams[:1000]],axis=0)
data[:5],data[-5:]

data=data.sample(frac=1)
data=data.reset_index()
data=data.drop(['index'],axis=1)
data[:10]

# Visualizing the count of spam and ham messages in pie-chart after balancing the data

plt.figure(figsize=(15,15))
plt.title('Spam or Ham Counts in PIE-Chart')
plt.pie(data['v1'].value_counts(),labels=data['v1'].unique(),explode=[0,0.3],autopct='%1.2f%%',colors=['green','red'])
plt.savefig('pie2.png',dpi=400,bbox_inches='tight')
plt.plot()

"""Wordcloud"""

text = ' '.join(spams['v2'].astype(str).tolist())
stop = set(wordcloud.STOPWORDS)
    
fig_wordcloud = wordcloud.WordCloud(stopwords=stop,background_color='lightgrey',
                colormap='viridis', width=800, height=600).generate(text)
    
plt.figure(figsize=(20,14), frameon=True)
plt.imshow(fig_wordcloud)  
plt.axis('off')
plt.title('Spam Messages', fontsize=20 )
plt.savefig('wordcloud1.png',dpi=400,bbox_inches='tight')
plt.show()

text = ' '.join(hams['v2'].astype(str).tolist())
stop = set(wordcloud.STOPWORDS)
    
fig_wordcloud = wordcloud.WordCloud(stopwords=stop,background_color='lightgrey',
                    colormap='viridis', width=800, height=600).generate(text)
    
plt.figure(figsize=(20,14), frameon=True)
plt.imshow(fig_wordcloud)  
plt.axis('off')
plt.title('Ham messages', fontsize=20 )
plt.savefig('wordcloud2.png',dpi=400,bbox_inches='tight')
plt.show()

"""Removing Null entries and duplicate rows"""

dataset.dropna(inplace=True)
dataset.drop_duplicates(inplace=True)
dataset.reset_index(inplace=True)
dataset.shape

X=data['v2']
y=data['v1']

y=pd.get_dummies(y,drop_first=True)
print(y.head())

"""# 3. Data Cleaning"""

#stopwords of english language
stopword=set(stopwords.words('english'))

lematizer=WordNetLemmatizer()

n,=X.shape
n

# Data Cleaning

def clean(X):

    # replacing all characters except alphabets with space
    temp=re.sub('[^a-zA-Z]',' ',X)

    # Lowering all the characters
    temp=temp.lower()

    # Splitting the sentences into set of words
    temp=temp.split()

    # lemmatize the word if it is not present in stopwords
    temp=[lematizer.lemmatize(word) for word in temp if word not in set(stopword)]

    #Joining the Lemmatized words with space
    temp=' '.join(temp)

    # Returning the cleaned sentences
    return temp

for i in range(len(X)):
    X[i]=clean(X[i])

X[:3]

"""# 4. Feature Extraction"""

# Vocabulary size
voc_size=5000

# Maximum sentence length
sent_len=15

tfidf=sklearn.feature_extraction.text.TfidfVectorizer(max_features=voc_size)

tfidf.fit(X)

encoded=tfidf.transform(X)

encoded[:3]

"""Splitting the Dataset into training and testing"""

# splitting the data in ratio of 70 : 30 

X_train,X_test,y_train,y_test=train_test_split(encoded,y,test_size=0.3)

from sklearn.naive_bayes import MultinomialNB

"""# 5.Machine learning implementation"""

# Using Multinomial naive bayes
model=MultinomialNB()

model.fit(X_train,y_train)

"""Performance Analysis"""

y_pred =model.predict(X_test)
report=classification_report(y_test,y_pred)
matrix=confusion_matrix(y_test,y_pred)
print('Classification Report : \n',classification_report(y_test,y_pred))

"""Confusion Matrix"""

plt.figure(figsize=(10,10))
plt.title('Confusion Matrix')
sns.heatmap(matrix,annot=True,cmap='Blues',cbar=False)
plt.xlabel('Predicted Label')
plt.ylabel('Actual Label')
plt.savefig('matrix.png',dpi=400,bbox_inches='tight')

"""# 6. Saving the Model"""

import joblib

# Saving the Model using joblib
joblib.dump(model,'mymodel.pkl')

# saving the tfidf vectorizer using joblib
joblib.dump(tfidf,'tfidf.pkl')

!pip freeze > requirements.txt

"""#Reusing """

encoder=joblib.load('tfidf.pkl')
mymodel=joblib.load('mymodel.pkl')

def process(data):
    data=re.sub('[^a-zA-Z]'," ",data)
    data=data.lower()
    data=data.split()
    data=[lematizer.lemmatize(word) for word in data if word not in set(stopword)]
    data=" ".join(data)
    return data

def predict(data):
    data=[process(word ) for word in data]
    data=encoder.transform(data)
    pred=mymodel.predict(data)
    return pred


data=[input()]


predict(data)