import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
data = load_iris() 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Class'] = data.target_names[data.target] 
df.head() 
x = df.iloc[:, :-1].values 
y = df.Class.values
from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
from sklearn.neighbors import KNeighborsClassifier 
knn_classifier = KNeighborsClassifier(n_neighbors=5) 
knn_classifier.fit(x_train, y_train)
predictions = knn_classifier.predict(x_test)
from sklearn.metrics import accuracy_score, confusion_matrix 
print("Testing accuracy Score is : ",
      accuracy_score(y_test, knn_classifier.predict(x_test)))
