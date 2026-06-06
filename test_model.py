import pickle
import pandas as pd

with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)

data = {
    "gender": "Male",
    "SeniorCitizen": 0,
    "Partner": "Yes",
    "Dependents": "No",
    "tenure": 24,
    "PhoneService": "Yes",
    "MultipleLines": "No",
    "InternetService": "DSL",
    "OnlineSecurity": "Yes",
    "OnlineBackup": "No",
    "DeviceProtection": "Yes",
    "TechSupport": "No",
    "StreamingTV": "No",
    "StreamingMovies": "No",
    "Contract": "One year",
    "PaperlessBilling": "Yes",
    "PaymentMethod": "Electronic check",
    "MonthlyCharges": 65.5,
    "TotalCharges": 1572.0
}

df = pd.DataFrame([data])

print(df.dtypes)

prediction = model.predict(df)

print(prediction)