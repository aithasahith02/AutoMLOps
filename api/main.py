# This is a dummy API intended to be replaced by the Readmission model 
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    weight: float
    height: float
    Drug_name: str

@app.get("/")
def read_root():
    return {"message": "Dummy Readmission API is live 🚀"}

@app.post("/predict")
def predict(data: InputData):
    return {
        "readmission_risk": "High",  
        "probability": 0.87,         # dummy value
        "input_received": data.dict()
    }

