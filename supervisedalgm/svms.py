import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

# Load dataset
df = pd.read_csv("student_data.csv")

# Input and Output
X = df[["Study_Hours"]]
y = df["Result"]

# Train SVM Model
model = SVC(kernel="linear")
model.fit(X, y)

# User Input
hours = float(input("Enter Study Hours: "))
prediction = model.predict([[hours]])

print("Prediction:", prediction[0])

# Plot Data
plt.figure(figsize=(8,5))

# Plot Fail students
plt.scatter(df[df["Result"]=="Fail"]["Study_Hours"],
            [0]*len(df[df["Result"]=="Fail"]),
            color="red", label="Fail", s=100)

# Plot Pass students
plt.scatter(df[df["Result"]=="Pass"]["Study_Hours"],
            [1]*len(df[df["Result"]=="Pass"]),
            color="green", label="Pass", s=100)

# Decision Boundary
x = np.linspace(df["Study_Hours"].min(), df["Study_Hours"].max(), 100).reshape(-1,1)
y_pred = model.predict(x)

boundary = []
for value in y_pred:
    if value == "Fail":
        boundary.append(0)
    else:
        boundary.append(1)

plt.plot(x, boundary, color="blue", linewidth=2, label="Decision Boundary")

# User Input Point
if prediction[0] == "Fail":
    plt.scatter(hours, 0, color="black", s=150, marker="*", label="New Student")
else:
    plt.scatter(hours, 1, color="black", s=150, marker="*", label="New Student")

plt.yticks([0,1], ["Fail","Pass"])
plt.xlabel("Study Hours")
plt.ylabel("Result")
plt.title("SVM Classification")
plt.legend()
plt.grid(True)

plt.show()