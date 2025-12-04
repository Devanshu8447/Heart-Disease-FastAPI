from fastapi import APIRouter, HTTPException
from schema.patient import PredictRequest, Patient
from model.heart_model import predict_with_confidence
from model.patient_repo import load_patients, save_patients

router = APIRouter()


@router.post("/predict", response_model=Patient)
def predict_endpoint(req: PredictRequest):
    try:
        prediction, risk, confidence = predict_with_confidence(req.dict())
        patients = load_patients()
        new_id = patients[-1]["id"] + 1 if patients else 1

        patient_record = req.dict()
        patient_record.update(
            {
                "id": new_id,
                "prediction": prediction,
                "risk": risk,
                "confidence": confidence,
            }
        )

        patients.append(patient_record)
        save_patients(patients)
        return patient_record
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal error during prediction: {str(e)}"
        )
