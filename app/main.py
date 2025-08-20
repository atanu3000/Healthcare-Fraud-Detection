from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schema.schemas import PredictInput, PredictionResponse
from config.utils import prepare_features
from model.predictor import predict as model_predict
import time

app = FastAPI(title="Healthcare Fraud Detection API", version="1.0.1")

# Allow requests from your frontend origin
origins = [
    "http://localhost:8080",
    "https://medguard-ai.vercel.app",
    # add more origins here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

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
        payload_dict = payload.model_dump()
        features = prepare_features(payload_dict)
        res = model_predict(features)
        confidence = int(round(res["probability"] * 100))
        if res["fraudulent"]:
            msg = f"Alert: This claim is likely fraudulent. Confidence: {confidence}%"
        else:
            msg = f"This claim appears normal. Confidence: {confidence}%"
        response = PredictionResponse(
            fraudulent=res["fraudulent"],
            probability=res["probability"],
            model_version=res.get("model_version", "unknown"),
            message=msg
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
