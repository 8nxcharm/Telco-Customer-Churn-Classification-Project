from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Telco Customer Churn API")

# Load trained pipeline
model = joblib.load("models/global_best_model.pkl")


# ---- Input schema ----
class Customer(BaseModel):
    gender: str
    senior_citizen: int
    partner: str
    dependents: str

    tenure: int
    monthly_charges: float
    total_charges: float

    phone_service: str
    multiple_lines: str
    internet_service: str
    online_security: str
    online_backup: str
    device_protection: str
    tech_support: str
    streaming_tv: str
    streaming_movies: str

    contract: str
    paperless_billing: str
    payment_method: str


@app.get("/")
def home():
    return {"message": "Telco Customer Churn Prediction API is live"}


@app.post("/predict")
def predict(data: Customer):
    # Convert request to DataFrame
    df = pd.DataFrame([data.dict()])

    # Predict class and probability
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0, 1]

    return {
        "prediction": int(pred),
        "probability": round(float(prob), 4),
        "label": "Churn" if pred == 1 else "No Churn"
    }
