import streamlit as st
import pickle
import os
import numpy as np

# Debugging path file
st.write("Direktori Saat Ini:", os.getcwd())
st.write("File dalam Direktori:", os.listdir())

# Periksa apakah scikit-learn terpasang
try:
    import sklearn
except ModuleNotFoundError:
    st.error("Modul 'scikit-learn' tidak ditemukan. Silakan pasang dengan perintah 'pip install scikit-learn'.")

# Verifikasi dan memuat model
milkquality_model_path = 'milkquality_model.pkl'
scaler_model_path = 'Scaler.pkl'
if os.path.exists(milkquality_model_path) and os.path.exists(scaler_model_path):
    with open(milkquality_model_path, 'rb') as f:
        milkquality = pickle.load(f)
    with open(scaler_model_path, 'rb') as f:
        scaler = pickle.load(f)
else:
    st.error(f"File model tidak ditemukan: {milkquality_model_path} atau {scaler_model_path}")

# Judul aplikasi web
st.title("Prediksi Kualitas Susu")

# Membagi kolom input
col1, col2 = st.columns(2)

with col1:
    pH = st.text_input("pH")
    if pH != '':
        pH = float(pH)  # Konversi ke float

with col2:
    Temperatur = st.text_input("Temperature")
    if Temperatur != '':
        Temperatur = float(Temperatur)  # Konversi ke float

with col1:
    Rasa = st.text_input("Taste (0=bad, 1=good)")
    if Rasa != '':
        Rasa = float(Rasa)  # Konversi ke float

with col2:
    Bau = st.text_input("Odor (0=bad, 1=good)")
    if Bau != '':
        Bau = float(Bau)  # Konversi ke float

with col1:
    Lemak = st.text_input("Fat (0=bad, 1=good)")
    if Lemak != '':
        Lemak = float(Lemak)  # Konversi ke float

with col2:
    Kekeruhan = st.text_input("Turbidity (0=bad, 1=good)")
    if Kekeruhan != '':
        Kekeruhan = float(Kekeruhan)  # Konversi ke float

with col1:
    Warna = st.text_input("Color")
    if Warna != '':
        Warna = float(Warna)  # Konversi ke float

# Kode prediksi
Prediksi_Susu = ''
if st.button("Prediksi Kualitas Susu SEKARANG"):
    try:
        # Scaling fitur input numerik
        scaled_features = scaler.transform([[pH, Temperatur]])
        
        # Menggabungkan semua fitur menjadi satu array
        features = np.array([scaled_features[0][0], scaled_features[0][1], Rasa, Bau, Lemak, Kekeruhan, Warna]).reshape(1, -1)
        
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
