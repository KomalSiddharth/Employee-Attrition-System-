import streamlit as st
import pickle
import numpy as np
#  load the trained model
model=pickle.load(open("attrition_model.pkl","rb"))
# Streamlit UI
st.title("Employee Attrition Prediction System")
# collect user input
age = st.slider("Age", 18, 60, 30)
monthly_income = st.number_input("Monthly Income ($)", min_value=1000, max_value=20000, value=5000)
job_satisfaction = st.slider("Job Satisfaction (1-5)", 1, 5, 3)
work_life_balance = st.slider("Work-Life Balance (1-5)", 1, 5, 3)
years_at_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)

# predict button
if st.button("Predict Attrition"):
    input_data = np.array([[age, monthly_income, job_satisfaction, work_life_balance, years_at_company]])
    prediction = model.predict(input_data)[0]

    if prediction==1:
        st.error("Employee is likely to leave")
    else:
        st.success("Employee is likely to stay")