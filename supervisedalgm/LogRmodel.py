import pandas as pd

from sklearn.ensemble import RandomForestClassifier

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

data = pd.read_csv('LogRmodel.csv')

encoders = {}

for col in data.columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le   
    print(data[col])

print(encoders)

x = data[['Performance','Attendance','StudyLevel']]
y = data['Result']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=10)
model.fit(x_train, y_train)

sample = [[1,0,1]]

print(sample)

# Predict
prediction = model.predict(sample)

# Decode result
result = encoders['Result'].inverse_transform(prediction)

print("Prediction:", result)