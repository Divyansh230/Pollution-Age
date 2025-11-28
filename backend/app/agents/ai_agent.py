from langgraph.graph import StateGraph, END
import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def lung_age_ai_agent(real_age, lung_age):
    prompt = f"""
    User age: {real_age}
    Pollution-adjusted Lung Age: {lung_age}

    Explain in emotional + scientific way why their lungs are aging faster.
    Give friendly advice, motivation, and lifestyle tips.
    """
    response = genai.GenerativeModel("gemini-2.5-flash").generate_content(prompt)
    return response.text
