from fastapi import APIRouter, HTTPException
from typing import List
from schema.patient import Patient
from model.patient_repo import load_patients, save_patients

router = APIRouter()

@router.get("/patients", response_model=List[Patient])
def get_all_patients():
    return load_patients()

@router.get("/patients/{pid}", response_model=Patient)
def get_patient(pid: int):
    patients = load_patients()
    for p in patients:
        if p["id"] == pid:
            return p
    raise HTTPException(status_code=404, detail="Patient not found")

@router.put("/patients/{pid}", response_model=Patient)
def update_patient(pid: int, patient: Patient):
    patients = load_patients()
    for i, p in enumerate(patients):
        if p["id"] == pid:
            patients[i] = patient.dict()
            save_patients(patients)
            return patients[i]
    raise HTTPException(status_code=404, detail="Patient not found")

@router.delete("/patients/{pid}")
def delete_patient(pid: int):
    patients = load_patients()
    new_patients = [p for p in patients if p["id"] != pid]
    if len(patients) == len(new_patients):
        raise HTTPException(status_code=404, detail="Patient not found")
    save_patients(new_patients)
    return {"detail": "Deleted"}
