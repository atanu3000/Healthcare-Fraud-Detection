# app/main.py
from fastapi import FastAPI, HTTPException
from schema.schemas import PredictInput, PredictionResponse
from config.utils import prepare_features
from model.predictor import predict as model_predict
import time

app = FastAPI(title="Healthcare Fraud Detection API", version="0.1.0")

@app.get("/", tags=["root"])
async def root():
    return {"service": "Healthcare Fraud Detection", "status": "running", "version": app.version}

@app.get("/health", tags=["health"])
async def health():
    if not hasattr(app.state, "start_time"):
        app.state.start_time = time.time()
    uptime_seconds = int(time.time() - app.state.start_time)
    return {"status": "ok", "uptime": f"{uptime_seconds} seconds"}

@app.post("/predict", response_model=PredictionResponse, tags=["predict"])
async def predict_endpoint(payload: PredictInput):
    try:
        # payload is already validated and derived fields computed by Pydantic
        payload_dict = payload.dict()
        features = prepare_features(payload_dict)
        res = model_predict(features)
        response = PredictionResponse(
            fraudulent=res["fraudulent"],
            probability=res["probability"],
            model_version=res.get("model_version", "unknown"),
            message="Prediction returned successfully"
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
