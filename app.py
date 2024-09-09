import streamlit as st
import pickle
import numpy as np

# Load the ridge regressor model and the standard scaler
ridge_model = pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/scaler.pkl', 'rb'))

# Title of the app
st.title('FWI Prediction')

# Input fields
Temperature = st.text_input('Enter Temperature', value="")
RH = st.text_input('Enter RH', value="")
Ws = st.text_input('Enter Wind Speed (Ws)', value="")
Rain = st.text_input('Enter Rain', value="")
FFMC = st.text_input('Enter FFMC', value="")
DMC = st.text_input('Enter DMC', value="")
ISI = st.text_input('Enter ISI', value="")
Classes = st.text_input('Enter Classes', value="")
Region = st.text_input('Enter Region', value="")

# Prediction
if st.button('Predict'):
    if Temperature and RH and Ws and Rain and FFMC and DMC and ISI and Classes and Region:
        new_data = np.array([[float(Temperature), float(RH), float(Ws), float(Rain),
                              float(FFMC), float(DMC), float(ISI), float(Classes), float(Region)]])
        new_data_scaled = standard_scaler.transform(new_data)
        result = ridge_model.predict(new_data_scaled)
        st.success(f'The FWI prediction is: {result[0]}')
    else:
        st.error('Please provide values for all inputs.')

