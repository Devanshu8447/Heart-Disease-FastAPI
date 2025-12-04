import json
from config import settings
import os

def load_patients():
    if not os.path.exists(settings.DATA_FILE):
        with open(settings.DATA_FILE, "w") as f:
            json.dump([], f)
    with open(settings.DATA_FILE, "r") as f:
        return json.load(f)

def save_patients(patients):
    with open(settings.DATA_FILE, "w") as f:
        json.dump(patients, f, indent=2)
