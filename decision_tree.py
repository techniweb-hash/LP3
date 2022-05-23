import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

read_file = pd.read_csv("/decision_tree_data.csv")
read_file.to_csv("decision_tree_data.csv", index=None)
data = pd.read_csv("decision_tree_data.csv")

x = data.iloc[:,1:-1]
y = data.iloc[:,5].values


labelencoder = LabelEncoder()

x=x.apply(LabelEncoder().fit_transform)

classifier = DecisionTreeClassifier(criterion="entropy")
classifier.fit(x,y)

inp = np.array([1,1,0,0])
y_pred = classifier.predict([inp])
print(y_pred)