import pickle
import numpy as np
import streamlit as st

#load save model
milkquality=pickle.load(open('milkquality_model.pkl','rb'))
scaler=pickle.load(open('Scaler.pkl','rb'))
le=pickle.load(open('le.pkl','rb'))

#judul web
st.title("Prediksi Kualitas Susu dengan Decision Tree")
primaryColor="#F63366"
backgroundColor="#FFFFFF"

#untuk input data
col1, col2=st.columns(2)
with col1:
    pH=st.text_input("pH")
    if pH != '':
        pH = float(pH)  # Konversi ke float
with col2:
    Temprature=st.text_input("Temprature")
    if Temprature != '':
        Temprature = float(Temprature)  # Konversi ke float
with col1:
    Taste=st.text_input("Taste")
    if Taste != '':
        Taste = float(Taste)  # Konversi ke float
with col2:
    Odor=st.text_input("Odor")
    if Odor != '':
        Odor = float(Odor)  # Konversi ke float
with col1:
    Lemak=st.text_input("Lemak")
    if Lemak != '':
        Lemak = float(Lemak)  # Konversi ke float
with col2:
    Turbidity=st.text_input("Turbidity")
    if Turbidity != '':
        Turbidity = float(Turbidity)  # Konversi ke float
with col1:
    Colour=st.text_input("Colour")
    if Colour != '':
        Colour = float(Colour)  # Konversi ke float

#kode untuk predikisi
Prediksi_Susu =''
if st.button("Prediksi Kualitas Susu SEKARANG"):
    # Mengubah argumen menjadi array numpy dua dimensi
    sc=scaler.transform([[pH,Temprature]])
    le=le.transform([[Taste, Odor, Lemak, Turbidity, Colour]])
    # Melakukan prediksi dengan Decison Tree
    Prediksi_Susu = milkquality.predict([[sc[0][0],sc[0][1],le[0][0],le[0][0],le[0][1],le[0][2],le[0][3],le[0][4]]])
    
    if Prediksi_Susu[0]==0:
        Prediksi_Susu ="high"
    elif Prediksi_Susu[0] == 1:
        Prediksi_Susu = "low"
    elif Prediksi_Susu[0] == 2:
        Prediksi_Susu = "medium"
    else:
        Prediksi_Susu = "tidak ditemukan jenis kualitas susu"

st.success(Prediksi_Susu)
