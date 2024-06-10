import pickle
import numpy as np
import streamlit as st

# Fungsi untuk memuat file dengan penanganan kesalahan
def load_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        st.error(f"File {file_name} tidak ditemukan. Pastikan file tersebut ada di direktori yang benar.")
        st.stop()
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat file {file_name}: {e}")
        st.stop()

# Muat model yang disimpan dan file lainnya yang diperlukan
milkquality = load_file('milkquality_model.pkl')
scaler = load_file('Scaler.pkl')
le = load_file('le.pkl')

# Judul web
st.title("Prediksi Kualitas Susu dengan Decision Tree")

# Untuk input data
col1, col2 = st.columns(2)
with col1:
    pH = st.text_input("pH")
    if pH:
        pH = float(pH)  # Konversi ke float
with col2:
    Temprature = st.text_input("Temperatur")
    if Temprature:
        Temprature = float(Temprature)  # Konversi ke float
with col1:
    Taste = st.text_input("Rasa")
    if Taste:
        Taste = float(Taste)  # Konversi ke float
with col2:
    Odor = st.text_input("Bau")
    if Odor:
        Odor = float(Odor)  # Konversi ke float
with col1:
    Lemak = st.text_input("Lemak")
    if Lemak:
        Lemak = float(Lemak)  # Konversi ke float
with col2:
    Turbidity = st.text_input("Kekeruhan")
    if Turbidity:
        Turbidity = float(Turbidity)  # Konversi ke float
with col1:
    Colour = st.text_input("Warna")
    if Colour:
        Colour = float(Colour)  # Konversi ke float

# Kode untuk prediksi
Prediksi_Susu = ''
if st.button("Prediksi Kualitas Susu SEKARANG"):
    try:
        # Pastikan semua input telah diisi
        if '' in [pH, Temprature, Taste, Odor, Lemak, Turbidity, Colour]:
            st.error("Mohon isi semua kolom.")
        else:
            # Transformasi input
            fitur_terukur = scaler.transform([[pH, Temprature]])
            fitur_terkode = le.transform([[Taste, Odor, Lemak, Turbidity, Colour]])
            
            # Gabungkan fitur yang sudah diukur dan dikodekan
            fitur_gabungan = np.hstack((fitur_terukur, fitur_terkode))
            
            # Prediksi dengan Decision Tree
            prediksi = milkquality.predict(fitur_gabungan)
            
            # Peta prediksi ke label kualitas
            label_kualitas = {0: "high", 1: "low", 2: "medium"}
            Prediksi_Susu = label_kualitas.get(prediksi[0], "tidak ditemukan jenis kualitas susu")
        
            st.success(Prediksi_Susu)
    except ValueError as e:
        st.error(f"Input tidak valid: {e}")
