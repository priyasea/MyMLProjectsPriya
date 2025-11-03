FROM agrigorev/zoomcamp-model:2025

WORKDIR /app

# Install system dependencies and update pip
RUN apt-get update && apt-get install -y build-essential && pip install --upgrade pip

# Install Python packages
RUN pip install fastapi uvicorn scikit-learn


# Copy your FastAPI app
COPY predict_leadscore.py .

EXPOSE 9696

ENTRYPOINT ["uvicorn", "predict_leadscore:app", "--host", "0.0.0.0", "--port", "9696"]
