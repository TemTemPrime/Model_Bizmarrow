import streamlit as st
import pandas as pd
import joblib  # or pickle depending on how you saved your model

# -----------------------------
# Load your trained model
# -----------------------------
@st.cache_resource
def load_model():
    model = joblib.load("model.pkl")  # change to your model file
    return model

model = load_model()

# -----------------------------
# App Title
# -----------------------------
st.title("Prediction App")
st.write("Enter Title, Town, and State to get prediction")

# -----------------------------
# User Inputs
# -----------------------------
title = st.text_input("Title")
town = st.text_input("Town")
state = st.text_input("State")

# -----------------------------
# Prediction Button
# -----------------------------
if st.button("Predict"):
    if title and town and state:
        
        # Create DataFrame with correct column names
        input_data = pd.DataFrame({
            "title": [title],
            "town": [town],
            "state": [state]
        })

        # Make prediction
        prediction = model.predict(input_data)

        st.success(f"Prediction: ₦{prediction[0]:,.0f}")

    
    else:
        st.warning("Please fill in all fields.")
