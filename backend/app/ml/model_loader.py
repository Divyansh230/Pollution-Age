import joblib
from app.config import MODEL_PATH

def load_model():
    model = joblib.load(MODEL_PATH)
    return model

ml_model = load_model()
