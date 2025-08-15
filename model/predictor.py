import joblib
import numpy as np
from typing import Dict, Any
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "dt_clf_model.pkl"

class ModelWrapper:
    def __init__(self):
        # self.model = None
        # self.version = "1.0.0"
        if MODEL_PATH.exists():
            try:
                self.model = joblib.load(MODEL_PATH)
                self.version = getattr(self.model, "version")
            except Exception as e:
                # fallback to rule-based
                self.model = None

    def predict(self, features: Dict[str, Any]):
        """
        Return fraudulent(bool), probability(float)
        If a pickled sklearn-like model exists, call model.predict_proba(X)
        Otherwise run a deterministic heuristic.
        """
        if self.model is not None:
            features_order = sorted(features.keys())
            X = np.array([[features[k] for k in features_order]])

            try:
                probs = self.model.predict_proba(X)
                prob = float(probs[0, 1]) if probs.shape[1] > 1 else float(probs[0, 0])
                return prob >= 0.5, prob, self.version
            except Exception:
                pred = self.model.predict(X)
                prob = float(pred[0])
                return bool(pred[0]), prob, self.version

        # Heuristic fallback:
        prob = self.heuristic_score(features)
        return prob >= 0.5, prob, self.version

    def heuristic_score(self, f: Dict[str, Any]) -> float:
        """
        Simple rule-based scoring to use until an actual model is supplied.
        YOU SHOULD REPLACE with your trained model.
        """
        score = 0.0
        # feature-based heuristics
        if f.get("InscClaimAmtReimbursed", 0) > 10000:
            score += 0.4
        if f.get("IPAnnualReimbursementAmt", 0) > 10000:
            score += 0.25
        if f.get("TotalClaims", 0) > 200:
            score += 0.2
        if f.get("DeductibleAmtPaid", 0) == 0 and f.get("InscClaimAmtReimbursed", 0) > 0:
            score += 0.05
        # chronic condition count weight
        cc = f.get("ChronicConditionCount", f.get("ChronicConditionCount", 0))
        score += min(cc / 50.0, 0.1)
        # clamp
        return max(0.0, min(1.0, score))


# create singleton wrapper to avoid reloading on each request
_model_wrapper = ModelWrapper()

def predict(features: Dict[str, Any]):
    fraudulent, prob, version = _model_wrapper.predict(features)
    return {"fraudulent": fraudulent, "probability": prob, "model_version": version}
