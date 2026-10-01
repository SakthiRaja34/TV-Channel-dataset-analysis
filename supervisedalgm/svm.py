import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Step 1: Create dataset
data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7, 8],
    'Attendance': [50, 55, 60, 65, 70, 75, 80, 85],
    'Result': [0, 0, 0, 0, 1, 1, 1, 1]  # 0 = Fail, 1 = Pass
}

df = pd.DataFrame(data)

# Step 2: Split input and output
X = df[['StudyHours', 'Attendance']]
y = df['Result']

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 4: Create SVM model
model = SVC(kernel='linear')  # you can try 'rbf' also

# Step 5: Train model
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 8: Test with new data
new_student = [[10, 30]]  # StudyHours=10, Attendance=30
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")