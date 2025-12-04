from fastapi import FastAPI
from api import predict, patients  # Import your API routers
from model.heart_model import load_model

app = FastAPI()  # Create FastAPI instance

# Attach routers with prefixes
app.include_router(predict.router, prefix="/api")
app.include_router(patients.router, prefix="/api")

# Global health and home routes
MODEL_VERSION = "1.0"
model = load_model()


@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API"}


@app.get("/health")
def health_check():
    return {"status": "OK", "version": MODEL_VERSION, "model_loaded": model is not None}
