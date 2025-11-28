from pydantic import BaseModel

class AgeInput(BaseModel):
    age: float
