import numpy as np
from app.ml.model_loader import ml_model

def predict_lung_age(real_age):
    default_inputs = np.array([[real_age, 210, 180, 230, 42, 20, 1.1, 25, 45, 3]])
    prediction = ml_model.predict(default_inputs)[0]
    return round(prediction, 1)
