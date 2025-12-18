FROM python:3.11-slim

WORKDIR /app

# Needed for LightGBM / XGBoost
RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*

# Install API dependencies
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy API code
COPY api/app.py .

# Copy trained model
COPY models /app/models

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
