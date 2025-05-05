import streamlit as st
import joblib
import numpy as np
import base64

model = joblib.load('diabetes.pkl')

# Function to set background image
def set_bg(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


model=joblib.load('diabetes.pkl')

def main():
    # Set background image
    set_bg("photos/diabetes.jpg")  # Change filename if needed

    st.title("Check your diabeties ")
    st.subheader("Enter the following health details to check your diabeties")
    Glucose=st.number_input("Choose your glucose from slider",min_value=0.0, max_value=200.00,step=0.1)
    BloodPressure=st.number_input("Choose your blood pressure from slider",min_value=0.0, max_value=150.0,step=0.1)
    Insulin=st.number_input("Choose your insulin level  from slider",min_value=0.0, max_value=900.0,step=0.1)
    DiabetesPedigreeFunction=st.number_input("Choose your dpf from slider",min_value=0.0, max_value=4.0,step=0.1)
    Age=st.number_input("Choose your age from slider",min_value=0.0, max_value=80.0,step=0.1)









    if st.button("Predict"):
        features = [[Glucose, BloodPressure, Insulin, DiabetesPedigreeFunction, Age]]
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error("The model predicts that you may have diabetes.")
        else:
            st.success("The model predicts that you are not likely to have diabetes.")

if __name__ == '__main__':
    main()