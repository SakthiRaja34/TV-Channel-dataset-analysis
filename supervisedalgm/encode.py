import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Read the dataset
data = pd.read_csv("encode.csv")

# Encode all columns
encoder = LabelEncoder()
for column in data.columns:
    data[column] = encoder.fit_transform(data[column])

# Features and target
X = data[["Performance", "Attendance", "StudyLevel"]]
y = data["Result"]

# Create and train the model
model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# Test data
test = [[1, 2, 2]]

# Predict
prediction = model.predict(test)

# Calculate accuracy
y_prediction = model.predict(X)
accuracy = accuracy_score(y, y_prediction)

# Display results
print("Prediction:", prediction[0])
print("Accuracy:", accuracy)