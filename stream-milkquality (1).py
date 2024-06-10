import streamlit as st
import pickle
import os

# Verifikasi dan memuat model
file_path = 'milkquality_model.sav'
if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        milkquality model = pickle.load(open('/path/to/your/file/milkquality_model.sav', 'rb'))
else:
    st.error(f"File not found: {file_path}")

# judul web
st.title('Prediksi Milk Quality')

# membagi Kolom
col1, col2 = st.columns(2)

with col1:
    pH = st.text_input("pH")
    if pH != '':
        pH = float(pH)  # Convert to float
with col2:
    Temprature = st.text_input("Temperature")
    if Temprature != '':
        Temprature = float(Temprature)  # Convert to float
with col1:
    Taste = st.text_input("Taste")
    if Taste != '':
        Taste = float(Taste)  # Convert to float
with col2:
    Odor = st.text_input("Odor")
    if Odor != '':
        Odor = float(Odor)  # Convert to float
with col1:
    Lemak = st.text_input("Fat")
    if Lemak != '':
        Lemak = float(Lemak)  # Convert to float
with col2:
    Turbidity = st.text_input("Turbidity")
    if Turbidity != '':
        Turbidity = float(Turbidity)  # Convert to float
with col1:
    Colour = st.text_input("Color")
    if Colour != '':
        Colour = float(Colour)  # Convert to float

# Prediction code
Prediksi_Susu = ''
if st.button("Prediksi Kualitas Susu SEKARANG"):
    # Scaling numerical input features
    scaled_features = scaler.transform([[pH, Temprature]])
    
    # Combining all features into a single array
    features = np.array([scaled_features[0][0], scaled_features[0][1], Taste, Odor, Lemak, Turbidity, Colour]).reshape(1, -1)
    
    # Making prediction with Decision Tree
    Prediksi_Susu = milkquality.predict(features)
    
    # Interpreting the prediction result
    if Prediksi_Susu[0] == 0:
        Prediksi_Susu = "high"
    elif Prediksi_Susu[0] == 1:
        Prediksi_Susu = "low"
    elif Prediksi_Susu[0] == 2:
        Prediksi_Susu = "medium"
    else:
        Prediksi_Susu = "tidak ditemukan jenis kualitas susu"

st.success(Prediksi_Susu)
        CustomerCredit_prediksi = 'Customer dengan History Kredit yang Baik'
    else:
        CustomerCredit_prediksi = 'Customer dengan History Kredit yang Buruk'
        
    st.success(CustomerCredit_prediksi)
