from pydantic import BaseModel

class PredictRequest(BaseModel):
    name: str
    email: str
    phone: str
    age: int
    sex: int
    dataset: int
    cp: int
    trestbps: float
    chol: float
    fbs: int
    restecg: int
    thalch: float
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int


class Patient(PredictRequest):
    id: int
    prediction: int
    risk: str
    confidence: float = None

