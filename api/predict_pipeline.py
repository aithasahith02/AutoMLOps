import joblib
import numpy as np
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # go up one level from /api/
ARTIFACT_DIR = os.path.join(BASE_DIR, "model", "artifacts")

model = joblib.load(os.path.join(ARTIFACT_DIR, "model.pkl"))
scaler = joblib.load(os.path.join(ARTIFACT_DIR, "scaler.pkl"))
feature_columns = joblib.load(os.path.join(ARTIFACT_DIR, "feature_columns.pkl"))

def preprocess_input(input_dict):
    df = pd.DataFrame([input_dict]) 
    for col in feature_columns:
        if col not in df.columns:
            df[col] = 0
    df = df[feature_columns]
    scaled = scaler.transform(df)
    return scaled

def predict(input_dict):
    X = preprocess_input(input_dict)
    proba = model.predict_proba(X)[0][1]
    pred = int(proba >= 0.5)
    return {
        "prediction": "Positive" if pred else "Negative",
        "probability": round(proba, 4)
    }

