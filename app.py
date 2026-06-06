import streamlit as st
import requests

st.title("Customer Churn Prediction")

# ------------------------
# Categorical Inputs
# ------------------------
gender = st.selectbox("Gender", ["Male", "Female"])

senior_citizen = st.selectbox("Senior Citizen", [0, 1])

partner = st.selectbox("Partner", ["Yes", "No"])

dependents = st.selectbox("Dependents", ["Yes", "No"])

phone_service = st.selectbox("Phone Service", ["Yes", "No"])

multiple_lines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])

internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])

online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])

streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

payment_method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# ------------------------
# Numerical Inputs
# ------------------------
tenure = st.number_input("Tenure", min_value=0)

monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

total_charges = st.number_input("Total Charges", min_value=0.0)

# ------------------------
# Predict Button
# ------------------------
if st.button("Predict"):

    data = {
        "gender": gender,
        "SeniorCitizen": senior_citizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error(f"Error: {response.text}")