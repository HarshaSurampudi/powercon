from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import pickle

app = FastAPI()

pkl_file = open('type_encoder.pkl', 'rb')
type_encoder = pickle.load(pkl_file)
pkl_file.close()

loaded_model = pickle.load(open("finalized_model.sav", 'rb'))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class FeatureSet(BaseModel):
    typ: str
    sales: float
    employees: float
    plant_area: float
    prod_level: float
    prod_hours: float


@app.post("/api/predict")
def predict(fset: FeatureSet):
    fset.typ = type_encoder.transform([fset.typ])[0]
    x = [[fset.typ, fset.sales, fset.employees, fset.plant_area, fset.prod_level, fset.prod_hours]]
    return loaded_model.predict(x)[0]
