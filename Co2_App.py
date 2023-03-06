import streamlit as st
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Title
st.title('Predicting the Co2 Emission of a Car')

# Image
st.image('co2.jpg')

# Inputs
engine_size = st.number_input('Engine Size', min_value=0.0, max_value=10.0, value=1.0)
cylinders = st.number_input('Cylinders', min_value=0, max_value=10, value=1)
Fuel_Consumption_Comb = st.number_input('Fuel Consumption Combined', min_value=0.0, max_value=100.0, value=1.0)

# Output
output = model.predict([[engine_size, cylinders, Fuel_Consumption_Comb]])

# Display the output
st.write(' ## The predicted Co2 Emission is: ', round(output[0][0],2))

