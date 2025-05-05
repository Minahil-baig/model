import streamlit as st
import joblib
import numpy as np
import os

model_path = 'rf_model_trained.joblib'

if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

rf_model_trained = joblib.load(model_path)
print("Model loaded:", rf_model_trained)

# Optional: test predict to verify it's fitted
try:
    rf_model_trained.predict([[7, 200, 10000, 250, 300, 0.3, 150, 200, 6.5]])
    print("Model is trained and can predict.")
except Exception as e:
    print("ERROR: Loaded model is not trained:", e)
# Load the trained model
rf_model_trained = joblib.load('rf_model_trained.joblib')

# Streamlit UI
st.title("Water Quality Classification")
st.write("This app classifies whether a water sample is safe or not.")
pH = st.number_input("pH Level (6.5 - 8.5)")
Hardness = st.number_input("Hardness (<= 300 mg/L)")
Solids = st.number_input("Solids (<= 500 mg/L)")
Chloramines = st.number_input("Chloramines (<= 4 mg/L)")
Sulfate = st.number_input("Sulfate (<= 250 mg/L)")
Conductivity = st.number_input("Conductivity (<= 500 µS/cm)")
Organic_carbon = st.number_input("Organic Carbon (<= 5 mg/L)")
Trihalomethanes = st.number_input("Trihalomethanes (<= 80 µg/L)")
Turbidity = st.number_input("Turbidity (<= 1 NTU)")

# Prediction
if st.button("Predict"):
    features = np.array([[pH, Hardness, Solids, Chloramines, Sulfate,
                          Conductivity, Organic_carbon, Trihalomethanes, Turbidity]])
    prediction = rf_model_trained.predict(features)
    if 6.5 <= pH <= 8.5 and Solids <= 500 and Hardness <= 300:
        st.success("Water is Safe to Drink")
    else:
        st.error("Water is NOT Safe to Drink ")