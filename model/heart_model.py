import pickle
import pandas as pd
from config import settings

_model = None

def load_model():
    global _model
    if _model is None:
        with open(settings.MODEL_PATH, "rb") as f:
            _model = pickle.load(f)
    return _model


def predict_with_confidence(features: dict):
    model = load_model()
    feature_names = [
        "age", "sex", "dataset", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalch", "exang", "oldpeak", "slope", "ca", "thal"
    ]
    input_df = pd.DataFrame([[features[name] for name in feature_names]], columns=feature_names)
    pred = int(model.predict(input_df)[0])
    # Use predict_proba for confidence score
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(input_df)[0][pred]   # Confidence of predicted class
    else:
        proba = None
    risk = "High Risk" if pred == 1 else "Low Risk"
    return pred, risk, proba

