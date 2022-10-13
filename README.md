
# Spam Classification

>Project status : Active and Version : 1.00


## Table of content :
* **Project intro**

        1. General info

        2. Skills Required

        3. Technologies used

        4. Setup

        5. Dataset



* **Project Description**
* **Codes and technical aspects**
* **Deployment**
* **Credits and My intro**

# 1. Project introduction

## General info

This project creates the machine learning model that helps us to predict whether the given text message is spam or not.

## Skills Required

   * Programming Language - Python 

   * Machine Learning

   * Natural language processing

   * Predictive modeling

   * etc.


## Technologies used

This project is created using [**python**](https://www.python.org/) and other libraries like :

* [Pandas](https://pandas.pydata.org/)
* [Numpy](https://numpy.org/)
* [Sklearn/Scikit-Learn](https://scikit-learn.org/stable/#)
* [NLTK](https://www.nltk.org/)
* etc.

<img height='300' width='300' src="https://user-images.githubusercontent.com/85100877/143047907-f5b9f36f-35d9-41b9-8bfe-d9ed224bf642.png">


The other libraries are enlisted in the [requirements.txt](requirements.txt) file.

## Setup

 
To run this project , install [**python**](https://www.python.org/) locally and install the requirements using [pip](https://pypi.org/project/pip/) or [conda](https://docs.conda.io/en/latest/) -

```terminal
	pip install -r requirements.txt
```

else you can use the [google colab notebook](Spam_Classifier.ipynb) for running the code online without installing any libraries , packages and dependencies.

<img height='300' width='800' src='https://user-images.githubusercontent.com/85100877/143045414-3468cf84-395e-4ad5-8f2c-cc7ab878b3f7.png'>


## Dataset


The dataset used in this project is available in [Kaggle](https://www.kaggle.com/uciml/sms-spam-collection-dataset)

The SMS Spam Collection is a set of SMS tagged messages that have been collected for SMS Spam research. It contains one set of SMS messages in English of 5,574 messages, tagged acording being ham (legitimate) or spam.

The files contain one message per line. Each line is composed by two columns: v1 contains the label (ham or spam) and v2 contains the raw text.

<img width="374" alt="image" src="https://user-images.githubusercontent.com/85100877/143047742-fa19a55b-b1a4-4e9c-acf7-22ca0b61a2d5.png">




# 2.Project Description



# 3.Codes and Technical aspects

This project is entirely based on the machine learning and Natural language processing.

For that , we will be using **Python** Language as it is suitable and contains various libraries and packages  , and has easy syntax.
Alternatively , **R** language can also be used.

The pie-chart of value counts is as :  
<img height='400' width='400' src='https://user-images.githubusercontent.com/85100877/149865604-b7a8ab5f-1d34-4ef2-95e3-7f7e6bd6ddc1.png'>

The data is highly imbalanced , so we need to slice it to make it balanced.  
The pie-chart of balanced data is :  
<img height='400' width='400' src='https://user-images.githubusercontent.com/85100877/149865785-2c84df94-394a-4efb-b744-f251f5fa49eb.png'>



The word cloud of spam messages is as : 

<img height='400' width='400' src='https://user-images.githubusercontent.com/85100877/149865894-c8a4ceae-9c8a-4644-ab40-e69bccf84b8a.png'>


The word cloud of ham messages is as :

<img height='400' width='400' src='https://user-images.githubusercontent.com/85100877/149865924-d40947f5-6f8a-4848-983d-4a14d3deb9e9.png'>  

For running the project , python must be installed in your local system.
The required packages and libraries are listed in [requirements.txt](requirements.txt).

You can also use **Google-Colab** . **Colaboratory**, or “Colab” for short, is a product from Google Research. Colab allows anybody to write and execute arbitrary python code through the browser, and is especially well suited to machine learning, data analysis and education.
The colab notebook is also uploaded here.


The code simply contains multiple parts :

First of all ,we have to import all the required libraries like nltk, sklearn , etc.

And then , we have to import our dataset which contains the messages with the label of spam or not spam.

We have our dataset in the **csv** format . The v2 column contains message and v1 contains label.
We import our data using **pandas** library and save as the dataframe. 
We slice the dataset to make it balanced.

The message we have in our dataset might not be clean . So we have to remove some unwanted stuffs like stopwords (i.e. "just" ,"is","oh","an" ,etc. ) and we also have to reduce the word into the word root form ( i.e. playing,plays,played to play, ).
we can do it so by using **Lamatization process**. The **NLTK** library provides the tool for that.


After this , we have to convert the words into vectors because the machine learning algorithm can't be directly fed with strings or characters . To we have to convert the sentences into vectors (i.e. numeric matrix )
This process is called feature extraction.
There are multiple tools for that like **Countvectorizer ,TF-IDF, word2vec**,etc. 
We are here using **TF-IDF** which is one of the widely used one.


Then , we split the dataset into training and testing (in the ratio of 7:3).

In the machine learning part , we are using **Multinomial Naive Baye's** algorithm to create a model.
This model preforms better in these cases and is also economical (in the case of time , memory and computational cost) than others.

We create an object of Multinomial Naive Baye`s algorithm and train it using the training dataset( both messages and labels ).


we predict the value for the testing messages (at this time only messages are passed not their labels) and compare with the original value/labels .
By this the proformance of the model is analyzed using various metrices like accuracy , confusion matrix , classification report , etc.


If the performance of the model is good . The model is ready to use and can be saved. 
Else the model needs to be re-trained ( by using another algorithm or by parameter tuning .)


Both model and the vectorizer needs to be saved for the deployment or future use.




# 4.Deployment

Hence , the model is created using machine learning . The model needs to be deployed for its practical use.

We create a Web-App using the [Flask](https://flask.palletsprojects.com/en/2.0.x/). 

![image](https://user-images.githubusercontent.com/85100877/143044908-a797ef8b-cfd6-41fe-a33f-390eb16c9111.png)

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.


The sample Deployment web page looks like :: 
![image](https://user-images.githubusercontent.com/85100877/150265296-5e6baaec-2684-433e-962d-dcf080ba6900.png)


# 5. Credits and My intro

This project is entirely based on the Machine Learning Algorithms and Natural Language Processing.

This project is created by : me.

## *About Me*

Myself ( Nitish Pandey )....  
I am currently pursuating graduation in Bachelor of Technology ( B.Tech ) from Kalinga Institute of Industrial Technology (KIIT), Bhuwaneswor- (2020-24).    

I am a Machine Learning enthusiast and Competitive programmer ,  
doing various projects in Machine Learning / Data Science and learning competitive programming .   

## Skills I acquire :  
    * Programming Language ( C/C++ and Python )

    * Data Science and Machine Learning ( along with Deep Learning ) 

    * Problem Solving ( Competitive Programming and Algorithms )

    * And Various SoftCore Skills ( like critical thinking ,time management , Project Management , Communications Skill , etc. )





Feel free to contact me :  
  
Github : [@nitish-pandey](https://www.github.com/nitish-pandey)  
Linked In : [nitish-pandey-250b84224](https://www.linkedin.com/in/nitish-pandey-250b84224/)  
Instagram : [@n.pand3y](http://www.instagram/n.pand3y)
