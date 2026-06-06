from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI()

with open("churn_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.get("/")
def home():
    return {"message": "Customer Churn API Running"}

class CustomerChurn(BaseModel):
    gender: str
    SeniorCitizen: int
    Partner: str
    Dependents: str
    tenure: int
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float


@app.post("/predict")
def predict(customer: CustomerChurn):

    try:
        df = pd.DataFrame([customer.model_dump()])

        print("\n" + "=" * 50)
        print("INPUT DATAFRAME")
        print("=" * 50)
        print(df)

        print("\n" + "=" * 50)
        print("DTYPES")
        print("=" * 50)
        print(df.dtypes)

        print("\n" + "=" * 50)
        print("NULL VALUES")
        print("=" * 50)
        print(df.isnull().sum())

        print("\n" + "=" * 50)
        print("MODEL TYPE")
        print("=" * 50)
        print(type(model))

        print("\n" + "=" * 50)
        print("PREPROCESSOR")
        print("=" * 50)
        print(model.named_steps['preprocessor'])

        # Test preprocessing separately
        print("\n" + "=" * 50)
        print("TESTING PREPROCESSOR")
        print("=" * 50)

        transformed = model.named_steps['preprocessor'].transform(df)

        print("Transformation successful!")
        print("Transformed shape:", transformed.shape)

        prediction = model.predict(df)

        return {
            "prediction": "Yes" if prediction[0] == 1 else "No"
        }

    except Exception as e:
        import traceback

        print("\n" + "=" * 50)
        print("FULL ERROR")
        print("=" * 50)
        print(traceback.format_exc())

        return {
            "error": str(e)
        }