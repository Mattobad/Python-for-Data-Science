# -*- coding: utf-8 -*-
"""
Movie Sentiment Analysis
"""

"""
Reading into Python
"""
reviews_train = []

for line in open('Datasets/aclImdb/movie_data/full_train.txt','r',encoding='utf-8'):
    reviews_train.append(line.strip())
    
reviews_test = []


for line in open('Datasets/aclImdb/movie_data/full_test.txt','r',encoding='utf-8'):
    reviews_test.append(line.strip())
    
"""
Data Cleaning
"""

import re 

REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE =re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    
    reviews = [REPLACE_NO_SPACE.sub("",line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
    
    
    return reviews

 
reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)



"""
Vectorization -> converting each review to a numeric representation
"""


from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(binary=True)

cv.fit(reviews_train_clean)
X = cv.transform(reviews_train_clean)
X_test = cv.transform(reviews_test_clean)


"""
Build Classifier
"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

target = [1 if i < 12500 else 0 for i in range(25000)]

X_train,X_val, y_train, y_val = train_test_split(
        X, target, train_size = 0.75 )

for c in [0.01,0.05,0.25,0.5,1]:
    
    lr = LogisticRegression(C=c)
    lr.fit(X_train,y_train)
    
    print("Accuracy for C=%s : %s"% (c,accuracy_score(y_val,lr.predict(X_val))))
    
    
    
"""
Train Final Model
"""

final_model = LogisticRegression(C=0.05)

final_model.fit(X,target)

print("Final Accuracy: %s" %
      accuracy_score(target,final_model.predict(X_test)))

"""
5 most discriminating words for both positive and negative words
"""

feature_to_coef = {
        word: coef for word, coef in zip(
                cv.get_feature_names(),final_model.coef_[0])
        }

for best_positive in sorted(
        feature_to_coef.items(),
        key=lambda x: x[1],
        reverse=True)[:5]:
        print(best_positive)
        
        
for best_negative in sorted(
        feature_to_coef.items(),
        key =lambda x:x[1])[:5]:
        print(best_negative)
        
#Naive Bayes
        
from sklearn import naive_bayes

nb = naive_bayes.MultinomialNB()
nb.fit(X,target) 
print("Final Accuracy: %s" %
      accuracy_score(target,nb.predict(X_test)))
    
#SVM

from sklearn.svm import LinearSVC

final_svm_ngram = LinearSVC(C=0.01)
final_svm_ngram.fit(X, target)
print ("Final Accuracy: %s" 
       % accuracy_score(target, final_svm_ngram.predict(X_test)))