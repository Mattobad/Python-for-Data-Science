# -*- coding: utf-8 -*-
"""
Naive Bayes classification
"""

# Assigning features and label variables
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']

play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']


"""
#Encoding Features

First, you need to convert these string labels into numbers. for example: 'Overcast', 
'Rainy', 'Sunny' as 0, 1, 2. This is known as label encoding. Scikit-learn provides 
LabelEncoder library 
for encoding labels with a value between 0 and one less than the number of discrete classes.

"""

# Import LabelEncoder
from sklearn import preprocessing
#creating labelEncoder
le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
weather_encoded=le.fit_transform(weather)

temp_encoded = le.fit_transform(temp)

label = le.fit_transform(play)

print()
print ("weather encoded values = ",weather_encoded)
print()
print ("temp encoded values = ",temp_encoded)
print()
print ("play encoded values = ",label)



"""
combining both the features(temp, weather) into single variable(list of tuples)
"""

#Combinig weather and temp into single listof tuples
features=zip(weather_encoded,temp_encoded)

for values in features:
    print (values)

"""
Generating the Model
-> Create naive bayes classifier
-> Fit the dataset on classifier
-> perform prediction
"""

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(features,label.reshape(-1,1))

#Predict Output
predicted= model.predict([[0,2]]) # 0:Overcast, 2:Mild
print ("Predicted Value:", predicted)


