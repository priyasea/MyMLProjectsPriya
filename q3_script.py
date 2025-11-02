import pickle
from fastapi import FastAPI
import uvicorn
from typing import Dict, Any, Literal
from pydantic import BaseModel, Field,ConfigDict





app = FastAPI(title="lead_scoring")


with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

datapoint = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

print(pipeline.predict_proba(datapoint)[0, 1])
