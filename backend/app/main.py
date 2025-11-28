from fastapi import FastAPI
from app.routes.predict_routes import router

app = FastAPI(
    title="Pollution Age API",
    description="Predict lung age and explain using Gemini AI",
    version="1.0"
)

app.include_router(router, prefix="/api")
