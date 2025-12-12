from langchain_groq import ChatGroq
import os
from langchain_openai.chat_models import ChatOpenAI
from src.config.settings import settings


class LLMModel:
    """Handles different LLM models"""

    def __init__(self, model="gpt-5-nano"):
        if model in ["gpt-5", "gpt-5-mini", "gpt-5-nano"]:
            self.llm = self._get_openai_client(model)
        else:
            self.llm = self._get_groq_client(model)

    def _get_groq_client(self,model='llama-3.1-8b-instant'):
        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=model,
            temperature=settings.TEMPERATURE
        )

    def _get_openai_client(self, model='gpt-5-nano'):
        return ChatOpenAI(
            model=model,
            temperature=settings.TEMPERATURE,
            api_key=settings.OPENAI_API_KEY
        )
