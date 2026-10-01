import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("A:\MLWORKOUT\supervisedalgm\data.csv")


x = data[["Marks", "Attendance"]]
y = data["Result"]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = DecisionTreeClassifier()
model.fit(x_train, y_train)


test = [[38, 24]]
prediction = model.predict(test)

y_prediction = model.predict(x)
accuracy = accuracy_score(y, y_prediction)

print("Result:", prediction)
print("Accuracy:", accuracy)