import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score 

df = pd.read_csv("ftrandom.csv")

x = df[['StudyHours','Attendance']]

y = df['Result']

model = RandomForestClassifier(n_estimators=1000)

model.fit(x, y)

test = [[5,90]]
prediction = model.predict(test)

y_prediction = model.predict(x)
accuracy= accuracy_score(y, model.predict(x))


print("Result: ",prediction)
print("Accuracy:", accuracy)