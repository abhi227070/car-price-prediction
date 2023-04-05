import streamlit as st
import pickle
import pandas as pd
from PIL import Image
import numpy as np

st.title("Car Price Prediction")

car=Image.open("2022-mclaren-senna-rear-5k-r7.jpg")

st.image(car,"Welcome to car prediction")

data=pd.read_csv("car_dataset.csv")

model=pickle.load(open("car_price.pkl",'rb'))

Fuel_Type = st.selectbox(
    'Fuel Type',
    (data['Fuel_Type'].unique()))
Seller_Type = st.selectbox(
    'Seller Type',
    (data['Seller_Type'].unique()))
Transmission = st.selectbox(
    'Transmission',
    (data['Transmission'].unique()))
Owner = st.selectbox(
    'Owner Number',
    (data['Owner'].unique()))
Year = st.selectbox(
    'Year',
    (data['Year'].unique()))
Kms_Driven = st.number_input('Kms Driven')
Present_Price = st.number_input('Present price')

if st.button("Predict"):
    input1=pd.DataFrame([[Year,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner]],columns=['Year','Present_Price','Kms_Driven','Fuel_Type','Seller_Type','Transmission','Owner'])
    prediction=model.predict(input1)[0]

    st.success(str(np.round(prediction,2))+" (in rupees)")