from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("models/ranker.pkl")

@app.post("/recommend")
def recommend(user_features):
    scores = model.predict(np.array([user_features]))
    return {"score": float(scores[0])}
