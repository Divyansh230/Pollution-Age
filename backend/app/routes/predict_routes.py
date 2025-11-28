from fastapi import APIRouter
from app.schemas.predict_schema import AgeInput
from app.ml.predictor import predict_lung_age
from app.agents.ai_agent import lung_age_ai_agent

router = APIRouter()

@router.post("/predict")
def get_lung_age(data: AgeInput):
    real_age = data.age
    lung_age = predict_lung_age(real_age)
    ai_message = lung_age_ai_agent(real_age, lung_age)

    return {
        "real_age": real_age,
        "pollution_lung_age": lung_age,
        "age_difference": round(lung_age - real_age, 1),
        "ai_analysis": ai_message
    }
