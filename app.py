import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="AQI Prediction App", layout="centered")
st.title("Air Quality Index (AQI) Prediction")

st.write('Predict the Air Quality Index (AQI) based on input parameters.')
#Load the pre-trained model
model = joblib.load('LR_AQI_Prediction.joblib')

#input fields for the features
pm25 = st.number_input("PM2.5", 0.0, 500.0, 50.0)
pm10 = st.number_input("PM10", 0.0, 500.0, 80.0)
no2 = st.number_input("NO2", 0.0, 300.0, 40.0)
so2 = st.number_input("SO2", 0.0, 300.0, 20.0)
co = st.number_input("CO", 0.0, 10.0, 1.0)
temperature = st.number_input("Temperature (°C)", -30.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 50.0)

input_data = np.array([[pm25, pm10, no2, so2, co, temperature, humidity]])

def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"

if st.button("Predict AQI"):
    prediction = model.predict(input_data)
    st.success(f"Predicted AQI: {round(prediction[0], 2)}")
    st.info(f"AQI Category: {aqi_category(prediction[0])}")