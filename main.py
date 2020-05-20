def accuracy(y_test,y_pred,limit):
    correct = 0

    length = len(y_pred)
    for i in range(0,length):
        if(abs(y_pred[i]-y_test[i]) <= limit):
            correct += 1
    return ((correct/length)*100)

import pandas as pd
# Importing dataset
dataset = pd.read_csv('t20.csv')
# Attributes Used: Runs,Wickets,Overs,Striker,Non-striker
X = dataset.iloc[:,[7,8,9,12,13]].values
# Attributes Used: Total
y = dataset.iloc[:, 14].values

print(X[0])


# Splitting into Training and Testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



# Training
from sklearn.linear_model import LinearRegression
lin = LinearRegression()
lin.fit(X_train,y_train)



# Testing
y_pred = lin.predict(X_test)
score = lin.score(X_test,y_test)*100
print("R square value:" , score)
print("Accuracy:" , accuracy(y_test,y_pred,20))



import numpy as np
new_prediction = lin.predict(sc.transform(np.array([[103,0,13,50,50]])))
print("Prediction score:" , new_prediction)


import pickle


# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(lin, open(filename, 'wb'))



