import numpy as np
import joblib
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Membaca model prediksi anemia
dtree = joblib.load('milkquality_model.sav')

# Membaca model scaler
scaler = joblib.load('Scaler.sav')

# Membaca Label Encoder
le = joblib.load('le.sav')

# Judul web
st.title('Prediksi Kualitas Susu')

# Menampilkan hasil prediksi
pH_input = st.text_input('Input Nilai pH')
Temprature_input = st.text_input('Input nilai Temprature ')
Taste_input = st.text_input('Input Taste ')
Odor_input = st.text_input('Input nilai Odor')
Colour_input = st.text_input('Input nilai Colour')
Lemak_input = st.text_input('Input nilai Lemak')
Turbidity_input = st.text_input('Input nilai Turbidity')

# Validasi input
if pH_input.strip() and Temprature_input.strip() and Taste_input.strip() and Odor_input.strip() and Colour_input.strip() and Lemak_input.strip() and Turbidity_input.strip():
    pH = float(pH_input)
    Temprature = float(Temprature_input)
    Taste = float(Taste_input)
    Odor = float(Odor_input)
    Colour = float(Colour_input)
    Lemak = float(Lemak_input)
    Turbidity = float(Turbidity_input)

    # Code untuk prediksi
    # Membuat tombol untuk prediksi
    if st.button('Test Prediksi Kualitas Susu'):
        input_data = np.array([pH, Temprature, Taste, Odor, Colour, Lemak, Turbidity]).reshape(1, -1)
        milkquality_prediction = dtree.predict(input_data)

        # Menampilkan hasil prediksi
if Prediksi_Susu[0] == 0:
            Prediksi_Susu = "high"
        elif Prediksi_Susu[0] == 1:
            Prediksi_Susu = "low"
        elif Prediksi_Susu[0] == 2:
            Prediksi_Susu = "medium"
        else:
            Prediksi_Susu = "tidak ditemukan jenis kualitas susu"
else:
    st.warning('Mohon lengkapi semua kolom input.')
