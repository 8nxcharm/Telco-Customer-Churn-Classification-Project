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
def predict(data: CustomerData):
    try:
        # Convert input to DataFrame
        df = pd.DataFrame([data.dict()])

        # 🔥 FIX: Rename columns to EXACT training names
        df = df.rename(columns={
            "senior_citizen": "SeniorCitizen",
            "partner": "Partner",
            "dependents": "Dependents",
            "monthly_charges": "MonthlyCharges",
            "total_charges": "TotalCharges",
            "phone_service": "PhoneService",
            "multiple_lines": "MultipleLines",
            "internet_service": "InternetService",
            "online_security": "OnlineSecurity",
            "online_backup": "OnlineBackup",
            "device_protection": "DeviceProtection",
            "tech_support": "TechSupport",
            "streaming_tv": "StreamingTV",
            "streaming_movies": "StreamingMovies",
            "paperless_billing": "PaperlessBilling",
            "payment_method": "PaymentMethod"
        })

        pred = model.predict(df)[0]

        return {
            "label": "Churn" if pred == 1 else "No Churn"
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
