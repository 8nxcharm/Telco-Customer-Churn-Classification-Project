# Telco Customer Churn Classification Project

## Overview
This project implements an end-to-end machine learning pipeline to predict customer churn using the Telco Customer Churn dataset. The system includes data normalization, exploratory analysis, multiple classification models, hyperparameter tuning, and deployment using FastAPI and Streamlit.

## Dataset
- Source: Telco Customer Churn Dataset
- Target Variable: `churn` (binary classification)

## Database Design
- Data was normalized into a 3rd Normal Form (3NF) SQLite database.
- Tables include Customer, Billing, Services, Contract, and Churn.
- SQL JOINs were used to reconstruct the modeling dataset.

## Exploratory Data Analysis
- Churn is an imbalanced target.
- Stratified train/test split was used.
- Key findings:
  - Tenure is negatively correlated with churn.
  - Monthly charges are positively correlated with churn.
- Missing values in `total_charges` were imputed using the median.

## Modeling
- Preprocessing:
  - StandardScaler for numerical features
  - One-hot encoding for categorical features
- Baseline model: Logistic Regression
- Advanced models:
  - Ridge
  - Gradient Boosting
  - XGBoost
  - LightGBM
- Experiments included:
  - With and without PCA
  - With and without Optuna hyperparameter tuning
- Evaluation metric: F1-score

## Deployment
- Best model saved using joblib.
- FastAPI used to serve the model.
- Streamlit used for user interaction.
- Application deployed using Docker Compose on a cloud environment.

## How to Run
```bash
docker compose up --build
