#Movie Sentiment Analysis

import re 
from sklearn import naive_bayes
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle


#Reading into Python


reviews_train = []

for line in open('Datasets/aclImdb/movie_data/full_train.txt','r',encoding='utf-8'):
    reviews_train.append(line.strip())
    
reviews_test = []


for line in open('Datasets/aclImdb/movie_data/full_test.txt','r',encoding='utf-8'):
    reviews_test.append(line.strip())
    

#Data Cleaning


REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE =re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

def preprocess_reviews(reviews):
    
    reviews = [REPLACE_NO_SPACE.sub("",line.lower()) for line in reviews]
    reviews = [REPLACE_WITH_SPACE.sub(" ", line) for line in reviews]
    
    
    return reviews

 
reviews_train_clean = preprocess_reviews(reviews_train)
reviews_test_clean = preprocess_reviews(reviews_test)


#Normalization

def get_lemmatized_text(corpus):
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    return [' '.join([lemmatizer.lemmatize(word) for word in review.split()]) for review in corpus]

lemmatized_reviews = get_lemmatized_text(reviews_train_clean)
lemmatized_reviews_test = get_lemmatized_text(reviews_test_clean)



ngram_vectorizer = CountVectorizer(binary=True, ngram_range=(1, 2))
ngram_vectorizer.fit(lemmatized_reviews)
X = ngram_vectorizer.transform(lemmatized_reviews)
X_test = ngram_vectorizer.transform(lemmatized_reviews_test)


target = [1 if i < 12500 else 0 for i in range(25000)]

X_train, X_val, y_train, y_val = train_test_split(
    X, target, train_size = 0.75
)

for c in [0.01, 0.05, 0.25, 0.5, 1]:
    
    lr = LogisticRegression(C=c)
    lr.fit(X_train, y_train)
    print ("Accuracy for C=%s: %s" 
           % (c, accuracy_score(y_val, lr.predict(X_val))))


final_lr_ngram = LogisticRegression(C=0.5)
final_lr_ngram.fit(X, target)

# save the model to disk
lrModel = 'finalized_model_LR.sav'
pickle.dump(final_lr_ngram, open(lrModel, 'wb'))
 
# load the model from disk
loaded_model = pickle.load(open(lrModel, 'rb'))
print ("Final Accuracy of Logistic Regression: %s" 
       % accuracy_score(target, final_lr_ngram.predict(X_test)))


   
#SVM


final_svm_ngram = LinearSVC(C=0.5)
final_svm_ngram.fit(X, target)

# save the model to disk
svmModel = 'finalized_model_SVM.sav'
pickle.dump(final_svm_ngram, open(svmModel, 'wb'))
 
# load the model from disk
loaded_model = pickle.load(open(svmModel, 'rb'))
print ("Final Accuracy of support vector Machine: %s" 
       % accuracy_score(target, final_svm_ngram.predict(X_test)))


#Naive Bayes
      
nb = naive_bayes.MultinomialNB()
nb.fit(X,target) 
# save the model to disk
naiveModel = 'finalized_model_Naive.sav'
pickle.dump(nb, open(naiveModel, 'wb'))

 
# load the model from disk
loaded_model = pickle.load(open(naiveModel, 'rb'))

print("Final Accuracy Naive Bayes: %s" %
      accuracy_score(target,loaded_model.predict(X_test)))



 
