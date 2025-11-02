import pickle
from fastapi import FastAPI
import uvicorn
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field,ConfigDict


app = FastAPI(title="lead_scoring")


with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict_leadscore")
def predict_leadscore(customer: Dict[str, Any]):
    prob = predict_single(customer)

    return {
        "converted_probability": prob,
        "converted": bool(prob >= 0.5)
    }