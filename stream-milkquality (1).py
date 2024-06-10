import numpy as np
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler

# Load your scaler and model
scaler = joblib.load('path_to_your_scaler.pkl')  # Adjust the path as needed
milkquality = joblib.load('path_to_your_model.pkl')  # Adjust the path as needed

# Input fields
pH_input = st.text_input("pH")
Temperature_input = st.text_input("Temperature")
Taste_input = st.text_input("Taste")
Odor_input = st.text_input("Odor")
Colour_input = st.text_input("Colour")
Lemak_input = st.text_input("Lemak")
Turbidity_input = st.text_input("Turbidity")

# Validasi input
if (
    pH_input.strip()
    and Temperature_input.strip()
    and Taste_input.strip()
    and Odor_input.strip()
    and Colour_input.strip()
    and Lemak_input.strip()
    and Turbidity_input.strip()
):
    pH = float(pH_input)
    Temperature = float(Temperature_input)
    Taste = float(Taste_input)
    Odor = float(Odor_input)
    Colour = float(Colour_input)
    Lemak = float(Lemak_input)
    Turbidity = float(Turbidity_input)

    # Code untuk prediksi
    # Membuat tombol untuk prediksi
    if st.button("Prediksi Kualitas Susu"):
        try:
            # Scaling fitur input numerik
            scaled_features = scaler.transform([[pH, Temperature]])
            
            # Menggabungkan semua fitur menjadi satu array
            features = np.array([
                scaled_features[0][0], scaled_features[0][1], Taste, Odor, Lemak, Turbidity, Colour
            ]).reshape(1, -1)
            
            # Membuat prediksi dengan Decision Tree
            Prediksi_Susu = milkquality.predict(features)
            
            # Menginterpretasi hasil prediksi
            if Prediksi_Susu[0] == 0:
                Prediksi_Susu = "high"
            elif Prediksi_Susu[0] == 1:
                Prediksi_Susu = "low"
            elif Prediksi_Susu[0] == 2:
                Prediksi_Susu = "medium"
            else:
                Prediksi_Susu = "tidak ditemukan jenis kualitas susu"
            
            st.success(Prediksi_Susu)
        except Exception as e:
            st.error(f"Terjadi kesalahan selama prediksi: {e}")
