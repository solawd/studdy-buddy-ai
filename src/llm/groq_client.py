from langchain_groq import ChatGroq
from src.config.settings import settings

def get_groq_llm(model='llama-3.1-8b-instant'):
    if not model:
        model = 'llama-3.1-8b-instant'
    return ChatGroq(
        api_key = settings.GROQ_API_KEY,
        model = model,
        temperature=settings.TEMPERATURE
    )