import joblib
import numpy as np
import streamlit as st

model = joblib.load('heart_disease_model.pkl')

st.title("Heart Disease Prediction App")

age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.radio("Sex", ["Male", "Female"])
sex_val = 1 if sex == "Male" else 0
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol (chol)", min_value=100, max_value=600, value=200)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl (fbs)", ["Yes", "No"])
fbs_val = 1 if fbs == "Yes" else 0
restecg = st.selectbox("Rest ECG (restecg)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", min_value=60, max_value=220, value=150)
exang = st.radio("Exercise Induced Angina (exang)", ["Yes", "No"])
exang_val = 1 if exang == "Yes" else 0
oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

if st.button("Predict"):
    data = np.array([[age, sex_val, cp, trestbps, chol, fbs_val, restecg,
                      thalach, exang_val, oldpeak, slope, ca, thal]])
    result = model.predict(data)[0]
    if result == 1:
        st.error("🔴 Heart Disease Present")
    else:
        st.success("🟢 No Heart Disease Detected")
