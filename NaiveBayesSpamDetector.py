# -*- coding: utf-8 -*-
"""
Naive Bayes Spam detector
"""

import pandas as pd

df = pd.read_table('SMSSpamCollection',
                   sep ='\t',
                   header=None, 
                   names=['label','message'])


#converting string label into binary
df['label'] =df.label.map({'ham':0,'spam':1})

# converting every character of message to lowercase

df['message'] = df.message.map(lambda x: x.lower())

# removing any punctuation   
"""
i didn't got the replace('[^/w/s],'')
"""
df['message'] = df.message.str.replace('[^\w\s]', '')  


"""
Tokenize the msg into single words using nltk
"""

import nltk

df['message'] =df['message'].apply(nltk.word_tokenize)

"""
Performing some word stemming. The idea of stemming is to normalize our text for 
all variation of words carry the same meaning, regardless of the tense.

Using Porter Stemming one of the must popular algorithm
"""

from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

df['message'] = df['message'].apply(lambda x: [stemmer.stem(y) for y in x])  

"""
Finally, we will transform the data into occurrences, 
which will be the features that we will feed into our model:
"""

from sklearn.feature_extraction.text import CountVectorizer

# This converts the list of words into space-separated strings
df['message'] = df['message'].apply(lambda x: ' '.join(x))

count_vect = CountVectorizer()  
counts = count_vect.fit_transform(df['message'])  


"""
We could leave it as the simple word-count per message, but it is better 
to use Term Frequency Inverse Document Frequency, more known as tf-idf:
"""

from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer().fit(counts)

counts = transformer.transform(counts)  


"""
Training the Model
Now that we have performed feature extraction from our data, it is time 
to build our model. We will start by splitting 
our data into training and test sets
"""
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(counts, df['label'], test_size=0.1, random_state=69) 


"""
Then, all that we have to do is initialize 
the Naive Bayes Classifier and fit the data.
 For text classification problems, 
the Multinomial Naive Bayes Classifier is well-suited:
"""

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB().fit(X_train, y_train)  


"""
Evaluating the Model
Once we have put together our classifier,
 we can evaluate its performance in the testing set:
"""

import numpy as np

predicted = model.predict(X_test)

print(np.mean(predicted == y_test))  


"""
 But it is not enough by just providing the accuracy, 
 since our dataset is imbalanced when it comes to the labels 
 (86.6% legitimate in contrast to 13.4% spam). It could happen that 
 our classifier is over-fitting the legitimate
 class while ignoring the spam class.
 To solve this uncertainty, let's have a look at the confusion matrix:
"""

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predicted))  