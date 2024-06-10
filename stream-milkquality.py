import pickle
import numpy as np
import streamlit as st

# Load saved model and other necessary files
try:
    milkquality = pickle.load(open('milkquality_model.pkl', 'rb'))
    scaler = pickle.load(open('Scaler.pkl', 'rb'))
    le = pickle.load(open('le.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

# Title of the web app
st.title("Prediksi Kualitas Susu dengan Decision Tree")

# For input data
col1, col2 = st.columns(2)
with col1:
    pH = st.text_input("pH")
    if pH:
        pH = float(pH)  # Convert to float
with col2:
    Temprature = st.text_input("Temprature")
    if Temprature:
        Temprature = float(Temprature)  # Convert to float
with col1:
    Taste = st.text_input("Taste")
    if Taste:
        Taste = float(Taste)  # Convert to float
with col2:
    Odor = st.text_input("Odor")
    if Odor:
        Odor = float(Odor)  # Convert to float
with col1:
    Lemak = st.text_input("Lemak")
    if Lemak:
        Lemak = float(Lemak)  # Convert to float
with col2:
    Turbidity = st.text_input("Turbidity")
    if Turbidity:
        Turbidity = float(Turbidity)  # Convert to float
with col1:
    Colour = st.text_input("Colour")
    if Colour:
        Colour = float(Colour)  # Convert to float

# Code for prediction
Prediksi_Susu = ''
if st.button("Prediksi Kualitas Susu SEKARANG"):
    try:
        # Ensure all inputs are provided
        if '' in [pH, Temprature, Taste, Odor, Lemak, Turbidity, Colour]:
            st.error("Please fill in all the fields.")
        else:
            # Transform inputs
            scaled_features = scaler.transform([[pH, Temprature]])
            encoded_features = le.transform([[Taste, Odor, Lemak, Turbidity, Colour]])
            
            # Combine scaled and encoded features
            combined_features = np.hstack((scaled_features, encoded_features))
            
            # Predict with Decision Tree
            prediction = milkquality.predict(combined_features)
            
            # Map prediction to quality label
            quality_labels = {0: "high", 1: "low", 2: "medium"}
            Prediksi_Susu = quality_labels.get(prediction[0], "tidak ditemukan jenis kualitas susu")
        
            st.success(Prediksi_Susu)
    except ValueError as e:
        st.error(f"Invalid input: {e}")
