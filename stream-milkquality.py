import numpy as np
import joblib
import streamlit as st
from sklearn.preprocessing import MinMaxScaler

# Membaca model prediksi anemia
dtree = joblib.load('milkquality_model.sav')

# Membaca model scaler
scaler = joblib.load('Scaler.sav')


# Judul web
st.title('Prediksi Kualitas Susu')

Sex_input = st.selectbox(
    "Pilih jenis kelamin:",
    ('Laki-Laki', 'Perempuan')
)
gender_mapping = {'Laki-Laki': 1, 'Perempuan': 0}
Sex_y = gender_mapping[Sex_input]

# Menampilkan hasil prediksi
pH_input = st.text_input('Input Nilai pH')
Temprature_input = st.text_input('Input nilai Temprature ')
Taste_input = st.selectbox(
    "Pilih jenis Taste:",
    ('Bad', 'Good')
)
Odor_input = st.selectbox(
    "Pilih jenis Odor:",
    ('Bad', 'Good')
)
Colour_input = st.selectbox(
    "Pilih jenis Colour:",
    ('Alice Blue', 'Ghost White', 'Honeydew', 'Oldlace', 'Snow', 'White', 'Whitesmoke', 'Wildsand', 'grey')
)
Lemak_input = st.selectbox(
    "Pilih jenis Lemak:",
    ('Bad', 'Good')
)
Turbidity_input = st.selectbox(
    "Pilih jenis Turbidity:",
    ('Bad', 'Good')
)


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
   if st.button("Prediksi Kualitas Susu"):

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
