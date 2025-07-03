import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

class GeminiLLM:
    def __init__(self,user_controls_input):
        self.user_controls_input=user_controls_input

    def get_gemini_llm_model(self):
        try:
            self.gemini_api_key=os.getenv("GEMINI_API_KEY")

            llm = ChatGoogleGenerativeAI(api_key = self.gemini_api_key, model="gemini-2.5-flash")

        except Exception as e:
            raise ValueError(f"Error Occurred with Exception : {e}")
        
        return llm