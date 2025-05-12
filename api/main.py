from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from .predict_pipeline import predict

app = FastAPI()


class InputData(BaseModel):
    mean_radius: Optional[float] = None
    mean_texture: Optional[float] = None
    mean_perimeter: Optional[float] = None
    mean_area: Optional[float] = None
    mean_smoothness: Optional[float] = None
    mean_compactness: Optional[float] = None
    mean_concavity: Optional[float] = None
    mean_concave_points: Optional[float] = None
    mean_symmetry: Optional[float] = None
    mean_fractal_dimension: Optional[float] = None
    radius_error: Optional[float] = None
    texture_error: Optional[float] = None
    perimeter_error: Optional[float] = None
    area_error: Optional[float] = None
    smoothness_error: Optional[float] = None
    compactness_error: Optional[float] = None
    concavity_error: Optional[float] = None
    concave_points_error: Optional[float] = None
    symmetry_error: Optional[float] = None
    fractal_dimension_error: Optional[float] = None
    worst_radius: Optional[float] = None
    worst_texture: Optional[float] = None
    worst_perimeter: Optional[float] = None
    worst_area: Optional[float] = None
    worst_smoothness: Optional[float] = None
    worst_compactness: Optional[float] = None
    worst_concavity: Optional[float] = None
    worst_concave_points: Optional[float] = None
    worst_symmetry: Optional[float] = None
    worst_fractal_dimension: Optional[float] = None


@app.get("/")
def root():
    return {"message": "ML model is live!"}


@app.post("/predict")
def predict_readmission(data: InputData):
    input_dict = data.dict()
    result = predict(input_dict)
    return result

