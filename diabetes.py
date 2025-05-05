import streamlit as st
import joblib

# Load your trained model
model = joblib.load('diabetes.pkl')

# Function to add a background image using a URL
def add_background_image(url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{url}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
            opacity: 0.7;  /* Optional: Add opacity to the background image for better text visibility */
        }}
        .stTitle, .stSubheader, .stText, .stButton {{
            color: white;  /* Change text color to white for better contrast */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    # Adding the background image URL here
    background_url = "https://img.freepik.com/free-photo/healthcare-medical-concept-world-diabetes-day-14-november_53476-5107.jpg?w=740"
    
    # Call the function to set the background image
    add_background_image(background_url)

    st.title('Diabetes Prediction App')

    st.subheader('Enter your health information:')

    # Input fields for user data
    glucose = st.number_input('Glucose', min_value=0, max_value=300, value=100)
    blood_pressure = st.number_input('Blood Pressure', min_value=0, max_value=200, value=70)
    insulin = st.number_input('Insulin', min_value=0.0, max_value=900.0, value=30.5)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=5.0, value=0.5, format="%.3f")
    age = st.number_input('Age', min_value=1, max_value=120, value=30)

    # Predict button
    if st.button('Predict'):
        input_data = [[glucose, blood_pressure, insulin, dpf, age]]
        prediction = model.predict(input_data)
        result = 'Diabetic' if prediction[0] == 1 else 'Non-Diabetic'
        st.success(f'Prediction Result: {result}')

if __name__ == '__main__':
    main()

