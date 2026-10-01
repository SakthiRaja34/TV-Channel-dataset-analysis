import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🎓 Student Result Analysis System")  

# Student Details
name = st.text_input("Enter Student Name")
roll_no = st.text_input("Enter Roll Number")

st.subheader("Enter Marks")

m1 = st.number_input("Python", min_value=0, max_value=100)
m2 = st.number_input("Java", min_value=0, max_value=100)
m3 = st.number_input("Database", min_value=0, max_value=100)
m4 = st.number_input("Web Technology", min_value=0, max_value=100)
m5 = st.number_input("AI", min_value=0, max_value=100)

if st.button("Analyze Result"):

    total = m1 + m2 + m3 + m4 + m5
    percentage = total / 5

    # Grade Calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    if min(m1, m2, m3, m4, m5) >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    st.success("Result Generated Successfully!")

    st.write("### Student Information")
    st.write("Name:", name)
    st.write("Roll No:", roll_no)

    st.write("### Performance Summary")
    st.write("Total Marks:", total)
    st.write("Percentage:", round(percentage, 2), "%")
    st.write("Grade:", grade)
    st.write("Result:", result)

    # DataFrame
    df = pd.DataFrame({
        "Subject": ["Python", "Java", "Database", "Web Technology", "AI"],
        "Marks": [m1, m2, m3, m4, m5]
    })

    st.write("### Subject-wise Marks")
    st.dataframe(df)

    st.write("### Marks Visualization")
    st.bar_chart(df.set_index("Subject"))